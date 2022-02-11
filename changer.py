def datatime(datatime):
    time_str=datatime.strftime('%Y:%m:%d:%H:%M:%S')
    time_listing=time_str.split(":")
    mean_split=("year","month","day","hour","minute","second")
    time={}
    a=0
    for one_time in time_listing :
        time[mean_split[a]]=int(one_time)
        a=a+1
    return time

def time_calculation(a_time,type,b_time):
    if type=="<"or">"or"<"or">":
        mean_split=("year","month","day","hour","minute","second")
        for split in mean_split :
            if a_time[split]!=b_time[split]:
                if type=="<":
                    return (a_time[split]<b_time[split])
                elif type==">":
                    return (a_time[split]>b_time[split])


1>=2
1<=2
                