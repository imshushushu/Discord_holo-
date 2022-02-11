import json
import datetime
import changer
import os
import file 

def make_tag(member):
    path="member/"+member+"/info.json"
    f = open(path, 'r',encoding="utf-8_sig")
    tags = json.load(f)
    b=True
    while b==True:
        b=False
        print(tags["info"]["name"]+"のニックネームを入力")
        others={}
        a=0
        while True:
            othename=input()
            if othename=="n":
                break
            others[str(a)]=othename
            a=a+1
        print("間違えない？")
        if input()=="n":
            b=True
            continue
        tags["info"]["Nick"]
        print("書き込みする")
        f = open(path, 'w',encoding="utf-8_sig")
        json.dump(tags, f)
members = os.listdir("member")
for member in members :
    make_tag(member)