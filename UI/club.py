from tkinter import *

#Клуб
def window_of_club():
    window= Toplevel()
    window.title('Добавить Клуб')
    window.geometry('1366x600')
    titles=[ 'Полное наименование юридического лица','Сокращенное наименование','Организационно-правовая форма',
             'Юридический адрес','Фактический адрес','Телефон','Email', 'Сайт', 'ИНН', 'КПП', 'ОКПО', 'ОГРН','Наименовае Банка',
             'Корреспонденсткий счет', 'Расчетный счет', 'БИК банка', 'Наличие Устава (1 - если есть, 0- если нет)',
             'Регистрация в МинЮсте (обязательно для НКО) (1 - если есть, 0- если нет)',
             'Регистрация в налоговой (1 - если есть, 0- если нет)',
             'Протокол создания юридического лица (1 - если есть, 0- если нет)',
             'Протокол назначения руководителя Юридического лица (1 - если есть, 0- если нет)',
             'Документ подтверждающий наличие офиса (1 - если есть, 0- если нет)']
    all_txt_items={}
    for lbl in range(0,10):
        lbl_col=Label(window,text=titles[lbl],width=25,height=3,background='lightblue',anchor=W,wraplength=160,justify=LEFT)
        lbl_col.grid(row=lbl, column=0)
    for txt in range(0,10):
        txt_col=Text(window,width=30, height=3, wrap=WORD)
        txt_col.grid(row=txt, column=1)
        all_txt_items[titles[txt]]=txt_col
    for lbl in range(10,20):
        lbl_col=Label(window,text=titles[lbl],width=25,height=3,background='lightblue',anchor=W,wraplength=160,justify=LEFT)
        lbl_col.grid(row=lbl-10, column=2)
    for txt in range(10,20):
        txt_col=Text(window,width=30, height=3, wrap=WORD)
        txt_col.grid(row=txt-10, column=3)
        all_txt_items[titles[txt]]=txt_col
    for lbl in range(20,22):
        lbl_col=Label(window,text=titles[lbl],width=35,height=3,background='lightblue',anchor=W,wraplength=180,justify=LEFT)
        lbl_col.grid(row=lbl-20, column=4)
    for txt in range(20,22):
        txt_col=Text(window,width=30, height=3, wrap=WORD)
        txt_col.grid(row=txt-20, column=5)
        all_txt_items[titles[txt]]=txt_col

    creatClub=Button(window,text='Создать Клуб',command=creat_club,width=35,height=3)
    creatClub.grid(row=2,column=4,sticky=W)

    clr = Button(window, text='Очистить', command=clear, width=35, height=3)
    clr.grid(row=3, column=4, sticky=W)

def creat_club():
    pass

def clear():
    pass


