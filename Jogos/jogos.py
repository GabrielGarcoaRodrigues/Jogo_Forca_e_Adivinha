import forca
import adivinhacao

def escolher_jogo():
    print("*********************************")
    print("********Escolha seu jogo!********")
    print("*********************************")

    print("(1) Advinhação ou (2) Forca")
    jogo = int(input("Escolha seu jogo: "))

    if(jogo == 1):
        print("Jogando Advinhação")
        adivinhacao.jogar()
    elif(jogo == 2):
        print("Jogando Forca")
        forca.jogar()

if(__name__ == "__main__"):
    escolher_jogo()
