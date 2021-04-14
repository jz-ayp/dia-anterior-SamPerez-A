"""
Tarea extra: Día anterior
Author: Samuel Alejandro Pérez
Fecha de entrega: 08/04/21
Grupo: ESI-232A4
Profesor: Jorge Zaldivar
Este programa calcula día anterior de una fecha determinada por el usuario.
"""
#entradas
dia=int(input("Día:"))
mes=int(input("Mes:"))
anio=int(input("Año:"))
bisiesto = False
## Las lineas de codigo para el año bisiesto están bien solo que me faltó saber acomodar para que
la salida
#del mes de febrero ejecutara como si tuviera 28 o 29 días.
#Proceso
if anio % 400 == 0:
 bisiesto = True
elif anio % 4 == 0:
 bisiesto = True
if mes in (1, 3, 5, 7, 8, 10, 12):
 dias_mes = 30
elif mes == 2:
 if bisiesto:
 dias_mes =29
 else:
 dias_mes =28
else :
 dias_mes = 31
if dia > 1:
 dia -= 1
else:
 dia = dias_mes
 if mes == 1:
 mes = 12
 anio -= 1
 dia = 31
 else:
 mes -= 1
#salidas
print ("Día: ", dia)
print ("Mes: ", mes)
print ("Año: ", anio)
