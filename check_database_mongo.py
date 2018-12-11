import pymongo


def connectdb():
    db = pymongo.MongoClient()
    return db


def query_by_account(table, user):
    results = table.find({'Account': user})
    ans = []
    for i in results:
        ans.append(i)
    return ans


def query_account_by_keyword(table, key):
    results = table.find()
    ans = []
    for i in results:
        if key in i['Labels']:
            ans.append(i['Account'])
    return ans


def query_all_keywords(table):
    results = table.find()
    ans = {}
    k = 0
    for i in results:
        k += 1
        for key in i['Labels']:
            if key in ans:
                ans[key] += 1
            else:
                ans[key] = 1
    ans = [[i, ans[i]] for i in ans]
    ans[:] = sorted(ans, key=lambda k: k[-1], reverse=True)
    return ans


def query_user_pic_nums(table, user):
    results = table.find({'Account': user}).count()
    return results


def query_user_keywords(table, user):
    results = table.find({'Account': user})
    ans = {}
    k = 0
    for i in results:
        k += 1
        for key in i['Labels']:
            if key in ans:
                ans[key] += 1
            else:
                ans[key] = 1
    ans = [[i, ans[i]] for i in ans]
    ans[:] = sorted(ans, key=lambda k: k[-1], reverse=True)
    return ans


def main():
    db = connectdb()
    tdb = db.wj_601
    table = tdb.account_info
    result = query_by_account(table, "@NBA")
    print(result)


if __name__ == '__main__':
    main()
