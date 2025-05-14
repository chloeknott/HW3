from app import db
from datetime import datetime
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    password = db.Column(db.String(128), nullable=False)
    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    body = db.Column(db.String(256))
    # timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    # def __repr__(self):
    #  return '<Posts {}>'.format(self.body)

# class Age(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     age = db.Column(db.String(32))

# Define the Recipe model/table for storing recipes
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key for each recipe
    title = db.Column(db.String(100), nullable=False)  # Recipe title
    description = db.Column(db.String(255), nullable=False)  # Short description of the recipe
    ingredients = db.Column(db.Text, nullable=False)  # Ingredients required
    instructions = db.Column(db.Text, nullable=False)  # Instructions to prepare the recipe
    username = db.Column(db.String(32))  # Username of the creator (optional)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    recipe_id = db.Column(db.String(32), nullable=False)
    username = db.Column(db.String(32), nullable=False)
