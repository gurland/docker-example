from peewee import PostgresqlDatabase, Model, CharField

db = PostgresqlDatabase(database='postgres', host='db', user='postgres', password='test', port='5432')


class Tweet(Model):
    text = CharField()

    class Meta:
        database = db


db.create_tables([Tweet], safe=True)
