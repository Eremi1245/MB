# from Backend.Modules.Users import *
from UI.Start_UI import *


# x=Club('ЦСКА')
# x.add_to_db()
# stad=Stadium('Спартаковец')
# stad.add_to_db()
# # x.attestation(stad,2021,'2020-02-02')
# # x.attestations[2021].add_to_db()
# print(users)

#Запускаем Интерфейс
app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())