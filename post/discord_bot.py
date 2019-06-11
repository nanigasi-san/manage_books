import discord
import requests
import json

TOKEN = "NTExNjk1MDQxODc4NTU2Njk0.XP9KQw.p1blUZuBk6LURPQtGCytbozHYP8"#アクセストークン
client = discord.Client()
def post_and_responce(data):
    URL = "http://127.0.0.1:5000/rental"
    res = requests.post(URL,data=data).json()
    return res

@client.event
async def on_ready():
    userlist = client.users
    for user in userlist:
        print(user)

@client.event
async def on_message(msg):
    channel = msg.channel
    if msg.author == client.user:
        return

    if msg.content[:5] == "$rent":
        book_title = msg.content[6:]
        username = msg.author
        data = {"lending": True,
                "title": book_title}
        res = post_and_responce(json.dumps(data))
        await channel.send(str(res))

    if msg.content[:7] == "$return":
        book_title = msg.content[8:]
        username = msg.author
        data = {"lending": False,
                "title": book_title}
        res = post_and_responce(json.dumps(data))
        await channel.send(str(res["res"]))


client.run(TOKEN)