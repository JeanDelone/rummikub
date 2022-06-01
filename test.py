from cards import *

card = Card(BLACK, 1)

lista1 = [
    [Card(BLACK, 1), Card(BLACK, 2)],
    [Card(BLACK, 1), Card(BLACK, 4)],
    [Card(BLUE, 3)],
    [Card(BLACK, 1), Card(BLACK, 2), Card(BLACK, 3)],
    [Card(BLACK, 1), Card(BLACK, 2), Card(BLACK, 3), Card(BLACK, 4)],
]

lista2 = [
    [Card(BLACK, 1), Card(BLACK, 2)],
    [Card(BLACK, 1), Card(BLACK, 4)],
    [Card(BLUE, 3)],
    [Card(BLACK, 1), Card(BLACK, 2), Card(BLACK, 3), Card(BLACK, 4)],
    [Card(BLACK, 1), Card(BLACK, 2), Card(BLACK, 3)]
]

lista3 = [
    [Card(BLACK, 1), Card(BLACK, 2)],
    [Card(BLACK, 1), Card(BLACK, 4)],
    [Card(BLUE, 3)],
    [Card(BLACK, 1), Card(BLACK, 2), Card(BLACK, 3)],
    [Card(BLACK, 1), Card(BLACK, 2), Card(BLACK, 3), Card(BLACK, 4)]
]
print(lista1==lista3)
print(lista1==lista2)
print(lista1)
print(lista2)
print(sorted(lista2, key = lambda lista: sorted(lista, key = lambda x: (x.number, x.color))) == sorted(lista2, key = lambda lista: sorted(lista, key = lambda x: (x.number, x.color))))
# print(sorted(lista2, key = lambda lista: (lista[0].number, len(lista))) == sorted(lista1, key = lambda x: (x[0].number, len(x))))











# copy_lista = lista1.copy()

# temporary_removal_list = []
# for list in lista1:
#     if card in list:
        
#         temporary_removal_list.append(list)

# for element in temporary_removal_list:
#     copy_lista.remove(element)


# print(copy_lista)

