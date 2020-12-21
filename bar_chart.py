from matplotlib import pyplot as plt

plt.bar([1,3,5,7,9],[5,2,7,8,2],label="First bar")
plt.bar([2,4,6,8,10],[8,6,2,5,6],label="Second bar",color="g")
plt.legend()

plt.title("Bar Graph")
plt.xlabel("bar number")
plt.ylabel("bar height")

plt.show()