from flask import Blueprint, render_template, request
from utils import get_posts_by_user, get_post_by_pk, get_comments_by_post_id, search_for_posts, load_post_from_data


# Создаем блупринт
post_blueprint = Blueprint('post_blueprint', __name__, template_folder="./templates")


# Создаем вьюшку для получения всех пользователей
@post_blueprint.route('/', methods=['GET'])
def page_posts_all():
    posts = load_post_from_data()
    return render_template("index.html", posts=posts)


# Создаем вьюшку для получения информации о пользователе и коментария к посту
@post_blueprint.route('/posts/<int:uid>', methods=['GET'])
def page_posts_uid(uid):
    posts = get_post_by_pk(uid)
    comment = get_comments_by_post_id(uid)
    return render_template("post.html", posts=posts, comments=comment)


# Создаем вьюшку для поиска по словам
@post_blueprint.route('/search/', methods=['GET'])
def page_posts_search():
    search = request.args.get("s")
    posts = search_for_posts(search)

    return render_template("search.html", search=search, posts=posts)


# Создаем вьюшку для получения информации по имени пользователя
@post_blueprint.route('/users/<username>', methods=['GET'])
def page_posts_username(username):
    users = get_posts_by_user(username)
    return render_template("user-feed.html", users=users)

