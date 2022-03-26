'''
Proyecto 53: El Estreno de la Película de Harry Potter
Ya está a la venta los tickets del estreno de la película “Harry Potter y el Príncipe Mestizo" en la Sala Premium de Cines Montaña. Para esto, en una lista, se
anota:
el número del ticket, el número de fila (1 a 11) y la letra de la columna del asiento (De 
la A hasta la L).
Se conoce que los asientos de las filas 1-5 cuestan Bs. 20; los asientos de las filas 6-8
cuestan Bs. 30 y los asientos de las filas 9-11 cuestan Bs 17. Desarrolle un programa que
lea la información de la lista y determine:
1. Número del ticket y fila de la primera persona que compró el primer ticket en un asiento de la 
columna F y cuantos después de él se sentaron en la misma fila.
2. El Total de Bs recaudado por venta de tickets.
'''
#Propósito: Ejercicio de listas y archivos
#Autora: Esthefanía Medina
#Materia: Computación I
#Sección: 02
#Fecha: 22/03/2022
#Programa: Estreno de Harry Potter y el Príncipe Mestizo

#Apertura del Archivo
from io import open
arch = open('harrypotter6.txt', 'r')

#Inicio de Herramientas
registro = 0
cF = 0
band = 0
c15 = 0
c68 = 0
c911 = 0
dinero1 = 0
dinero2 = 0
dinero3 = 0
dineroT = 0
ticket1 = 0
fila1 = 0

#Recorrido y Proceso
for contenido in arch:
    lista = contenido.split(',')
    ticket = int(lista[0])
    fila = int(lista[1])
    columna = str(lista[2].strip('\n'))
    
        #Contador de F
    if columna == 'F':
        cF += 1
        if band == 0:
            ticket1 = ticket
            fila1 = fila
            band = 1
            print('Primer Ticket en la columna F:', '\nTicket N°: ', ticket1, '\nFila: ', fila1)
    
    #Contador de Dinero 
    if 1 <= fila <= 5:
        c15 += 1
        dinero1 = c15 * 20
    
    if 6 <= fila <= 8:
        c68 += 1
        dinero2 = c68 * 30
        
    if 9 <= fila <= 11:
        c911 += 1
        dinero3 = c911 * 17

print('Total de Tickets en F: ', cF)               
dineroT = dinero1 + dinero2 + dinero3
print('Total recaudado por la venta de tickets: ', dineroT)


#Cierre del Archivo    
arch.close()