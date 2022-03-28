#-*-coding:utf-8;-*-
#qpy:3
#qpy:console
from os import listdir
from os.path import split,splitext
from json import loads,dumps
from urllib.parse import unquote
from socket import socket,AF_INET,SOCK_STREAM
from androidhelper import Android
from bottle import hook,response,route,request,run
from tornado.options import parse_command_line
parse_command_line()
ad=Android()
path="/storage/emulated/0/Music/piano"
origrp=[]
for i in listdir(path):
    if splitext(i)[1]==".wav":
        origrp+=[path+"/"+i]
cli=socket(AF_INET,SOCK_STREAM)
try:
    cli.connect(("localhost",1866))
except:
    suc=False
else:
    cli.send((dumps(origrp)+"\n").encode("utf-8"))
    files=loads(cli.recv(65536).decode("utf-8").strip("\n"))
    suc=True
fls=[]
if suc:
    for i in files:
        fls+=[splitext(split(i)[1])[0]]
@hook("after_request")
def admit():
    response.headers["Content-Type"]="application/json"
    response.headers["Access-Control-Allow-Origin"]="*"
    response.headers["Access-Control-Allow-Headers"]="*"
@route("/<name>")
def answer(name):
    global cli,fls,path
    nm=unquote(name)
    if nm in fls:
        cli.send((path+"/"+nm+".wav\n").encode("utf-8"))
        return dumps({"succeed":True})
    else:
        return dumps({"succeed":False})
@route("/")
def answer():
    txt=dict(request.query.decode("utf-8"))
    if txt.__contains__("text"):
        global ad
        ad.ttsSpeak(txt["text"])
        return dumps({"succeed":ad.ttsIsSpeaking().result})
    else:
        global fls
        return dumps({"list":fls})
run(server="tornado",host="0.0.0.0",port=4088)