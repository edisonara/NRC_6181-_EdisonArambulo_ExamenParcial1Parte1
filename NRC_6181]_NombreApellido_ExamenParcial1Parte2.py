from holidays import CA


class Calculo:
    def __init__(self):
        '''
        inicializado en nuestra clase
        '''
        pass
    def Factorial(self, factorial):
        '''calculamos los datos el factorial de un numero

        pasa un valor 
        retorna el resultado contar '''
        for contar in range(1,factorial+1):
            
            contar=contar*(contar+2)
        return contar
    def Suma(self, contar):
        '''suma de una cadena de numeros 
           pasa la cantidad de numeros 
           '''
        for con in range(contar):
            sumar=sumar+sumar+ con
        return sumar


    def testPrimo(self, num):
        '''
        vemos si el numero es primo 
        pro lo qeu podemos decir que ç
        pasa el  valor 
        retorna verdadero o falso segun corresponda
        '''
        for n in range(2, num):
            if num % n == 0:
                print("No es primo", n, "es divisor")
                return False
        print("Es primo ")
        return True 

    def tesPrimos(self, dato1, dato2 ):
        pass


ecuacion= Calculo()## objeto instanciado de la clase Calculo
print(ecuacion.testPrimo(5))