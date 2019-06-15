import discord
import requests
from json import dumps

TOKEN = "NTExNjk1MDQxODc4NTU2Njk0.XP9KQw.p1blUZuBk6LURPQtGCytbozHYP8"#アクセストークン
client = discord.Client()
def post_and_responce(subject,data):
    URL = "http://127.0.0.1:5000/"+subject
    res = requests.post(url=URL,data=data)
    return res.json()

def get_books():
    URL = "http://127.0.0.1:5000/books_data"
    res = requests.get(URL)
    return res.json()

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
        username = str(msg.author)
        data = {"lending": True,
                "title": book_title,
                "username": username}
        res = post_and_responce("rental",dumps(data))
        await channel.send(res["res"])

    if msg.content[:7] == "$return":
        book_title = msg.content[8:]
        username = str(msg.author)
        data = {"lending": False,
                "title": book_title,
                "username": ''}
        res = post_and_responce("rental",dumps(data))
        await channel.send(res["res"])

    if msg.content == "$books":
        books = get_books()["data"]
        title_user = [str(t)+"："+str(u) for t,u in books]
        book_str = "\n".join(title_user)
        await channel.send(book_str)
    
    if msg.content[:4] == "$add":
        book_data = msg.content[5:].split("\n")
        data = {"title":book_data[0],
                "author":book_data[1],
                "genre":book_data[2]}
        res = post_and_responce("newbook",dumps(data))
        await channel.send(res["res"])

    if msg.content[:4] == "$del":
        book_title = msg.content[5:]
        data = {"title":book_title}
        res = post_and_responce("delbook",dumps(data))
        await channel.send(res["res"])

client.run(TOKEN)