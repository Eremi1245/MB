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
from os import getcwd
from time import sleep

path_to_db = getcwd()[0:-7] + 'DB\\db_config.ini'


def read_db_config(filename=path_to_db, section='mysql'):
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


db_config = read_db_config()

conn = mysql.connector.connect(**db_config)

cursor = conn.cursor()


def connect(func):
    """Подключение в БД """

    @wraps(func)
    def wrapper(*args, **kwargs):
        conn = mysql.connector.connect(**db_config)

        try:
            # print('Соединение с MySQL базой...')
            if not conn.is_connected():
                # print('соединение установлено.')
                print('соединения нет!!!.')
            # else:
            #     print('соединения нет!!!.')

        except Error as error:
            print(error)
        func_result = func(*args, **kwargs)
        if func_result:
            conn.close()
            # print('Соединение закрыто.')
            return func_result
        else:
            conn.close()
            # print('Соединение закрыто.')

    return (wrapper)


class User:
    users_id = 1

    def __init__(self, type):
        self.type = type
        self.user_id = User.users_id
        User.users_id += 1

    @connect
    def add_to_db(self):
        """
		Добавить юзера в БД
		"""
        table = 'users'
        columns = 'id, users_type'
        values = {1: [f"{self.user_id}, '{self.type}'"]}
        value_str = ''
        value_str = value_str + f'({",".join(values[list(values.keys())[0]])})' + ';'
        query = f"INSERT INTO {table}({columns}) VALUES {value_str}"

        cursor.execute(query)
        conn.commit()

    @connect
    def del_from_db(self):
        """
		Удалить юзера из БД
		"""
        query = f'DELETE FROM users WHERE id = {self.user_id}'
        cursor.execute(query)
        conn.commit()

    @connect
    def update_data_user(self, table, columns, vls, id):
        """
		Обновление данных о юзере
		"""
        quer_vls = ''
        columns = columns.split(' ')
        vls = vls.split(' ')
        if len(columns) == len(vls):
            for i in range(len(columns)):
                quer_vls = quer_vls + f"{columns[i]}='{vls[i]}', "

        query = f"UPDATE {table} SET {quer_vls[:-2]} WHERE {id}={self.user_id}"
        cursor.execute(query)
        conn.commit()


class Club:
    def __init__(self, name, shrt_name='None', o_p_f='None', jur_addr='None', fact_addr='None', phone='None',
                 site='None', email='None', inn='None', kpp='None', okpo='None', ogrn='None', bank_name='None',
                 cor_ac='None', check_ac='None', bik='None', ustav='None', reg_in_min_just='None', reg_in_tax='None',
                 creat_club='None', creat_rucovod='None', ofice='None'):
        self.name = name
        self.shrt_name = shrt_name
        self.o_p_f = o_p_f
        self.jur_addr = jur_addr
        self.fact_addr = fact_addr
        self.phone = phone
        self.site = site
        self.email = email
        self.inn = inn
        self.kpp = kpp
        self.okpo = okpo
        self.ogrn = ogrn
        self.bank_name = bank_name
        self.cor_ac = cor_ac
        self.check_ac = check_ac
        self.bik = bik
        self.ustav = ustav
        self.reg_in_min_just = reg_in_min_just
        self.reg_in_tax = reg_in_tax
        self.creat_club = creat_club
        self.creat_rucovod = creat_rucovod
        self.ofice = ofice
        self.user_club = User('Клуб')
        self.user_club.add_to_db()

    @connect
    def add_to_db(self):
        table = 'clubs'
        columns = 'club_id,name,phone,email,shrt_name,o_p_f,jur_addr,' \
                  'fact_addr,site,inn,kpp,okpo,ogrn,bank_name,cor_ac,' \
                  'check_ac,bik,ustav,reg_in_min_just,reg_in_tax,creat_club,''creat_rucovod,ofice'
        values = f"({self.user_club.user_id},'{self.name}', '{self.phone}', '{self.email}', '{self.shrt_name}'," \
                 f"'{self.o_p_f}', '{self.jur_addr}','{self.fact_addr}', '{self.site}', '{self.inn}'," \
                 f"'{self.kpp}', '{self.okpo}','{self.ogrn}', '{self.bank_name}', '{self.cor_ac}'," \
                 f"'{self.check_ac}', '{self.bik}', '{self.ustav}','{self.reg_in_min_just}'," \
                 f"'{self.reg_in_tax}', '{self.creat_club}', '{self.creat_rucovod}','{self.ofice}')"
        query = f"INSERT INTO {table}({columns}) VALUES {values}"
        cursor.execute(query)
        conn.commit()

    def del_from_db(self):
        query = f'DELETE FROM clubs WHERE club_id = {self.user_club.user_id}'
        cursor.execute(query)
        conn.commit()
        self.user_club.del_from_db()

    @connect
    def update_data_user(self, columns='', vls=''):
        self.user_club.update_data_user(table='clubs', columns=columns, vls=vls, id='club_id')


class State:
    def __init__(self, club_id, name, second_name, patrom='None', phone='None', email='None', name_of_state='None',
                 doc_of_study='None', licence='None'):
        self.club_id = self.check_club_id(club_id)
        self.name = name
        self.second_name = second_name
        self.patrom = patrom
        self.phone = phone
        self.email = email
        self.name_of_state = name_of_state
        self.doc_of_study = doc_of_study
        self.licence = licence
        self.user_state = User('Сотрудник Клуба')
        self.user_state.add_to_db()

    @connect
    def add_to_db(self):
        table = 'club_state'
        columns = 'user_id,club_id,name, second_name, patrom,phone, email, name_of_state,doc_of_study,licence'
        values = f"({self.user_state.user_id},{self.club_id},'{self.name}', '{self.second_name}', '{self.patrom}', " \
                 f"'{self.phone}','{self.email}', '{self.name_of_state}','{self.doc_of_study}', '{self.licence}')"
        query = f"INSERT INTO {table}({columns}) VALUES {values}"
        cursor.execute(query)
        conn.commit()

    def del_from_db(self):
        query = f'DELETE FROM club_state WHERE user_id = {self.user_state.user_id}'
        cursor.execute(query)
        conn.commit()
        self.user_state.del_from_db()

    @connect
    def update_data_user(self, columns='', vls=''):
        self.user_state.update_data_user(table='club_state', columns=columns, vls=vls, id='user_id')

    @connect
    def check_club_id(self, club_id):
        query = f"select club_id from clubs where name='{club_id}'"
        cursor.execute(query)
        result = cursor.fetchall()[0][0]
        return result


class Stadium:
    def __init__(self, name, shrt_name='None', o_p_f='None', jur_addr='None', phone='None',
                 site='None', email='None', inn='None', kpp='None', okpo='None', ogrn='None', in__Reg_stad=0,
                 conf_in_expluatation=0,instr_pub_order=0,instr_pub_order_date_until='2021-01-01',
                 act_categ=0,act_categ_date_until='2021-01-01',statd_plan=0):
        self.name = name
        self.shrt_name = shrt_name
        self.o_p_f = o_p_f
        self.jur_addr = jur_addr
        self.phone = phone
        self.site = site
        self.email = email
        self.inn = inn
        self.kpp = kpp
        self.okpo = okpo
        self.ogrn = ogrn
        self.in__Reg_stad =in__Reg_stad
        self.conf_in_expluatation = conf_in_expluatation
        self.instr_pub_order = instr_pub_order
        self.instr_pub_order_date_until = instr_pub_order_date_until
        self.act_categ = act_categ
        self.act_categ_date_until = act_categ_date_until
        self.statd_plan = statd_plan
        self.user_stadium = User('Стадион')
        self.user_stadium.add_to_db()

    @connect
    def add_to_db(self):
        table = 'stadiums'
        columns = 'stad_id,name,shrt_name,o_p_f,jur_addr,phone,site,email,inn,kpp,okpo,ogrn,in__Reg_stad,' \
                  'conf_in_expluatation,instr_pub_order,instr_pub_order_date_until,act_categ,' \
                  'act_categ_date_until,statd_plan'
        values = f"({self.user_stadium.user_id},'{self.name}', '{self.shrt_name}', '{self.o_p_f}', '{self.jur_addr}'," \
                 f"'{self.phone}', '{self.site}','{self.email}', '{self.inn}', '{self.kpp}','{self.okpo}', " \
                 f"'{self.ogrn}','{self.in__Reg_stad}', '{self.conf_in_expluatation}', '{self.instr_pub_order}'," \
                 f"'{self.instr_pub_order_date_until}', '{self.act_categ}'," \
                 f" '{self.act_categ_date_until}','{self.statd_plan}')"
        query = f"INSERT INTO {table}({columns}) VALUES {values}"
        cursor.execute(query)
        conn.commit()

    def del_from_db(self):
        query = f'DELETE FROM stadiums WHERE stad_id = {self.user_stadium.user_id}'
        cursor.execute(query)
        conn.commit()
        self.user_stadium.del_from_db()

    @connect
    def update_data_user(self, columns='', vls=''):
        self.user_stadium.update_data_user(table='stadiums', columns=columns, vls=vls, id='stad_id')

#     @connect
# def attestation():
#     id,club_id,year,date,application_1,application_2
#     tinyint
#     default
#     '0'
#     COMMENT
#     'О проведении политики ',
#     application_3
#     tinyint
#     default
#     '0'
#     COMMENT
#     'Соблюдение регламентов',
#     application_4
#     tinyint
#     default
#     '0'
#     COMMENT
#     'Список сотрудников',
#     application_5
#     tinyint
#     default
#     '0'
#     COMMENT
#     'Гарантийное письмо',
#     reg_in_min_just
#     tinyint
#     default
#     '0',
#     reg_in_tax
#     tinyint
#     default
#     '0',
#     creat_club
#     tinyint
#     default
#     '0',
#     ustav
#     enum('Актуальные', 'Не актуальные'),
#     creat_rucovod
#     enum('Актуальные', 'Не актуальные'),
#     ofice
#     enum('Актуальные', 'Не актуальные'),
#     stadium
#     BIGINT
#     UNSIGNED
#     NOT
#     NULL,
#     document
#     VARCHAR(255),
#     document_until
#     Date,
#     stadium_status
#     tinyint
#     default
#     '0',
#     status
#     tinyint
#     default
#     '0',