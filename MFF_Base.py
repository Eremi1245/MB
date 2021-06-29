from Backend.Modules.Users2 import *
from Backend.Modules.Kdk_modul import *
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
from os import *
from functools import partial
import windnd


# 3.Визуал КДК (Для вкладки) + окно "Создания заседания"
# 4.Визуал уведомление
# 5.Визуал решение
# 6.Визуал кнопки "Смотреть" для юзеров + Удаление
# 7.Добавление в каждую вкладку своих юзеров

@connect
def meet_info():
    query = 'select id,date_meeting,notes from kdk;'
    cursor.execute(query)
    meetings = cursor.fetchall()
    return meetings


def window_of_case():
    case_window = Toplevel()
    case_window.title('Дело')
    case_window.geometry('600x600')


all_txt_items_stad = {}

files_paths_stad = {}


def window_of_stadium():
    stad_window = Toplevel()
    stad_window.title('Добавить Стадион')
    stad_window.geometry('1100x600')
    stad_titles = ['Офиц Наименование', 'Название', 'Организационно-правовая форма',
                   'Юридический адрес', 'Телефон', 'Сайт', 'Email', 'ИНН', 'КПП', 'ОКПО', 'ОГРН',
                   'В реестре объектов спорта', 'Ввод в эксплуатацию',
                   'Инструкция по обеспечению безопасности', 'Инструкция до', 'Акт обследования и категорирования',
                   'Акт до', 'План стадиона', 'Категория РФС']

    # Функиця создания Стадиона
    def creat_stad():
        if all_txt_items_stad['В реестре объектов спорта'].get('1.0', END)[0:-1] != '':
            reestr = 1
        else:
            reestr = 0
        if all_txt_items_stad['Ввод в эксплуатацию'].get('1.0', END)[0:-1] != '':
            eclpuatation = 1
        else:
            eclpuatation = 0
        if all_txt_items_stad['Инструкция по обеспечению безопасности'].get('1.0', END)[0:-1] != '':
            instruction = 1
        else:
            instruction = 0
        if all_txt_items_stad['Акт обследования и категорирования'].get('1.0', END)[0:-1] != '':
            act_categ = 1
        else:
            act_categ = 0
        if all_txt_items_stad['План стадиона'].get('1.0', END)[0:-1] != '':
            stad_plan = 1
        else:
            stad_plan = 0
        if all_txt_items_stad['Категория РФС'].get('1.0', END)[0:-1] == '':
            categ_rfs = 'no category'
        else:
            categ_rfs = all_txt_items_stad['Категория РФС'].get('1.0', END)[0:-1]
        try:
            new_stad = Stadium(all_txt_items_stad['Офиц Наименование'].get('1.0', END)[0:-1],
                               all_txt_items_stad['Название'].get('1.0', END)[0:-1],
                               all_txt_items_stad['Организационно-правовая форма'].get('1.0', END)[0:-1],
                               all_txt_items_stad['Юридический адрес'].get('1.0', END)[0:-1],
                               all_txt_items_stad['Телефон'].get('1.0', END)[0:-1],
                               all_txt_items_stad['Сайт'].get('1.0', END)[0:-1],
                               all_txt_items_stad['Email'].get('1.0', END)[0:-1],
                               all_txt_items_stad['ИНН'].get('1.0', END)[0:-1],
                               all_txt_items_stad['КПП'].get('1.0', END)[0:-1],
                               all_txt_items_stad['ОКПО'].get('1.0', END)[0:-1],
                               all_txt_items_stad['ОГРН'].get('1.0', END)[0:-1],
                               reestr, eclpuatation, instruction,
                               all_txt_items_stad['Инструкция до'].get('1.0', END)[0:-1],
                               act_categ, all_txt_items_stad['Акт до'].get('1.0', END)[0:-1],
                               stad_plan, categ_rfs)
            new_stad_label = Label(stad_window,
                                   text=f'Стадион {all_txt_items_stad["Название"].get("1.0", END)[0:-1]} создан '
                                        f'и добавлен в базу, номер id - {new_stad.user_stadium.user_id}',
                                   width=35, height=5, background='green', anchor=W, wraplength=180, justify=LEFT)
            new_stad_label.grid(row=5, column=4, sticky=W)
            new_stad.add_files(files_paths_stad)
        except Exception as er:
            new_stad_label = Label(stad_window,
                                   text=f'Стадион {all_txt_items_stad["Название"].get("1.0")} не создан, '
                                        f'ошибка: {er}',
                                   width=35, height=5, background='red', anchor=W, wraplength=180, justify=LEFT)
            new_stad_label.grid(row=5, column=4, sticky=W)
            print(er)

    def clear_stad_window():
        for item in all_txt_items:
            all_txt_items_stad[item].delete('1.0', END)

    def save_pth_stad(key_attr, file):
        file = file[0].decode('CP1251')
        all_txt_items_stad[key_attr].insert('1.0', file)
        files_paths_stad[key_attr] = file

    # создаем меню
    for lbl in range(0, 11):
        lbl_col = Label(stad_window, text=stad_titles[lbl], width=25, height=3,
                        background='lightblue', anchor=W, wraplength=160, justify=LEFT)
        lbl_col.grid(row=lbl, column=0)
    for txt in range(0, 11):
        txt_col = Text(stad_window, width=30, height=3, wrap=WORD)
        txt_col.grid(row=txt, column=1)
        all_txt_items_stad[stad_titles[txt]] = txt_col
    # Окна с возможностью перетащить документ
    for lbl in range(11, 14):
        lbl_col = Label(stad_window, text=stad_titles[lbl], width=25, height=3, background='lightblue', anchor=W,
                        wraplength=160,
                        justify=LEFT)
        lbl_col.grid(row=lbl - 11, column=2)
    for txt in range(11, 14):
        txt_col = Text(stad_window, width=30, height=3, wrap=WORD)
        txt_col.grid(row=txt - 11, column=3)
        all_txt_items_stad[stad_titles[txt]] = txt_col
        key = stad_titles[txt]
        windnd.hook_dropfiles(txt_col, func=partial(save_pth_stad, key))
    for lbl in range(14, 15):
        lbl_col = Label(stad_window, text=stad_titles[lbl], width=25, height=3, background='lightblue',
                        anchor=W, wraplength=160, justify=LEFT)
        lbl_col.grid(row=lbl - 11, column=2)
    for txt in range(14, 15):
        txt_col = Text(stad_window, width=30, height=3, wrap=WORD)
        txt_col.grid(row=txt - 11, column=3)
        all_txt_items_stad[stad_titles[txt]] = txt_col
    for lbl in range(15, 16):
        lbl_col = Label(stad_window, text=stad_titles[lbl], width=25, height=3, background='lightblue', anchor=W,
                        wraplength=160,
                        justify=LEFT)
        lbl_col.grid(row=lbl - 11, column=2)
    for txt in range(15, 16):
        txt_col = Text(stad_window, width=30, height=3, wrap=WORD)
        txt_col.grid(row=txt - 11, column=3)
        all_txt_items_stad[stad_titles[txt]] = txt_col
        key = stad_titles[txt]
        windnd.hook_dropfiles(txt_col, func=partial(save_pth_stad, key))
    for lbl in range(16, 17):
        lbl_col = Label(stad_window, text=stad_titles[lbl], width=25, height=3, background='lightblue', anchor=W,
                        wraplength=160,
                        justify=LEFT)
        lbl_col.grid(row=lbl - 11, column=2)
    for txt in range(16, 17):
        txt_col = Text(stad_window, width=30, height=3, wrap=WORD)
        txt_col.grid(row=txt - 11, column=3)
        all_txt_items_stad[stad_titles[txt]] = txt_col
    for lbl in range(17, 19):
        lbl_col = Label(stad_window, text=stad_titles[lbl], width=25, height=3, background='lightblue', anchor=W,
                        wraplength=160,
                        justify=LEFT)
        lbl_col.grid(row=lbl - 11, column=2)
    for txt in range(17, 19):
        txt_col = Text(stad_window, width=30, height=3, wrap=WORD)
        txt_col.grid(row=txt - 11, column=3)
        all_txt_items_stad[stad_titles[txt]] = txt_col
        key = stad_titles[txt]
        windnd.hook_dropfiles(txt_col, func=partial(save_pth_stad, key))

    create_stad_button = Button(stad_window, text='Создать Стадион', command=creat_stad, width=35, height=3)
    create_stad_button.grid(row=2, column=4, sticky=W)

    clr = Button(stad_window, text='Очистить', command=clear_stad_window, width=35, height=3)
    clr.grid(row=3, column=4, sticky=W)


# Функция для общей вкладки "Юзеры"
all_txt_items = {}

files_paths = {}

applic_data = {}


def save_pth(key, file):
    file = file[0].decode('CP1251')
    all_txt_items[key].insert('1.0', file)
    files_paths[key] = file


def clear():
    for item in all_txt_items:
        all_txt_items[item].delete('1.0', END)


# Окно создание клуба
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
        if all_txt_items['Устав (перетащить)'].get('1.0', END)[0:-1] != '':
            ustav = 1
        else:
            ustav = 0
        if all_txt_items['МинЮст (перетащить)'].get('1.0', END)[0:-1] != '':
            min_ust = 1
        else:
            min_ust = 0
        if all_txt_items['ФНС (перетащить)'].get('1.0', END)[0:-1] != '':
            fns = 1
        else:
            fns = 0
        if all_txt_items['Протокол создания юридического лица (перетащить)'].get('1.0', END)[0:-1] != '':
            creat_company = 1
        else:
            creat_company = 0
        if all_txt_items['Протокол назначения руководителя (перетащить)'].get('1.0', END)[0:-1] != '':
            header = 1
        else:
            header = 0
        if all_txt_items['Офис (перетащить)'].get('1.0', END)[0:-1] != '':
            ofice = 1
        else:
            ofice = 0
        try:
            new_user = Club(all_txt_items['Полное наименование юридического лица'].get('1.0', END)[0:-1],
                            all_txt_items['Телефон'].get('1.0', END)[0:-1],
                            all_txt_items['Email'].get('1.0', END)[0:-1],
                            all_txt_items['Сокращенное наименование'].get('1.0', END)[0:-1],
                            all_txt_items['Организационно-правовая форма'].get('1.0', END)[0:-1],
                            all_txt_items['Юридический адрес'].get('1.0', END)[0:-1],
                            all_txt_items['Фактический адрес'].get('1.0', END)[0:-1],
                            all_txt_items['Сайт'].get('1.0', END)[0:-1],
                            all_txt_items['ИНН'].get('1.0', END)[0:-1],
                            all_txt_items['КПП'].get('1.0', END)[0:-1],
                            all_txt_items['ОКПО'].get('1.0', END)[0:-1],
                            all_txt_items['ОГРН'].get('1.0', END)[0:-1],
                            all_txt_items['Наименовае Банка'].get('1.0', END)[0:-1],
                            all_txt_items['Корреспонденсткий счет'].get('1.0', END)[0:-1],
                            all_txt_items['Расчетный счет'].get('1.0', END)[0:-1],
                            all_txt_items['БИК банка'].get('1.0', END)[0:-1],
                            ustav, min_ust, fns, creat_company, header, ofice)
            new_user_label = Label(window,
                                   text=f'Клуб {all_txt_items["Сокращенное наименование"].get("1.0", END)[0:-1]} создан '
                                        f'и добавлен в базу, номер id - {new_user.user_club.user_id}',
                                   width=35, height=5, background='green', anchor=W, wraplength=180, justify=LEFT)
            new_user_label.grid(row=2, column=5, sticky=W)
            new_user.add_files(files_paths)
        except Exception as er:
            new_user_label = Label(window,
                                   text=f'Клуб {all_txt_items["Сокращенное наименование"].get("1.0", END)[0:-1]} не создан, '
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


# Основное меню
def start():
    main_menu = Tk()
    main_menu.title('База команд МФФ')
    main_menu.geometry('1366x768')

    # image2 = Image.open('img/main_menu.jpg')
    # image1 = ImageTk.PhotoImage(image2)
    # bg_label = Label(main_menu, image=image1)
    # bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    @connect
    def users_info():
        query = 'select * from info_about_all_users;'
        cursor.execute(query)
        number = cursor.fetchall()
        return number

    def show_users(count):
        try:
            for i in users_info():
                lbl0 = Label(frame_lables, text=f'{i[0]}')
                lbl0.grid(column=0, row=count)
                lbl1 = Label(frame_lables, text=f'{i[1]}')
                lbl1.grid(column=1, row=count)
                lbl2 = Label(frame_lables, text=f'{i[2]}')
                lbl2.grid(column=2, row=count)
                lbl3 = Label(frame_lables, text=f'{i[3]}')
                lbl3.grid(column=3, row=count)
                lbl4 = Label(frame_lables, text=f'{i[4]}')
                lbl4.grid(column=4, row=count)
                btn_info = Button(frame_lables, text="Смотреть", command=partial(look_club, lbl0.cget("text")))
                btn_info.grid(column=5, row=count)
                btn_del = Button(frame_lables, text="Удалить", command=del_club)
                btn_del.grid(column=6, row=count)
                count += 1
        except TypeError as err:
            print(f'Ошибка {err}')  # забить в логи

    @connect
    def look_club(ghg):
        print(ghg)
        # query = 'select * from info_about_all_users;'
        # cursor.execute(query)
        # number = cursor.fetchall()
        # return number
        # window = Toplevel()
        # window.title('Клуб')
        # window.geometry('600x600')

    def del_club():
        pass

    def meeting_info():
        meetings = meet_info()
        try:
            for meet in range(len(meetings)):
                lbl_obj = Label(frame_meeting, text=f'{meetings[meet][0]}')
                lbl_obj.grid(column=0, row=meet + 1)
                lbl_obj = Label(frame_meeting, text=f'{meetings[meet][1]}')
                lbl_obj.grid(column=1, row=meet + 1)
                lbl_obj = Label(frame_meeting, text=f'{meetings[meet][2]}')
                lbl_obj.grid(column=2, row=meet + 1)
                if len(meetings) != 0:
                    meet_button = Button(frame_meeting, text="Добавить Дело", command=window_of_case)
                    meet_button.grid(column=3, row=meet + 1)

                # txt_col = Text(window, width=30, height=3, wrap=WORD)
                # txt_col.grid(row=txt, column=1)
        except Error as er:
            print(er)

    def attet_window():
        try:
            att_window = Toplevel()
            att_window.title('Добавить Аттестацию')
            att_window.geometry('700x300')

            def creat_attestat():
                if applic_1.get('1.0', END)[:-1] == '':
                    appl_1 = 0
                else:
                    appl_1 = 1
                if applic_2.get('1.0', END)[:-1] == '':
                    appl_2 = 0
                else:
                    appl_2 = 1
                if applic_3.get('1.0', END)[:-1] == '':
                    appl_3 = 0
                else:
                    appl_3 = 1
                if applic_4.get('1.0', END)[:-1] == '':
                    appl_4 = 0
                else:
                    appl_4 = 1
                if applic_5.get('1.0', END)[:-1] == '':
                    appl_5 = 0
                else:
                    appl_5 = 1
                new_att = Attestation(clubs.get().split(',')[0][1:], stad.get().split(',')[0][1:], year.get(), appl_1,
                                      appl_2,
                                      appl_3, appl_4, appl_5, text_doc.get('1.0', END)[:-1],
                                      text_doc_until.get('1.0', END)[:-1])
                new_att.add_docs_to_club(clubs.get().split(',')[1][2:-4], applic_data)

            def install_mff(txt_object, lbl_object):
                k = Toplevel()
                k.title('Добавить Аттестацию')
                k.geometry('1x1')
                filename = filedialog.askopenfilename()
                txt_object.insert('1.0', filename)
                applic_data[lbl_object] = filename
                k.destroy()
                return filename

            @connect
            def take_clubs():
                query = 'select club_id, shrt_name from clubs;'
                cursor.execute(query)
                number = cursor.fetchall()
                return number

            def take_stads():
                query = 'select stad_id, shrt_name from stadiums;'
                cursor.execute(query)
                number = cursor.fetchall()
                return number

            # document = 'None', document_until = '0000-00-00'
            Label(att_window, text='Клуб').grid(row=0, column=0)
            clubs = StringVar(att_window)
            clubs.set([x for x in take_clubs()])
            komanda1 = OptionMenu(att_window, clubs, *[x for x in take_clubs()])
            komanda1.config(width=15)
            komanda1.grid(row=0, column=1)
            Label(att_window, text='Год').grid(row=0, column=2)
            year = StringVar(att_window)
            year.set(['2020', '2021', '2022', '2023', '2024', '2025'])
            attet_year = OptionMenu(att_window, year, *['2020', '2021', '2022', '2023', '2024', '2025'])
            attet_year.config(width=15)
            attet_year.grid(row=0, column=3)
            Label(att_window, text='Стадион').grid(row=0, column=4)
            stad = StringVar(att_window)
            stad.set([x for x in take_stads()])
            attet_stad = OptionMenu(att_window, stad, *[x for x in take_stads()])
            attet_stad.config(width=15)
            attet_stad.grid(row=0, column=5)
            Label(att_window, text='Заявление 1').grid(row=1, column=0)
            applic_1 = Text(att_window, width=15, height=1, wrap=WORD)
            applic_1.grid(row=1, column=2)
            applic_1_button = Button(att_window, text='Загрузить',
                                     command=partial(install_mff, applic_1, 'Заявление 1'),
                                     width=7, height=1)
            applic_1_button.grid(row=1, column=1)
            Label(att_window, text='Заявление 2').grid(row=2, column=0)
            applic_2 = Text(att_window, width=15, height=1, wrap=WORD)
            applic_2.grid(row=2, column=2)
            applic_2_button = Button(att_window, text='Загрузить',
                                     command=partial(install_mff, applic_2, 'Заявление 2'), width=7,
                                     height=1)
            applic_2_button.grid(row=2, column=1)
            Label(att_window, text='Заявление 3').grid(row=3, column=0)
            applic_3 = Text(att_window, width=15, height=1, wrap=WORD)
            applic_3.grid(row=3, column=2)
            applic_3_button = Button(att_window, text='Загрузить',
                                     command=partial(install_mff, applic_3, 'Заявление 3'), width=7,
                                     height=1)
            applic_3_button.grid(row=3, column=1)
            Label(att_window, text='Заявление 4').grid(row=4, column=0)
            applic_4 = Text(att_window, width=15, height=1, wrap=WORD)
            applic_4.grid(row=4, column=2)
            applic_4_button = Button(att_window, text='Загрузить',
                                     command=partial(install_mff, applic_4, 'Заявление 4'), width=7,
                                     height=1)
            applic_4_button.grid(row=4, column=1)
            Label(att_window, text='Заявление 5').grid(row=5, column=0)
            applic_5 = Text(att_window, width=15, height=1, wrap=WORD)
            applic_5.grid(row=5, column=2)
            applic_5_button = Button(att_window, text='Загрузить',
                                     command=partial(install_mff, applic_5, 'Заявление 5'), width=7,
                                     height=1)
            applic_5_button.grid(row=5, column=1)
            Label(att_window, text='Документ').grid(row=6, column=0)
            text_doc = Text(att_window, width=15, height=1, wrap=WORD)
            text_doc.grid(row=6, column=1)
            Label(att_window, text='Документ до').grid(row=7, column=0)
            text_doc_until = Text(att_window, width=15, height=1, wrap=WORD)
            text_doc_until.grid(row=7, column=1)
            creat_attestation = Button(att_window, text='Аттестировать', command=creat_attestat)
            creat_attestation.grid(row=8, column=0, columnspan=2)
        except Error as er:
            print(er)

    def update():
        main_menu.update()
        show_users(1)
        meeting_info()

    def add(date, notes, lbl_1):
        KDK(date.get('1.0', END)[0:-1], notes.get('1.0', END)[0:-1])
        date.destroy()
        notes.destroy()
        lbl_1.destroy()
        meeting_info()

    def window_of_kdk():
        meets = meet_info()
        if meets is None:
            meets = 1
        else:
            meets = len(meets) + 1
        label_for_kdk_1 = Label(frame_meeting, text='Укажите дату заседния',
                                background='lightblue', anchor=W, wraplength=160, justify=LEFT)
        label_for_kdk_1.grid(row=meets, column=0)
        text_for_kdk_1 = Text(frame_meeting, width=15, height=1, wrap=WORD)
        text_for_kdk_1.grid(row=meets, column=1)
        text_for_kdk_2 = Text(frame_meeting, width=15, height=5, wrap=WORD)
        text_for_kdk_2.grid(row=meets, column=2)
        button_for_kdk = Button(frame_meeting, text="Добавить",
                                command=partial(add, text_for_kdk_1, text_for_kdk_2, label_for_kdk_1))
        button_for_kdk.grid(row=meets, column=3)

    search = Entry()
    search.grid(row=0, column=2)
    add_stadium = Button(text="Добавить стадион", command=window_of_stadium)
    add_stadium.grid(row=0, column=0)
    add_club = Button(text="Добавить клуб", command=window_of_club)
    add_club.grid(row=0, column=1)
    add_kdk = Button(text="Добавить Заседание КДК", command=window_of_kdk)
    add_kdk.grid(row=0, column=2)
    attet_button = Button(text="Аттестация", command=attet_window)
    attet_button.grid(row=0, column=3)
    update_button = Button(text="Обновить", command=update)
    update_button.grid(row=0, column=4)
    tab_control = ttk.Notebook(main_menu)
    # Вкладки
    tab_of_users = Frame(tab_control, width=560, height=560)
    tab_of_clubs = Frame(tab_control, width=560, height=560)
    tab_of_stadiums = Frame(tab_control, width=560, height=560)
    tab_of_kdk = Frame(tab_control, width=560, height=560)
    tab_of_penalty = Frame(tab_control, width=560, height=560)
    # Размещение вкладок
    tab_control.add(tab_of_users, text='Юзеры')
    tab_control.grid(row=1, rowspan=5, column=0, columnspan=5)
    canvas = Canvas(tab_of_users, width=560, height=560)
    canvas.grid(row=0, column=0, sticky="news")
    # Link a scrollbar to the canvas
    vsb = Scrollbar(tab_of_users, orient="vertical", command=canvas.yview)
    vsb.grid(row=0, column=1, sticky='ns')
    canvas.configure(yscrollcommand=vsb.set)
    frame_lables = Frame(canvas, width=560, height=560)
    canvas.create_window((0, 0), window=frame_lables, anchor='nw')
    lbl = Label(frame_lables, text='ID')
    lbl.grid(column=0, row=0)
    lbl = Label(frame_lables, text='Название')
    lbl.grid(column=1, row=0)
    lbl = Label(frame_lables, text='сайт')
    lbl.grid(column=2, row=0)
    lbl = Label(frame_lables, text='Email')
    lbl.grid(column=3, row=0)
    lbl = Label(frame_lables, text='Статус')
    lbl.grid(column=4, row=0)
    lbl = Label(frame_lables, text='Инфо')
    lbl.grid(column=5, row=0)
    show_users(1)

    main_menu.update()
    canvas.config(scrollregion=canvas.bbox("all"))

    tab_control.add(tab_of_clubs, text='Клубы')
    tab_control.grid(row=1, rowspan=5, column=0, columnspan=5)

    tab_control.add(tab_of_stadiums, text='Стадионы')
    tab_control.grid(row=1, rowspan=5, column=0, columnspan=5)

    tab_control.add(tab_of_kdk, text='КДК')
    tab_control.grid(row=1, rowspan=5, column=0, columnspan=5)

    canvas_kdk = Canvas(tab_of_kdk, width=560, height=560)
    canvas_kdk.grid(row=0, column=0, sticky="news")
    # Link a scrollbar to the canvas
    vsb = Scrollbar(tab_of_kdk, orient="vertical", command=canvas.yview)
    vsb.grid(row=0, column=1, sticky='ns')
    canvas_kdk.configure(yscrollcommand=vsb.set)
    frame_meeting = Frame(canvas_kdk, width=560, height=560)
    canvas_kdk.create_window((0, 0), window=frame_meeting, anchor='nw')
    lbl = Label(frame_meeting, text='Заседание')
    lbl.grid(column=0, row=0)
    lbl = Label(frame_meeting, text='Решения')
    lbl.grid(column=1, row=0)
    lbl = Label(frame_meeting, text='Заметки')
    lbl.grid(column=2, row=0)
    meeting_info()
    add_button = Button(frame_meeting, text="Добавить Заседание", command=window_of_kdk)
    add_button.grid(column=3, row=0)
    main_menu.update()
    canvas_kdk.config(scrollregion=canvas.bbox("all"))

    tab_control.add(tab_of_penalty, text='Штрафы')
    tab_control.grid(row=1, rowspan=5, column=0, columnspan=5)

    main_menu.mainloop()


start()

# проверить правильно ли добавляется штат в клуб
# убрать старый label во вкладе "Новый Клуб"
