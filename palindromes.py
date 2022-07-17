
palindromos = []
noPalindromes = []

print('---Para salir ingrese: x')
palabra = input('Ingresa una palabra: ')
while palabra != 'x':
    if palabra == palabra[::-1] and palabra != 'x':
        print('Es palindromo!')
        palindromos.append(palabra)
        palabra = input('Ingresa una palabra: ')
        
    
    elif palabra == 'x':
        print('Fin')
    else:
        print('No es palindromo')
        noPalindromes.append(palabra)
        palabra = input('Ingresa una palabra: ')
        
print('-- Palindromos:', palindromos,'Total:', len(palindromos))
print('-- No palindromos:',noPalindromes,'Total:', len(noPalindromes))
print(f'Total de palabras ingresadas: {len(palindromos)+len(noPalindromes)}')