from app.controller.easy.DataBase import *

class Andamento(Model):

    id = IntegerField(primary_key=True)
    id_advogado = TextField(null=True)
    id_processo = TextField(null=True)
    numero_processo = TextField(null=True)
    data_andamento = TextField(null=True)
    data_cadastro = TextField(null=True)
    descricao = TextField(null=True)
    id_empresa = TextField(null=True)
    status = TextField(null=True)
    data_leitura = TextField(null=True)
    id_migracao = TextField(null=True)
    timestamp = DateTimeField(default=datetime.now())

    class Meta:
        database = db

    @staticmethod
    def save_or_update(andamento):
        andamento_existente = Andamento.get_or_none(Andamento.id_migracao == andamento.id_migracao)
        if andamento_existente:
            andamento_existente.id_advogado = andamento.id_advogado
            andamento_existente.id_processo = andamento.id_processo
            andamento_existente.numero_processo = andamento.numero_processo
            andamento_existente.data_andamento = andamento.data_andamento
            andamento_existente.data_cadastro = andamento.data_cadastro
            andamento_existente.descricao = andamento.descricao
            andamento_existente.id_empresa = andamento.id_empresa
            andamento_existente.status = andamento.status
            andamento_existente.data_leitura = andamento.data_leitura
            andamento_existente.id_migracao = andamento.id_migracao
            andamento_existente.save()
        else:
            andamento.save()

    @staticmethod
    def all():
        return Andamento.select()

    @staticmethod
    def dbCreateTable():
        db.create_tables([Andamento])