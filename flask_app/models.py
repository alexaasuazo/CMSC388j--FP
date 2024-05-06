from flask_login import UserMixin
from datetime import datetime
from . import db, login_manager
from bson.objectid import ObjectId


# TODO: implement
@login_manager.user_loader
def load_user(user_id):
    return User.objects(username=user_id).first()

# TODO: implement fields
class User(db.Document, UserMixin):
    username = db.StringField(unique=True, required=True)
    email = db.StringField(unique=True, required=True)
    password = db.StringField(required=True)
    profile_pic = db.ImageField()

    # Returns unique string identifying our object
    def get_id(self):
        # TODO: implement
        return self.username


# TODO: implement fields
class Review(db.Document):
    commenter = db.DynamicField(required=True)
    content = db.StringField(required=True)
    date = db.DateTimeField(required=True)
    imdb_id = db.StringField(required=True, max_length=9)
    movie_title = db.StringField(required=True)
    image = db.ImageField()
    review_id = db.StringField(required=True, default=lambda: str(ObjectId()), unique=True)
    #Uncomment when other fields are ready for review pictures

class Reply(db.Document):
    review_id = db.StringField(required=True)
    commenter = db.DynamicField(required=True)
    content = db.StringField(required=True)
    date = db.DateTimeField(required=True)