from flask_testing import TestCase
from application import app, db
from flask import url_for
from application.models import Country
from application.models import Player


class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        # Will be called before every test
        # Create table schema
        db.create_all()
        db.session.add(Country(description="Run unit test"))
       # db.session.add(Player(description="Run unit test"))
        db.session.commit()


    def tearDown(self):
        # Will be called after every test
        db.session.remove()
        db.drop_all()

