# import cherrypy
from app.controller.ExportCSV import ExportCSV
from app.controller.ImportCSV import ImportCSV
from app.controller.ImportTableUniube import ImportTableUniube
from app.controller.ImportFiles import ImportFiles

path_raiz = '/media/projetos/test/PROCESSO SELETIVO MIGRAÇÃO BASE MODELO/'
nome_empresa= 'uniube'
path_projeto= '/media/projetos/test/project/'
ImportCSV(f'{path_raiz}Base cliente.xlsx')
ImportTableUniube(f'{path_raiz}EasyJur/tb_usuarios.xlsx', 36369)
ExportCSV(f'{path_raiz}EasyJur/', f'{path_projeto}app/db/easy.db')
ImportFiles(nome_empresa).organiza_arquivos()