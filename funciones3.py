from cgi import print_arguments


print("\n----------EJERCICIO 1---------")
x = [ [5,2,3], [10,8,9] ]

for i in x[1]:
    lista = x[1]
    if lista[0] == 10:
        lista[0] = 15
#print("Resultado cambiado será:",x)

#Otra forma:

x[1][0] = 15
print("Resultado cambiado para x será:",x)


estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

lista2 = estudiantes[0]
lista2['last_name'] = 'Bryant'
print("Resultado cambiado para estudiantes será:",estudiantes)

#Otra forma:
estudiantes[0]['last_name'] = 'Bryant'

directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
directorio_deportes['fútbol'][0] = 'Andres'
print("El resultado cambiado para deportes será:", directorio_deportes)

z = [ {'x': 10, 'y': 20} ]
z[0]['y']=30
print("El resultado cambiado para z será:",z)

print("\n----------EJERCICIO 2---------")
estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(diccionario):
    for i in diccionario:
        lista_estudiantes = list(i.items()) 
        print(lista_estudiantes[0][0],"-", lista_estudiantes[0][1],",", lista_estudiantes[1][0],"-", lista_estudiantes[1][1]) #asi se imprimen cada elemento de la lista 
iterateDictionary(estudiantes)

print("\n----------EJERCICIO 3---------")
def names(dictionary):
    print("LISTA DE NOMBRES")
    for i in dictionary:
        dictionary_name = list(i.items())
        print(dictionary_name[0][1])
names(estudiantes)

def apellidos(dictionary):
    print("\nLISTA DE APELLIDOS")
    for i in dictionary:
        dictionary_last = list(i.items())
        print(dictionary_last[1][1])
apellidos(estudiantes)

print("\n----------EJERCICIO 4---------")
dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def info_dojo(diccionario):
    for i in diccionario:
        print("\n")
        print(str(len(diccionario[i])), i) #largo del diccionario con la clave
        for j in diccionario[i]:
            print(j)

info_dojo(dojo)
