if __name__ == '__main__':
    from tkinter import *
    from tkinter import ttk
    from stadium import *
    from club import *
    from kdk import *
    from Backend.Modules.Users2 import *
else:
    from tkinter import *
    from tkinter import ttk
    from UI.stadium import *
    from UI.club import *
    from UI.kdk import *
    from Backend.Modules.Users2 import *


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

    def check_club():
        pass

    def del_club():
        pass

    search = Entry()
    search.grid(row=0, column=2)
    add_stadium = Button(text="Добавить стадион", command=window_of_stadium)
    add_stadium.grid(row=0, column=0)
    add_club = Button(text="Добавить клуб", command=window_of_club)
    add_club.grid(row=0, column=1)
    add_club = Button(text="Добавить Заседание КДК", command=window_of_kdk)
    add_club.grid(row=0, column=2)
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
    count_of_row = 1
    try:
        for i in users_info():
            lbl = Label(frame_lables, text=f'{i[0]}')
            lbl.grid(column=0, row=count_of_row)
            lbl = Label(frame_lables, text=f'{i[1]}')
            lbl.grid(column=1, row=count_of_row)
            lbl = Label(frame_lables, text=f'{i[2]}')
            lbl.grid(column=2, row=count_of_row)
            lbl = Label(frame_lables, text=f'{i[3]}')
            lbl.grid(column=3, row=count_of_row)
            lbl = Label(frame_lables, text=f'{i[4]}')
            lbl.grid(column=4, row=count_of_row)
            btn_info = Button(frame_lables, text="Смотреть", command=check_club)
            btn_info.grid(column=5, row=count_of_row)
            btn_del = Button(frame_lables, text="Удалить", command=del_club)
            btn_del.grid(column=6, row=count_of_row)
            count_of_row += 1
    except TypeError as err:
        print(f'Ошибка {err}')  # забить в логи

    main_menu.update()
    canvas.config(scrollregion=canvas.bbox("all"))

    tab_control.add(tab_of_clubs, text='Клубы')
    tab_control.grid(row=1, rowspan=5, column=0, columnspan=5)

    tab_control.add(tab_of_stadiums, text='Стадионы')
    tab_control.grid(row=1, rowspan=5, column=0, columnspan=5)

    tab_control.add(tab_of_kdk, text='КДК')
    tab_control.grid(row=1, rowspan=5, column=0, columnspan=5)

    tab_control.add(tab_of_penalty, text='Штрафы')
    tab_control.grid(row=1, rowspan=5, column=0, columnspan=5)

    main_menu.mainloop()