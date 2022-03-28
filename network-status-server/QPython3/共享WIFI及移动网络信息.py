#-*-coding:utf-8;-*-
#qpy:3
#qpy:console
from json import dumps
from time import time,sleep
from androidhelper import Android
from threading import Thread,Lock
from bottle import hook,response,route,run
from tornado.options import parse_command_line
parse_command_line()
ad=Android()
sigtime=0.0
cando=Lock()
def killer():
    global ad,cando,sigtime
    while True:
        cando.acquire()
        if sigtime!=0.0 and time()>sigtime:
            ad.stopTrackingSignalStrengths()
            print("Stop tracking signal strength.")
            sigtime=0.0
        cando.release()
        sleep(0.02)
@hook("after_request")
def admit():
    response.headers["Content-Type"]="application/json"
    response.headers["Access-Control-Allow-Origin"]="*"
    response.headers["Access-Control-Allow-Headers"]="*"
@route("/wifi")
def answer():
    global ad
    ad.wifiStartScan()
    sleep(2.5)
    res=ad.wifiGetScanResults().result
    return dumps({"scan_results":res})
@route("/network_operator")
def answer():
    global ad
    mcres=ad.getNetworkOperator().result
    return dumps({"network_operator":mcres})
@route("/cell_location")
def answer():
    global ad
    clres=ad.getCellLocation().result
    return dumps({"cell_location":{"lac":clres["lac"],"cid":clres["cid"]}})
@route("/phone_information")
def answer():
    global ad
    mcres=ad.getNetworkOperator().result
    clres=ad.getCellLocation().result
    return dumps({"network_operator":mcres,"cell_location":{"lac":clres["lac"],"cid":clres["cid"]}})
@route("/signal_strength")
def answer():
    global ad,cando,sigtime
    cando.acquire()
    if sigtime==0.0:
        ad.startTrackingSignalStrengths()
        print("Start tracking signal strength.")
    res=ad.readSignalStrengths().result
    sigtime=time()+10
    cando.release()
    return dumps({"signal_strength":res})
@route("/all_information")
def answer():
    global ad,cando,sigtime
    cando.acquire()
    if sigtime==0.0:
        ad.startTrackingSignalStrengths()
        print("Start tracking signal strength.")
    mcres=ad.getNetworkOperator().result
    clres=ad.getCellLocation().result
    res=ad.readSignalStrengths().result
    sigtime=time()+10
    cando.release()
    return dumps({"network_operator":mcres,"cell_location":{"lac":clres["lac"],"cid":clres["cid"]},"signal_strength":res})
@route("/")
def answer():
    global ad,cando,sigtime
    cando.acquire()
    if sigtime==0.0:
        ad.startTrackingSignalStrengths()
        print("Start tracking signal strength.")
    mcres=ad.getNetworkOperator().result
    clres=ad.getCellLocation().result
    res=ad.readSignalStrengths().result
    sigtime=time()+10
    cando.release()
    return dumps({"network_operator":mcres,"cell_location":{"lac":clres["lac"],"cid":clres["cid"]},"signal_strength":res})
Thread(target=killer).start()
run(server="tornado",host="0.0.0.0",port=4082)