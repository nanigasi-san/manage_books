from flask import Blueprint,render_template,request,redirect,url_for,jsonify
from web.bookdb import get_db
import json

bp = Blueprint("books",__name__)

@bp.route("/newbook",methods=["POST"])
def newbook():
    posted_data = request.data.decode("utf-8")
    data = json.loads(posted_data)
    title = data["title"]
    author = data["author"]
    genre = data["genre"]
    if not ((1<=len(title)<=20) and (1<=len(author)<=20) and (1<=len(genre)<=20)):
        return jsonify(res=":(",message="長さが1<=n<=20の範囲外です")
    db = get_db()
    titles = db.execute(
    "SELECT * FROM books WHERE title = '{0}'".format(title)
    ).fetchall()
    titles = [t[0] for t in titles]
    if (len(titles) == 1):
        return jsonify(res=":(",message="タイトルが重複しています")
    db.commit()
    db.execute(
    "INSERT INTO books (title, author, genre, lending, username, timestamp) VALUES (?, ?, ?, ?, ?, ?)",
    (title,author,genre,False,'','')
    )
    db.commit()
    return jsonify(res=":)")


@bp.route("/delbook",methods=["POST"])
def delbook():
    try:
        posted_data = request.data.decode("utf-8")
        data = json.loads(posted_data)
        title = data["title"]
        db = get_db()
        db.execute(
        "DELETE FROM books WHERE title = '{0}'".format(title)
        )
        db.commit()
        return jsonify(res=":)")
    except:
        return jsonify(res=":(")


@bp.route("/books_data",methods=["GET"])
def books_data():
    try:
        db = get_db()
        titles = db.execute(
        "SELECT title,username,timestamp FROM books"
        ).fetchall()
        db.commit()
        titles = [(title[0],title[1],title[2]) for title in titles]
        print(titles)
        return jsonify(res=":)",data=titles)
    except:
        return jsonify(res=":(")