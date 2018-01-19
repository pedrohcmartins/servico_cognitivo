# -*- encoding: utf-8 -*-

from views import db


class UserSentiment(db.Model):
    __tablename__ = 'tb_userSentiment'

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    desc = db.Column(db.Text)
    language = db.Column(db.Text)
    key = db.Column(db.Text)
    sentiment = db.Column(db.Text)

    def __init__(self, name, email, desc, language, key, sentiment):
        self.name = name
        self.email = email
        self.desc = desc
        self.language = language
        self.key = key
        self.sentiment = sentiment


db.create_all()
