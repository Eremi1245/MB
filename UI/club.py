from tkinter import *
from Backend.Modules.Users2 import *
from functools import partial
import windnd
from pyperclip import copy, paste



if __name__ == '__main__':
    path_to_db = getcwd()[0:-16] + '\\DB\\db_config.ini'
else:
    path_to_db = getcwd() + '\\DB\\db_config.ini'

home_cwd = getcwd()


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


# Клуб

all_txt_items = {}

@connect
def user_number():
    query = 'select COUNT(id) from users;'
    cursor.execute(query)
    number = cursor.fetchone()[0]
    return number


def save_pth(key, file):
    all_txt_items[key].insert('1.0', file)


def window_of_club():
    window = Toplevel()
    window.title('Добавить Клуб')
    window.geometry('1366x600')
    titles = ['Полное наименование юридического лица', 'Сокращенное наименование', 'Организационно-правовая форма',
              'Юридический адрес', 'Фактический адрес', 'Телефон', 'Email', 'Сайт', 'ИНН', 'КПП', 'ОКПО', 'ОГРН',
              'Наименовае Банка',
              'Корреспонденсткий счет', 'Расчетный счет', 'БИК банка', 'Устав (перетащить)',
              'МинЮст (перетащить)',
              'ФНС (перетащить)',
              'Протокол создания юридического лица (перетащить)',
              'Протокол назначения руководителя (перетащить)',
              'Офис (перетащить)']

    # Функиця создания Клуба
    def creat_club():
        data_for_folders = {}
        if all_txt_items['Устав (перетащить)'].get('1.0', END) != '':
            ustav = 1
            data_for_folders['Устав'] = all_txt_items['Устав (перетащить)'].get('1.0', END)
        else:
            ustav = 0
        if all_txt_items['МинЮст (перетащить)'].get('1.0', END) != '':
            min_ust = 1
            data_for_folders['МинЮст'] = all_txt_items['МинЮст (перетащить)'].get('1.0', END)
        else:
            min_ust = 0
        if all_txt_items['ФНС (перетащить)'].get('1.0', END) != '':
            fns = 1
            data_for_folders['ФНС'] = all_txt_items['ФНС (перетащить)'].get('1.0', END)
        else:
            fns = 0
        if all_txt_items['Протокол создания юридического лица (перетащить)'].get('1.0', END) != '':
            creat_company = 1
            data_for_folders['Прткл о создании'] = \
                all_txt_items['Протокол создания юридического лица (перетащить)'].get('1.0', END)
        else:
            creat_company = 0
        if all_txt_items['Протокол назначения руководителя (перетащить)'].get('1.0', END) != '':
            header = 1
            data_for_folders['Нзнч Руковод'] = \
                all_txt_items['Протокол назначения руководителя (перетащить)'].get('1.0', END)
        else:
            header = 0
        if all_txt_items['Офис (перетащить)'].get('1.0', END) != '':
            ofice = 1
            data_for_folders['Офис'] = all_txt_items['Офис (перетащить)'].get('1.0', END)
        else:
            ofice = 0
        try:
            new_user = Club(all_txt_items['Полное наименование юридического лица'].get('1.0', END),
                            all_txt_items['Телефон'].get('1.0', END),
                            all_txt_items['Email'].get('1.0', END),
                            all_txt_items['Сокращенное наименование'].get('1.0', END),
                            all_txt_items['Организационно-правовая форма'].get('1.0', END),
                            all_txt_items['Юридический адрес'].get('1.0', END),
                            all_txt_items['Фактический адрес'].get('1.0', END),
                            all_txt_items['Сайт'].get('1.0', END),
                            all_txt_items['ИНН'].get('1.0', END),
                            all_txt_items['КПП'].get('1.0', END),
                            all_txt_items['ОКПО'].get('1.0', END),
                            all_txt_items['ОГРН'].get('1.0', END),
                            all_txt_items['Наименовае Банка'].get('1.0', END),
                            all_txt_items['Корреспонденсткий счет'].get('1.0', END),
                            all_txt_items['Расчетный счет'].get('1.0', END),
                            all_txt_items['БИК банка'].get('1.0', END),
                            ustav, min_ust, fns, creat_company, header, ofice)
            new_user_label = Label(window,
                                   text=f'Клуб {all_txt_items["Сокращенное наименование"].get("1.0", END)} создан '
                                        f'и добавлен в базу, номер id - {new_user.user_club.user_id}',
                                   width=35, height=5, background='green', anchor=W, wraplength=180, justify=LEFT)
            new_user_label.grid(row=2, column=5, sticky=W)
            new_user.add_files(data_for_folders)
        except Exception as er:
            new_user_label = Label(window,
                                   text=f'Клуб {all_txt_items["Сокращенное наименование"].get("1.0", END)} не создан, '
                                        f'ошибка: {er}',
                                   width=35, height=5, background='red', anchor=W, wraplength=180, justify=LEFT)
            new_user_label.grid(row=2, column=5, sticky=W)
            print(er)

    # Продолжаем создавать меню
    for lbl in range(0, 10):
        lbl_col = Label(window, text=titles[lbl], width=25, height=3, background='lightblue', anchor=W, wraplength=160,
                        justify=LEFT)
        lbl_col.grid(row=lbl, column=0)
    for txt in range(0, 10):
        txt_col = Text(window, width=30, height=3, wrap=WORD)
        txt_col.grid(row=txt, column=1)
        all_txt_items[titles[txt]] = txt_col
    for lbl in range(10, 20):
        lbl_col = Label(window, text=titles[lbl], width=25, height=3, background='lightblue', anchor=W, wraplength=160,
                        justify=LEFT)
        lbl_col.grid(row=lbl - 10, column=2)
    for txt in range(10, 16):
        txt_col = Text(window, width=30, height=3, wrap=WORD)
        txt_col.grid(row=txt - 10, column=3)
        all_txt_items[titles[txt]] = txt_col
    # Окна с возможностью перетащить документ
    for txt in range(16, 20):
        txt_col = Text(window, width=30, height=3, wrap=WORD)
        txt_col.grid(row=txt - 10, column=3)
        all_txt_items[titles[txt]] = txt_col
        key = titles[txt]
        windnd.hook_dropfiles(txt_col, func=partial(save_pth, key))
    for lbl in range(20, 22):
        lbl_col = Label(window, text=titles[lbl], width=35, height=3, background='lightblue', anchor=W, wraplength=180,
                        justify=LEFT)
        lbl_col.grid(row=lbl - 20, column=4)
    for txt in range(20, 22):
        txt_col = Text(window, width=30, height=3, wrap=WORD)
        txt_col.grid(row=txt - 20, column=5)
        all_txt_items[titles[txt]] = txt_col
        key = titles[txt]
        windnd.hook_dropfiles(txt_col, func=partial(save_pth, key))

    create_club_button = Button(window, text='Создать Клуб', command=creat_club, width=35, height=3)
    create_club_button.grid(row=2, column=4, sticky=W)

    clr = Button(window, text='Очистить', command=clear, width=35, height=3)
    clr.grid(row=3, column=4, sticky=W)


def clear():
    for item in all_txt_items:
        all_txt_items[item].delete('1.0', END)
