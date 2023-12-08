from app.controller.uniube.DataBase import *
from app.controller.easy.Processos import Processos
class Andamentos(Model):

    id = IntegerField(primary_key=True)
    processo_id = IntegerField()
    cliente_id = IntegerField()
    numero_processo = TextField()
    conteudo = TextField()
    data_andamento = DateField()
    status = TextField()
    timestamp = DateTimeField(default=datetime.now())

    class Meta:
        database = db

    @staticmethod
    def all():
        return Andamentos.select()

    @staticmethod
    def dbCreateTable():
        db.create_tables([Andamentos])