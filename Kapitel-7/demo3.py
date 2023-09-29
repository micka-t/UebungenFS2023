import numpy as np

a = np.array([1,2,3,4], dtype=np.float64)
b = np.array([[1,2,3],[4,5,6],[7,8,9]])

if 50 in b:
    print("5 kommt in der Matrix b vor!")
else:
    print("Schade!")

print(b[:,1])

c= np.zeros([4,4])
c[0,1] = 5
print(c)

d = np.arange(-2*np.pi,2*np.pi+0.1,0.1)
print(d)

e = np.linspace(0,1,1000)
print(e)

f = np.random.random(20) #Wichtig für Übung 7 Aufgabe 1
print(f)

