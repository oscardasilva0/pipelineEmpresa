import datetime

from app.controller.easy.DataBase import *
import re

class Pessoas(Model):

    id= IntegerField(primary_key=True)
    tipo=TextField(null=True)
    nome=TextField(null=True)
    apelido=TextField(null=True)
    website=TextField(null=True)
    cpf=TextField(null=True)
    rg=TextField(null=True)
    cnpj=TextField(null=True)
    endereco=TextField(null=True)
    numero=TextField(null=True)
    complemento=TextField(null=True)
    bairro=TextField(null=True)
    id_cidade=TextField(null=True)
    cep=TextField(null=True)
    estado=TextField(null=True)
    observacoes=TextField(null=True)
    ddd1=TextField(null=True)
    telefone=TextField(null=True)
    ddd2=TextField(null=True)
    telefone2=TextField(null=True)
    ddd3=TextField(null=True)
    celular=TextField(null=True)
    ddd4=TextField(null=True)
    celular2=TextField(null=True)
    email=TextField(null=True)
    email2=TextField(null=True)
    profissao=TextField(null=True)
    data_cadastro=TextField(null=True)
    id_empresa=TextField(null=True)
    estado_civil=TextField(null=True)
    nacionalidade=TextField(null=True)
    aniversario=TextField(null=True)
    rg_orgao=TextField(null=True)
    nis=TextField(null=True)
    pis=TextField(null=True)
    ctps=TextField(null=True)
    id_migracao=TextField(null=True)
    pais=TextField(null=True)
    cnh=TextField(null=True)
    timestamp = DateTimeField(default=datetime.now())

    @staticmethod
    def dbCreateTable():
        db.create_tables([Pessoas])

    @staticmethod
    def all():
        return Pessoas.select()

    @staticmethod
    def get_pessoa_nome(name: str):
        db.create_tables([Pessoas])
        return Pessoas.get_or_none(Pessoas.nome.contains(name))

    @staticmethod
    def get_pessoa_id(id: int):
        db.create_tables([Pessoas])
        return Pessoas.get_or_none(Pessoas.id == id)
    @staticmethod
    def save_or_update(pessoa):
        pessoa_existente = Pessoas.get_or_none(Pessoas.cpf == pessoa.cpf)
        if pessoa_existente:
            pessoa_existente.nome= pessoa.nome
            pessoa_existente.cpf= pessoa.cpf
            pessoa_existente.endereco= pessoa.endereco
            pessoa_existente.numero= pessoa.numero
            pessoa_existente.complemento= pessoa.complemento
            pessoa_existente.id_cidade= pessoa.id_cidade
            pessoa_existente.ddd1= pessoa.ddd1
            pessoa_existente.telefone= pessoa.telefone
            pessoa_existente.ddd2= pessoa.ddd2
            pessoa_existente.telefone2= pessoa.telefone2
            pessoa_existente.ddd3= pessoa.ddd3
            pessoa_existente.celular= pessoa.celular
            pessoa_existente.ddd4= pessoa.ddd4
            pessoa_existente.celular2= pessoa.celular2
            pessoa_existente.email= pessoa.email
            pessoa_existente.data_cadastro= pessoa.data_cadastro
            pessoa_existente.id_empresa= pessoa.id_empresa
            pessoa_existente.id_migracao= pessoa.id_migracao
            pessoa_existente.save()
        else:
            pessoa.save()

    class Meta:
        database = db
