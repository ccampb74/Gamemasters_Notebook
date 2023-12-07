import unittest
import random
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.app.models import Campaigns


class MyTestCase(unittest.TestCase):
    def test_campaign_creation(self):
        rand_id = random.randint
        obj = Campaigns(
            id=rand_id,
            name="Test Name",
            general_story="Test Story",
            game_master_id="c",
            players="v",
        )
        self.assertEqual(obj.id, rand_id)
