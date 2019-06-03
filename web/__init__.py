from flask import Flask
def create_app():
    app = Flask(__name__)
    from . import books,authors
    app.register_blueprint(books.bp)
    app.register_blueprint(authors.bp)
    @app.route("/test")
    def apptest():
        return "アプリケーションセットアップ完了！"
        
    return app