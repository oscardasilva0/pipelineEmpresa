import pandas as pd
from app.controller.uniube.Andamentos import Andamentos
from app.controller.uniube.Cidade import Cidade
from app.controller.uniube.Cliente import Cliente
from app.controller.uniube.Grupos import Grupos
from app.controller.uniube.Processos import Processos
import datetime
import numpy as np
class ImportCSV:
    pathRoute: str

    def import_cidade(self):
        tabela = pd.read_excel(self.pathRoute, sheet_name='CIDADE')
        Cidade.dbCreateTable()
        for i, cidade in tabela.iterrows():
            Cidade.insert(id=cidade.id, cidade_uf=cidade.cidade_uf) \
                .on_conflict_replace(True).execute()

    def import_cliente(self):
        tabela = pd.read_excel(self.pathRoute, sheet_name='CLIENTE')
        Cliente.dbCreateTable()
        for i, cliente in tabela.iterrows():
            Cliente.insert(id=cliente.id, nome=cliente.nome, cpf=cliente.cpf,email=cliente.email,telefones=cliente.telefones,\
                           endereco=cliente.endereco,grupos=cliente.Grupos, cidade=cliente.cidade)\
                .on_conflict_replace(True).execute()

    def import_processo(self):
        print()
        tabela = pd.read_excel(self.pathRoute, sheet_name='PROCESSO')
        Processos.dbCreateTable()
        for i, processo in tabela.iterrows():
            Processos.insert(id=processo.id, numero=processo.numero, cliente=processo.cliente, adverso=processo.adverso,
                           instancia=processo.instancia, responsaivel=processo.responsáivel, status=processo.status,\
                            cadastro_data=processo.cadastrodata, dist_data=processo.distdata,\
                             grupos=processo.grupos, acao=processo.acao)\
                .on_conflict_replace(True).execute()

    def import_andamentos(self):
        tabela = pd.read_excel(self.pathRoute, sheet_name='ANDAMENTOS')
        Andamentos.dbCreateTable()
        for i, andamento in tabela.iterrows():
            data_andamento = datetime.datetime.strptime(andamento.dataandamento, "%d/%m/%Y").date()
            Andamentos.insert(id=andamento.id, processo_id=andamento.Processoid, cliente_id=andamento.clienteid,\
                          numero_processo=andamento.numeroprocesso, conteudo=andamento.conteudo,\
                          data_andamento=data_andamento, status=andamento.status)\
                          .on_conflict_replace(True).execute()

    def import_grupos(self):
        tabela = pd.read_excel(self.pathRoute, sheet_name='GRUPOS')
        Grupos.dbCreateTable()
        for i, grup in tabela.iterrows():
            Grupos.insert(id=grup.id,nome_grupo=grup.nomegrupo,cor=grup.cor).on_conflict_replace().execute()

    def __init__(self, pathRoute):
        self.pathRoute = pathRoute
        self.import_cidade()
        self.import_cliente()
        self.import_processo()
        self.import_andamentos()
        self.import_grupos()