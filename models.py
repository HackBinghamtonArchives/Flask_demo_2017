from peewee import *

db = SqliteDatabase('people.db')


class Language(Model):
    name = CharField()
    description = TextField()

class Member(Model):
    name = CharField()
    checked_in = BooleanField()
    known_languages = ForeignKeyField(Language, related_name="members", null=True)

    class Meta:
        database = db

class Workshop(Model):
    name = CharField()
    language_used = ForeignKeyField(Language, related_name="workshops", null=True)

    class Meta:
        database = db
