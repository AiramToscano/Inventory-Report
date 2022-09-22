import csv
from .importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, caminho):
        caminhoCerto = caminho.split('.')
        if (caminhoCerto[1] == 'csv'):
            lista = []
            with open(caminho) as file:
                read = csv.DictReader(file)
                for row in read:
                    lista.append(row)
            return lista
        if (caminhoCerto[1] != 'csv'):
            raise ValueError("Arquivo inválido")
