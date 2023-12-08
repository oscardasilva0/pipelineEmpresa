from app.controller.uniube.DataBase import *
import re

class Cliente(Model):

    id = IntegerField(primary_key=True)
    nome = TextField()
    cpf = TextField()
    email = TextField()
    cidade = TextField()
    telefones = TextField()
    endereco = TextField()
    grupos = TextField()
    timestamp = DateTimeField(default=datetime.now())

    class Meta:
        database = db

    @staticmethod
    def all():
        return Cliente.select()

    @staticmethod
    def dbCreateTable():
        db.create_tables([Cliente])

    def separaDDD(self, telefoneCompleto):
        telefoneSomenteNumero = re.sub(r'[^\d\- ]', '',telefoneCompleto)
        telefoneCompletoSplit = telefoneSomenteNumero.strip().split(' ',1)
        if(len(telefoneCompletoSplit) != 2):
            return
        return {'ddd':str(telefoneCompletoSplit[0]), 'telefone':str(telefoneCompletoSplit[1])}

    def getTelefone(self):
        telefones = str(self.telefones).split(';')
        lista_telefonica =[]
        for tel in telefones:
            phone = self.separaDDD(tel)
            if(phone ==None):
                continue
            lista_telefonica.append(phone)

        return lista_telefonica;