from app.controller.easy.DataBase import *

class Migracao(Model):

    id = IntegerField(primary_key=True,index=True)
    timestamp = DateTimeField(default=datetime.now())

    class Meta:
        database = db

    @staticmethod
    def all():
        return Migracao.select()

    @staticmethod
    def dbCreateTable():
        db.create_tables([Migracao])
