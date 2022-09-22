import xmltodict
from .importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, caminho):
        caminhoCerto = caminho.split('.')
        if (caminhoCerto[1] == 'xml'):
            with open(caminho, 'r', encoding='utf-8') as file:
                my_xml = file.read()
                my_dict = xmltodict.parse(my_xml)
            return my_dict['dataset']['record']
        if (caminhoCerto[1] != 'xml'):
            raise ValueError("Arquivo inválido")
