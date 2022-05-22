from flask import Flask, render_template, request
# Импортируем блюпринт
from app.post.views import post_blueprint
from app.api.views import api_blueprint

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# регистрируем первый блюпринт
app.register_blueprint(post_blueprint)

# регистрируем второй блюпринт
app.register_blueprint(api_blueprint)

if __name__ == "__main__":
    app.run(debug=False)
