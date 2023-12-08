from app.controller.easy.DataBase import *


class Grupo(Model):

    id= IntegerField(primary_key=True)
    nome= TextField(null=True)
    id_empresa= IntegerField(null=True)
    id_migracao= IntegerField(null=True)
    timestamp = DateTimeField(default=datetime.now())

    @staticmethod
    def dbCreateTable():
        db.create_tables([Grupo])

    @staticmethod
    def all():
        return Grupo.select()

    class Meta:
        database = db
