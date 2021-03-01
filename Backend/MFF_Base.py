from Modules.Users import *


x=Club('ЦСКА')
x1=Club('Спартак')
x2=Club('Локомотив')
x.add_to_db()
x1.add_to_db()
x2.add_to_db()
x.del_from_db()
x4=Club('Fabricf')
x4.add_to_db()
x2.update_data_user('phone email','79057630517 xxxdsds@mail.ru')
k=State('Спартак','Антон','Иванов','Владимирович')
k.add_to_db()
k1=State('Локомотив','Антон','Иванов','Владимирович')
k1.add_to_db()
k.del_from_db()
k1.update_data_user('phone email','79057630517 xxxdsds@mail.ru')

# # x1.add_to_db()
# print(x.user_id,x1.user_id,x2.user_id,x3.user_id,x5.user_id)
#
# if s.values():
#     print('тут что то есть')
# else:
#     print('тут ничего нет')
#
# s={1:2}
#
#
# if s.values():
#     print('тут что то есть')
# else:
#     print('тут ничего нет')