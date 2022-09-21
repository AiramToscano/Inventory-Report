import csv


from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport


class Inventory():

    def import_data(caminho, tipodeRelatorio):
        if (tipodeRelatorio == "simples"):
            lista = []
            with open(caminho) as file:
                read = csv.DictReader(file)
                for row in read:
                    lista.append(row)
            return SimpleReport.generate(lista)
        if (tipodeRelatorio == "completo"):
            lista = []
            with open(caminho) as file:
                read = csv.DictReader(file)
                for row in read:
                    lista.append(row)
            return CompleteReport.generate(lista)
