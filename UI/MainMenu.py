if __name__ == '__main__':
    from tkinter import *
    from tkinter import ttk
    from stadium import *
    from club import *
    from kdk import *
    from CaseGui import *
    from Backend.Modules.Users2 import *
    from os import *
    from pyperclip import copy,paste
    from functools import partial
else:
    from tkinter import *
    from tkinter import ttk
    from UI.stadium import *
    from UI.club import *
    from UI.kdk import *
    from UI.CaseGui import *
    from Backend.Modules.Users2 import *
    from os import *
    from pyperclip import copy, paste
    from functools import partial

esc_num=115

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
