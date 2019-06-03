from flask import Flask
def create_app():
    app = Flask(__name__)

    @app.route("/test")
    def apptest():
        return "アプリケーションセットアップ完了！"
        
    return app