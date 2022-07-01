frase = 'Algoritimos e programaçãO de Computadores I'
contletra = 0
for c in frase:
    if c in 'oO':
        print('Vogal; ', c)
        contletra += 1
print('Total de letras o ou O: ', contletra)      