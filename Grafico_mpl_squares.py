import matplotlib.pyplot as plt

#input_values =[1,2,3,4,5]
#squares =[1,4,9,16,25]
#plt.plot(input_values, squares,linewidth=5)
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.title("Números Quadrados", fontsize=24)
plt.xlabel("Valor",fontsize = 14)
plt.ylabel("Quadrado do Valor", fontsize = 14)
plt.tick_params(axis='both',labelsize=14)
#plt.scatter(2,4, s=200)
#plt.scatter(input_values, squares, s=200)
plt.axis([0, 1100, 0, 1100000])
#plt.scatter(x_values, y_values,c='red', edgecolors='none', s=40)
#plt.scatter(x_values, y_values,c=(0,1,0.8), edgecolors='none', s=40)
plt.scatter(x_values, y_values,c=y_values, cmap = plt.cm.Blues, edgecolors='none', s=40)

#plt.axis([0, 1100, 0, 1100000])
plt.show()
plt.savefig('grafico.png', bbox_inches='tight')