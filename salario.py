nombre = input(" su nombre:")
sueldo = float(input("su sueldo: "))
afp = int(input("ingrese el descuento de afp"))
prevision = input("¿a que pertenece fonasa o isapre")
previsionPorc = int(input(f"cuanto le descuentan {prevision}"))
seguro = int(input("ingrese la cesantia "))
print(nombre,sueldo,afp,prevision,previsionPorc,seguro)
operacion = afp*sueldo//100
operacion_2 = previsionPorc*sueldo//100
operacion_3 = seguro*sueldo//100
descuentos = (operacion+operacion_2+operacion_3)
smp = (sueldo-descuentos)

print("menu de opciones")
print(f"1:calular su sueldo imponible")
print(f"2:calculr su descuento")
print(f"3:salir")
opc = int(input("ingrese una opcion"))

while opc !=3:
    if opc ==1:
        print(smp)
        print("menu de opciones")
        print(f"1:calular su descuento")
        print(f"2:calcular su sueldo imponible")
        print(f"3:salir")
        opc = int(input("ingrese una opcion"))
    elif opc ==2:
        print(f"su descuendo de AFP es:{operacion} descuendo de org:{operacion_2} seguro: {operacion_3} ")
        print("menu de opciones")
        print(f"1:calular su descuento")
        print(f"2:calcular su sueldo imponible")
        print(f"3:salir")
        opc = int(input("ingrese una opcion"))
else: opc ==3
print("usted ha salido, hasta luego")
