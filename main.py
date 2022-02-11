from unicodedata import name
import discord
import json
import time
import math
from discord.ext import tasks
import changer
import datetime
import file



# 自分のBotのアクセストークンに置き換えてください
TOKEN = 

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
        
    
# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    if message.content=="/holo":
        f = open("week_schedule.json", 'r',encoding="utf-8_sig")
        json_dict = json.load(f)
        await message.channel.send("**ホロ配信履歴Betaテスト版を送信します**\n\n")
        for id in json_dict:
            video=json_dict[id]
            f = open("member/"+video["member"]+"/info.json", 'r',encoding="utf-8_sig")
            mem= json.load(f)
            name=mem["info"]["name"]
            url="https://youtu.be/"+id
            title=video["title"]
            send_thing="タイトル: "+title+"\n名前: "+name+"\nurl: "+url+"\n"
            await message.channel.send(send_thing)
        f = open("manager.json", 'r',encoding="utf-8_sig")
        json_dict = json.load(f)
        access_time=json_dict["last_access"]
        await message.channel.send ("("+str(access_time["day"])+"日"+str(access_time["hour"])+"時"+str(access_time["minute"])+"分更新)")
        print ("("+str(access_time["day"])+"日"+str(access_time["hour"])+"時"+str(access_time["minute"])+"分更新)")



    if message.content=="/will_holo":
        f = open("week_schedule.json", 'r',encoding="utf-8_sig")
        json_dict = json.load(f)
        await message.channel.send("**ホロ配信履歴Betaテスト版を送信します**\n\n")
        for id in json_dict:
            video=json_dict[id]
            if changer.time_calculation(video["starttime"],"<",changer.datatime(datetime.datetime.now())):
                continue
            f = open("member/"+video["member"]+"/info.json", 'r',encoding="utf-8_sig")
            mem= json.load(f)
            name=mem["info"]["name"]
            url="https://youtu.be/"+id
            title=video["title"]
            send_thing="タイトル: "+title+"\n名前: "+name+"\nurl: "+url+"\n"
            await message.channel.send(send_thing)
        f = open("manager.json", 'r',encoding="utf-8_sig")
        json_dict = json.load(f)
        access_time=json_dict["last_access"]
        await message.channel.send ("("+str(access_time["day"])+"日"+str(access_time["hour"])+"時"+str(access_time["minute"])+"分更新)")
        print ("("+str(access_time["day"])+"日"+str(access_time["hour"])+"時"+str(access_time["minute"])+"分更新)")

    if message.content=="/join":
        send_message=await message.author.send("このbotのサービスを提供するために、必要なデータを保存されることを同意しますか。\nよろしければ「Y」を、拒否したい場合は「N」を押してください。")
        await send_message.add_reaction("🇾")
        await send_message.add_reaction("🇳")
        path="access_reaction.json"
        f = open(path, 'r',encoding="utf-8_sig")
        data = json.load(f)
        data[send_message.id]={"type":"join","user":message.author.id}
        f = open(path, 'w',encoding="utf-8_sig")
        json.dump(data, f)


@client.event
async def on_reaction_add(reaction, user):
    path="access_reaction.json"
    f = open(path, 'r',encoding="utf-8_sig")
    datas= json.load(f)
    for rid in datas:
        if reaction.message.id==rid:
            hid=rid
            break
    else:
        return
    if datas[hid]["type"]=="join":
        def remove_access_json(datas,hid):
            path="access_reaction.json"
            del datas[hid]
            f = open(path, 'w',encoding="utf-8_sig")
            json.dump(datas, f)
            return

        if reaction.emoji =="🇾":
            await user.send("確認できました\n登録ありがとうございます\n登録処理を開始します")
            remove_access_json(datas,hid)
            await file.new_user(user.id)
        if reaction.emoji =="🇳":
            await user.send("登録がキャンセルされました")
            remove_access_json(datas,hid)

@tasks.loop(seconds=2)
async def task_2sec():
    pass

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)


"""
        f = open(path, 'r')
        json_dict = json.load(f)
        json_dict
        print(json_dict)
        f = open(path, 'w')
        json.dump(json_dict, f)
        
    """