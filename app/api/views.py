from flask import Blueprint, jsonify, render_template
from utils import get_posts_by_user, get_post_by_pk, get_comments_by_post_id, search_for_posts, load_post_from_data

# Создаем блупринт
api_blueprint = Blueprint('api_blueprint', __name__, template_folder="./templates")


@api_blueprint.route("/api/posts")
def index_test():
    posts = load_post_from_data()
    return jsonify(posts)


@api_blueprint.route("/api/posts/<int:uid>")
def post_page_test(uid):
    post = get_post_by_pk(uid)
    return jsonify(post)
