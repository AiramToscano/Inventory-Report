
import json
from .importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, caminho):
        caminhoCerto = caminho.split('.')
        if (caminhoCerto[1] == 'json'):
            with open(caminho) as file:
                read = json.load(file)
            return read
        if (caminhoCerto[1] != 'json'):
            raise ValueError("Arquivo inválido")
