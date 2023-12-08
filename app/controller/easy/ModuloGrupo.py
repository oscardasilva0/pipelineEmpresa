from app.controller.easy.DataBase import *


class ModuloGrupo(Model):

    id= IntegerField(primary_key=True)
    id_registro = TextField(null=True)
    id_grupo = TextField(null=True)
    id_empresa = TextField(null=True)
    id_modulo = TextField(null=True)
    data_cadastro = TextField(null=True)

    timestamp = DateTimeField(default=datetime.now())

    class Meta:
        database = db

    @staticmethod
    def save_or_update(modulo_grupo):
        modulo_grupo_existente = ModuloGrupo.get_or_none((ModuloGrupo.id_registro == modulo_grupo.id_registro)&\
                                 (ModuloGrupo.id_registro == modulo_grupo.id_registro)& \
                                 (ModuloGrupo.id_registro == modulo_grupo.id_registro))
        if modulo_grupo_existente:
            modulo_grupo_existente.id_registro = modulo_grupo.id_registro
            modulo_grupo_existente.id_grupo = modulo_grupo.id_grupo
            modulo_grupo_existente.id_empresa = modulo_grupo.id_empresa
            modulo_grupo_existente.id_modulo = modulo_grupo.id_modulo
            modulo_grupo_existente.save()
        else:
            modulo_grupo.save()

    @staticmethod
    def dbCreateTable():
        db.create_tables([ModuloGrupo])

    @staticmethod
    def all():
        return ModuloGrupo.select()
