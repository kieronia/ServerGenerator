import requests #pip install requests
import time

webhookurl = "https://discordapp.com/api/webhooks/123123/abcdefg" #WEBHOOK HERE

while True:
    word = requests.get("https://random-word-api.herokuapp.com/word?number=1").text[2:-2]
    dataaa = {
        "content" : f"discord.gg/{word}", #! Don't touch anything here tbh
        "username" : "Discord.gg Server 'generator'", #! Username for webhook
        "avatar_url" : "https://www.pngkit.com/png/detail/19-194063_discord-logo-discord-icon.png   ", #! Profile Picture For Webhook (eg. https://www.ascii.wtf/ascii.png)
    }

    requests.post(webhookurl, data=dataaa)
    print(f"discord.gg/{word}")
    time.sleep(1)#change if u wanna but discord ratelimits will  prevent messages being sent from the webhook
