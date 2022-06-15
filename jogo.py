import adivinhacao
import forca

print("**********************************")
print("*******Bem vindo aos Jogos!*******")
print("**********************************")

def selecionar_jogo():
    print("\nQual Jogo você quer Jogar? ")
    sel = int(input("\n1 - Jogo Adivinhação\n2 - Jogo da Forca\n\nSelecione uma opção acima: "))
    if sel == 1:
        adivinhacao.jogar_adivinhacao()
    else:
        forca.jogar_forca()
    print('teste' , sel)

if __name__ == '__main__':
    selecionar_jogo()