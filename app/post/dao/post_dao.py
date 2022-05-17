import json

DATA_PATH = "./data/data.json"


class PostDAO:
    def __init__(self, PATH):
        """ При создании экземпляра DAO нужно указать путь к файлу с данными"""
        self.path = PATH

    def load_post_from_data(self):
        """ Функция возвращает все посты """
        with open(DATA_PATH, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
