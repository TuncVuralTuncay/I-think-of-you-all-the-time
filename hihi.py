import os
import requests
import time
while True:
    rl = requests.get("http://tuncvr-api.glitch.me/kntrlsars")
    a = rl.json()
    if(a == True):
        os.system("mpv sound.mp3")
    elif(a == False):
        print("a")
    time.sleep(15)