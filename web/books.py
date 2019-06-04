from flask import Blueprint,render_template,request,redirect,url_for
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
    pass