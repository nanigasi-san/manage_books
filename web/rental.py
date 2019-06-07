from flask import Blueprint,render_template,request,redirect,url_for,jsonify
from web.bookdb import get_db
import json
bp = Blueprint("rental",__name__)
@bp.route("/rental",methods=["POST"])
def rental():
    db = get_db()
    try:
        data = json.loads(request.data.decode("utf-8"))
        db.execute(
        "UPDATE books set now = {0} WHERE id = {1}".format(data["now"],data["id"]))
        db.commit()
        return jsonify(res=":)")
    except:
        return jsonify(res=":(")