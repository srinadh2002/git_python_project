import math
n=int(input())
k=math.sqrt(n)

if(int(k+0.5)**2==n):
    print("yes,it is perfect square")
else:
    print("not perfect square")
