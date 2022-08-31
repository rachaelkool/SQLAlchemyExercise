"""Seed file to make sample data for user db."""

from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add pets
user1 = User(first_name='Mary', last_name='Jenkins')


# Add new objects to session, so they'll persist
db.session.add(user1)

# Commit--otherwise, this never gets saved!
db.session.commit()