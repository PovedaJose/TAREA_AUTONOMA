class Ejercicios:     
    def __init__(self):
        pass
    

    """Estructuras selectivas simples"""       
    def Ejercicio3(self): 
        calf= float(input("Ingrese la calificación del examen que obtuvo el estudiante: "))
        if calf >=7:
            print("La nota es {}, APROBADO" .format(calf))
    
    

    """Estructuras selectivas dobles"""           
    def Ejercicio4(self):                          
        Nota= float(input("Ingrese la calificación del examen que obtuvo el estudiante: "))
        if Nota >=7:
            print("La nota es {}, APROBADO" .format(Nota))
        else:
            print("La nota es {}, REPROBADO" .format(Nota))
    


    def Ejercicio5(self):                           
        Suel_I= float(input("Ingrese el sueldo que poseía: "))
        if Suel_I <= 600:
            N_Suel= Suel_I+(Suel_I*0.1)
            print("Su nuevo sueldo es {}" .format(N_Suel))
        else:
            N_Suel= Suel_I
            print("Su sueldo sigue siendo {}" .format(N_Suel))



    """Estructuras selectivas compuestas"""       
    def Ejercicio6(self):                        
        horas_T= int(input("Ingrese las horas que trabajó: "))
        pago_H= float(input("Ingrese el pago de la hora normal: "))
        if horas_T > 40:
            horas_E= horas_T-40
            if horas_E > 8:
                horas_E_T= horas_E-8
                pago_H_E= (pago_H*2*8) + (pago_H*3*horas_E_T)
            else:
                pago_H_E= pago_H*2*horas_E
            paga_total= pago_H*40+pago_H_E
        else:
            paga_total= pago_H*horas_T
        print("El pago total por las horas trabajadas es {}" .format(paga_total))
    


    def Ejercicio7(self):                           
        nu1= int(input("Ingrese el primer número: "))
        nu2= int(input("Ingrese el segundo número: "))
        nu3= int(input("Ingrese el tercer número: "))
        if nu1> nu2 and nu1> nu3:
            print("El número mayor es {}" .format(nu1))
        elif nu2> nu1 and nu2> nu3:
            print("El número mayor es {}" .format(nu2))
        else:
            print("El número mayor es {}" .format(nu3))
    


    """Estructuras selectivas múltiples"""
    def Ejercicio8(self):                           
        num = int(input("Ingrese un número: "))
        valor = int(input("Ingrese un valor: "))
        if num == 1:
            Resultado = 100*valor
        elif num == 2:
            Resultado = 100**valor
        elif num == 3:
            Resultado = 100/valor
        else:
            Resultado = 0
        print("El resultado del número {} y el valor {} es de: {} ".format(num ,valor, Resultado ))
    

    
    """Expresiones lógicas"""  
    def Ejercicio9(self):                                
        Cal1= int(input("Ingrese la primera calificación: "))
        Cal2= int(input("Ingrese la segunda calificación: "))
        if Cal1 >=80 and Cal2>=80:
            print("La calificacion 1: {},la calificación 2:{} es ACEPTADO" .format(Cal1,Cal2))
        else:
            print("La calificacion 1: {},la calificación 2:{} es RECHAZADO" .format(Cal1,Cal2))
    


    def Ejercicio10(self):
        Cal1= int(input("Ingrese la primera calificación: "))
        Cal2= int(input("Ingrese la segunda calificación: "))
        if Cal1 >=90 or Cal2>=90:
            print("La calificacion 1: {},la calificación 2:{} es ACEPTADO" .format(Cal1,Cal2))
        else:
            print("La calificacion 1: {},la calificación 2:{} es RECHAZADO" .format(Cal1,Cal2))
    

       
clas1= Ejercicios()
clas1.Ejercicio3()
clas1.Ejercicio4()
clas1.Ejercicio5()
clas1.Ejercicio6()
clas1.Ejercicio7()
clas1.Ejercicio8()
clas1.Ejercicio9()
clas1.Ejercicio10()