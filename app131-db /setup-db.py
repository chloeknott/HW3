from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from app import myapp_obj, db
from app import models

with myapp_obj.app_context():
    db.create_all()

    test_user = models.User(
        username="test-user",
        password="password"
    )

    recipe = models.Recipe(
        title="Pasta",
        description="Marinara",
        ingredients="Tomatoes",
        instructions="Boil water",
        username="test-user",
    )

    db.session.add(test_user)
    db.session.add(recipe)
    db.session.commit()