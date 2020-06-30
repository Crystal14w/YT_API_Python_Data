#!/usr/bin/python3
#Testing YT API

from youtube_api import YouTubeDataAPI
from apiclient.discovery import build
import pprint

api_key = 'AKAIXXXXXXXX'
youtube = build('youtube','v3',developerKey=api_key)

type(youtube)

req = youtube.search().list(q='avengers', part='snippet', type='video')
type(req)
res = req.execute()

pprint.pprint(res)
