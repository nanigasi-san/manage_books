import discord
import requests
import json

TOKEN = "NTExNjk1MDQxODc4NTU2Njk0.XP9KQw.p1blUZuBk6LURPQtGCytbozHYP8"#アクセストークン
client = discord.Client()
def post_and_responce(data):
    URL = "http://127.0.0.1:5000/rental"
    res = requests.post(URL,data=data).json()
    return res

def get_books():
    URL = "http://127.0.0.1:5000/books_data"
    res = requests.get(URL).json()
    return (res["data"],res["res"])

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
        res = post_and_responce(json.dumps(data))
        await channel.send(str(res["res"]))

    if msg.content[:7] == "$return":
        book_title = msg.content[8:]
        username = str(msg.author)
        data = {"lending": False,
                "title": book_title,
                "username": ''}
        res = post_and_responce(json.dumps(data))
        await channel.send(str(res["res"]))

    if msg.content == "$books":
        books,_ = get_books()
        book_str = "\n".join(books)
        await channel.send(book_str)

client.run(TOKEN)