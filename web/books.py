from flask import Blueprint,render_template,request,redirect,url_for,jsonify
from web.bookdb import get_db

bp = Blueprint("books",__name__)
@bp.route("/",methods=["GET","POST"])
def index():
    db = get_db()
    alldata = db.execute("SELECT * FROM books").fetchall()
    if request.method == "POST":
        genre = request.form["genre"]
        message = '分野が「{0}」を含む本は'.format(genre)

        searchdata = db.execute("SELECT * FROM books WHERE genre like '%"+genre+"%'").fetchall()

        if len(searchdata)>0:
            message += "以下の通りです"
        else:
            searchdata = alldata
            message += "見つかりませんでした"
        return render_template("index.html",message=message,books=searchdata)
    else:
        message="お探しの分野は何ですか"
        return render_template("index.html",message=message,books=alldata)

def get_testdata():
    return [
    {"id":1,"title":"プリンキピア","author":"ニュートン","genre":"物理"},
    {"id":2,"title":"化学原論","author":"ラボアジェ","genre":"科学"},
    {"id":3,"title":"整数論","author":"ガウス","genre":"数学"},
    {"id":4,"title":"天体の回転について","author":"コペルニクス","genre":"物理"},
    {"id":5,"title":"熱の解析的理論","author":"フーリエ","genre":"数学"},
    {"id":6,"title":"発微算法","author":"関考和","genre":"数学"},
    ]

def search_testdata(key,sword):
    alldata = get_testdata()
    return [data for data in alldata if (sword in data[key])]

@bp.route("/newbook",methods=["GET","POST"])
def newbook():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        genre = request.form["genre"]
        db = get_db()
        titles = db.execute(
        "SELECT * FROM books WHERE title = '{0}'".format(title)
        ).fetchall()
        titles = [t[0] for t in titles]
        if len(titles) == 1:
            return render_template("newbook.html")
        db.commit()
        db.execute(
        "INSERT INTO books (title, author, genre, lending, username) VALUES (?, ?, ?, ?, ?)",
        (title,author,genre,False,'')
        )
        db.commit()
        return redirect(url_for("books.index"))
    else:
        return render_template("newbook.html")

@bp.route("/delbook",methods=["GET","POST"])
def delbook():
    if request.method == "POST":
        title = request.form["title"]
        db = get_db()
        db.execute(
        "DELETE FROM books WHERE title = '{0}'".format(title)
        )
        db.commit()
        return redirect(url_for("books.index"))
    else:
        return render_template("delbook.html")


@bp.route("/books_data",methods=["GET"])
def books_data():
    try:
        db = get_db()
        titles = db.execute(
        "SELECT title FROM books"
        ).fetchall()
        db.commit()
        titles = [title[0] for title in titles]
        return jsonify(res=":)",data=titles)
    except:
        return jsonify(res=":(")