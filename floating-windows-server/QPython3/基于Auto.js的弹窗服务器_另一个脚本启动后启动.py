#-*-coding:utf-8;-*-
#qpy:3
#qpy:console
codjs='var client=new java.net.Socket("localhost",%d);var in_byte=client.getInputStream();var in_char=new java.io.InputStreamReader(in_byte,"utf-8");var buffer=new java.io.BufferedReader(in_char);var out_str=client.getOutputStream();var writer=new java.io.PrintWriter(out_str);var line0;var res=null;%swhile(true){line0=buffer.readLine();if(line0!=null){if(res==null){writer.write("OK\\n");writer.flush();}else{writer.write(JSON.stringify(res)+"\\n");writer.flush();break;}}else{break;}}writer.close();out_str.close();buffer.close();in_char.close();in_byte.close();client.close();'
codhead='var frm=floaty.window(<frame><vertical bg="#bf9acd32" w="auto" h="auto"><vertical bg="#cfffffff" margin="5dp" padding="5dp" w="auto" h="auto"><horizontal w="auto" h="auto">%s<vertical layout_gravity="center_vertical" w="auto" h="auto">%s%s</vertical></horizontal><horizontal layout_gravity="right" w="auto" h="auto">%s</horizontal></vertical></vertical></frame>);frm.setAdjustEnabled(true);frm.exitOnClose();'
tmpicon='<img id="icon" layout_gravity="top" marginRight="%ddp" w="40dp" h="40dp"/>'
tmptext='<text text="%s" textSize="14sp" textColor="#ff000000" ellipsize="marquee" w="auto" h="auto"/>'
tmpgroup='<radiogroup w="auto" h="auto">%s</radiogroup>'
tmpradio='<radio id="radio%d" text="%s" checked="%s" textSize="14sp" textColor="#ff000000" w="auto" h="auto"/>'
tmpcheck='<checkbox id="check%d" text="%s" checked="%s" textSize="14sp" textColor="#ff000000" w="auto" h="auto"/>'
tmpinput='<input id="input" text="%s" hint="%s" password="%s" singleLine="%s" focusable="true" textSize="14sp" textColor="#ff000000" textSizeHint="14sp" textColorHint="#ff999999" minWidth="100dp" w="auto" h="auto"/>'
tmpseek='<horizontal gravity="center_vertical" w="auto" h="auto"><seekbar id="seek" max="%d" progress="%d" w="180dp" h="auto"/><text id="sview" text="%d" textSize="14sp" textColor="#ff000000" w="auto" h="auto"/></horizontal>'
tmpbtn='<button id="btn%d" text="%s" textSize="14sp" w="auto" h="auto"/>'
codinput='frm.input.on("touch_down",()=>{frm.requestFocus();frm.input.requestFocus();});'
codseek='var progress=%d;frm.seek.setOnSeekBarChangeListener({onProgressChanged:function(sb,prog,user){progress=prog;frm.sview.setText(String(prog));}});'
codbtn='frm.btn%d.on("click",()=>{res={"clicked":%d%s}});'
codicon='try{frm.icon.setSource("%s");}catch(err){toast(err);console.error(err);}'
def delbol(i):
    if i:
        return "true"
    else:
        return "false"
def delstr(i):
    return i.replace("&","&amp;amp;").replace("<","&amp;lt;").replace(">","&amp;gt;").replace("'","&amp;apos;").replace('"',"&amp;quot;").replace("\n","").replace("\r","")
def formlist(i,typ):
    if type(i)!=list:
        i=[i]
    for itm in range(0,len(i)):
        if type(i[itm])!=typ:
            try:
                i[itm]=typ(i[itm])
            except:
                del(i[itm])
    return i
def code(x):
    if x.__contains__("text"):
        if type(x["text"])!=str:
            try:
                x["text"]=str(x["text"])
            except:
                del(x["text"])
    if x.__contains__("text"):
        global tmptext
        text=""
        for i in x["text"].split("\n"):
            text+=tmptext%(delstr(i))
    else:
        text=""
    if x.__contains__("type"):
        if x["type"]=="radios":
            global tmpgroup,tmpradio
            if x.__contains__("items"):
                x["items"]=formlist(x["items"],str)
            else:
                x["items"]=[]
            if x.__contains__("default"):
                if type(x["default"])!=int:
                    try:
                        x["default"]=int(x["default"])
                    except:
                        del(x["default"])
            if not x.__contains__("default"):
                x["default"]=-1
            tmp=""
            addxx=',"value":['
            for i in range(0,len(x["items"])):
                tmp+=tmpradio%(i,delstr(x["items"][i]),delbol(i==x["default"]))
                if i>0:
                    addxx+=","
                addxx+="frm.radio%d.isChecked()"%(i)
            addxx+="]"
            inc=tmpgroup%(tmp)
            addinp=""
        elif x["type"]=="checkboxes":
            global tmpcheck
            if x.__contains__("items"):
                x["items"]=formlist(x["items"],str)
            else:
                x["items"]=[]
            if x.__contains__("default"):
                x["default"]=formlist(x["default"],int)
            else:
                x["default"]=[]
            inc=""
            addxx=',"value":['
            for i in range(0,len(x["items"])):
                inc+=tmpcheck%(i,delstr(x["items"][i]),delbol(i in x["default"]))
                if i>0:
                    addxx+=","
                addxx+="frm.check%d.isChecked()"%(i)
            addxx+="]"
            addinp=""
        elif x["type"]=="input":
            global tmpinput,codinput
            if x.__contains__("multi"):
                if type(x["multi"])!=bool:
                    try:
                        x["multi"]=bool(x["multi"])
                    except:
                        del(x["multi"])
            if x.__contains__("password"):
                if type(x["password"])!=bool:
                    try:
                        x["password"]=bool(x["password"])
                    except:
                        del(x["password"])
            if x.__contains__("hint"):
                if type(x["hint"])!=str:
                    try:
                        x["hint"]=str(x["hint"])
                    except:
                        del(x["hint"])
            if x.__contains__("default"):
                if type(x["default"])!=str:
                    try:
                        x["default"]=str(x["default"])
                    except:
                        del(x["default"])
            if not x.__contains__("multi"):
                x["multi"]=False
            if not x.__contains__("password"):
                x["password"]=False
            if not x.__contains__("hint"):
                x["hint"]=""
            if not x.__contains__("default"):
                x["default"]=""
            inc=tmpinput%(delstr(x["default"]),delstr(x["hint"]),delbol(x["password"]),delbol(not x["multi"]))
            addxx=',"value":frm.input.text()'
            addinp=codinput
        elif x["type"]=="seekbar":
            global tmpseek,codseek
            if x.__contains__("max"):
                if type(x["max"])!=int:
                    try:
                        x["max"]=int(x["max"])
                    except:
                        del(x["max"])
            if x.__contains__("default"):
                if type(x["default"])!=int:
                    try:
                        x["default"]=int(x["default"])
                    except:
                        del(x["default"])
            if not x.__contains__("max"):
                x["max"]=100
            if not x.__contains__("default"):
                x["default"]=0
            inc=tmpseek%(x["max"],x["default"],x["default"])
            addxx=',"value":progress'
            addinp=codseek%(x["default"])
        else:
            inc=""
            addxx=""
            addinp=""
    else:
        inc=""
        addxx=""
        addinp=""
    if x.__contains__("icon"):
        if type(x["icon"])!=str:
            try:
                x["icon"]=str(x["icon"])
            except:
                del(x["icon"])
    if x.__contains__("icon"):
        global tmpicon,codicon
        if text!="" or inc!="":
            hasb=3
        else:
            hasb=0
        icon=tmpicon%(hasb)
        addicon=codicon%(repr(x["icon"])[1:-1].replace('"','\\"'))
    else:
        icon=""
        addicon=""
    global tmpbtn,codbtn
    if x.__contains__("button"):
        x["button"]=formlist(x["button"],str)
    else:
        x["button"]=["确定"]
    button=""
    addbtn=""
    for i in range(0,len(x["button"])):
        button+=tmpbtn%(i,delstr(x["button"][i]))
        addbtn+=codbtn%(i,i,addxx)
    global codhead
    return codhead%(icon,text,inc,button)+addicon+addinp+addbtn
from json import loads,dumps
from time import clock,sleep
from socket import socket,AF_INET,SOCK_STREAM
from threading import Thread
def dome():
    global codjs,autocli,client,wait
    myclient=client
    wait=False
    rec=loads(myclient.recv(65536).decode("utf-8").strip("\n"))
    tmpser=socket(AF_INET,SOCK_STREAM)
    port=16384
    while True:
        try:
            tmpser.bind(("127.0.0.1",port))
        except:
            port+=1
        else:
            break
    tmpser.listen(1)
    ulticode=codjs%(port,code(rec))
    autocli.send(("弹窗-%d\n%s\n"%(port,ulticode)).encode("utf-8"))
    tmpcli,addr=tmpser.accept()
    print("Connected to Auto.js %s:%d"%addr)
    tmpcli.setblocking(False)
    firstime=True
    tsend="Keep\n".encode("utf-8")
    while True:
        try:
            tmpcli.send(tsend)
        except:
            resp={"clicked":-1}
            break
        else:
            if firstime:
                brktime=clock()+1.5
                firstime=False
            else:
                brktime=clock()+0.5
            while True:
                try:
                    trecv=tmpcli.recv(65536)
                except:
                    if clock()>brktime:
                        sucrecv=False
                        break
                else:
                    sucrecv=True
                    break
            if sucrecv:
                res=trecv.decode("utf-8").strip("\n")
                if res=="OK":
                    sleep(0.02)
                elif res=="":
                    resp={"clicked":-1}
                    break
                else:
                    resp=loads(res)
                    break
            else:
                resp={"clicked":-1}
                break
    if rec.__contains__("type") and resp.__contains__("value"):
        if rec["type"]=="radios":
            tm=-1
            for i in range(0,len(resp["value"])):
                if resp["value"][i]==True:
                    tm=i
                    break
            resp["value"]=tm
        elif rec["type"]=="checkboxes":
            tm=[]
            for i in range(0,len(resp["value"])):
                if resp["value"][i]==True:
                    tm+=[i]
            resp["value"]=tm
    myclient.send((dumps(resp)+"\n").encode("utf-8"))
    myclient.close()
    tmpcli.close()
    tmpser.close()
autocli=socket(AF_INET,SOCK_STREAM)
autocli.connect(("localhost",1860))
server=socket(AF_INET,SOCK_STREAM)
server.bind(("0.0.0.0",4086))
server.listen(16)
while True:
    client,addr=server.accept()
    print("Connected to client %s:%d"%addr)
    wait=True
    Thread(target=dome).start()
    while wait:
        pass