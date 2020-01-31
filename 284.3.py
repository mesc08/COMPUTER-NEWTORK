# P(x, U) = e ^- U * U^x / X!

import matplotlib.pyplot as plt
import math
import random
def factorial(x):
        if x==1:
                return 1
        else:
                return x * factorial(x-1)
print("Enter the no. of values of K is :")
k = int(input())

x = []
for i in range(1,k+1):
        x.append(i)

print("Enter the value of lambda : ")
U = int(input())

y = []

for i in x:
        res = ((math.exp(-1*U))*(U**i))/factorial(i)
        y.append(res)

plt.plot(x,y,'-ro')
plt.xlabel("The values of x")
plt.ylabel("Values of poisson distribution function")
plt.title("Poisson Distribution")
plt.show()
