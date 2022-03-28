#-*-coding:utf-8;-*-
#qpy:3
#qpy:console
from json import dumps
from socket import socket,AF_INET,SOCK_STREAM
from androidhelper import Android
def dealDict(dic):
    if dic.__contains__("gps"):
        dc=dic["gps"]
        return {"provider":dc["provider"],"accuracy":dc["accuracy"],"latitude":dc["latitude"],"longitude":dc["longitude"],"altitude":dc["altitude"],"bearing":dc["bearing"],"speed":dc["speed"],"time":dc["time"]}
    elif dic.__contains__("network"):
        dc=dic["network"]
        return {"provider":dc["provider"],"accuracy":dc["accuracy"],"latitude":dc["latitude"],"longitude":dc["longitude"],"altitude":dc["altitude"],"bearing":dc["bearing"],"speed":dc["speed"],"time":dc["time"]}
    elif dic.__contains__("passive"):
        dc=dic["passive"]
        return {"provider":dc["provider"],"accuracy":dc["accuracy"],"latitude":dc["latitude"],"longitude":dc["longitude"],"altitude":dc["altitude"],"bearing":dc["bearing"],"speed":dc["speed"],"time":dc["time"]}
    else:
        return {"provider":None,"accuracy":None,"latitude":None,"longitude":None,"altitude":None,"bearing":None,"speed":None,"time":None}
ad=Android()
soc=socket(AF_INET,SOCK_STREAM)
soc.bind(("127.0.0.1",1864))
soc.listen(1)
cli,add=soc.accept()
ad.makeToast("Location server : Successfully connected to the client.")
while True:
    rea=cli.recv(65536).decode("utf-8").strip("\n")
    if rea=="read":
        cli.send((dumps(dealDict(ad.readLocation().result))+"\n").encode("utf-8"))
    elif rea=="open":
        ad.startLocating(1000,0)
        print("Start locating.")
    elif rea=="close":
        ad.stopLocating()
        print("Stop locating.")