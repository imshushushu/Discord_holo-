import json
import os
from discord import Member

def read_members_info():
    members = os.listdir("member")
    data={}
    for member in members:
        path="member/"+member+"/info.json"
        f = open(path, 'r',encoding="utf-8_sig")
        json_dict = json.load(f) 
        data[member]=json_dict
    return data

def write_members_info(data,member=all):
    def write(data,member):
        path="member/"+member+"/info.json"
        f = open(path, 'w',encoding="utf-8_sig")
        json.dump(data, f)
    if member==all:
        del member
        members = os.listdir("member")
        for member in members:
            write(data,member)
        return True
    else:    
        write(data,member)
        return True

def white_archives(data,video_id,member):
    path="member/"+member+"/stream_delivered.json"
    if os.path.isfile(path)==False:
        f = open(path, 'w')
        f.write("{}")
        f.close()
    f = open(path, 'r',encoding="utf-8_sig")
    json_dict = json.load(f)
    if video_id in json_dict :
        return
    json_dict[video_id]=data
    f = open(path, 'w',encoding="utf-8_sig")
    json.dump(json_dict, f)

def white_schedule(data,video_id):
    path="week_schedule.json"
    f = open(path, 'r',encoding="utf-8_sig")
    json_dict = json.load(f)
    json_dict[video_id]=data
    f = open(path, 'w',encoding="utf-8_sig")
    json.dump(json_dict, f)

def video_search_id(id):
    members = os.listdir("member")
    to_access=["week_schedule.json","recently_videos.json"]
    for member in members:
        to_access.apped("member/"+member+"/stream_delivered.json")
        to_access.apped("member/"+member+"/archives_video.json")
    for path in to_access:
        f = open(path, 'r',encoding="utf-8_sig")
        json_dict = json.load(f)
        for video_id in json_dict :
            if video_id==id:
                return json_dict[video_id]
    return False

async def new_user(user_id):
    f = open("user_data/"+user_id+".json", 'w')
    f.write('{}')
    f.close()

def read_member():
    