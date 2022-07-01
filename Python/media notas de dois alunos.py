reprovado = 0
exame = 0
aprovado = 0


for cont in range(1, 3):
    print('Entre com as notas do aluno nro: ', cont)
    nota1 = eval(input('Digite a primeira nota: '))
    nota2 = eval(input('Digite a segunda nota: '))
    media = (nota1 + nota2)/2
    print('Media do aluno %.1f' % media)
    if media < 5:
        print('Reprovado ;(')
        reprovado += 1

    elif media < 7:
        print('Exame :|')
        exame = exame+1
    else:
        print('Aprovado ;)')
        aprovado = aprovado+1
print('Total de exame: ', exame)