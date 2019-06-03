from flask import Flask
def create_app():
    app = Flask(__name__)
    from . import books
    app.register_blueprint(books.bp)

    @app.route("/test")
    def apptest():
        return "アプリケーションセットアップ完了！"
        
    return app