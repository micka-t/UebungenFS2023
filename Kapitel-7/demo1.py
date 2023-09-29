import matplotlib.pyplot as plt

x = []
y = []
for i in range(0,101):
    value = i/10-5
    x.append(value)
    y.append(value**2)

plt.plot(x,y)
plt.show()