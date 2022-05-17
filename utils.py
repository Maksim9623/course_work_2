import json

DATA_PATH = "./data/data.json"
COMMENTS_PATH = "./data/comments.json"


def load_post_from_data():
    """ Функция возвращает все посты """
    with open(DATA_PATH, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def get_posts_by_user(user_name):
    """ возвращает посты определенного пользователя """
    user_names = load_post_from_data()
    for name in user_names:
        if name['poster_name'].lower() == user_name.lower():
            return name


def load_from_comment():
    """ Функция возвращает все коментарии"""
    with open(COMMENTS_PATH, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def get_comments_by_post_id(post_id):
    """ возвращает комментарии определенного поста """
    id_ = load_from_comment()
    for i in id_:
        if i['pk'] == post_id:
            return i




def search_for_posts(query):
    """ возвращает список постов по ключевому слову """
    contents = load_post_from_data()
    for content in contents:
        if query.lower() in content['content'].lower():
            return content


def get_post_by_pk(pk):
    """ возвращает один пост по его идентификатору """
    posts = load_post_from_data()
    for post in posts:
        if post['pk'] == pk:
            return post
