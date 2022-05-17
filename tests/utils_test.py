from utils import get_posts_by_user, get_post_by_pk, get_comments_by_post_id, search_for_posts
import pytest





# Задаем, какие ключи ожидаем получать у кандидата
keys_should_be = {"pk", "name", "position"}


class TestPost:

    def test_get_all(self, candidates_dao):
        """ Проверяем, верный ли список кандидатов возвращается """
        candidates = candidates_dao.get_all()
        assert type(candidates) == list, "возвращается не список"
        assert len(candidates) > 0, "возвращается пустой список"
        assert set(candidates[0].keys()) == keys_should_be, "неверный список ключей"

    def test_get_by_id(self, candidates_dao):
        """ Проверяем, верный ли кандидат возвращается при запросе одного """
        candidate = candidates_dao.get_by_pk(1)
        assert(candidate["pk"] == 1), "возвращается неправильный кандидат"
        assert set(candidate.keys()) == keys_should_be, "неверный список ключей"

