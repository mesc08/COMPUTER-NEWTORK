"""
Name : Srijan Chakraborty
Roll Number: 39/Cse/17086/284
Reg No: 284
"""
import matplotlib.pyplot as plt
def cyclic_shift_autocorelation(s,ans,a):
        p = ""
        k = ""
        for i in range(0,ans-a-1):
                p+=s[i]
        for j in range(ans-a-1,ans-1):
                k+=s[j]
        k = k + p
        print(k)
        ans1 = 0
        for i in range(0,ans-1):
	        if(int(s[i]) ^ int(k[i])==0):
	                ans1+=1
        make = (ans1)/(ans-1)
        return make
def cyclic_shift_autocorelation1(s,ans,a):
        p = ""
        k = ""
        for i in range(0,ans-a-1):
                p+=s[i]
        for j in range(ans-a-1,ans-1):
                k+=s[j]
        k = k + p
        ans1 = 0
        for i in range(0,ans-1):
	        if(int(s[i]) ^ int(k[i])==0):
	                ans1+=1
        make = (ans1)/(ans-1)
        return make
print("                              ","Welcome and Lets Begin with lfsr")
print("-------------------------------------------------------------------------------------------------------------------")
print("Enter the the value of r ")
r = int(input())
length = ((2**r) - 1)
print("Enter the value of shift")
a = int(input())
print("Enter the value of initial seed")
l  = list(map(int,input().split()))
f = l[:]
z = []
z.append(l)
d = {}
d[0] = l
for j in range(1,length):
	k = l[0]^l[r-1]
	b = []
	b.append(k)
	for i in range(1, r):
		b.append(l[i-1])
	l = b[:]
	z.append(l)
	d[j] = l
	b.clear()
z.append(f)
for i in range(0,length):
        print(z[i])
ans = 0
for i in range(1,length+1):
	if f == z[i]:
		ans = i + 1
		break
print("The period is ", ans)
print("Enter the sequence you want to find")
find = list(map(int,input().split()))
if find in z:
	print("YES "+ str(find) +"is present")
else:
	print("NO " + str(find) +" is not present") 
no_of_ones = 0
no_of_zeroes = 0
for i in range(0,ans):
	 for j in range(0,r):
	 	if(z[i][j] == 1):
	 		no_of_ones+=1
	 	else:
	 		no_of_zeroes+=1
print("The no. of ones ",no_of_ones)
print("The no. of zeroes ",no_of_zeroes)
s = ""
for i in range(0,ans-1):
	s+=str(z[i][r-1])
print(s)
mo = cyclic_shift_autocorelation(s,ans,a)
print("Autocorrelation is ", mo)
o = []
print("Enter the number of periods")
period = int(input())
for j in range(0,period):
        for i in range(0,ans-1):
                o.append(cyclic_shift_autocorelation1(s,ans,i))
plt.plot(o)
plt.xlabel("x axis")
plt.ylabel("auto corelation")
plt.show()
