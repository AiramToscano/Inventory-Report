from collections import Counter
from .simple_report import SimpleReport


class CompleteReport(SimpleReport):

    def generateEmpresaCount(lista):
        arrayNomes = []
        arrayNomesCout = []
        for i in lista:
            arrayNomes.append(i["nome_da_empresa"])
        couter = Counter(arrayNomes)
        for key, value in couter.items():
            arrayNomesCout.append(f"{key}: {value}\n")
        return '- '.join(arrayNomesCout)

    def generate(lista):
        Fabricaoantiga = SimpleReport.generatedatefabricao(lista)
        Validade = SimpleReport.generatedatevalidade(lista)
        Empresa = SimpleReport.generateEmpresa(lista)
        EmpresaCount = CompleteReport.generateEmpresaCount(lista)
        return (
            f"Data de fabricação mais antiga: {Fabricaoantiga}\n"
            f"Data de validade mais próxima: {Validade}\n"
            f"Empresa com mais produtos: {Empresa}\n"
            f"Produtos estocados por empresa:\n- {EmpresaCount}"
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
#      },
#      {
#        "id": 1,
#        "nome_do_produto": "MESA",
#        "nome_da_empresa": "teste",
#        "data_de_fabricacao": "2020-05-20",
#        "data_de_validade": "2025-02-09",
#        "numero_de_serie": "FR48",
#        "instrucoes_de_armazenamento": "Conservar em local fresco"
#      },
#      {
#        "id": 1,
#        "nome_do_produto": "MESA",
#        "nome_da_empresa": "teste1",
#        "data_de_fabricacao": "2020-05-20",
#        "data_de_validade": "2025-02-09",
#        "numero_de_serie": "FR48",
#        "instrucoes_de_armazenamento": "Conservar em local fresco"
#      }
#    ]


# print(CompleteReport.generate(lista))
