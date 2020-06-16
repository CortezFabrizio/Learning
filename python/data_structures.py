# Data Structures


#Listas para una serie de valores ordenados accesibles mediante su posicion y agregando o eliminando,etc
Lista = ["dou",2]

acceso_elemento = print(Lista[0])

agregando_lista = input("Elemento a introducir en la lista ")
agregado = Lista.append(agregando_lista)
print(Lista)

#------------------------------------------------------------------------------------------------------

#Diccionarios Para entablar elemento con una clave de acceso:

Diccionarios = {"Clave":"Elemento","Argentina":"Buenos Aires",1:"dou"}

acceso_dic = print(Diccionarios["Clave"])
#Para modificar un elemento:
agregando_dic = Diccionarios["Clave"]=2
print(Diccionarios)

#Agregar clave y elemento
gh = Diccionarios["ds"]= 2
print(Diccionarios)

#-----------------------------------------------------------------------------------------------------------------

#Tuplas para tener una lista inmutable

tupla_ejemplo = (1,"dou",5)
print(tupla_ejemplo[1])

# Esto no se puede hacer por su naturaleza de no contar con ese atributo : tupla_ejemplo.append("string")

#--------------------------------------------------------------------------------------------------------


# Mediante sets los elementos no se repiten,no se puede tampoco acceder a un elemento especifico con [posicion](estan desordenados),y solo
# puedes agregar elementos

set_ejemplo_intentar_repeticiones = {1,6,1}
#Solo imprime sus elementos sin repeticion

print(set_ejemplo_intentar_repeticiones)
