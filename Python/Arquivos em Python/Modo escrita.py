
idade= int(input("Digite sua idade: "))
outfile = open('Texto para exemplo_escrita.txt', 'w')
outfile.write('Texto para exemplo_escrita.txt')
outfile.write(' Sua idade e {} anos. \n'.format(idade))
outfile.close()


# Para abrir um arquivo em modo escrita é usado o método open() como segue: outfile = open(filename, 'w')