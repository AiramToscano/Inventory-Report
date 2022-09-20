from inventory_report.inventory.product import Product


def test_cria_produto():
    produto1 = Product(
        2,
        'skol',
        'service',
        '20-09-2022',
        '20-09-2023',
        '234534',
        'gelado')
    assert produto1.id == 2
    assert produto1.data_de_fabricacao == '20-09-2022'
    assert produto1.data_de_validade == '20-09-2023'
    assert produto1.nome_do_produto == 'skol'
    assert produto1.instrucoes_de_armazenamento == 'gelado'
    assert produto1.numero_de_serie == '234534'
    assert produto1.nome_da_empresa == 'service'
