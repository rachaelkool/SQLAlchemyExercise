"""Blogly application."""

from flask import Flask, render_template, redirect, flash, session, request
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

db.create_all()

@app.route('/')
def list_users():
    users = User.query.all()
    return render_template('list.html', users = users)

@app.route('/users/new', methods=["GET"])
def show_form():
    return render_template('new_user_form.html')


@app.route("/users/new", methods=["POST"])
def new_user():
    new_user = User(
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
        image_url=request.form['image_url'] or None)

    db.session.add(new_user)
    db.session.commit()

    return redirect("/")

@app.route('/users/<int:user_id>')
def show_pet(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user_details.html', user = user)

@app.route('/users/<int:user_id>/edit')
def edit(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('edit.html', user = user)

# need to update user not create a new user
@app.route("/users/<int:user_id>/edit", methods=["POST"])
def update_edit(user_id):
    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']


    db.session.add(user)
    db.session.commit()

    return redirect("/")

@app.route('/users/<int:user_id>/delete', methods=["POST"])
def delete(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/")

