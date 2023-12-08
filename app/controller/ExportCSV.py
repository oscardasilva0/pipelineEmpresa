import pandas as pd
import time
import sqlite3
import shutil
import numpy as np
class ExportCSV:
    pathRoute: str
    cnx: str
    timestr: str
    def export_andamentos(self):
        df = pd.read_sql_query("SELECT * FROM andamento", self.cnx)
        df = self.remove_nan_df(df)
        nome_arquivo_excel = self.make_file('andamentos')
        nome_folha_destino = 'andamento'
        self.escreve_arquivo(nome_arquivo_excel, nome_folha_destino, df)

    def export_grupo(self):
        df = pd.read_sql_query("SELECT * FROM grupo", self.cnx)
        df = self.remove_nan_df(df)
        nome_arquivo_excel = self.make_file('grupo')
        nome_folha_destino = 'Planilha1'
        self.escreve_arquivo(nome_arquivo_excel, nome_folha_destino, df)

    def export_module_grupos(self):
        df = pd.read_sql_query("SELECT * FROM modulogrupo", self.cnx)
        df = self.remove_nan_df(df)
        nome_arquivo_excel = self.make_file('modulo_grupos')
        nome_folha_destino = 'modulo grupos'
        self.escreve_arquivo(nome_arquivo_excel, nome_folha_destino, df)

    def export_pessoas(self):
        df = pd.read_sql_query("SELECT * FROM pessoas", self.cnx)
        df = self.remove_nan_df(df)
        nome_arquivo_excel = self.make_file('pessoas')
        nome_folha_destino = 'pessoas'
        self.escreve_arquivo(nome_arquivo_excel, nome_folha_destino, df)

    def export_processos(self):
        df = pd.read_sql_query("SELECT * FROM processos", self.cnx)
        df = self.remove_nan_df(df)
        nome_arquivo_excel = self.make_file('processos')
        nome_folha_destino = 'processos'
        self.escreve_arquivo(nome_arquivo_excel, nome_folha_destino, df)

    def escreve_arquivo(self, nome_arquivo_excel, nome_folha_destino, df):
        with pd.ExcelFile(nome_arquivo_excel) as xls:
            dfs = {sheet_name: xls.parse(sheet_name) for sheet_name in xls.sheet_names}
        dfs[nome_folha_destino] = df
        with pd.ExcelWriter(nome_arquivo_excel, engine='openpyxl') as writer:
            for sheet_name, df_sheet in dfs.items():
                df_sheet.to_excel(writer, sheet_name=sheet_name, index=False)

    def make_file(self, nome: str):
        nome_arquivo_excel = f'{self.pathRoute}{self.timestr}{nome}.xlsx'
        shutil.copy(f'{self.pathRoute}tb_{nome}.xlsx', nome_arquivo_excel)
        return nome_arquivo_excel

    def remove_nan_df(self, df):
        df = df.fillna('')
        df = df.replace('NaN', np.nan)
        df = df.replace(np.nan, '', regex=True)
        df = df.drop("timestamp", axis=1)
        return df

    def __init__(self, pathRoute: str, pathDB: str):
        self.pathRoute = pathRoute
        self.cnx = sqlite3.connect(pathDB)
        self.timestr = time.strftime("%Y%m%d-%H%M%S")
        self.export_andamentos()
        self.export_grupo()
        self.export_module_grupos()
        self.export_processos()
        self.export_pessoas()




