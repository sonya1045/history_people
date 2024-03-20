import sqlite3

db_name = 'historical_people.db'

def open():  #функція відкриття бази даних
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()


def close():     #функція закриття бд
    cursor.close()
    conn.close()


def do(query):  #запит
    cursor.execute(query)
    conn.commit()

def clear_db():
    ''' видаляє всі таблиці '''
    open()
    query = '''DROP TABLE IF EXISTS quiz_content'''
    do(query)
    query = '''DROP TABLE IF EXISTS questions'''
    do(query)
    query = '''DROP TABLE IF EXISTS quiz'''
    do(query)
    close()

    
def create(): #створюємо три нові таблиці
    open()
    do('''CREATE TABLE IF NOT EXISTS auth(
        id INTEGER PRIMARY KEY,
        login VARCHAR,
        password VARCHAR) ''')
    
    do('''CREATE TABLE IF NOT EXISTS history_peoples(
        id INTEGER PRIMARY KEY,
        name VARCHAR,
        photo VARCHAR,
        info TEXT)''')
    
    close()


def login_check(login_zn):
    open()
    cursor.execute('SELECT login FROM auth WHERE login == ?', [login_zn])
    res = cursor.fetchone()
    
    conn.commit()
    close()
    if res is not None:
        return True
    else:
        return False


def pass_check(password_zn):
    open()
    cursor.execute('SELECT password FROM auth WHERE password == ?', [password_zn])
    res = cursor.fetchone()
    
    conn.commit()
    close()
    if res is not None:
        return True
    else:
        return False
    
def add_people():  #додати вікторину
    names = [
        ('Нікола Тесла', ),
        ('Леонардо да Вінчі', ),
        ('Ісаак Ньютон', ),

    ]
    open()
    cursor.executemany('''INSERT INTO history_peoples (name) VALUES (?)''', names)
    conn.commit()
    close()

def get_info():
    '''Повертає назви'''
    open()
    cursor.execute('SELECT id, name FROM history_peoples ORDER BY name')
    result = cursor.fetchall()
    close()
    print(result)
    return result

def get_name_and_info(person):
    open()
    cursor.execute('SELECT id, name, photo, info FROM history_peoples WHERE id = ? ORDER BY id', (person,))
    info = cursor.fetchone()
    close()
    return info

def new_people(new_login, new_password):
    open()
    cursor.execute('INSERT INTO auth (login, password) VALUES (?, ?)', (new_login, new_password))
    conn.commit()
    close()
    
def main():  #головна функція з запуском всіх функцій
    # clear_db()
    # create()
    # add_people()
    # get_info()
    pass


if __name__ == "__main__":
    main()