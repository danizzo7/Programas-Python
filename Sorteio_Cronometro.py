import time
import random



print("Responda umo mais rapido possivel")
jogar ="s"

while jogar.lower()=="s":
    inicial=time.time()
    sortear=random.randint(1,9)
    resposta=int(input("Quanto é 2 * " + str(sortear) + " ? "))

    final = time.time()
    tempo = round(final-inicial,0)
    if resposta == sortear * 2:
        print("Parabens, resposta correta!!  " , end="")
        if tempo < 4:
            print("Seu tempo foi de: " + str(tempo)+ " segundos!!! Execelente!")
        if tempo >= 4:
            print("Seu tempo foi de: " + str(tempo)+ " segundos....  Precisa Melhorar!!!")

        jogar = input("Deseja jogar novamente?  s/n ")
        if jogar.lower() == "n":
            break

    else:
        print("Ahh resposta errada!!!! Sorte na proxima vez")
        jogar=input("Deseja jogar novamente?  s/n ")
        if jogar.lower() == "n":
            break
print("Ate a proxima!!!")

