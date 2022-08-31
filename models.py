"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL= "https://i.pinimg.com/custom_covers/222x/85498161615209203_1636332751.jpg"

def connect_db(app):
    db.app = app    
    db.init_app(app)


class User(db.Model): 
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    first_name = db.Column(db.String(50), nullable=False)

    last_name = db.Column(db.String(50), nullable=False)

    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)