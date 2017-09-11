from peewee import *

db = SqliteDatabase('people.db')


class Language(Model):
    name = CharField()
    description = TextField()

class Member(Model):
    name = CharField()
    checked_in = BooleanField()
    known_languages = ForeignKeyField(Language, related_name="members")

    class Meta:
        database = db

class Workshop(Model):
    name = CharField()
    language_used = ForeignKeyField(Language, related_name="workshops")

    class Meta:
        database = db
