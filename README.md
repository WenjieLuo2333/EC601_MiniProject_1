# EC601_MiniProject_1<br/>
EC601<br/>
[Mini_Proj_3_With_Database url here.](https://github.com/WenjieLuo2333/601_mini_proj_3)
# Summary:<br/>
get_all_tweets(screen_name) in tweetAPIexample.py: grab and download pictures from specified twitter account.<br/>
get_anno(img_path,out_path) in google-vision.py: get annotation of the pictures and add into pictures.<br/>
generate_video(i_path,o_path) in google-vision.py: generate a video from a set of pictures.<br/>


# Twitter Api:<br/>
Developer Account Required.<br/>
And then we can get four keys.<br/>
Get time_line follow the example provided by professors.<br/>
However,instead of dump info into json. We should download images with the url.<br/>
The structure of Tweepy-Status can be found in GithubGist.<br/>
I use the "media_url" to get the images.<br/>
<br/>
# Google Api:<br/>
Google Cloud Platform register required<br/>
Just follow the "quick start" to install google-cloud and enable the api<br/>
After getting the annotation, use python lib PIL to add those text into the pictures<br/>
<br/>
# FFmpeg:<br/>
simply install and run generate_video(i_path,o_path)<br/>

# All_in_One_API.py<br/>
import the other python files and just need to run this file
