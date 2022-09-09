import random
def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    #chute = input("Digite um numero: ") aqui vai receber uma str, entao tem q transformar ela em int, pode usar a funçao -> numero = int(chute) ou...
    rodada = 1
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Digite o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5
    print("\nVocê começa com 1000 pontos\n")
    #for rodada in range(1, total_de_tentativas + 1): fazendo o mesmo laço com o for
    while(total_de_tentativas >= rodada):
        print("Tentativa {} de {}".format(rodada,total_de_tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))

        if(chute < 1 or chute > 100):
            print("você deve digitar um número entre 1 e 100")
            continue

        acertou = chute == numero_secreto

        if(acertou):
            print(f"Parabens, você acertou! e fez {pontos} pontos !")
            break
        else:
            if(chute > numero_secreto):
                print("Você errou!!! O seu chute foi maior que o numero secreto.")
                if(total_de_tentativas == rodada):
                    print(f"Você não acertou, o número secreto era {numero_secreto} e você fez {pontos} pontos")
            elif(chute < numero_secreto):
                print("Você errou!!! O seu chute foi menor que o numero secreto.")
                if (total_de_tentativas == rodada):
                    print(f"Você não acertou, o número secreto era {numero_secreto} e você fez {pontos} pontos")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        rodada = rodada + 1

    print("\nFim do jogo")

if(__name__ == "__main__"):#chamando a função jogar
    jogar()

