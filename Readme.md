
# Teste Pippeline

Uma breve descrição sobre o que esse projeto faz e para quem ele é

### Documentação para a realização do De/Para

### Orientações: Na pasta do teste existem quatro arquivos
    1. Orientações para o teste (Orientações para migração.docx)
    2. Base do cliente (Base cliente.xlsx)
    3. Pasta de GED do cliente (GEDTEST.rar) 
    4. Modelo de tabelas Easyjur (pasta Easyjur)
### Siga as instruções abaixo para realização do teste.

É importante saber que o intuito principal de nosso procedimento é trazer todos os dados possíveis do cliente para a EasyJur. Você executará o procedimento do departamento jurídico responsável pela Universidade de Uberaba - Empresa.
Para definirmos se são dados de migração ou não, utilizamos a coluna id_migracao. Nela inserimos as chaves primárias contidas na base anterior do cliente para que posteriormente realizemos todos os vínculos necessários entre as tabelas. Use a coluna a seu favor! 
As datas devem ser inseridas no formato internacional, sendo AAAA-MM-DD.
Data de cadastro é um requisito obrigatório.

## Usuários
A tabela de usuários não é migrada, pois o próprio cliente cadastra todos os colaboradores que usarão a plataforma. É dessa tabela que são tirados os responsáveis pelos registros de nosso sistema. O id_empresa está contido em todas as tabelas da EasyJur e são de preenchimento obrigatório, pois é essa coluna que define o ambiente de cada departamento.

## Pessoas
A tabela de pessoas contém todos os contatos do escritório. A mesma possui informações como telefone, celular, endereço, e-mail, etc. Todas as pessoas vinculadas em um processo estão contidas nessa tabela.

## Processos
Aqui você encontrará todos os processos desse departamento. Os processos que não possuem nenhum número são do tipo administrativo e todos os que não  possuírem 25 caracteres são extrajudiciais. 
Não deixe de inserir a numeração das pastas.
Ao preencher as colunas nome_cliente e nome_contrario, monte um update unindo as tabelas necessárias para que retorne o conteúdo correto. Se desejar, basta inserir o sql em um bloco de notas e nos enviar.

## Andamentos
Os andamentos são o histórico do processo no tribunal. O cliente solicitou que alteremos o status de todos os andamentos dos processos com data de distribuição até o último dia do ano de 2019 para lido.

## Grupos
A tabela de grupos guarda todas as etiquetas cadastradas no sistema. Essas etiquetas serão vinculadas aos registros que constam na EasyJur.


## Módulo grupos
Essa tabela é a união entre a tabela de grupos e as outras tabelas do sistema. Ex: nela o sistema entenderá que o processo de ID 20 possui a etiqueta Sonserina. É possível inserir etiquetas em qualquer módulo da EasyJur.

## GED
A Empresa também possui arquivos referentes aos clientes e estes também devem ser migrados, no entanto, estão todos em uma mesma pasta com o nome do respectivo cliente ou numeração CNJ do processo, e tal formato não é funcional para nosso API, que vincula arquivos com registros cadastrados. 
Para que nosso api consiga realizar o vínculo necessário é preciso que os arquivos estejam no seguinte diretório:
nome da empresa > CLIENTES > id_cliente no caso de um arquivo relacionado a um cliente
nome da empresa > PROCESSOS > id_processo no caso de um arquivo relacionado a um cliente.

Por exemplo: Mylen Walter de Melo possui um documento que deve estar no seguinte diretório:
Empresa > CLIENTES > 1 
O objetivo então é organizar todos os arquivos da pasta GEDTESTE no formato especificado
## Referência

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


## Instalação

Instale my-project com python 3.9.5

```bash
  pip install
  #path_raiz = '/media/projetos/test/PROCESSO SELETIVO MIGRAÇÃO BASE MODELO/' #pasta raiz em que esta os arquivos
  #nome_empresa= 'nome da pasta da empresa'
  #path_projeto= '/test/project/'#caminho em que esta o projeto python
```
    