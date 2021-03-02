from Modules.Users import *


x=Club('ЦСКА')
x.add_to_db()
stad=Stadium('Спартаковец')
stad.add_to_db()
x.attestation(stad,2021,'2020-02-02')
x.attestations[2021].add_to_db()
print(x.attestations)
print(x.attestations[2021].status)

