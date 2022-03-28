#-*-coding:utf-8;-*-
#qpy:3
#qpy:console
from json import loads,dumps
from time import time,sleep
from socket import socket,AF_INET,SOCK_STREAM
from threading import Thread,Lock
from bottle import hook,response,route,run
from tornado.options import parse_command_line
parse_command_line()
senname=["acceleration","magnet","orientation","gyroscope","light","proximity","gravity","linear_acceleration","rotation","step_counter"]
sensign=["acc","mag","ori","gyr","lig","pro","gra","lin","rot","ste"]
loctcp=socket(AF_INET,SOCK_STREAM)
sentcp=socket(AF_INET,SOCK_STREAM)
try:
    loctcp.connect(("localhost",1864))
except:
    locexist=False
else:
    locexist=True
try:
    sentcp.connect(("localhost",1862))
except:
    senexist=False
else:
    senexist=True
if senexist:
    sentime=[0.0]*10
    def senopen(typ):
        global sentcp
        sentcp.send(("open\n%s\n"%(typ)).encode("utf-8"))
    def senread(typ):
        global sentcp
        sentcp.send(("read\n%s\n"%(typ)).encode("utf-8"))
        return loads(sentcp.recv(65536).decode("utf-8").strip("\n"))
    def senclose(typ):
        global sentcp
        sentcp.send(("close\n%s\n"%(typ)).encode("utf-8"))
if locexist:
    loctime=0.0
    def locopen():
        global loctcp
        loctcp.send("open\n".encode("utf-8"))
    def locread():
        global loctcp
        loctcp.send("read\n".encode("utf-8"))
        return loads(loctcp.recv(65536).decode("utf-8").strip("\n"))
    def locclose():
        global loctcp
        loctcp.send("close\n".encode("utf-8"))
cando=Lock()
def killer():
    global cando,locexist,senexist,sensign
    if senexist:
        global sentime
    if locexist:
        global loctime
    while True:
        if senexist:
            for i in range(0,10):
                cando.acquire()
                if sentime[i]!=0.0 and time()>sentime[i]:
                    senclose(sensign[i])
                    sentime[i]=0.0
                cando.release()
                sleep(0.02)
        if locexist:
            cando.acquire()
            if loctime!=0.0 and time()>loctime:
                locclose()
                loctime=0.0
            cando.release()
            sleep(0.02)
@hook("after_request")
def admit():
    response.headers["Content-Type"]="application/json"
    response.headers["Access-Control-Allow-Origin"]="*"
    response.headers["Access-Control-Allow-Headers"]="*"
@route("/location")
def answer():
    global cando,locexist
    cando.acquire()
    res={}
    if locexist:
        global loctime
        if loctime==0.0:
            locopen()
            sleep(3)
        res["location"]=locread()
        loctime=time()+30
    cando.release()
    return dumps(res)
@route("/acceleration")
def answer():
    global cando,senexist,senname,sensign
    cando.acquire()
    res={}
    if senexist:
        global sentime
        if sentime[0]==0.0:
            senopen(sensign[0])
            sleep(0.5)
        res[senname[0]]=senread(sensign[0])
        sentime[0]=time()+15
    cando.release()
    return dumps(res)
@route("/magnet")
def answer():
    global cando,senexist,senname,sensign
    cando.acquire()
    res={}
    if senexist:
        global sentime
        if sentime[1]==0.0:
            senopen(sensign[1])
            sleep(0.5)
        res[senname[1]]=senread(sensign[1])
        sentime[1]=time()+15
    cando.release()
    return dumps(res)
@route("/orientation")
def answer():
    global cando,senexist,senname,sensign
    cando.acquire()
    res={}
    if senexist:
        global sentime
        if sentime[2]==0.0:
            senopen(sensign[2])
            sleep(0.5)
        res[senname[2]]=senread(sensign[2])
        sentime[2]=time()+15
    cando.release()
    return dumps(res)
@route("/gyroscope")
def answer():
    global cando,senexist,senname,sensign
    cando.acquire()
    res={}
    if senexist:
        global sentime
        if sentime[3]==0.0:
            senopen(sensign[3])
            sleep(0.5)
        res[senname[3]]=senread(sensign[3])
        sentime[3]=time()+15
    cando.release()
    return dumps(res)
@route("/light")
def answer():
    global cando,senexist,senname,sensign
    cando.acquire()
    res={}
    if senexist:
        global sentime
        if sentime[4]==0.0:
            senopen(sensign[4])
            sleep(0.5)
        res[senname[4]]=senread(sensign[4])
        sentime[4]=time()+15
    cando.release()
    return dumps(res)
@route("/proximity")
def answer():
    global cando,senexist,senname,sensign
    cando.acquire()
    res={}
    if senexist:
        global sentime
        if sentime[5]==0.0:
            senopen(sensign[5])
            sleep(0.5)
        res[senname[5]]=senread(sensign[5])
        sentime[5]=time()+15
    cando.release()
    return dumps(res)
@route("/gravity")
def answer():
    global cando,senexist,senname,sensign
    cando.acquire()
    res={}
    if senexist:
        global sentime
        if sentime[6]==0.0:
            senopen(sensign[6])
            sleep(0.5)
        res[senname[6]]=senread(sensign[6])
        sentime[6]=time()+15
    cando.release()
    return dumps(res)
@route("/linear_acceleration")
def answer():
    global cando,senexist,senname,sensign
    cando.acquire()
    res={}
    if senexist:
        global sentime
        if sentime[7]==0.0:
            senopen(sensign[7])
            sleep(0.5)
        res[senname[7]]=senread(sensign[7])
        sentime[7]=time()+15
    cando.release()
    return dumps(res)
@route("/rotation")
def answer():
    global cando,senexist,senname,sensign
    cando.acquire()
    res={}
    if senexist:
        global sentime
        if sentime[8]==0.0:
            senopen(sensign[8])
            sleep(0.5)
        res[senname[8]]=senread(sensign[8])
        sentime[8]=time()+15
    cando.release()
    return dumps(res)
@route("/step_counter")
def answer():
    global cando,senexist,senname,sensign
    cando.acquire()
    res={}
    if senexist:
        global sentime
        if sentime[9]==0.0:
            senopen(sensign[9])
            sleep(0.5)
        res[senname[9]]=senread(sensign[9])
        sentime[9]=time()+15
    cando.release()
    return dumps(res)
@route("/sensors")
def answer():
    global cando,senexist,senname,sensign
    cando.acquire()
    res={}
    if senexist:
        global sentime
        senpau=False
        for i in range(0,10):
            if sentime[i]==0.0:
                senopen(sensign[i])
                senpau=True
        if senpau:
            sleep(0.5)
        for i in range(0,10):
            res[senname[i]]=senread(sensign[i])
        sentime=[time()+15]*10
    cando.release()
    return dumps(res)
@route("/all_data")
def answer():
    global cando,locexist,senexist,senname,sensign
    cando.acquire()
    res={}
    locpau=False
    senpau=False
    if locexist:
        global loctime
        if loctime==0.0:
            locopen()
            locpau=True
    if senexist:
        global sentime
        for i in range(0,10):
            if sentime[i]==0.0:
                senopen(sensign[i])
                senpau=True
    if locpau:
        sleep(3)
    elif senpau:
        sleep(0.5)
    if locexist:
        res["location"]=locread()
        loctime=time()+30
    if senexist:
        for i in range(0,10):
            res[senname[i]]=senread(sensign[i])
        sentime=[time()+15]*10
    cando.release()
    return dumps(res)
@route("/")
def answer():
    global cando,locexist,senexist,senname,sensign
    cando.acquire()
    res={}
    locpau=False
    senpau=False
    if locexist:
        global loctime
        if loctime==0.0:
            locopen()
            locpau=True
    if senexist:
        global sentime
        for i in range(0,10):
            if sentime[i]==0.0:
                senopen(sensign[i])
                senpau=True
    if locpau:
        sleep(3)
    elif senpau:
        sleep(0.5)
    if locexist:
        res["location"]=locread()
        loctime=time()+30
    if senexist:
        for i in range(0,10):
            res[senname[i]]=senread(sensign[i])
        sentime=[time()+15]*10
    cando.release()
    return dumps(res)
Thread(target=killer).start()
run(server="tornado",host="0.0.0.0",port=4080)