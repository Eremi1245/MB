from Backend.Modules.Users2 import *
from UI.MainMenu import *
from Backend.Modules.Kdk_modul import *


club = Club('ЦСКА', 'ЦСКА', 'fdsf', 'fdsf', 'fdsf', 'fdsf', 'fdsf', 'fdsf', 1234, 1234, 1234, 1234, 'dfdfs', 1234, 1234,
            1234, 1, 1, 1, 1, 1, 1)
stad = Stadium('Спартаковец', 'Спартаковец', 'fsdfs', 'fsdfs', 'fsdfs', 'fsdfs', 'fsdfs', 1234, 123, 123, 123,
               1, 1, 1, '2021-06-18', 1, '2021-06-18', 1, 'hgfhf')
club2=Club('ЦСКА', 'fdsf', 'fdsf', 'fdsf', 'fdsf', 'fdsf', 'fdsf', 'fdsf', 1234, 1234, 1234, 1234, 'dfdfs', 1234, 1234,
            1234, 1, 1, 1, 1, 1, 1)

#
# zas=KDK('2021-06-11','')
# zas.creat_folder()
# case=Case('2021-06-11','Д-1-2021',club,club2,91)
# zas.cases.append(case)
# case.creat_folder()
# case.creat_notification()
j=Notification('2021-06-11',club,club2,91)


# attet = Attestation(club, stad, 2020, 1, 1, 1, 1, 1, 'contract', '2021-06-18')
#

# start()

#создать отображение базы на текущий момент в главном меню
# убрать старый label во вкладе "Новый Клуб"