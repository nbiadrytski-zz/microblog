from datetime import datetime

from app import db


class User(db.Model):  # db.Model is a base class for all models from Flask-SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # posts is not an actual database field,
    # but a high-level view of the relationship between users and posts
    # For a one-to-many relationship,
    # a db.relationship field is normally defined on the "one" side,
    # and is used as a convenient way to get access to the "many".
    # If I have a user stored in u,
    # the expression u.posts will run a database query that returns all the posts written by that user.
    # backref argument defines the name of a field
    # that will be added to the objects of the "many" class that points back at the "one" object.
    # This will add a post.author expression that will return the user given a post.
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}>'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    # timestamp is indexed, which is useful if you want to retrieve posts in chronological order
    # utcnow: timestamps will be converted to user's local time when they are displayed
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # user_id references an id value from the users table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Post {self.body}>'
