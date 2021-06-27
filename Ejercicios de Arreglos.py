class Ejercicios:    
    def __init__(self):
        pass

    def Ejercicio18(self):             
        calf = []
        for i in range(10):
            N_dato = int( input( "Dime el dato num {}: ".format(i)))
            calf.append(N_dato)
        print("Las calf son: {}".format(calf))
    
    
    def Ejercicio19(self):          
        nuevo = []
        B=[]
        A= []
        print(nuevo)
        for j in range(0,20):
            num = int(input("Ingrese un número: "))
            nuevo.append(num)
        for j in nuevo:
            if j >= 0:
                B.append(j)
            else:
                A.append(j)
        print("Los números positivos son: {}".format(B))
        print("Los números negativos son: {}".format(A))
    
    
    def Ejercicio20(self):         
        N_lista = []
        L_alumnos = []
        ALUMNOS = 30
        C_NOTAS = 6
        P_examenes = []
        for alumno in range(1, 31):
            alum_temporal = input('Nombre del alumno {}: '.format(alumno))
            L_alumnos.append(alum_temporal)
            for N in range(1, 7):
                print('Escriba la calificación del alumno "{}" en el exámen "{}"'.format(alum_temporal, N))
                """Lectura de las 6 calf de los 30 alumnos."""
                notas_temporal = round(float(input('Nota #{}: '.format(N))), 2)
                if N == 1:
                    N_lista.append([notas_temporal])
                else:
                    N_lista[alumno-1].append(notas_temporal)
            print('')
        for Nun_examen in range(6):
            suma_notas = 0
            for N in N_lista:
                suma_notas += N[Nun_examen]
            prom = round((suma_notas/ALUMNOS), 2)
            print('Promedio de exámen {}: {}'.format(Nun_examen+1, prom))
        print('')
        for num, alumno in enumerate(L_alumnos):
            suma_notas = sum(N_lista[num])
            prom = round((suma_notas/C_NOTAS), 2)
            print('{} su prom es: {}'.format(alumno, prom))
        prom_mayor = 0
        for Nun_examen in range(6):
            suma_notas = 0
            for N in N_lista:
                suma_notas += N[Nun_examen]
            prom = round((suma_notas/ALUMNOS), 2)
            if prom_mayor < prom:
                prom_mayor = prom
            P_examenes.append(prom)
        print('')
        print('El exámen', P_examenes.index(prom_mayor)+1,'obtuvo el mayor prom:', prom_mayor)


class1= Ejercicios()
class1.Ejercicio18()
class1.Ejercicio19()
class1.Ejercicio20()