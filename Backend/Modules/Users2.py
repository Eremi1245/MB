from configparser import ConfigParser
from functools import wraps
import mysql.connector
from mysql.connector import Error
from os import getcwd
from datetime import datetime as dt

if __name__ == '__main__':
    path_to_db = getcwd()[0:-16] + '\\DB\\db_config.ini'
else:
    path_to_db = getcwd() + '\\DB\\db_config.ini'


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

conn = mysql.connector.connect(**db_config)  # соединение с базой данных

cursor = conn.cursor()  # курсор


def connect(func):
    """Подключение в БД """

    @wraps(func)
    def wrapper(*args, **kwargs):
        connec = mysql.connector.connect(**db_config)

        try:
            # print('Соединение с MySQL базой...')
            if not connec.is_connected():
                # print('соединение установлено.')
                print('соединения нет!!!.')
            # else:
            #     print('соединения нет!!!.')

        except Error as error:
            print(error)
        func_result = func(*args, **kwargs)
        if func_result:
            connec.close()
            # print('Соединение закрыто.')
            return func_result
        else:
            connec.close()
            # print('Соединение закрыто.')

    return wrapper


users = []


class User:

    def __init__(self, type_of_user):
        self.type_of_user = type_of_user
        self.user_id = len(users) + 1
        users.append(self)

    @connect
    def add_to_db(self):
        """
        Добавить юзера в БД
        """
        table = 'users'
        columns = 'id, users_type'
        values = {1: [f"{self.user_id}, '{self.type_of_user}'"]}
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
    def update_data_user(self, table, columns, vls):
        """
        Обновление данных о юзере
        """
        quer_vls = ''
        columns = columns.split(' ')
        vls = vls.split(' ')
        if len(columns) == len(vls):
            for i in range(len(columns)):
                quer_vls = quer_vls + f"{columns[i]}='{vls[i]}', "

        query = f"UPDATE {table} SET {quer_vls[:-2]} WHERE id ={self.user_id}"
        cursor.execute(query)
        conn.commit()


class Club:
    def __init__(self, name, phone='None', email='None', shrt_name='None',
                 o_p_f='None', jur_addr='None', fact_addr='None', site='None', inn=0, kpp=0, okpo=0, ogrn=0,
                 bank_name=0,
                 cor_ac=0, check_ac=0, bik=0, ustav=0, reg_in_min_just=0,
                 reg_in_tax=0, creat_club=0, creat_rucovod=0, ofice=0):
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
        self.attestations = {}
        self.user_club = User('Клуб')
        self.user_club.add_to_db()
        self.add_to_db()

    @connect
    def add_to_db(self):
        table = 'clubs'
        columns = 'club_id,name,phone,email,shrt_name,o_p_f,jur_addr,' \
                  'fact_addr,site,inn,kpp,okpo,ogrn,bank_name,cor_ac,' \
                  'check_ac,bik,ustav,reg_in_min_just,reg_in_tax,creat_club,creat_rucovod,ofice'
        values = f"({self.user_club.user_id},'{self.name}', '{self.phone}', '{self.email}', '{self.shrt_name}'," \
                 f"'{self.o_p_f}', '{self.jur_addr}','{self.fact_addr}', '{self.site}', '{self.inn}'," \
                 f"'{self.kpp}', '{self.okpo}','{self.ogrn}', '{self.bank_name}', '{self.cor_ac}'," \
                 f"'{self.check_ac}', '{self.bik}', '{self.ustav}','{self.reg_in_min_just}'," \
                 f"'{self.reg_in_tax}', '{self.creat_club}', '{self.creat_rucovod}','{self.ofice}')"
        query = f"INSERT INTO {table}({columns}) VALUES {values}"
        cursor.execute(query)
        conn.commit()

    @connect
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
                 site='None', email='None', inn='None', kpp='None', okpo='None', ogrn='None', in__reg_stad=0,
                 conf_in_expluatation=0, instr_pub_order=0, instr_pub_order_date_until='2021-01-01',
                 act_categ=0, act_categ_date_until='2021-01-01', statd_plan=0, category='no category'):
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
        self.in__reg_stad = in__reg_stad
        self.conf_in_expluatation = conf_in_expluatation
        self.instr_pub_order = instr_pub_order
        self.instr_pub_order_date_until = instr_pub_order_date_until
        self.act_categ = act_categ
        self.act_categ_date_until = act_categ_date_until
        self.statd_plan = statd_plan
        self.category = category
        self.user_stadium = User('Стадион')
        self.user_stadium.add_to_db()
        self.add_to_db()

    @connect
    def add_to_db(self):
        table = 'stadiums'
        columns = 'stad_id,name,shrt_name,o_p_f,jur_addr,phone,site,email,inn,kpp,okpo,ogrn,in__Reg_stad,' \
                  'conf_in_expluatation,instr_pub_order,instr_pub_order_date_until,act_categ,' \
                  'act_categ_date_until,statd_plan,category_RFS'
        values = f"({self.user_stadium.user_id},'{self.name}', '{self.shrt_name}', '{self.o_p_f}', '{self.jur_addr}'," \
                 f"'{self.phone}', '{self.site}','{self.email}', '{self.inn}', '{self.kpp}','{self.okpo}', " \
                 f"'{self.ogrn}','{self.in__reg_stad}', '{self.conf_in_expluatation}', '{self.instr_pub_order}'," \
                 f"'{self.instr_pub_order_date_until}', '{self.act_categ}'," \
                 f" '{self.act_categ_date_until}','{self.statd_plan}','{self.category}')"
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


class Attestation:
    ation_id = 1

    def __init__(self, club, stadium, year, application_1=0, application_2=0, application_3=0,
                 application_4=0, application_5=0, document='None', document_until='0000-00-00'):
        self.stad_id = stadium.user_stadium.user_id
        self.club_id = club.user_club.user_id
        self.year = year
        # Заявления
        self.application_1 = application_1
        self.application_2 = application_2
        self.application_3 = application_3
        self.application_4 = application_4
        self.application_5 = application_5
        self.document = document
        self.document_until = document_until
        self.add_to_db()

    @connect
    def add_to_db(self):
        table = 'attestation'
        columns = 'club_id,`year`,application_1 , application_2 ,' \
                  'application_3,application_4 , application_5 ,' \
                  'stadium ,document,document_until'
        values = f"({self.club_id},{self.year}, {self.application_1}, {self.application_2}," \
                 f" {self.application_3},{self.application_4}, {self.application_5}," \
                 f"{self.stad_id}, '{self.document}', '{self.document_until}')"
        query = f"INSERT INTO {table}({columns}) VALUES {values}"
        cursor.execute(query)
        conn.commit()

    @connect
    def del_from_db(self):
        cursor.execute(f'DELETE FROM attestation WHERE id = {self.id}')
        conn.commit()

    @connect
    def update_attestation(self, columns='', vls=''):
        columns = columns.split(' ')
        vls = vls.split(' ')
        for i in range(len(columns)):
            setattr(self, columns[i], vls[i])
        self.check_stad_status()
        self.check_status()
        quer_vls = f"club_id={self.club_id},`year`='{self.year}',application_1='{self.application_1}'," \
                   f"application_2='{self.application_2}',application_3='{self.application_3}' ," \
                   f"application_4='{self.application_4}' ,application_5='{self.application_5}' ," \
                   f"reg_in_min_just='{self.reg_in_min_just}' ,reg_in_tax='{self.reg_in_tax}' ," \
                   f"creat_club='{self.creat_club}',ustav='{self.ustav}' ,creat_rucovod='{self.creat_rucovod}' ," \
                   f"ofice='{self.ofice}' ,stadium='{self.stad_id}' ,document='{self.document}' ," \
                   f"document_until='{self.document_until}' ,stadium_status='{self.stad_status}' ," \
                   f"status'='{self.status}'"
        query = f"UPDATE attestation SET {quer_vls} WHERE id={self.id}"
        cursor.execute(query)
        conn.commit()
