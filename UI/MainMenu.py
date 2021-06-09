if __name__ == '__main__':
    from tkinter import *
    from stadium import *
    from club import *
else:
    from tkinter import *
    from UI.stadium import *
    from UI.club import *

def start():
    main_menu=Tk()
    main_menu.title('База команд МФФ')
    main_menu.geometry('1366x768')
    search = Entry()
    search.grid(row=0, column=2)
    add_stadium = Button( text="Добавить стадион",command=window_of_stadium)
    add_stadium.grid(row=0, column=0)
    add_club = Button( text="Добавить клуб",command=window_of_club)
    add_club.grid(row=0, column=1)
    main_menu.mainloop()

