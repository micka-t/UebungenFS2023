import numpy as np

def summe(a,b):
    return a+b
e =np.e
s = "(1,2,summe(1,5),np.pi,np.e)"

r = eval(s)


print(type(r))
print(r)