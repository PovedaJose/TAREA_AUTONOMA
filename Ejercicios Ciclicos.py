class Ejercicios:     
    def __init__(self):
        pass
    

    """Estructuras FOR"""
    def Ejercicio11(self):           
        i=1
        suma=0
        for i in range(100):
            suma= suma+i*i
            i+=1
        print("La suma de los 100 números es: {}" .format(suma))
    

    
    """Estructuras WHILE"""
    def Ejercicio12(self):   
        i=1
        while i<=100:
            print("Presentación de los números: {}" .format(i))
            i+=1
        return i
    


    def Ejercicio13(self):   
        suma=0
        prod=1
        print("Desea continuar [S/N]:  ")
        resp= input().capitalize()
        while resp == "S":
            nume= int(input("Ingrese un número: "))
            suma= suma+nume
            prod= prod*nume
            print("El total de la suma es: {}" .format(suma))
            print("El total del prod es: {}" .format(prod))
            print("Desea continuar [S/N]:  ")
            resp=input().capitalize()
    


    def Ejercicio14(self):    
        suma=0
        prod=1
        nume= int(input("Ingrese un número: "))
        while nume!=-1:
            suma= suma+nume
            prod= prod*nume
            print("El total de la suma es: {}" .format(suma))
            print("El total del prod es: {}" .format(prod))
            nume= int(input("Ingrese un número: "))
    


    def Ejercicio15(self):    
        primo= True
        divisor=2
        nume= int(input("Ingrese un número: "))
        while divisor<nume and primo==True:
            res= nume%divisor
            if res==0:
                primo= False
            divisor+=1
        if primo== True:
            print("El número {} es primo" .format(nume))
        else:
            print("El número {} no es primo" .format(nume))
    
    

    """Estructuras REPEAT"""
    def Ejercicio16(self):                 
        I=1
        Serie=0
        nume= int(input("Ingrese un número: "))
        Band=True
        while Band:
            if Band ==True:
                Serie= Serie+(1/I)
                Band= False
            else:
                Serie= Serie-(1/I)
                Band= True
            I+=1
            if I>nume:
                break
            print("El resultado de la Serie es: {}" .format(Serie))
    
    
    
    """Bucles anidados"""
    def Ejercicio17(self):                  
        nume= int(input("Ingrese un número: "))
        fact=1
        for i in range(1, nume+1):
            fact*=i
        print("El factorial del número {} es: {}" .format(nume, fact))


clase1= Ejercicios()
clase1.Ejercicio11()
clase1.Ejercicio12()
clase1.Ejercicio13()
clase1.Ejercicio14()
clase1.Ejercicio15()
clase1.Ejercicio16()
clase1.Ejercicio17()