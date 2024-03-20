from flask import Flask, url_for, render_template, request, redirect, session
import sqlite3
from back import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def logination():
    global password_zn, login_zn
    
    if request.method=="GET":
        return render_template('log.html') 
    else:
        passwod_correct = request.form.get('password_zn')
        login_correct = request.form.get('login_zn')


        if login_check(login_correct):
            if pass_check(passwod_correct):
                session['auth'] = True
                return redirect(url_for('start'))
            else:
                return '<p> Пароль невірний </p>'
        else:
            return '<h1> Невірний логін</h1>'

@app.route('/start', methods=['GET', 'POST'])
def start():
    if request.method=="GET" and session['auth'] is True:
        names = get_info()
        named = tuple(sorted(names))
        return render_template('start.html', name_list = named)
    
    elif session['auth'] is False:
        return '<h1> Авторизуйтеся </h1>' 
    
    else:
        person = request.form.get('persons')
        info_about = get_name_and_info(person)
        return render_template('people.html', name=info_about[1], info=info_about[3], photo = info_about[2]) 


@app.route('/people', methods=['GET', 'POST'])
def people():
    if request.method=="GET":
        person = request.form.get('exit')
        info_about = get_name_and_info(person)
        return render_template('people.html', name=info_about[1], info=info_about[3]) 
    else:
        pass

@app.route('/new', methods=['GET', 'POST'])
def new_people():
    print('на сторінці')
    if request.method=="GET":
        return render_template('new.html') 
    else:
        print('пароль створюється')
        passwod_new = request.form.get('password_new')
        login_new = request.form.get('login_new')
        print(passwod_new, login_new)
        new_people(login_new, passwod_new)
        return '<h1> Запис пройшов успішно </h1>'


app.config['SECRET_KEY'] = '12345678'

if __name__ == '__main__':
    app.run(port=8000)