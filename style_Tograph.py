from matplotlib import pyplot as plt
from matplotlib import style

style.use("ggplot")

x=[5,8,10]
y=[12,6,16]

x2=[6,9,11]
y2=[6,15,17]

plt.plot(x,y,"g",label="First Line",linewidth=5)
plt.plot(x2,y2,"c",label="Second Line",linewidth=5)

plt.title("Info")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.legend()
plt.grid(True,color="k")
plt.show()