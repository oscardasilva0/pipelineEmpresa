import os
import re
from os import listdir
from os.path import isfile, join
import shutil
from app.controller.easy.Pessoas import Pessoas as PessoasEasy

class ImportFiles:
    empresa: str
    pastaRaiz: str
    def __init__(self, empresa):
        self.empresa = empresa
        self.pastaRaiz = '/media/projetos/test/PROCESSO SELETIVO MIGRAÇÃO BASE MODELO/GEDTEST/'
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    def organiza_arquivos(self):
        only_files = [f for f in listdir(self.pastaRaiz) if isfile(join(self.pastaRaiz, f))]
        processo_dir = f'{self.pastaRaiz}../{self.empresa}/processo/'
        cliente_dir = f'{self.pastaRaiz}../{self.empresa}/cliente/'
        nao_encontrado_dir = f'{self.pastaRaiz}../{self.empresa}/nao_encontrado/'
        os.makedirs(processo_dir, exist_ok=True)
        os.makedirs(cliente_dir, exist_ok=True)
        os.makedirs(nao_encontrado_dir, exist_ok=True)
        for file_name in only_files:
            file_name_letra = re.sub(r'[^A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ ]', '', file_name)
            file_name_letra = file_name_letra.strip()
            file_is_cliente = len(file_name_letra) > 0
            if(file_is_cliente):
                pessoa = PessoasEasy.get_pessoa_nome(file_name)
                if pessoa == None:
                    shutil.copy(f'{self.pastaRaiz}{file_name}', f'{nao_encontrado_dir}/{file_name}')
                else:
                    shutil.copy(f'{self.pastaRaiz}{file_name}', f'{cliente_dir}{pessoa.id_migracao}-{file_name}')
            else:
                shutil.copy(f'{self.pastaRaiz}{file_name}', f'{processo_dir}{file_name}')





