import json

from apiclient.discovery import build
API_KEY = 
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
CHANNEL_ID=

def check_channel(CHANNEL_ID):
    global YOUTUBE_API_SERVICE_NAME
    global YOUTUBE_API_VERSION
    global API_KEY
    youtube = build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=API_KEY
    )

    response = youtube.search().list(
        part = "snippet",
        channelId = CHANNEL_ID,
        maxResults = 1,
        order = "date" #日付順にソート
        ).execute()

    for item in response.get("items", []):
        print(item["id"]["kind"])
        if item["id"]["kind"] != "youtube#video":
            continue
        print('*' * 10)
        print(json.dumps(item, indent=2, ensure_ascii=False))
        print('*' * 10)


def youtube_video_data(VIDEO_ID_LIST):
    global YOUTUBE_API_SERVICE_NAME
    global YOUTUBE_API_VERSION
    global API_KEY

    youtube = build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=API_KEY
    )

    for video_id in VIDEO_ID_LIST:
        response = youtube.videos().list(
        part = 'snippet,statistics',
        id = video_id
        ).execute()

        for item in response.get("items", []):
            if item["kind"] != "youtube#video":
                continue
            print('*' * 10)
            print(json.dumps(item, indent=2, ensure_ascii=False))
            print('*' * 10)