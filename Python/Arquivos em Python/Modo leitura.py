def readFile(filename):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    wordList = content.split()
    print(wordList)
    return len(wordList), len(content)
n_words, n_chars = readFile('Texto para exemplo_leitura.txt')
print('Número de palavras:', n_words)
print('Número de caracteres:', n_chars)


# Para abrir um arquivo em modo leitura é usado o método open() como segue: infile = open(filename, 'r') 
