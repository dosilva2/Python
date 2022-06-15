#from functools import total_ordering
import random
import var
def jogar_adivinhacao():
    print("*********************************")
    print("Bem vindo no jogo de Adivinhação!")
    print("*********************************")
    
def sel_dif():
    print("\n\nSelecione o grau de dificuldade sendo:\n1 - Fácil\n2 - Médio\n3 - Difícil")
    op = input("\nSelecione uma opção: ")
    ver = op.isnumeric()
    if ver == False:
        print("Digite a opção 1, 2 ou 3: ") 
    elif op == 1:
        var.total_tentativas = 20
    elif op == 2:
        var.total_tentativas = 10
    elif op == 3:
        var.total_tentativas = 5
    else:
        print("Selecione uma opção válida 1: ")
        sel_dif()        

    rodada = 1

    for rodada in range(1, var.total_tentativas + 1):
        #for i in range(0, total_tentativas):
        print("Tentativa {} de {} ".format (rodada , var.total_tentativas))
        var.chute = int(input("Digite um numero entre um e 100: "))

        if(var.chute < 1 or var.chute > 100):
            print("Você deve digitar um número150 entre 1 e 100!")
            continue


        print("Você digitou ", var.chute)

        if var.acertou:
            print("Você acertou.")
            break
        else:
            if(var.maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(var.menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
        #rodada = rodada +1

    print("Fim do jogo.\n", var.numero_secreto)

if __name__ == '__main__':
    jogar_adivinhacao()
    sel_dif()