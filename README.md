# EC601_MiniProject_1
EC601
Summary
get_all_tweets(screen_name) in tweetAPIexample.py: grab and download pictures from specified twitter account.
get_anno(img_path,out_path) in google-vision.py: get annotation of the pictures and add into pictures
generate_video(i_path,o_path) in google-vision.py: generate a video from a set of pictures


Twitter Api
Developer Account Required.
And then we can get four keys.
Get time_line follow the example provided by professors.
However,instead of dump info into json. We should download images with the url.
The structure of Tweepy-Status can be found in GithubGist.
I use the "media_url" to get the images.

Google Api
Google Cloud Platform register required
Just follow the "quick start" to install google-cloud and enable the api
After getting the annotation, use python lib PIL to add those text into the pictures

FFmpeg
simply install and run generate_video(i_path,o_path)
