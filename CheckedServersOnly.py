
import threading, requests
import time
import random

webhookurl = "https://discordapp.com/api/" #put yo webhook url here!


def my_function(URL, proxy):
    proxies = {'https': 'https://%s' % (proxy)}
    valid = requests.get(URL, proxies = proxies,timeout=15)
    if valid.status_code == 200:
        dataaa = {
            "content" : f"@everyone \nServer found!\ndiscord.gg/{word}", #webhook message
            "username" : "Discord.gg Server 'generator'", #webhook username
            "avatar_url" : "https://www.pngkit.com/png/detail/19-194063_discord-logo-discord-icon.png   ", #webhook pfp
        }
        requests.post(webhookurl, data=dataaa)
        print(f"[+] discord.gg/{word} - VALID SERVER FOUND!")
        f = open("hq.txt", "a")
        f.write(f"{proxy}\n")
        f.close()
    else:
        print(f"[-] discord.gg/{word}")    
        f = open("hq.txt", "a")
        f.write(f"{proxy}\n")
        f.close()
while True:
    lines = open('proxies.txt').read().splitlines()
    randomproxy =random.choice(lines)
    word = requests.get("https://random-word-api.herokuapp.com/word?number=1").text[2:-2]
    threading.Thread(target = my_function, args = (f'https://discord.com/api/v8/invites/{word}', randomproxy,)).start()
    time.sleep(0.1)
#this version uses proxies and checks the servers to only try and send valids
