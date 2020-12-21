import matplotlib.pyplot as plt

days=[1,2,3,4,5]

sleeping=[7,8,6,11,7]
eating=[2,3,4,3,2]
working=[7,8,7,2,2]
plying=[8,5,7,8,13]

plt.plot([],[],color='m',label="Sleeping",linewidth=5)
plt.plot([],[],color='c',label="Eating",linewidth=5)
plt.plot([],[],color='r',label="Working",linewidth=5)
plt.plot([],[],color='k',label="Playing",linewidth=5)
plt.legend()

plt.stackplot(days,sleeping,eating,working,plying,colors=['m','c','r','k'])

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("STack Plot")
plt.show()