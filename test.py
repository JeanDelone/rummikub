from cards import *

card = Card(BLACK, 1)

lista1 = [
    [Card(BLACK, 1), Card(BLACK, 2)],
    [Card(BLACK, 1), Card(BLACK, 4)],
    [Card(BLUE, 3)],
    [Card(BLACK, 1), Card(BLACK, 2), Card(BLACK, 3)],
    [Card(BLACK, 1), Card(BLACK, 2), Card(BLACK, 3), Card(BLACK, 4)]
]

copy_lista = lista1.copy()

temporary_removal_list = []
for list in lista1:
    if card in list:
        
        temporary_removal_list.append(list)

for element in temporary_removal_list:
    copy_lista.remove(element)


print(copy_lista)

