from flask import Blueprint,render_template

bp = Blueprint("authors",__name__)
def get_authors():
    return [
    {"author":"ニュートン",
    "bio":"ニュートンです"},
    {"author":"ラボアジェ",
    "bio":"ラボアジェです"},
    {"author":"ガウス",
    "bio":"ガウスです"},
    {"author":"コペルニクス",
    "bio":"コペルニクスです"},
    {"author":"フーリエ",
    "bio":"フーリエです"},
    {"author":"関考和",
    "bio":"関考和です"},
    ]

def search_author(author):
    alldata = get_authors()
    for data in alldata:
        if author==data["author"]:
            return data

@bp.route("/authors/<author>")
def show(author):
    return render_template("authors.html",data=search_author(author))