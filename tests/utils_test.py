import pytest
from run import app


@pytest.fixture()
def keys_should_be():
    # Задаем, какие ключи ожидаем получать у кандидата
    return {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}


def test_api_posts(keys_should_be):
    """Проверяем что
    - возвращается список
    - у элементов есть нужные ключи"""
    response = app.test_client().get('api/posts')
    posts = response.json
    assert isinstance(posts, list), "Есть ошибка получения поста: выгружается не список"
    assert set(posts[0].keys()) == keys_should_be, "Ошибка получения ключей"


def test_api_posts_by_id(keys_should_be):
    """Проверяем что
    - возвращается словарь
    - у элемента есть нужные ключи"""
    response = app.test_client().get('api/posts/1')
    post = response.json
    assert isinstance(post, dict), "Есть ошибка получения поста по ID: выгружается не словарь"
    assert set(post.keys()) == keys_should_be, "Ошибка получения ключей при загрузке ID"




