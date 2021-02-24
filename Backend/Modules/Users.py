# 2.	Класс Клуб (юзер)
# 3.	Класс Штат(юзер)
# 4.	Класс тренер(штат)
# 5.	Класс Стадион(юзер)
# 6.	Класс Заседание КДК (юзер)
# 7.	Класс текстовый документ КДК (
# Функция создать
# Функция удалить
# Функция изменить
# Функция в пдф
# Функция отправить)
# 8.	Класс  уведомление КДК (текстовый документ КДК)
# 9.	Класс 
from configparser import ConfigParser
from functools import wraps
import mysql.connector
from mysql.connector import Error

def read_db_config(filename='db_config.ini', section='mysql'):
    """ Читает конфигурацию Базы данных и возвращает словарь с параметрами
    :param filename: имя конфига
    :param section: секция с данными базы данных
    :return: словарь с параментрами
    """
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return db


def connect(func):
    """Подключение в БД """
    @wraps(func)
    def wrapper(*args, **kwargs):
        db_config = read_db_config()

        try:
            print('Соединение с MySQL базой...')
            global conn
            conn = mysql.connector.connect(**db_config)
            global cursor
            cursor = conn.cursor()
            if conn.is_connected():
                print('соединение установлено.')
            else:
                print('соединения нет!!!.')

        except Error as error:
            print(error)
        func_result=func(*args, **kwargs)
        if func_result:
            conn.close()
            print('Соединение закрыто.')
            return func_result
        else:
            conn.close()
            print('Соединение закрыто.')

    return (wrapper)


class User:
	def __init__(self,name):
		self.name=name

	@connect
	def add_to_db(self,table=users,columns='name',values={1:self.name}):
    ''' Вставка значения'''
    value_str=''
    if len(values.keys())>1:
        for i in list(values.keys())[0:-1]:
            value_str=value_str+str(values[i])+','+'\n'
        value_str=value_str+str(values[list(values.keys())[-1]])+';'
    else:
        value_str=value_str+f'({str(values[list(values.keys())[-1]])})'+';'
    
    if columns=='':
    	query = f"INSERT INTO {table} VALUES {value_str}"
    else:
    	query = f"INSERT INTO {table}({columns}) VALUES {value_str}"
    cursor.execute(query)
    conn.commit()

    @connect
    def del_from_db(self,table=users,columns='name',values={1:self.name}):
    	query = f"DELETE FROM {table} WHERE {columns} = {values[1]}"
    	cursor = conn.cursor()
	    cursor.execute(query, (book_id,))
	    conn.commit()


Функции изменить инфо в БД
