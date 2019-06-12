from flask import Blueprint,render_template,request,redirect,url_for,jsonify
from web.bookdb import get_db
import json
bp = Blueprint("rental",__name__)
@bp.route("/rental",methods=["POST"])
def rental():
    db = get_db()
    all = list(db.execute("SELECT * FROM books").fetchall())
    id_title_dic = {}
    for row in all:
        id_title_dic[row[2]] = row[0]
    try:
        data = json.loads(request.data.decode("utf-8"))
        print(data)
        db.execute(
        "UPDATE books set lending = {0} WHERE id = {1}".format(data["lending"],id_title_dic[data["title"]]))

        db.execute(
        "UPDATE books set username = '{0}' WHERE id = {1}".format(data["username"],id_title_dic[data["title"]]))
        db.commit()
        return jsonify(res=":)")
    except:
        return jsonify(res=":(")