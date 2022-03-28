#-*-coding:utf-8;-*-
#qpy:3
#qpy:console
from os import listdir
from os.path import isdir
from urllib.parse import unquote
from bottle import route,request,static_file,run
from tornado.options import parse_command_line
parse_command_line()
head="<!DOCTYPE html> <html> <head> <meta charset='utf-8'/> <title>%s</title> <style type='text/css'>%s</style> </head> <body> "
css="a.isp:link{color: Green; } a.isp:visited{color: DarkGoldenRod; } a.isp:hover{color: FireBrick; } a.isp:active{color: OrangeRed; } a.isf:link{color: MediumBlue; } a.isf:visited{color: Purple; } a.isf:hover{color: FireBrick; } a.isf:active{color: OrangeRed; } "
body="<a href='%s' class='%s'>%s</a> <br/> "
tail="</body> </html> "
def make(pth):
    global head,css,body,tail
    fls=listdir("/sdcard/"+pth)
    fls.sort()
    htm=head%("内部存储/"+pth,css)
    for f in fls:
        if isdir("/sdcard/"+pth+"/"+f):
            clz="isp"
        else:
            clz="isf"
        htm+=body%("/"+pth+"/"+f,clz,f)
    htm+=tail
    return htm
@route("/<pt:path>")
def answer(pt):
    val=unquote(pt)
    if isdir("/sdcard/"+val):
        return make(val)
    else:
        dwn=dict(request.query.decode("utf-8"))
        if dwn.__contains__("download"):
            if dwn["download"]=="true":
                isd=True
            else:
                isd=False
        else:
            isd=False
        return static_file(val,root="/sdcard",download=isd)
@route("/")
def answer():
    global head,css,body,tail
    fls=listdir("/sdcard")
    fls.sort()
    htm=head%("内部存储",css)
    for f in fls:
        if isdir("/sdcard/"+f):
            clz="isp"
        else:
            clz="isf"
        htm+=body%("/"+f,clz,f)
    htm+=tail
    return htm
run(server="tornado",host="0.0.0.0",port=4084)