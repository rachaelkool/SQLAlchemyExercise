from unittest import TestCase

from app import app
from models import db, User

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

app.config['TESTING'] = True

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class PetViewsTestCase(TestCase):
    def setUp(self):
        User.query.delete()

        user = User(first_name='Goldie', last_name='Doo')
        db.session.add(user)
        db.session.commit()

        self.user_id = user.id

    def tearDown(self):
        db.session.rollback()

    def test_user_list(self):
        with app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Goldie', html)

    def test_user_form(self):
        with app.test_client() as client:
            resp = client.get("/users/new")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h2>Create a User</h2>', html)

    def test_add_user(self):
        with app.test_client() as client:
            d = {"first_name": "Nelson", "last_name": "Peterson", "image_url": "https://www.peakpx.com/en/search?q=profile+pic"}
            resp = client.post("/users/new", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Nelson", html)


# need to make last test work
    def test_edit(self):
        with app.test_client() as client:
            resp = client.get("/users/<int:user_id>/edit")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h2>Edit a User</h2>', html)


       
