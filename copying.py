from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from shutil import copy
from sys import argv


class FileCreator:
    """
    Класс для создания новых файлов по конфигурационному файлу xml
    для использования вызовите из консоли main.py с переданным путем до конфиг файла
    """

    def __init__(self):
        self.attributes: list = []
        if len(argv) != 2:
            raise Exception('Не верно указан параметр argv')
        self.argv = argv[1]

    def parsing_file(self) -> None:
        """
        Открываем и парсим конфигурационный xml файл
        """
        try:
            tree: ElementTree = ElementTree.parse(self.argv)
        except FileNotFoundError:
            raise FileNotFoundError(f'Конфигурационного файла не существует')
        root: Element = tree.getroot()
        if root:
            self.attributes: list = [child.attrib for child in root]

    def create_files(self) -> None:
        """
        Создаем новые файлы
        """
        for item in self.attributes:
            self.__create_file(item=item)

    @staticmethod
    def __create_file(item: dict) -> None:
        """
        Создание одного файла
        """
        try:
            copy(item['source_path'] + '/' + item['file_name'],
                 item['destination_path'] + '/' + item['file_name'])
        except FileNotFoundError:
            print(f"Не верно указаны source_path: {item['source_path']}"
                  f" или destination_path: {item['destination_path']}")


if __name__ == "__main__":
    creator = FileCreator()
    creator.parsing_file()
    creator.create_files()
