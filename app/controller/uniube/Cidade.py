from app.controller.uniube.DataBase import *


class Cidade(Model):

    id = IntegerField(primary_key=True)
    cidade_uf = TextField()
    timestamp = DateTimeField(default=datetime.now())

    class Meta:
        database = db


    @staticmethod
    def all():
        return Cidade.select()

    @staticmethod
    def get(id_cidade):
        return Cidade.get_or_none(Cidade.id == id_cidade)

    def separa_nome_cidade_uf(self):
        return  str(self.cidade_uf).split(' - ')

    @staticmethod
    def dbCreateTable():
        db.create_tables([Cidade])