from functools import total_ordering


print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_tentativas = 3
rodada = 1

for rodada in range(1, total_tentativas + 1):
    #for i in range(0, total_tentativas):
    print("Tentativa {} de {} ".format (rodada , total_tentativas))
    chute = int(input("Digite um numero entre um e 100: "))

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número150 entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    print("Você digitou ", chute)

    if acertou:
        print("Você acertou.")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")
    #rodada = rodada +1

print("Fim do jogo.")