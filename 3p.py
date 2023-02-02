from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index1():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def func():
    return '''Человечество вырастает из детства.</br>
            Человечеству мала одна планета.</br>
            Мы сделаем обитаемыми безжизненные пока планеты.</br>
            И начнем с Марса!</br>
            Присоединяйся!'''


@app.route('/image_mars')
def im():
    return f'<title>Привет, Марс!</title>' \
           f'<h1>Жди нас, Марс!</h1>' \
           f'<img src="{url_for("static", filename="img/mars.jpg")}"' \
           f' alt="здесь должна была быть картинка, но не нашлась">' \
           f'<p>Вот она какая, красная планета.</p>'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')