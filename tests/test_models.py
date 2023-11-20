# NOT YET BUILT
import inspect
import traceback

import bcrypt
import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.models import User


@pytest.fixture()
def app():
    app = Flask("models_test")

    with app.app_context():
        app.config['USER SIGNUP'] = 'User Sign Up'
        app.config['USER SIGNIN'] = 'User Sign In'

        db = SQLAlchemy()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
        db.init_app(app)

    return app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


# def test_given_a_valid_user_successfully_in_db():
#     db = SQLAlchemy()
#     password = "hi"
#     hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
#
#     new_user = User(
#         email="s",
#         username="s",
#         creation_date="now",
#         password=hashed
#     )
#     db.session.add(new_user)
#     db.session.commit()
#     print("test failed to add user", inspect.currentframe().f_code.co_name, traceback.print_tb())
