# npm --> node package manager

#pipenv 

#variables

#let age = 55
age = 55
name = 'pepe'
alive = True
dead = False

#console.log()---> print

print('hola!')
print(age)

print(name)
print('name')
print(dead, alive)

#tipos de datos

#texto --> '', ""
#texto preformateado `` --> f"" f''
print ('hola')
print ("hola")
print(f'hola, como estas {name}') # seria nuestro console.log(`hola, como estas ${name}`)

# number --> 0 0.2 -5 
# integer --> 0 5 10 58 5678463 
# float 0.5 0.9 1.5 7.5689

# null o undefined es None

# arrays ---> listas
# lista --> nuestro array --> ['arr', 'arb', 'arc']

#sets y tuplas 
# set es una listas con valores unicos, se representa con ()
# mySet = (1,2,3,4,5,6)
 
#tuplas 
# un array ordenado
# myTupla = {1,2,33,4,5}


#objetos 
# js --> {} --> obj  
# python --> {} --> diccionario

dict = {
    'name': 'pepe',
    'age': 55,
    'alive': True
}


print(dict)
print(dict['alive'])


#boolean
#True/False

## operadores logicos
# == igual a 
# < menor
# > mayor 
# <= menor igual
# >igual
# and
# or

# print(5=='5') #false, el == es como el === de js
# print(5>4)
# print(5<4)
# print(5>=5)
# print(5<=5)

# print(1>0 and 5<6)
# print(1>0 or 5<4 or 5<7)
# print((1>3 or 5<3) and 5==5)

##condicionales

# if (1>3):
#     print('respuesta dentro del if')
#     print('es mayor')
# print(' esto esta fuera del if')


# if (2>1):
#     print('es mayor que uno')
#     if (3>2):
#         print('es mayor que 2')

# age = 55
# if age is 5:
#     print('adivino!!!!')

# if age is not 10:
#     print('se escapo un console.log()')
# print(1 != 20)
# #if else

# if age is not None:
#     print('avemus edad!')
# else:
#     print('dime tu edad!!!!')

# #if else if else---> if elif else
# if age<16:
#     print('no puedes manejar')
# elif age<21:
#     print('puedes manejar')
# else:
#     print('puedes manejar y beber')

# test = 5 if 1>2 else 25 # como una ternaria en js
# print(test)


# ## funciones

# def myFunc():
#     return 'mi primera funcion'

# print(myFunc) # llamado
# print(myFunc()) #ejecucion

# def sum(a,b):
#     print(a)
#     print(b)
#     total = a+b
#     return total

# print(sum(5,8))


#loops

# for num in range(10):
#     print(num)



# for num in range(5,10):
#     print(num)



# for num in range(0,10,3):
#     print(num)

arr = ['pepe', 'lola', 'maria']
arr_dos = ['matia', 'julian', 'chelo']
print('len ---> ',len(arr))


for index in range(len(arr)):
    print('index ',index)
    print ('arr[index]', arr[index])

for num in arr:
    print('for directo --> ', num)


# arr.map(for_map)
# arr.map(el => console.log(el))

#map recibe primero funcion a ejecutar, ya sea una def o una lambda y como segundo o N cantidad de parametros, saeran todos iterables

def for_map(n, y):
    return len(n) + len(y)

#mapped = map(for_map, arr) ---> devuelve <map object at 0x7f6801895210>

mapped = list(map(for_map, arr, arr_dos)) #poner list para que devuelva como una lista la informacion
print(mapped)

y = list(map(lambda x: x+' Gomez', arr))
print(y)


def isEqualToFive(n):
    return len(n)==5

long_names = list(filter(isEqualToFive, arr))
print(long_names)


#funciones lambda son como las arrow functions pero SOLO SE PUEDEN DECLARAR EN UNA SOLA LINEA

#const cuadrados = num => num**2

#esto no se puede hacer con una funcion lambda, tiene que ser una sola linea
#const cuadrados = num => {
# let aux = num**2
# total = num**2 + aux
# return total
# }
cuadrados = lambda num: num **2
print(cuadrados(84))

suma = lambda a,b : a+b

print(suma(4,9))

##no se pueden sumar letras con numeros
print(str(2)+'hola') #str(2) convierte el 2 a '2' 



#----------------------------------------------------segunda parte--------------------------------------------------------------------------

def printer(string):
    print('ejecutando la funcion printer')
    print(string)


#un loop que ejecuta una funcion 
for i in range(10):
    printer(i)


#una funcion con un loop 
def loopInFunction():
    for num in range(5):
        print(num*2)
    return 'completed'

print(loopInFunction())

def returnsList():
    return [5,6,7,8]
#iterando el retorno de una funcion 
for num in returnsList(): #siempre cuando pensamos en funciones, pensamos en lo que retorna la funcion
    print(num)


ls = [1,2,3,4,5,6]
#range recibe 3 parametros, 
# el primero es donde incia
# el segundo, donde termina
# el tercero los pasos que da desde el inicio hasta el final
for num in range(10, 0, -1):
    print('-1s',num)
