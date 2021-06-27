class Ejercicios:
    def __init__(self):
        pass
    def Ejercicio1(self):
        t_compras = float(input("Ingrese total compra: "))
        des= t_compras * 0.15
        t_pagar = t_compras - des
        print("total compra:{}".format(t_pagar))
    
    def Ejercicio2(self):            
        SueldoBase= float(input("Ingrese su sueldo base: "))
        vent1= float(input("Ingrese el valor de su primera venta: "))
        vent2= float(input("Ingrese el valor de su segunda venta: "))
        vent3= float(input("Ingrese el valor de su tercera venta: "))
        Total_venta= vent1+vent2+vent3
        Comision= Total_venta*0.1
        Total= SueldoBase+Comision
        print("Su sueldo base es {}, mas las ventas realizadas {}, usted recibirá un total {}" .format(SueldoBase,Total_venta,Total))

obj1=Ejercicios()
obj1.Ejercicio1()
obj1.Ejercicio2()