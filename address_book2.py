import csv
from datetime import date
import uuid
ID = uuid.uuid1(51)
# print(f"Id:{ID}")


today = date.today()  # Para la fecha

nombre = input('Nombre: ')
apellido = input('Apellido: ')
direccion = input('Direccion: ')
numero = input('Telefono: ')
fecha = (f'{format(today.day)}/{format(today.month)}/{(today.year)}')


with open('names.csv', 'a+', newline='\n') as csvfile:
    fieldnames = ['Nombre', 'Apellido', 'Direccion',
                  'Telefono', 'Fecha Inscripcion', 'ID']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Nombre': nombre, 'Apellido': apellido,
                    'Direccion': direccion, 'Telefono': numero, 'Fecha Inscripcion': fecha, 'ID': ID})
    #writer.writerow({'Nombre': '', 'Apellido': '','Direccion': '','Telefono':'', 'Fecha':'', 'ID':'' })

print('Contacto','\n','Nombre y Apellido:', nombre, apellido, '\n','Direccion:',direccion,'Tel:', numero,'\n', fecha,'\n', ID)
# with open("names.csv", "a+", newline ='\n') as csvfile:
# wr = csv.writer(csvfile, dialect='excel', delimiter=',', lineterminator='')
# wr.writerow(newContacto)



#Leer el archivo
import csv
imprimir = input('Imprimo todos los contactos? (si/no) ')
if imprimir == 'si':
    with open('names.csv') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            print(row)
        
