from Backend.Modules.Users2 import *
# from UI.MainMenu import *
from Backend.Modules.Kdk_modul import *
from tkinter import *
from os import *
from pyperclip import copy, paste
from functools import partial
import windnd

# club = Club('огонь', 'вода', 'fdsf', 'fdsf', 'fdsf', 'fdsf', 'fdsf', 'fdsf', 1234, 1234, 1234, 1234, 'dfdfs', 1234,
#             1234,
#             1234, 1, 1, 1, 1, 1, 1)
#
# her = State(club, 'name', 'second_name', 'patrom', '7489895', 'email', 'name_of_state',
#             1, 'licence')
# stad = Stadium('Спартаковец', 'Спартаковец', 'fsdfs', 'fsdfs', 'fsdfs', 'fsdfs', 'fsdfs', 1234, 123, 123, 123,
#                1, 1, 1, '2021-06-18', 1, '2021-06-18', 1, 'hgfhf')
#
# club2=Club('Земля', 'воздух', 'fdsf', 'fdsf', 'fdsf', 'fdsf', 'fdsf', 'fdsf', 1234, 1234, 1234, 1234, 'dfdfs', 1234, 1234,
#             1234, 1, 1, 1, 1, 1, 1)
# #
# #
# zas=KDK('2021-06-11','Пробуем создать заседание')
# zas.creat_case('Д-125-2021', '12:00:00', [club,club2],
#                'Первенства г.Москвы по футболу среди '
#                'команд спортивных школ «Пятая Лига» сезона 2021г.',
#                [81,85,93],0,1,'Пробуем создать дело')
# case=zas.cases[0]
# print(case.creat_notification)
# case.creat_notification()
# print(case.my_notifications[0].create_notification)
# case.my_notifications[0].create_notification()


# attet = Attestation(club, stad, 2020, 1, 1, 1, 1, 1, 'contract', '2021-06-18')
#
def window_of_kdk():
    pass

def window_of_case():
    window = Toplevel()
    window.title('Дело')
    window.geometry('600x600')

def window_of_stadium():
    window= Toplevel()
    window.title('Добавить Стадион')
    window.geometry('800x800')
    # titles=[ 'Полное наименование юридического лица','Сокращенное наименование','Организационно-правовая форма',
    #          'Юридический адрес','Фактический адрес','Телефон','Email', 'Сайт', 'ИНН', 'КПП', 'ОКПО', 'ОГРН','Наименовае Банка',
    #          'Корреспонденсткий счет', 'Расчетный счет', 'БИК банка', 'Наличие Устава(1 - если есть, 0- если нет)',
    #          'Регистрация в МинЮсте (обязательно для НКО) (1 - если есть, 0- если нет)',
    #          'Регистрация в налоговой (1 - если есть, 0- если нет)',
    #          'Протокол создания юридического лица (1 - если есть, 0- если нет)',
    #          'Протокол назначения руководителя Юридического лица (1 - если есть, 0- если нет)',
    #          'Документ подтверждающий наличие офиса (1 - если есть, 0- если нет)']
    # for lbl in range (0)
    # text=Text(window,width=25, height=5, wrap=WORD)
    # text.grid(row=0, column=0)
def save_pth(key, file):
    all_txt_items[key].insert('1.0', file)

all_txt_items = {}
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

def start():
    main_menu = Tk()
    main_menu.title('База команд МФФ')
    main_menu.geometry('1366x768')

    @connect
    def users_info():
        query = 'select * from info_about_all_users;'
        cursor.execute(query)
        number = cursor.fetchall()
        return number

    def show_users(count):
        try:
            for i in users_info():
                lbl = Label(frame_lables, text=f'{i[0]}')
                lbl.grid(column=0, row=count)
                f=f'{i[0]}'
                lbl1 = Label(frame_lables, text=f'{i[1]}')
                lbl1.grid(column=1, row=count)
                lbl2 = Label(frame_lables, text=f'{i[2]}')
                lbl2.grid(column=2, row=count)
                lbl3 = Label(frame_lables, text=f'{i[3]}')
                lbl3.grid(column=3, row=count)
                lbl4 = Label(frame_lables, text=f'{i[4]}')
                lbl4.grid(column=4, row=count)
                btn_info = Button(frame_lables, text="Смотреть", command=partial(check_club, lbl.cget("text")))
                btn_info.grid(column=5, row=count)
                btn_del = Button(frame_lables, text="Удалить", command=del_club)
                btn_del.grid(column=6, row=count)
                count += 1
        except TypeError as err:
            print(f'Ошибка {err}')  # забить в логи

    def check_club(ghg):
        print(ghg)
        # window = Toplevel()
        # window.title('Клуб')
        # window.geometry('600x600')

    def del_club():
        pass

    def meeting_info():
        meetings=listdir(getcwd()+'\\MFF_Base\\КДК')
        print(meetings)
        for meet in range(len(meetings)):
            lbl = Label(frame_meeting, text=f'{meetings[meet]}')
            lbl.grid(column=0, row=1)
            lbl = Label(frame_meeting, text='')
            lbl.grid(column=1, row=1)
            # txt_col = Text(window, width=30, height=3, wrap=WORD)
            # txt_col.grid(row=txt, column=1)

    def update():
        main_menu.update()
        show_users(1)
        meeting_info()


    search = Entry()
    search.grid(row=0, column=2)
    add_stadium = Button(text="Добавить стадион", command=window_of_stadium)
    add_stadium.grid(row=0, column=0)
    add_club = Button(text="Добавить клуб", command=window_of_club)
    add_club.grid(row=0, column=1)
    add_club = Button(text="Добавить Заседание КДК", command=window_of_kdk)
    add_club.grid(row=0, column=2)
    update_button=Button(text="Обновить", command=update)
    update_button.grid(row=0, column=3)
    tab_control = ttk.Notebook(main_menu)
    # Вкладки
    tab_of_users = ttk.Frame(tab_control, width=560, height=560)
    tab_of_clubs = ttk.Frame(tab_control, width=560, height=560)
    tab_of_stadiums = ttk.Frame(tab_control, width=560, height=560)
    tab_of_kdk = ttk.Frame(tab_control, width=560, height=560)
    tab_of_penalty = ttk.Frame(tab_control, width=560, height=560)
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
    add_button=Button(frame_meeting,text="Добавить заседание", command=window_of_case)
    add_button.grid(column=3, row=0)
    main_menu.update()
    canvas_kdk.config(scrollregion=canvas.bbox("all"))


    tab_control.add(tab_of_penalty, text='Штрафы')
    tab_control.grid(row=1, rowspan=5, column=0, columnspan=5)

    main_menu.mainloop()

start()


# проверить правильно ли добавляется штат в клуб
# убрать старый label во вкладе "Новый Клуб"
