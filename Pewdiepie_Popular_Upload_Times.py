#!/usr/bin/python3
#Time_Uploads_YT_API_DATA
#Pewdiepie Channel Upload Hours

from datetime import datetime, timedelta
from apiclient.discovery import build
import matplotlib.pyplot as plt

YOUTUBE_DEVELOPER_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
youtube = build('youtube', 'v3', developerKey=YOUTUBE_DEVELOPER_KEY)

def get_channel(channel_name):
    return youtube.search().list(q=channel_name, type='channel', part='id,snippet').execute()['items'][0]


def get_videos(channel_id, part='id,snippet', limit=10):
    res = youtube.channels().list(id=channel_id, 
                                  part='contentDetails').execute()
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    
    videos = []
    next_page_token = None
    
    while 1:
        res = youtube.playlistItems().list(playlistId=playlist_id, 
                                           part=part, 
                                           maxResults=min(limit, 50),
                                           pageToken=next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')
        
        if next_page_token is None or len(videos) >= limit:
            break

    return videos

def parse_publish_timestamp(video):
    return (datetime.strptime(video['snippet']['publishedAt'], "%Y-%m-%dT%H:%M:%SZ"))
#Add timedelta for GMT timezone
#            + timedelta(hours=5, minutes=30))

#Set limit based on current total videos
channel_id = get_channel('pewdiepie')['id']['channelId']
videos = get_videos(channel_id, limit=4200)
publish_timestamps = [parse_publish_timestamp(video) for video in videos]
publish_times = [t.hour + t.minute/60 for t in publish_timestamps]

#Build Bar Graph
plt.hist(publish_times, bins=24)
plt.xticks(range(24))
plt.title('Pewdiepie Popular Upload Times')
plt.xlabel('Hours')
plt.ylabel('Number of Videos')
plt.show()
