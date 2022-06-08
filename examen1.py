class Docente:
    def __init__(self, nombre, apellido, edad):
        self.nombre=nombre
        self.apellido = apellido
        self.edad= int(edad)
    def RecibirDato(self):
        self.nombre=input('ingrese nombre: ')
        self.apellido=input('ingrese apellido: ')
        self.edad=int(input('ingrese edadd: '))

class ExtrasDocente(Docente):
    def __init__ (self, salario):
        self.rol= ' docente'
        self.departameto=['computacion ', 'ciencias exactas', 'ciencias medicas']
        self.salario=salario
        
while True:
    '''
    En esta aparteado se encuentra un condicional el cual 
    nosserivara para definir el numeros de dato que tendra nuestra lista
        - Con lo siguiente se encuetra condicionado 
          con que si el numero ingresado tiene que ser mayor o igual a 5 '''
    cantidad= int(input('ingrese el numero de frutas que ingresara: '))
    if cantidad>0: # while corre al infinito por lo que esto lo condiciona(salir del bucle se el # es 5 o mayor) 
        break

for i in range(0, cantidad): 
    docente1= ExtrasDocente(0)
    docente1.RecibirDato()
    listaDocentes=[]
    departament= int(input('0.computacion 1.ciencias exactas 2.cienciades medicas ingrese el departamento a definir: '))

    docente1.salario= (input('ingrese el salario: '))
    print(_______________________________________________________)

    listaDocentes.append(docente1)
print(docente1.nombre)
print(docente1.apellido)
print(docente1.edad)
print(docente1.rol)
print(docente1.salario)
print(docente1.departameto[departament])
for i in range(0, 1): # primer ouput de la lista 
    print(listaDocentes)
