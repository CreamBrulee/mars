from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 style="text-align: center">Анкета претендента</h1>
                            <h2 style="text-align: center">на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                    <input type="surname" class="form-control" id="surname" aria-describedby="emailHelp" placeholder="Введите фамилию" name="surname">
                                    <input type="firstname" class="form-control" id="firstname" placeholder="Введите имя" name="firstname">
                                    <p>   </p>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="educationSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="form-check">Какие у Вас есть профессии?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="1" value='Инженер-исследователь'>
                                          <label class="form-check-label" for="1">
                                            Инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="2" value='Инженер-строитель'>
                                          <label class="form-check-label" for="2">
                                            Инженер-строитель
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="3" value='Пилот'>
                                          <label class="form-check-label" for="3">
                                            Пилот
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="4" value='Метеоролог'>
                                          <label class="form-check-label" for="4">
                                            Метеоролог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="5" value='Инженер по жизнеобеспечению'>
                                          <label class="form-check-label" for="5">
                                            Инженер по жизнеобеспечению
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="6" value='Инженер по радиационной защите'>
                                          <label class="form-check-label" for="6">
                                            Инженер по радиационной защите
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="7" value='Врач'>
                                          <label class="form-check-label" for="7">
                                            Врач
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof" id="8" value='Экзобиолог'>
                                          <label class="form-check-label" for="8">
                                            Экзобиолог
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                               
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form.get('surname'))
        print(request.form.get('firstname'))
        print(request.form.get('email'))
        print(request.form.get('education'))
        print(request.form.getlist('prof'))
        print(request.form.get('sex'))
        print(request.form.get('about'))
        print(request.form.get('accept'))
        f = request.files['file']
        print(f.read())
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
