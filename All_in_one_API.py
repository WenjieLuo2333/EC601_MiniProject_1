import tweetAPIexample
import google_vision

def all_in_one_API(account,i_p,o_p,video_i,video_o):
		tweetAPIexample.get_all_tweets(account)
		google_vision.get_anno(i_p,o_p)
		google_vision.generate_video(video_i,video_o)

if __name__ == '__main__':
	all_in_one_API("@NBA","./imgs/","./labeled_imgs/","./labeled_imgs/img%03d.jpg","labeled_video.avi")