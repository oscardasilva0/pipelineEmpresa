from app.controller.easy.DataBase import *


class Usuario(Model):
    id= IntegerField(primary_key=True)
    nome = TextField(null=True)
    email = TextField(null=True)
    celular = TextField(null=True)
    user = TextField(null=True)
    password = TextField(null=True)
    userlevel = TextField(null=True)
    status = TextField(null=True)
    numero_oab = TextField(null=True)
    uf_oab = TextField(null=True)
    id_empresa = IntegerField(null=True)
    modulos = TextField(null=True)
    modulos_ver = TextField(null=True)
    tag_pega = TextField(null=True)
    intCodGrupo = IntegerField(null=True)
    tipo = TextField(null=True)
    id_migracao = IntegerField(null=True)
    timestamp = DateTimeField(default=datetime.now())

    @staticmethod
    def dbCreateTable():
        db.create_tables([Usuario])

    class Meta:
        database = db

    @staticmethod
    def all():
        return Usuario.select()

    @staticmethod
    def get_email(email: str):
        return Usuario.get_or_none(Usuario.email.contains(email))