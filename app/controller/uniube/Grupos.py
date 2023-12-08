from app.controller.uniube.DataBase import *


class Grupos(Model):
    id = IntegerField(primary_key=True)
    nome_grupo = TextField()
    cor = TextField()
    timestamp = DateTimeField(default=datetime.now())

    @staticmethod
    def dbCreateTable():
        db.create_tables([Grupos])

    @staticmethod
    def all():
        return Grupos.select()

    class Meta:
        database = db