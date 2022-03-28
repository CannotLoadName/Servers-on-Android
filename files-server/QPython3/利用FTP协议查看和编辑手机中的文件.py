#-*-coding:utf-8;-*-
#qpy:3
#qpy:console
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
au=DummyAuthorizer()
au.add_anonymous("/sdcard",perm="elr")
au.add_user("sdcard","admin","/sdcard",perm="elradfmwMT")
au.add_user("qpython","admin","/data/data/com.hipipal.qpy3/files",perm="elradfmwMT")
au.add_user("system","admin","/system",perm="elr")
ha=FTPHandler
ha.authorizer=au
ser=FTPServer(("0.0.0.0",4090),ha)
ser.serve_forever()