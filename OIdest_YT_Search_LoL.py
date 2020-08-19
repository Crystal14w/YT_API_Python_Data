from youtube_api import YouTubeDataAPI
from apiclient.discovery import build
import pprint
from datetime import datetime


start_time = datetime(year=2009, month=10, day=27).strftime('%Y-%m-%dT%H:%M:%SZ')
end_time = datetime(year=2009, month=12, day=31).strftime('%Y-%m-%dT%H:%M:%SZ')

api_key = 'AKAIXXXXXXXX'
youtube = build('youtube','v3',developerKey=api_key)

type(youtube)

req = youtube.search().list(q='league of legends', part='snippet', type='video',
                                                         publishedAfter=start_time,
                                                         publishedBefore=end_time).execute()

pprint.pprint(req)
