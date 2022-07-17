import csv
import random
from datetime import datetime
from datetime import date


Id = []
idnumeros = list('1234567890')
for i in range(5):
    Id.append(random.choice(idnumeros)) #Elige nnumeros para el id
random.shuffle(Id) 
Id = ("".join(Id))  #ordena en un str

today = date.today() #Para la fecha
    
nombre = input('Nombre: ')
direccion = input('Direccion: ')
numero = input('Telefono: ')
fecha =(f'{format(today.day)}/{format(today.month)}/{(today.year)}') 





newContacto = [ Id,nombre,direccion,numero,fecha,'\n']
print('Contacto: ',','.join(newContacto))
with open("tpFinal/Ej5/addresses.csv", "a+", newline ='\n') as csvfile:
    wr = csv.writer(csvfile, dialect='excel', delimiter=',', lineterminator='')
    wr.writerow(newContacto)
