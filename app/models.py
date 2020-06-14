from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

db = SQLAlchemy()


def init_app(app):
    db.app = app
    db.init_app(app)
    return db


def create_tables(app):
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    if not database_exists(engine.url):
        create_database(engine.url)
        db.metadata.create_all(engine)
        db.session.commit()
    return engine


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(60), nullable=False)
    addressLine1 = db.Column(db.String(32), nullable=True)
    addressLine2 = db.Column(db.String(32), nullable=True)
    city = db.Column(db.String(32), nullable=True)
    district = db.Column(db.String(32), nullable=True)
    country = db.Column(db.String(32), nullable=False)

    def create(self, email):
        self.email = email
        return self



