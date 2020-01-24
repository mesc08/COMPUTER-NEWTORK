import matplotlib.pyplot as plt
import math
print("For Uniform Distribution")
print("Enter the value of a")
a = int(input())
print("Enter the value of b")
b = int(input())
fx = 1/(b-a)
x = []
y = []
for i in range(a,b+1):
	x.append(i)
	y.append(fx)
plt.plot(x,y)
plt.title("Uniform Distribution")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()

print("Print Normal Distribution")
mean = 0
print("Mean is ", mean)
variance = 1
print("Variance is",variance)
standard_deviation = 1
const1 = 1/math.sqrt(2*3.142857)
const2 = 0.5
x1 = [-3,-2,-1,0,1,2,3]
y1 = []
for i in range(0,len(x1)):
	z = x1[i]*x1[i]
	a = z*-1*const2
	y1.append(const1*math.exp(a))
plt.plot(x1,y1)
plt.title("Normal Distribution")
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.show()

print("Print Normal Distribution using Uniform Distribution")
print("Enter the values of a")
a = list(map(int,input().split()))
print("Enter the value of b")
b = list(map(int,input().split()))
z = []
h = []
o = []
for i in range(0,len(b)):
	k = []
	for j in range(a[i],b[i]+1):
		k.append(j)
	o.append(k)
for i in range(0,len(b)):
	z = []
	for j in range(a[i],b[i]+1):
		z.append(1/(b[i]-a[i]))
	h.append(z)
for i in range(0,len(b)):
	plt.plot(o[i],h[i])
plt.title("Using uniform distribution plot normal distribution")
plt.xlabel("x - axis")
plt.ylabel("y -axis")
plt.show()
