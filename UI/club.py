from tkinter import *
from Backend.Modules.Users2 import *

# Клуб
all_txt_items = {}


def window_of_club():
    window = Toplevel()
    window.title('Добавить Клуб')
    window.geometry('1366x600')
    titles = ['Полное наименование юридического лица', 'Сокращенное наименование', 'Организационно-правовая форма',
              'Юридический адрес', 'Фактический адрес', 'Телефон', 'Email', 'Сайт', 'ИНН', 'КПП', 'ОКПО', 'ОГРН',
              'Наименовае Банка',
              'Корреспонденсткий счет', 'Расчетный счет', 'БИК банка', 'Наличие Устава (1 - если есть, 0- если нет)',
              'Регистрация в МинЮсте (обязательно для НКО) (1 - если есть, 0- если нет)',
              'Регистрация в налоговой (1 - если есть, 0- если нет)',
              'Протокол создания юридического лица (1 - если есть, 0- если нет)',
              'Протокол назначения руководителя Юридического лица (1 - если есть, 0- если нет)',
              'Документ подтверждающий наличие офиса (1 - если есть, 0- если нет)']

    # Функиця создания Клуба
    def creat_club():
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
                            all_txt_items['Наличие Устава (1 - если есть, 0- если нет)'].get('1.0', END),
                            all_txt_items[
                                'Регистрация в МинЮсте (обязательно для НКО) (1 - если есть, 0- если нет)'].get('1.0',
                                                                                                                END),
                            all_txt_items['Регистрация в налоговой (1 - если есть, 0- если нет)'].get('1.0', END),
                            all_txt_items['Протокол создания юридического лица (1 - если есть, 0- если нет)'].get('1.0',
                                                                                                                  END),
                            all_txt_items[
                                'Протокол назначения руководителя Юридического лица (1 - если есть, 0- если нет)'].get(
                                '1.0', END),
                            all_txt_items['Документ подтверждающий наличие офиса (1 - если есть, 0- если нет)'].get(
                                '1.0', END))
            new_user_label = Label(window,
                                   text=f'Клуб {all_txt_items["Сокращенное наименование"].get("1.0", END)} создан '
                                        f'и добавлен в базу, номер id - {new_user.user_club.user_id}',
                                   width=35, height=3, background='green', anchor=W, wraplength=180, justify=LEFT)
            new_user_label.grid(row=2, column=5, sticky=W)
        except Exception as er:
            new_user_label = Label(window,
                                   text=f'Клуб {all_txt_items["Сокращенное наименование"].get("1.0", END)} не создан, '
                                        f'ошибка: {er}',
                                   width=35, height=5, background='red', anchor=W, wraplength=180, justify=LEFT)
            new_user_label.grid(row=2, column=5, sticky=W)

    # Продолэаем создавать меню
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
    for txt in range(10, 20):
        txt_col = Text(window, width=30, height=3, wrap=WORD)
        txt_col.grid(row=txt - 10, column=3)
        all_txt_items[titles[txt]] = txt_col
    for lbl in range(20, 22):
        lbl_col = Label(window, text=titles[lbl], width=35, height=3, background='lightblue', anchor=W, wraplength=180,
                        justify=LEFT)
        lbl_col.grid(row=lbl - 20, column=4)
    for txt in range(20, 22):
        txt_col = Text(window, width=30, height=3, wrap=WORD)
        txt_col.grid(row=txt - 20, column=5)
        all_txt_items[titles[txt]] = txt_col

    create_club_button = Button(window, text='Создать Клуб', command=creat_club, width=35, height=3)
    create_club_button.grid(row=2, column=4, sticky=W)

    clr = Button(window, text='Очистить', command=clear, width=35, height=3)
    clr.grid(row=3, column=4, sticky=W)


def clear():
    for item in all_txt_items:
        all_txt_items[item].delete('1.0', END)
