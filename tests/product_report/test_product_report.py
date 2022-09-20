from inventory_report.inventory.product import Product


def test_relatorio_produto():
    produto1 = Product(
        2,
        'skol',
        'service',
        '20-09-2022',
        '20-09-2023',
        '234534',
        'gelado')
    obj = (
            f"O produto {produto1.nome_do_produto}"
            f" fabricado em {produto1.data_de_fabricacao}"
            f" por {produto1.nome_da_empresa} com validade"
            f" até {produto1.data_de_validade}"
            f" precisa ser armazenado {produto1.instrucoes_de_armazenamento}."
        )
    assert produto1.__repr__() == obj
