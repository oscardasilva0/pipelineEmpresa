from app.controller.easy.DataBase import *
class Processos(Model):

    id = IntegerField(primary_key=True)
    id_processo = TextField(null=True)
    id_advogado_responsavel = TextField(null=True)
    id_cliente = TextField(null=True)
    nome_cliente = TextField(null=True)
    id_contrario = TextField(null=True)
    nome_contrario = TextField(null=True)
    numero = TextField(null=True)
    titulo_processo = TextField(null=True)
    n_pasta = TextField(null=True)
    instancia = TextField(null=True)
    tipo_processo = TextField(null=True)
    data_distribuicao = TextField(null=True)
    data_cadastro = TextField(null=True)
    status = TextField(null=True)
    id_empresa = TextField(null=True)
    id_migracao = TextField(null=True)
    timestamp = DateTimeField(default=datetime.now())

    class Meta:
        database = db

    @staticmethod
    def dbCreateTable():
        db.create_tables([Processos])

    @staticmethod
    def all():
        return Processos.select()
    @staticmethod
    def get_processo_numero(numero):
        return Processos.get_or_none(Processos.numero == numero)

    @staticmethod
    def save_or_update(proceso):
        proceso_existente = Processos.get_or_none(Processos.id_migracao == proceso.id_migracao)
        if proceso_existente:
            proceso_existente.id_processo = proceso.id_processo
            proceso_existente.id_advogado_responsavel = proceso.id_advogado_responsavel
            proceso_existente.id_cliente = proceso.id_cliente
            proceso_existente.nome_cliente = proceso.nome_cliente
            proceso_existente.id_contrario = proceso.id_contrario
            proceso_existente.nome_contrario = proceso.nome_contrario
            proceso_existente.numero = proceso.numero
            proceso_existente.titulo_processo = proceso.titulo_processo
            proceso_existente.n_pasta = proceso.n_pasta
            proceso_existente.instancia = proceso.instancia
            proceso_existente.tipo_processo = proceso.tipo_processo
            proceso_existente.data_distribuicao = proceso.data_distribuicao
            proceso_existente.data_cadastro = proceso.data_cadastro
            proceso_existente.status = proceso.status
            proceso_existente.id_empresa = proceso.id_empresa
            proceso_existente.id_migracao = proceso.id_migracao
            proceso_existente.save()
        else:
            proceso.save()

    @staticmethod
    def tipo(nome_processo: str):
        extra_judicial = len(nome_processo) == 25
        administrativo = nome_processo.matches("\\d")
        tipo = 'judicial'
        if(extra_judicial):
            tipo = 'extraJudicial'
        elif(administrativo):
            tipo = 'administrativo'
        return tipo
