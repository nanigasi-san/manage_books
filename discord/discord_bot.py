import discord
import requests
from json import dumps
from datetime import datetime

TOKEN = "NTExNjk1MDQxODc4NTU2Njk0.XP9KQw.p1blUZuBk6LURPQtGCytbozHYP8"#アクセストークン
client = discord.Client()
owner_id_list = [474487324093317130,465433493388656651]

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
    if (msg.author == client.user) or (msg.author.id not in owner_id_list):
        return

    if msg.content[:5] == "$rent":
        timestamp = datetime.now().strftime("%Y/%m/%d-%H:%M:%S")
        book_title = msg.content[6:]
        username = str(msg.author)
        data = {"lending": True,
                "title": book_title,
                "username": username,
                "timestamp": timestamp}
        res = post_and_responce("rental",dumps(data))
        await channel.send(res["res"])

    if msg.content[:7] == "$return":
        book_title = msg.content[8:]
        username = str(msg.author)
        data = {"lending": False,
                "title": book_title,
                "username": '',
                "timestamp": ''}
        res = post_and_responce("rental",dumps(data))
        await channel.send(res["res"])

    if msg.content == "$books":
        books = get_books()["data"]
        title_user = [str(t)+"："+str(u)+"："+str(s) for t,u,s in books]
        book_str = "\n".join(title_user)
        await channel.send(book_str)

    if msg.content[:4] == "$add":
        book_data = msg.content[5:].split("\n")
        data = {"title":book_data[0],
                "author":book_data[1],
                "genre":book_data[2]}
        res = post_and_responce("newbook",dumps(data))
        if "message" in res:
            await channel.send(res["res"]+"\n"+res["message"])
        else:
            await channel.send(res["res"])

    if msg.content[:4] == "$del":
        book_title = msg.content[5:]
        data = {"title":book_title}
        res = post_and_responce("delbook",dumps(data))
        await channel.send(res["res"])

    if msg.content == "$zen":
        await channel.send("""
        The Zen of Python, by Tim Peters
        Beautiful is better than ugly.
        Explicit is better than implicit.
        Simple is better than complex.
        Complex is better than complicated.
        Flat is better than nested.
        Sparse is better than dense.
        Readability counts.
        Special cases aren't special enough to break the rules.
        Although practicality beats purity.
        Errors should never pass silently.
        Unless explicitly silenced.
        In the face of ambiguity, refuse the temptation to guess.
        There should be one-- and preferably only one --obvious way to do it.
        Although that way may not be obvious at first unless you're Dutch.
        Now is better than never.
        Although never is often better than *right* now.
        If the implementation is hard to explain, it's a bad idea.
        If the implementation is easy to explain, it may be a good idea.
        Namespaces are one honking great idea -- let's do more of those!
        """)

client.run(TOKEN)