from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    from . import books,rental
    app.register_blueprint(books.bp)
    app.register_blueprint(rental.bp)

    from . import bookdb
    bookdb.init_app(app)

    app.config.from_mapping(
    SECRET_KEY='temp',
    DATABASE=os.path.join(app.instance_path,'bookdb.sqlite3'),
    )
    return app