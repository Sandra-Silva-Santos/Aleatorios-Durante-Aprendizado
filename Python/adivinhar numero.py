import random
sorteio  =  random.randint(1,11)
tentativa=1
while tentativa < 5:
    num=int(input("Digite um numero: "))
    tentativa+=1
    if num == sorteio:
        print("Parabens, voce acertou!")
        break
    elif num < sorteio:
        print("Voce errou, o numero sorteado e menor que o digitado")
    else:
        print("Voce errou, o numero sorteado e maior que o digitado")
    print("Tentativa: ",tentativa - 1)  
print("Fim do jogo")