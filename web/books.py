from flask import Blueprint,render_template

bp = Blueprint("books",__name__)
@bp.route("/")
def index():
    return render_template("index.html",books=get_testdata())

def get_testdata():
    return [
    {"id":1,"title":"プリンキピア","author":"ニュートン","genre":"物理"},
    {"id":2,"title":"化学原論","author":"ラボアジェ","genre":"科学"},
    {"id":3,"title":"整数論","author":"ガウス","genre":"数学"},
    {"id":4,"title":"天体の回転について","author":"コペルニクス","genre":"物理"},
    {"id":5,"title":"熱の解析的理論","author":"フーリエ","genre":"数学"},
    {"id":6,"title":"発微算法","author":"関考和","genre":"数学"},
    ]