#se puede modificar
lista = ["matias godoy","mati",True,1.98]

#no se puede modificar la tupla
tupla=("matias godoy","mati",True,1.98) 

lista[0] = 'mesi'
print(lista[1])#pisicion 1

#conjunto no se puede acceder por un indice y no almacena datos duplicados
conjunto = {"matias godoy","mati",True,1.98,"mati"}

#diccionario (dict)
diccionario = {
    'nombre':"matias godoy",
    'lugar':'quilicura', 
    'altura': 1.72,
    'estado': True
}
print(diccionario['nombre']);