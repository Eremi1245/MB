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

		try:
			print('Соединение с MySQL базой...')
			if conn.is_connected():
				print('соединение установлено.')
			else:
				print('соединения нет!!!.')

		except Error as error:
			print(error)
		func_result = func(*args, **kwargs)
		if func_result:
			conn.close()
			print('Соединение закрыто.')
			return func_result
		else:
			conn.close()
			print('Соединение закрыто.')

	return (wrapper)


class User:
	users_id = 1

	def __init__(self, name, phone='None', email='None'):
		self.name = name
		self.phone = phone
		self.email = email
		self.user_id = User.users_id
		User.users_id += 1

	@connect
	def add_to_db(self, table='users', columns='id, users_type, phone,email', values={}):
		"""
		Добавить юзера в БД
		:param table: Таблица для добавления
		:param columns: в какие колонки
		:param values: значения в виде value_str[первая строка]= [значение один,значение два, значение три]
		:return:
		"""
		if not values.keys:
			values[1] = [f"{self.user_id}, '{self.name}','{self.phone}','{self.email}'"]
		value_str = ''
		if len(values.keys()) > 1:
			for i in list(values.keys())[0:-1]:
				value_str = value_str + f'({str(values[i])})' + ',' + '\n'
			value_str = value_str + f'({str(values[list(values.keys())[-1]])})' + ';'
		elif len(values.keys()) == 1:
			value_str = value_str + f'({",".join(values[list(values.keys())[0]])})' + ';'

		if columns == '':
			query = f"INSERT INTO {table} VALUES {value_str}"
		else:
			query = f"INSERT INTO {table}({columns}) VALUES {value_str}"
		print(query)
		cursor.execute(query)
		conn.commit()

	@connect
	def del_from_db(self, table='users', columns='name', values={}):
		"""
		Удалить юзера из БД
		:param self:
		:param table:
		:param columns:
		:param values:
		:return:
		"""
		if not values.keys:
			values[1] = self.name
		query = f'DELETE FROM {table} WHERE {columns} = {values[1]}'
		cursor.execute(query)
		conn.commit()

	@connect
	def update_data_user(self, table='users', columns='name', values={}):
		"""
		Обновление данных о юзере
		:param values:
		:param table: 
		:param columns: 
		:return: 
		type value_str: dict
		"""
		if not values.keys:
			values[1] = self.name
		query = f"UPDATE {table} SET {columns} = {values[1]} WHERE {columns}={self.name}"
		cursor.execute(query)
		conn.commit()


class Club(User):
	def __init__(self, name, shrt_name='None', o_p_f='None', jur_addr='None', fact_addr='None', phone='None',
				 site='None', email='None', inn='None', kpp='None', okpo='None', ogrn='None', bank_name='None',
				 cor_ac='None', check_ac='None', bik='None', ustav='None', reg_in_min_just='None', reg_in_tax='None',
				 creat_club='None', creat_rucovod='None', ofice='None'):
		self.shrt_name = shrt_name
		self.o_p_f = o_p_f
		self.jur_addr = jur_addr
		self.fact_addr = fact_addr
		self.site = site
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
		super().__init__(name, phone, email)

	def add_to_db(self):
		super(Club, self).add_to_db(table='clubs', columns='club_id,name,phone,email,shrt_name,o_p_f,jur_addr,'
														   'fact_addr,site,inn,kpp,okpo,ogrn,bank_name,cor_ac,'
														   'check_ac,bik,ustav,reg_in_min_just,reg_in_tax,creat_club,'
														   'creat_rucovod,ofice', values={
			1: [f"{self.user_id},'{self.name}', '{self.phone}', '{self.email}', '{self.shrt_name}', '{self.o_p_f}', '{self.jur_addr}',"
				f"'{self.fact_addr}', '{self.site}','{self.inn}', '{self.kpp}', '{self.okpo}','{self.ogrn}', "
				f"'{self.bank_name}', '{self.cor_ac}', '{self.check_ac}', '{self.bik}', '{self.ustav}', "
				f"'{self.reg_in_min_just}','{self.reg_in_tax}', '{self.creat_club}', '{self.creat_rucovod}', "
				f"'{self.ofice}'"]})

	def del_from_db(self):
		super(Club, self).del_from_db(table='clubs', columns='name', values={})

	@connect
	def update_data_user(self, table='clubs', columns='', values={}):
		"""
		Изменить данные Клуба
		:param table: Таблица для добавления
		:param columns: в какие колонки вносим измненения
		:param values: значения в виде value_str[первая колонка]= новое значение
		:return:
		"""
		columns = columns.split(',')
		for col in range(len(columns)):
			query = f"UPDATE {table} SET {columns[col]} = {values[col]} WHERE club_id={self.user_id}"
			cursor.execute(query)
			conn.commit()


class State(User):
	def __init__(self, name, second_name, patrom='None', name_of_state='None', club_id='None', doc_of_study='None',
				 licence='None', phone='None', email='None'):
		self.second_name = second_name
		self.patrom = patrom
		self.name_of_state = name_of_state
		self.club_id = club_id
		self.doc_of_study = doc_of_study
		self.licence = licence
		super().__init__(name, phone, email)

		def add_to_db(self):
			super(State, self).add_to_db(table='club_state', columns='', values={
				1: [self.name, self.phone, self.email, self.second_name, self.patrom, self.name_of_state, self.club_id,
					self.doc_of_study, self.licence]})

		def del_from_db(self):
			super(State, self).del_from_db(table='club_state', columns='name', values={})

		@connect
		def update_data_user(self, table='club_state', columns='', values={}):
			columns = columns.split(',')
			for col in range(len(columns)):
				query = f"UPDATE {table} SET {columns[col]} = {values[col]} WHERE id={self.user_id}"
				cursor.execute(query)
				conn.commit()


class Stadium(User):
	pass
