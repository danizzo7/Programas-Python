from random import randint
import pygal

class Die():
    """ Uma classe que representa um único dado"""
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """"Devolve um valor aleatório entre 1 e o número de lados."""
        return  randint (1,self.num_sides)

#Cria um D6
die = Die()
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)
print(results)

frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

hist = pygal.Bar()
hist.title = "Frequencia de Dados"
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title  = "Resultado"
hist.y_title = "Frequencia do Resultado"
hist.add('D6',frequencies)
hist.render_to_file('Grafico_FrequenciaDados.svg')


