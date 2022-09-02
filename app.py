"""Blogly application."""

from flask import Flask, render_template, redirect, flash, session, request
from models import db, connect_db, User, Post

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
def show_user_form():
    return render_template('new_user_form.html')


@app.route("/users/new", methods=["POST"])
def handle_user_form():
    new_user = User(
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
        image_url=request.form['image_url'] or None)

    db.session.add(new_user)
    db.session.commit()

    return redirect("/")

@app.route('/users/<int:user_id>')
def show_user_details(user_id):
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

@app.route('/users/<int:user_id>/posts/new', methods=["GET"])
def show_post_form(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('new_post_form.html', user=user)

@app.route("/users/<int:user_id>/posts/new", methods=["POST"])
def handle_post_form(user_id):
    user= User.query.get_or_404(user_id)
    new_post= Post(
        title=request.form['title'],
        content=request.form['content'],
        user=user
    )
    db.session.add(new_post)
    db.session.commit()

    return redirect(f"/users/{user_id}")

@app.route('/posts/<int:post_id>')
def posts_show(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('show_posts.html', post=post)

@app.route('/posts/<int:post_id>/edit')
def posts_edit(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('edit_post.html', post=post)

@app.route('/posts/<int:post_id>/edit', methods=["POST"])
def posts_update(post_id):
    post = Post.query.get_or_404(post_id)
    post.title = request.form['title']
    post.content = request.form['content']
    db.session.add(post)
    db.session.commit()

    return redirect(f"/users/{post.user_id}")

@app.route('/posts/<int:post_id>/delete', methods=["POST"])
def posts_destroy(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()

    return redirect(f"/users/{post.user_id}")


