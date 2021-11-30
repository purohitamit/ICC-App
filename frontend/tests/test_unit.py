from flask_testing import TestCase
from application import app
from flask import url_for



class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    
