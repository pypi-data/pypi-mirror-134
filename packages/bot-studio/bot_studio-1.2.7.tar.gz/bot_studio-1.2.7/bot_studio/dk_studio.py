import subprocess
import os
import inspect
from .GetData import gettheuserid
from threading import Thread
folder=inspect.getfile(gettheuserid).split("site-packages")[0]
folder=folder+"site-packages\\datakund_bot_studio\\"
def start_studio():
    try:
        folderr=folder+"DataKund.exe"
        subprocess.run([folderr, "start"])
        #os.system(folder+"DataKund.exe start")
    except Exception as e:
        print("Exception is",e)
def main():
    save_login_info()
    Thread(target = start_studio).start()