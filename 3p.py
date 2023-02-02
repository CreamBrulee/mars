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


@app.route('/promotion_image')
def im1():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <title>Колонизация</title>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" href={url_for("static", filename="css/ind.css")}>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for("static", filename="img/mars.jpg")}"
                        alt="здесь должна была быть картинка, но не нашлась" width=400>
                        <div class="alert alert-dark" role="alert">
                          Человечество вырастает из детства.
                        </div>
                        <div class="alert alert-success" role="alert">
                          Человечеству мала одна планета.
                        </div>
                        <div class="alert alert-secondary" role="alert">
                          Мы сделаем обитаемыми безжизненные пока планеты.
                        </div>
                        <div class="alert alert-warning" role="alert">
                          И начнем с Марса!
                        </div>
                        <div class="alert alert-danger" role="alert">
                          Присоединяйся!
                        </div>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')