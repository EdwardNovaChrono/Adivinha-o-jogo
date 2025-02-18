import random

print("*******************************")
print("Bem-vindo ao jogo de advinhação")
print("*******************************")

numero_secreto = random.randrange(1,1000)
total_de_tentativas = 0
pontos = 1000
pontos_perdidos = 0
rodada = 0

print("Qual nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")
nivel = int(input("Defina o nível: "))

if(nivel == 1):
    total_de_tentativas = 30
    pontos_perdidos = 25
elif(nivel == 2):
    total_de_tentativas = 20
    pontos_perdidos = 50
else:
    total_de_tentativas = 10
    pontos_perdidos = 100

for rodada in range(total_de_tentativas):
    print("\nTentativa", rodada, "de", total_de_tentativas)

    chute = int(print("Digite um número entre 1 e 1000: "))
    print("\nVocê digitou ", chute)

    acertou = bool(chute == numero_secreto)
    maior = bool(chute > numero_secreto)
    menor = bool(chute < numero_secreto)

    if(acertou == True):
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    else:
        pontos = pontos - pontos_perdidos

        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
            print("Maximo {}".format (chute))
            rodada = rodada + 1
        if(menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")
            print("Mínimo {}".format (chute))
            rodada = rodada + 1   
        
if(rodada == total_de_tentativas):
    print("O número secreto era {}" .format(numero_secreto))

print("Fim de jogo!")
input()