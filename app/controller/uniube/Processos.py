from app.controller.uniube.DataBase import *

class Processos(Model):
    id = IntegerField(primary_key=True)
    numero = TextField(null=True)
    cliente = TextField(null=True)
    adverso = TextField(null=True)
    instancia = TextField(null=True)
    responsaivel = TextField()
    status = TextField(null=True)
    cadastro_data= DateField(null=True)
    dist_data = DateField(null=True)
    grupos = TextField(null=True)
    acao = TextField(null=True)
    timestamp = DateTimeField(default=datetime.now())

    class Meta:
        database = db

    @staticmethod
    def all():
        return Processos.select()

    @staticmethod
    def dbCreateTable():
        db.create_tables([Processos])