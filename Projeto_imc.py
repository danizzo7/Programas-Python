from Calculo_IMC import *

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = calculo_imc(peso,altura)
print(imc)

if imc < 18.5:
    print("Voce esta abaixo do peso")
elif imc >= 18.5 and imc <25:
    print("VOce esta com o peso normal")
elif imc >= 25 and imc < 30:
    print("VOce esta com sobrepeso")
elif imc >= 30 and imc <35:
    print("VOce esta com Obesidade grau I")
elif imc >= 35 and imc <40:
    print("VOce esta com Obesidade grau II")
else:
    print("VOce eom Obesidade grau III ou Morbida")

