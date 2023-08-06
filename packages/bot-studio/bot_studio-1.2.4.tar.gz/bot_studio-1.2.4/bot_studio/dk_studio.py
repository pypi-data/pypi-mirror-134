import subprocess
import os
def start_studio():
    try:
        folderr=folder+"DataKund.exe"
        subprocess.run([folderr, "start"])
        #os.system(folder+"DataKund.exe start")
    except Exception as e:
        print("Exception is",e)
def main():
    start_studio()