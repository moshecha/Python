def verpalindromos (palabra):
    if palabra == palabra[::-1] and palabra != 'x':
        print('Es palindromo!')
    elif palabra == 'x':
        return print('----Ha Finalizado')
    else:
        print('No es palindromo')
        

palindromos = list()
noPalindromos = list()
palabra=''
print('VALIDANDO PALINDROMOS!')
while palabra != 'x':
    palabra = input('(---Para salir ingrese: x )Ingresa una palabra: ')  
    verpalindromos(palabra)

    if palabra == palabra[::-1] and palabra != 'x':
        palindromos.append(palabra)
    elif palabra == 'x':
        print('-- Palindromos:', palindromos, 'Total:', len(palindromos))
        print('-- No palindromos:', noPalindromos, 'Total:', len(noPalindromos))
        print(f'Total de palabras ingresadas: {len(palindromos)+len(noPalindromos)}')
    else:
        noPalindromos.append(palabra)
        
#no he podido almacenar en una lista desde la funcion