# from app.controller.easy.Grupo import Grupo
import datetime
from app.controller.uniube.Andamentos import Andamentos as AndamentosUni
from app.controller.uniube.Cidade import Cidade as CidadeUni
from app.controller.uniube.Cliente import Cliente as ClienteUni
from app.controller.uniube.Grupos import Grupos as GruposUni
from app.controller.uniube.Processos import Processos as ProcessosUni
from app.controller.easy.Andamento import Andamento as AndamentoEasy
from app.controller.easy.Grupo import Grupo as GrupoEasy
from app.controller.easy.Migracao import Migracao as MigracaoEasy
from app.controller.easy.ModuloGrupo import ModuloGrupo as ModuloGrupoEasy
from app.controller.easy.Usuario import Usuario as UsuarioEasy
from app.controller.easy.Pessoas import Pessoas as PessoasEasy
from app.controller.easy.Processos import Processos as ProcessosEasy
import pandas as pd
import re


class ImportTableUniube:
    id_empresa: int
    pathRoute: str

    def import_usuarios(self):
        tabela = pd.read_excel(self.pathRoute)
        UsuarioEasy.dbCreateTable()
        for i, usuario in tabela.iterrows():
            UsuarioEasy.insert( \
                id=usuario.id, \
                nome=usuario.nome, \
                email=usuario.email, \
                celular=usuario.celular, \
                user=usuario.user, \
                password=usuario.password, \
                userlevel=usuario.userlevel, \
                status=usuario.status, \
                numero_oab=usuario.numero_oab, \
                uf_oab=usuario.uf_oab, \
                id_empresa=usuario.id_empresa, \
                modulos=usuario.modulos, \
                modulos_ver=usuario.modulos_ver, \
                tag_pega=usuario.tag_pega, \
                intCodGrupo=usuario.intCodGrupo, \
                tipo=usuario.tipo, \
                id_migracao=usuario.id_migracao) \
                .on_conflict_replace().execute()

    def merge_grupos(self):
        GrupoEasy.dbCreateTable()
        grupos = GruposUni.all()
        for grup in grupos:
            query = GrupoEasy.insert(id=int(grup.id),
                                     nome=str(grup.nome_grupo),
                                     id_empresa=int(self.id_empresa),
                                     id_migracao=int(grup.id)).on_conflict_replace().execute()

    def merge_pessoas(self):
        PessoasEasy.dbCreateTable()
        clientes = ClienteUni.all()
        for cliente in clientes:
            enderecoCompleto = f'{cliente.endereco}'
            enderecoSplit = str(enderecoCompleto).split(',')
            endereco = enderecoSplit[0]
            numero = enderecoSplit[1]
            complemento = f'{enderecoSplit[2]}' if len(enderecoSplit) == 3 else None
            id_cidade = cliente.cidade
            lista_telefones = cliente.getTelefone()

            ddd = f'{lista_telefones[0]["ddd"]}' if len(lista_telefones) >= 1 else None
            telefone = f'{lista_telefones[0]["telefone"]}' if len(lista_telefones) >= 1 else None
            ddd2 = f'{lista_telefones[1]["ddd"]}' if len(lista_telefones) >= 2 else None
            telefone2 = f'{lista_telefones[1]["telefone"]}' if len(lista_telefones) >= 2 else None
            ddd3 = f'{lista_telefones[2]["ddd"]}' if len(lista_telefones) >= 3 else None
            celular = f'{lista_telefones[2]["telefone"]}' if len(lista_telefones) >= 3 else None
            ddd4 = f'{lista_telefones[3]["ddd"]}' if len(lista_telefones) >= 4 else None
            celular2 = f'{lista_telefones[3]["telefone"]}' if len(lista_telefones) >= 4 else None

            pessoa = PessoasEasy()
            pessoa.nome = cliente.nome
            pessoa.cpf = cliente.cpf
            pessoa.endereco = endereco
            pessoa.numero = numero
            pessoa.complemento = complemento
            pessoa.id_cidade = cliente.cidade
            pessoa.ddd1 = ddd
            pessoa.telefone = telefone
            pessoa.ddd2 = ddd2
            pessoa.telefone2 = telefone2
            pessoa.ddd3 = ddd3
            pessoa.celular = celular
            pessoa.ddd4 = ddd4
            pessoa.celular2 = celular2
            pessoa.email = cliente.email
            pessoa.data_cadastro = datetime.datetime.now()
            pessoa.id_empresa = self.id_empresa
            pessoa.id_migracao = cliente.id
            PessoasEasy.save_or_update(pessoa)

    def merge_processos(self):
        ProcessosUni.dbCreateTable()
        ProcessosEasy.dbCreateTable()
        preocessos = ProcessosUni.all()
        for processoUni in preocessos:
            cliente = PessoasEasy.get_pessoa_id(int(processoUni.cliente))
            contrario = PessoasEasy.get_pessoa_id(int(processoUni.adverso))
            responsaivel = UsuarioEasy.get_email(processoUni.responsaivel)
            processoEasy = ProcessosEasy()
            processoEasy.id_processo = processoUni.id
            processoEasy.id_advogado_responsavel = responsaivel.id
            processoEasy.id_cliente = cliente.id
            processoEasy.nome_cliente = cliente.nome
            processoEasy.id_contrario = contrario.id
            processoEasy.nome_contrario = contrario.nome
            processoEasy.numero = processoUni.numero
            processoEasy.tipo_processo = None  # ProcessosEasy.tipo()
            processoEasy.id_migracao = processoUni.id
            processoEasy.instancia = processoUni.instancia
            processoEasy.titulo_processo = None  # processoUni.titulo_processo
            processoEasy.n_pasta = None  # processoUni.n_pasta
            processoEasy.data_distribuicao = processoUni.dist_data
            processoEasy.data_cadastro = processoUni.cadastro_data
            processoEasy.status = processoUni.status
            processoEasy.id_empresa = self.id_empresa
            processoEasy.id_migracao = processoUni.id
            ProcessosEasy.save_or_update(processoEasy)
            self.merge_modulo_grupo(processoUni.grupos, processoEasy.id_processo)

    def merge_andamentos(self):
        AndamentosUni.dbCreateTable()
        AndamentoEasy.dbCreateTable()
        andamentos = AndamentosUni.all()

        for andamentoUni in andamentos:
            processo = ProcessosEasy.get_processo_numero(andamentoUni.numero_processo)
            andamentoEasy = AndamentoEasy()
            if(processo != None):
                andamentoEasy.id_advogado = processo.id_advogado_responsavel
            andamentoEasy.id_processo = andamentoUni.processo_id
            andamentoEasy.numero_processo =andamentoUni.numero_processo
            andamentoEasy.data_andamento = andamentoUni.data_andamento
            andamentoEasy.data_cadastro = datetime.datetime.now()
            andamentoEasy.descricao = andamentoUni.conteudo
            andamentoEasy.id_empresa = self.id_empresa
            andamentoEasy.status = andamentoUni.status
            andamentoEasy.data_leitura = None#TextField()
            andamentoEasy.id_migracao = andamentoUni.id

            AndamentoEasy.save_or_update(andamentoEasy)

    def merge_modulo_grupo(self,grupos_processo :str, processo:int):
        ProcessosUni.dbCreateTable()
        ModuloGrupoEasy.dbCreateTable()
        GrupoEasy.dbCreateTable()
        grupos= GrupoEasy.all()
        lista_grupos_processo = str(re.sub('[^\d;]','',grupos_processo)).split(';')
        for grupo_processo in lista_grupos_processo:
            moduloGrupoEasy =ModuloGrupoEasy()
            moduloGrupoEasy.id_registro = processo
            moduloGrupoEasy.id_grupo = int(grupo_processo)
            moduloGrupoEasy.id_empresa = self.id_empresa
            moduloGrupoEasy.id_modulo = None
            moduloGrupoEasy.data_cadastro = datetime.datetime.now()
            ModuloGrupoEasy.save_or_update(moduloGrupoEasy)

    def __init__(self, pathRoute, id_empresa):
        MigracaoEasy.dbCreateTable()
        migracao, created = MigracaoEasy.get_or_create(timestamp=datetime.datetime.now())
        self.pathRoute = pathRoute
        self.id_empresa = id_empresa
        self.import_usuarios()
        self.merge_grupos()
        self.merge_pessoas()
        self.merge_processos()
        self.merge_andamentos()
