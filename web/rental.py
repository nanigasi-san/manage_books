from flask import Blueprint,render_template,request,redirect,url_for,jsonify
from web.bookdb import get_db
import json
bp = Blueprint("rental",__name__)
@bp.route("/rental",methods=["POST"])
def rental():
    db = get_db()
    try:
        data = json.loads(request.data.decode("utf-8"))
        print(data)
        db.execute(
        "UPDATE books set lending = {0} WHERE title = '{1}'".format(data["lending"],data["title"])
        )

        db.execute(
        "UPDATE books set username = '{0}' WHERE title = '{1}'".format(data["username"],data["title"])
        )
        db.commit()

        db.execute(
        "UPDATE books set timestamp = '{0}' WHERE title = '{1}'".format(data["timestamp"],data["title"])
        )
        db.commit()
        return jsonify(res=":)")
    except:
        return jsonify(res=":(")