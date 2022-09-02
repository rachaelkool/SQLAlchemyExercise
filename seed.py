"""Seed file to make sample data for user db."""

from models import User, db, Post
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()
Post.query.delete()

# Add user/ post
user1 = User(first_name='Mary', last_name='Jenkins')
post1 = Post(title="Test", content="Hi there", user_id= 1)


# Add new objects to session, so they'll persist
db.session.add(user1)
db.session.commit()

db.session.add(post1)

# Commit--otherwise, this never gets saved!
db.session.commit()