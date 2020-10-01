# Freela Sortear numeros
from random import randint
from time import sleep

numeros = list()
continuar = "s"

while True:

    try:
        if continuar.lower() == 'n':
            break
        else:
            if continuar.lower() != 's':
                print("Erro: Digite 's' para continuar ou 'n' para sair" )
                continuar = input("\nDeseja sortear os números? S/N ")
                valor = int(input("\nDigite o numero desejado: "))
            else:
                valor = int(input("\nDigite o numero desejado: "))

        def sorteia(lista):
            print("Sorteando os valores da lista: ", end='')

            while len(lista) != 15:
                r = randint(1,25)
                if r not in lista:
                    lista.append(r)
                # print(lista)
                print(f'{r}', end=' ', flush=True)
                sleep(0.3)
            print("PRONTO!")

        def soma15(lista):
            soma = 0
            for valor in lista:
                soma += valor
            print(f"Somando os 15 valores sorteados sem repetição de {numeros}, temos o valor total de {soma}")

            if soma == valor:
                print("\nA soma dos números deu igual ao valor digitado!!!!")
            else:
                print("\nA soma dos números deu diferente do valor digitado!!!!")

            lista.clear()

        sorteia(numeros)
        soma15(numeros)

        continuar = input("\nDeseja sortear os números? S/N ")
    except:
        print("Erro: Você digitou letras, digite apenas números")
print('\nObrigada por utilizar nosso aplicativo!!! Até breve!!!')


