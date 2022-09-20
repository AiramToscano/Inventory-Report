

from collections import Counter
from datetime import date, datetime
import time


class SimpleReport:

    def generatedatefabricao(lista):
        arrayDatas = []
        for i in lista:
            arrayDatas.append(i["data_de_fabricacao"])
        return sorted(arrayDatas)[0]

    def generatedatevalidade(lista):
        arrayDatas = []
        for i in lista:
            date1 = i["data_de_validade"]
            date2 = date.fromtimestamp(time.time())
            d1 = datetime.strptime(date1, '%Y-%m-%d')
            d2 = datetime.strptime(str(date2), '%Y-%m-%d')
            quantidade_dias = (d1 - d2).days
            if (quantidade_dias > 0):
                arrayDatas.append(i["data_de_validade"])

        return sorted(arrayDatas)[0]

    def generateEmpresa(lista):
        arrayNomes = []
        for i in lista:
            arrayNomes.append(i["nome_da_empresa"])
        couter = Counter(arrayNomes)
        max_empresa = max(couter, key=couter.get)
        return max_empresa

    def generate(lista):
        Fabricaoantiga = SimpleReport.generatedatefabricao(lista)
        Validade = SimpleReport.generatedatevalidade(lista)
        Empresa = SimpleReport.generateEmpresa(lista)
        return (
            f"Data de fabricação mais antiga: {Fabricaoantiga}\n"
            f"Data de validade mais próxima: {Validade}\n"
            f"Empresa com mais produtos: {Empresa}"
        )


# lista = [
#      {
#        "id": 2,
#        "nome_do_produto": "CADEIRA",
#        "nome_da_empresa": "Forces of Nature",
#        "data_de_fabricacao": "2022-04-04",
#        "data_de_validade": "2023-02-09",
#        "numero_de_serie": "FR48",
#        "instrucoes_de_armazenamento": "Conservar em local fresco"
#      },
#      {
#        "id": 1,
#        "nome_do_produto": "MESA",
#        "nome_da_empresa": "Forces of Nature",
#        "data_de_fabricacao": "2021-05-20",
#        "data_de_validade": "2024-02-09",
#        "numero_de_serie": "FR48",
#        "instrucoes_de_armazenamento": "Conservar em local fresco"
#      },
#      {
#        "id": 1,
#        "nome_do_produto": "MESA",
#        "nome_da_empresa": "teste",
#        "data_de_fabricacao": "2020-05-20",
#        "data_de_validade": "2025-02-09",
#        "numero_de_serie": "FR48",
#        "instrucoes_de_armazenamento": "Conservar em local fresco"
#      }
#    ]


# print(SimpleReport.generatedatefabricao(lista))
# print(SimpleReport.generatedatevalidade(lista))
# print(SimpleReport.generate(lista))
