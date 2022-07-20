
frase = ' '
simbolos = ['¿', '?', '.', ',', ';', ':', '¡', '!']
numfrase = 0
numpalabras = 0
cant_frases = 0
total_frases = open('phrases.txt')
for lineas in total_frases:
    cant_frases += 1

while frase != 'salir' and frase != 'x':

    frase = input('(Para salir ingrese: salir o x) Ingrese una Frase: ')
    if frase != 'salir' and frase != 'x':
        texto = open('phrases.txt', 'a')
        # agrega la frase nueva e ingresa una linea vacia
        texto.write(frase + '\n')
        texto.close()

        numfrase = frase.split()
        numfrase = len(numfrase)

        print('---Tu frase contiene %s palabras' % numfrase)

        if cant_frases >= 0:  # si hay frases ingresdas las cuenta
            cant_frases = 0
            total_frases = open('phrases.txt')
            for lineas in total_frases:
                cant_frases += 1
            print('---En el archivo hay', cant_frases, 'frases')

        with open('phrases.txt') as fichero:
            for linea in fichero:
                for simbolo in simbolos:
                    # remplaza los simbolos por espacios
                    linea = linea.replace(simbolo, ' ')
                palabras = linea.split()  # hace una lista de palabras

                for palabra in palabras:
                    numpalabras += 1
        print('---El archivo contiene %s palabras' % numpalabras)
        numpalabras = 0

        total_frases = open('phrases.txt')
        for i in total_frases:
            print('-', i)  # imprime todas las frases
    else:
        print('----Finalizado! ----')
