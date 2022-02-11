from lib2to3.pygram import pattern_symbols
from unicodedata import name
import file
import json
import os
async def video_give(word_list):
    if type('string') is word_list:
        print("関数video_giveの引数はリスト型")
    path="tag.json"
    f = open(path, 'r',encoding="utf-8_sig")
    tags = json.load(f)
    reslt=[]
    for one_word in word_list:
        for tag in tags:
            if one_word in tag :
                reslt.append(tag)
    return reslt

async def search_tag(target_tag,past=False,stream=True,video=True):
    paths=[]
    if past:
        members = os.listdir("member")
        for member in members:
            if stream:
                paths.append("member/"+member+"/stream_delivered.json")
            if video:
                paths.append("member/"+member+"/archives_video.json")
    if stream:
        paths.append("week_schedule.json")
    if video:
        paths.append("recently_videos.json")
    reslt=[]
    for path in paths:
        f = open(path, 'r',encoding="utf-8_sig")
        tags = json.load(f)
        for tag in tags:
            for on_tag in tags[tag]["tag"]:
                for check_tag in on_tag:
                    if check_tag==target_tag:
                        reslt.append(tag)
    return reslt

def make_tag():
    path="tag.json"
    f = open(path, 'r',encoding="utf-8_sig")
    tags = json.load(f)
    for tag_name in tags:
        list=[]
        if len(tags[tag_name])==0:
            continue
        tags[tag_name]["alias"]=[]
        for one_alias in tags[tag_name]:
            tags[tag_name]["alias"].append(tags[tag_name][one_alias])
    f = open(path, 'w',encoding="utf-8_sig")
    json.dump(tags, f)

make_tag()