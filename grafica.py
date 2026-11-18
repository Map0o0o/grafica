import matplotlib.pyplot as plt 
x = [1,2,3,4,5,6]
y = [10,15,13,18,22,25]


plt.plot(x, y, marker="o",color="purple")
plt.title("Grafica lineal")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(True)
plt.show()
