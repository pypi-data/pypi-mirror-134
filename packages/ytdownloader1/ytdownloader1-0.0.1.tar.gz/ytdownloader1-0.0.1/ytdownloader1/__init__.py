#!/usr/bin/env python
# coding: utf-8

# In[3]:


from pytube import YouTube


# In[6]:


def ytdownloader():
    Download_path=""
    try:
        #video_url="https://www.youtube.com/watch?v=8UNuEyQovhY&ab_channel=T-Series"
        video_url=input("Enter the video URL which you want to download")
        video_obj=YouTube(video_url)
        stream=video_obj.streams.get_highest_resolution()
        stream.download(Download_path)
    except:
        print("Video Not Found")
    print("<<<<<<<<Video downloaded successfully>>>>>>>>>>>")


