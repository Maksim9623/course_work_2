from flask import Flask, render_template, request
# Импортируем блюпринт
from app.post.views import post_blueprint

app = Flask(__name__)

# регистрируем первый блюпринт
app.register_blueprint(post_blueprint)


if __name__ == "__main__":
    app.run(debug=True)
