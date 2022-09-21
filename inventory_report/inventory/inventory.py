import csv
import json

import xmltodict


from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport


class Inventory():

    def import_data(caminho, tipodeRelatorio):
        caminhoCerto = caminho.split('.')
        if (caminhoCerto[1] == 'csv'):
            csv = Inventory.importcsv(caminho, tipodeRelatorio)
            return csv
        if (caminhoCerto[1] == 'json'):
            json = Inventory.importjson(caminho, tipodeRelatorio)
            return json

        if (caminhoCerto[1] == 'xml'):
            xml = Inventory.importxml(caminho, tipodeRelatorio)
            return xml

    def importcsv(caminho, tipodeRelatorio):
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

    def importjson(caminho, tipodeRelatorio):
        if (tipodeRelatorio == "simples"):
            with open(caminho) as file:
                read = json.load(file)
            return SimpleReport.generate(read)
        if (tipodeRelatorio == "completo"):
            with open(caminho) as file:
                read = json.load(file)
            return CompleteReport.generate(read)

    def importxml(caminho, tipodeRelatorio):
        if (tipodeRelatorio == "simples"):
            with open(caminho, 'r', encoding='utf-8') as file:
                my_xml = file.read()
                my_dict = xmltodict.parse(my_xml)
            return SimpleReport.generate(my_dict['dataset']['record'])
        if (tipodeRelatorio == "completo"):
            with open(caminho, 'r', encoding='utf-8') as file:
                my_xml = file.read()
                my_dict = xmltodict.parse(my_xml)
            return CompleteReport.generate(my_dict['dataset']['record'])
