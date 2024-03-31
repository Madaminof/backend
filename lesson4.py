# while for loops
import math
'''
from random import randint
random_num=randint(1,100)
counter=0
for i in range(10):
    new_nam=int(input(f"{i+1} - raund: "))
    counter+=1
    if new_nam>random_num:
        print("siz kiritgan son katta")
    elif new_nam<random_num:
        print("siz kiritgan son kichik")

    else:
        if new_nam==random_num:
            print(counter," ta imkonda ")
        print("yutdingiz")
        exit()
        
# while 1
a=int(input("a = "))
b=int(input("b = "))

while a>b:
    a-=b
print(a)

#while 2
a=int(input("a = "))
b=int(input("b = "))
counter=0
while a>=b:
    a-=b
    counter+=1
print(counter)

# while 3
n=int(input("n = "))
k=int(input("k = "))
counter=0
while n>=k:
    n-=k
    counter+=1
print("butun = ",counter)
print("qoldiq = ",n)

# while 4
n=int(input("n = "))
i=1
while i<n:
    
    i*=3
if i==n:
    
    print("3-ning darajasi")
else:
    print("3-ning darajasi emas")

# while 5
n=int(input("n = "))
print(math.log2(n))

#while 6
n=int(input("n = "))
i=1
while n>0:
    i*=n
    n-=2
print(i)

# while 7
n=int(input("n = "))
k=1
while k*k<=n:
    k+=1
print(k)    
    
# while 8
n=int(input("n = "))
k=1
while k*k>n:
    k+=1
print(k)

# while 9
n=int(input("n = "))
k=1
while math.pow(3,k)>=n:
    k+=1
print(k)

# while 10
n=int(input("n = "))
k=1
while math.pow(3,k)<=n:
    k+=1
print(k)


#while 11
n=int(input("n = "))
k=1
sum1=0
while sum1<n:
    sum1+=k
    k+=1
    
print(k-1,"",sum1)

# while 12
n=int(input("n = "))
k=0
sum1=0
while sum1<=n:
    sum1+=k
    k+=1
    
print(k-1,"",sum1)

# while 13
n=float(input("n = "))
k=0.0
sum1=.0
while sum1<n:
    sum1+=1/k
    k+=1
print(k-1,"",sum1)

# while 14
n=float(input("n = "))
k=0.0
sum1=0.0
while sum1<=n:
    k+=1
    sum1+=1/k
    
    
print(k-1,"",sum1-1/k)
'''
truePasword=1235
i=0
while i<3:
    i+=1
    password=int(input("parol kirit = "))
    if truePasword==password:
        print("topdinggiz")
        exit()
else:
    
    
    print("xato")
    
