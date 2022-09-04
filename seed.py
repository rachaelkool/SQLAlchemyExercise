"""Seed file to make sample data for user db."""

from models import User, db, Post, PostTag, Tag
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()
Post.query.delete()

# Add user/ post/ tag
user1 = User(first_name='Mary', last_name='Jenkins')
post1 = Post(title="Test", content="Hi there", user_id= 1)
tag1 = Tag(name="cool")
post_tag = PostTag(post_id=1, tag_id=1)

db.session.add(user1)
db.session.commit()

db.session.add(post1)
db.session.commit()

db.session.add(tag1)
db.session.commit()

db.session.add(post_tag)
db.session.commit()