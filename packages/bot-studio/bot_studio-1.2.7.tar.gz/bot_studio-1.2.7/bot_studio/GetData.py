import socket
import string
import json
import random
def getipaddress():
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    ipaddress=ipaddress.replace('.','-')
    return ipaddress
def create_random_id():
    randomkey = ''.join(random.choices(string.ascii_uppercase +string.digits, k = 10)) 
    return randomkey
def get_user_id():
    with open("C:/DataKundStudio/pip_user_id.json") as d:
        dta=json.load(d)
    return dta["user"]["uid"],dta
def save_user_id(userid,dta):
    if(dta=={}):
        dta={"user":{"uid":userid,"email":userid}}
    dta["user"]["uid"]=userid
    dta["user"]["email"]=userid
    with open("C:/DataKundStudio/logininfo.json","w") as d:
        d.write(json.dumps(dta))
    with open("C:/DataKundStudio/pip_user_id.json","w") as d:
        d.write(json.dumps(dta))
def gettheuserid():
    dta={}
    try:
        userid,dta=get_user_id()
    except:
        userid=create_random_id()
    save_user_id(userid,dta)
    return userid