import mysql.connector


def connectdb(ur, pas, database_name):
    db = mysql.connector.connect(
        user=ur,
        passwd=pas,
        database=database_name,
        use_unicode=True)
    print("Database Connected")
    return db


def operate(db, cmd):
    cursor = db.cursor()
    sql = cmd
    cursor.execute(sql)


def new_user(db, ur, pas):
    cursor = db.cursor()
    sql = """CREATE USER '%s'@'%%' IDENTIFIED BY '%s';""" % (ur, pas)
    cursor.execute(sql)


def create_table(db, table_name):
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS " + table_name)
    sql = """CREATE TABLE %s (
	        label CHAR(30) NOT NULL,
	        img_name CHAR(15),
	        USER CHAR(15)
	        )""" % (table_name)
    cursor.execute(sql)


def check_user_data(db, user_name):
    cursor = db.cursor()
    sql = """SELECT * FROM label_to_img WHERE USER = '%s'""" % (user_name)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results


def check_user_keyword(db, user_name):
    cursor = db.cursor()
    sql = """SELECT * FROM label_to_img WHERE USER = '%s'""" % (user_name)
    cursor.execute(sql)
    results = cursor.fetchall()
    keywords = {}
    for line in results:
        if line[0] in keywords:
            keywords[line[0]] += 1
        else:
            keywords[line[0]] = 1
    return keywords


def mysort(s):
    return s[-1]


def check_word_frequency(db):
    cursor = db.cursor()
    sql = """SELECT * FROM label_to_img"""
    cursor.execute(sql)
    results = cursor.fetchall()
    keywords = {}
    imgs = {}
    for line in results:
        if line[1] in imgs:
            imgs[line[1]] += 1
        else:
            imgs[line[1]] = 1
        if line[0] in keywords:
            keywords[line[0]] += 1
        else:
            keywords[line[0]] = 1
    ans = [[i, keywords[i], round(keywords[i] / len(imgs), 4)]
           for i in keywords]
    ans[:] = sorted(ans, key=mysort, reverse=True)
    return ans


def check_img_num(db):
    cursor = db.cursor()
    sql = """SELECT * FROM label_to_img"""
    cursor.execute(sql)
    results = cursor.fetchall()
    keywords = {}
    imgs = {}
    for line in results:
        if line[1] in imgs:
            imgs[line[1]] += 1
        else:
            imgs[line[1]] = 1
    return imgs


def check_user_word_frequency(db, user_name):
    cursor = db.cursor()
    sql = """SELECT * FROM label_to_img WHERE USER = '%s'""" % (user_name)
    cursor.execute(sql)
    results = cursor.fetchall()
    keywords = {}
    imgs = {}
    for line in results:
        if line[1] in imgs:
            imgs[line[1]] += 1
        else:
            imgs[line[1]] = 1
        if line[0] in keywords:
            keywords[line[0]] += 1
        else:
            keywords[line[0]] = 1
    ans = [[i, keywords[i], round(keywords[i] / len(imgs), 4)]
           for i in keywords]
    ans[:] = sorted(ans, key=mysort, reverse=True)
    return ans


def check_user_img_num(db, user_name):
    cursor = db.cursor()
    sql = """SELECT * FROM label_to_img WHERE USER = '%s'""" % (user_name)
    cursor.execute(sql)
    results = cursor.fetchall()
    keywords = {}
    imgs = {}
    for line in results:
        if line[1] in imgs:
            imgs[line[1]] += 1
        else:
            imgs[line[1]] = 1
    return imgs
