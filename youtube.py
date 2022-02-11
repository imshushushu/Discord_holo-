from dataclasses import dataclass
from distutils.util import change_root
from importlib.resources import path
from nturl2path import pathname2url
from turtle import Turtle
from googleapiclient.discovery import build
import time
import datetime
import isodate
import file
import changer
import json
YOUTUBE_API_KEY = 

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
def youtube_channel_detail(channel_id, api_key):
    api_service_name = 'youtube'
    api_version = 'v3'
    youtube = build(api_service_name, api_version, developerKey=api_key)
    search_response = youtube.channels().list(
        part='snippet,statistics',
        id=channel_id,
        ).execute()
    return search_response['items'][0]

def ch_info():    
    json_dict=file.read_members_info()
    for member in json_dict:
        time.sleep(0.75)
        d = youtube_channel_detail(json_dict[member]["ch"]["id"], YOUTUBE_API_KEY)
        json_dict[member]["ch"]["subscribers"]=d['statistics']['subscriberCount']
    file.white_members_info(json_dict)

def YouTubelist(channnel,member):
    # APIをたたく
    global YOUTUBE_API_KEY
    search_response = youtube.search().list(
        channelId=channnel,
        part='snippet',
        maxResults=1,
        order='date',
        type='video',
        pageToken=YOUTUBE_API_KEY
    ).execute()

    # VideoIDのリストを生成
    video_ids = []
    items = search_response['items']
    for item in items :
        video_ids.append(item['id']['videoId'])

    # それぞれのライブ開始・終了時刻を取得
    details = youtube.videos().list(
        part='liveStreamingDetails',
        id=video_ids
    ).execute()
    detailitems = details['items']

    # APIから返される時刻をy/m/d H:M:Sに変換
    JST = datetime.timedelta(hours=9)
    def timetrans(strtime):
        stime = datetime.datetime.fromisoformat(strtime[:-1]) + JST
        return stime.replace(microsecond=0)

    # 動画の長さを取得
    def videolength(video_id):
        Cdetail = youtube.videos().list(
            part='contentDetails',
            id=video_id
        ).execute()
        duration = Cdetail['items'][0]['contentDetails']['duration']
        return isodate.parse_duration(duration)
    searchdelta = datetime.timedelta(hours=1)

    # 判定部
    for item, detail in zip(items, detailitems):
        state = item['snippet']['liveBroadcastContent']
        
        if state == 'upcoming':
            starttime = timetrans(detail['liveStreamingDetails']['scheduledStartTime'])
            endtime = starttime + datetime.timedelta(hours=1)
        elif state == 'live':
            starttime = timetrans(detail['liveStreamingDetails']['actualStartTime'])
            endtime = datetime.datetime.now().replace(microsecond=0) + searchdelta
        else:
            try:
                starttime = timetrans(detail['liveStreamingDetails']['actualStartTime'])
            except:
                starttime = timetrans(item['snippet']['publishTime'])
                endtime = starttime + videolength(video_id)
            else :
                endtime = timetrans(detail['liveStreamingDetails']['actualEndTime'])

        overview =item["snippet"]["description"]
        title = item['snippet']['title']
        video_id = item['id']['videoId']
        print(starttime,endtime,title, video_id)
        nowtime=datetime.datetime.now()
        starttime=changer.datatime(starttime)
        endtime=changer.datatime(endtime)
        nowtime=changer.datatime(nowtime)  
        now_day=nowtime["day"]
        end_day=endtime["day"]
        print(now_day,end_day)
        elapsed_date=now_day-end_day
        video_data={"starttime":starttime,"title":title,"endtime":endtime,"status":elapsed_date,"overview":overview}
        if now_day-7 > end_day:
            file.white_archives(video_data,video_id,member)
            print("archives保存")
        else:
            video_data["channnel_id"]=channnel
            video_data["member"]=member
            file.white_schedule(video_data,video_id)
            print("schedule保存")
    nowtime=datetime.datetime.now()
    nowtime=changer.datatime(nowtime)
    path="manager.json"
    f = open(path, 'r',encoding="utf-8_sig")
    json_dict = json.load(f)
    json_dict["last_access"]=nowtime
    f = open(path, 'w',encoding="utf-8_sig")
    json.dump(json_dict, f)



