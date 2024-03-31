# lesson 5
# funksiyalar
import math
'''
def max1(a,b):
    print(max(a,b))

#max1(4,7)    

def my(name,age,city):
    print(f'ismim {name}\nyoshim {age}\nyashash manzil: {city}')

#my("samandar",19,"Tashkent")


def AVTOsalon(name,make,color,year=2023,probeg=0):
    print(f' {name}\n {make}\n {color}\n {year}\n {probeg}')

AVTOsalon("gentra","GM","black")    


d=lambda name ,make,color,year=2023,probeg=0: f" {name}\n {make}\n {color}\n {year}\n {probeg}"
print(d('jentra','GM','black',2024,10000))
   '''
# for while masalalari
'''
# for1
def for1(n,k):
    for i in range(n):
        print(k)
for1(3,5)

# for2
def for2(a,b):
    for i in range(a,b+1):
        print(i)
for2(3,7)

# for3
def for3(a,b):
    for i in range(a+1,b):
        print(i)
for3(4,9)

# for4
a=float(input("num = "))
def for4():
    for i in range(1,11):
        print(a*i)
for4()

# for5
a=float(input("num = "))
def for5():
    for i in range(0.1,1,0.1):
        print(a*i)
for5()

# for6
a=float(input("num = "))
def for6():
    for i in range(1.2,2+0.2,0.2):
        print(a*i)
for6()

# for7
def for7(a,b):
    sum1=0
    for i in range(a,b+1):
        sum1+=i;
    print(sum1)    
for7(2,6)        

# for8
def for7(a,b):
    multi=1
    for i in range(a,b+1):
        sum1+=i;
    print(sum1)    
for7(2,6)

# for9
def for9(a,b):
    sum1=0
    for i in range(a,b+1):
        sum1+=i**2;
    print(sum1)    
for9(2,6)

#for10
def for10(n):
    sum1=0
    for i in range(1,n+1):
        sum1+=1/i;
    print(sum1)    
for10(5)

# for11
def for11(n):
    sum1=0
    for i in range(n+1):
        sum1+=(n+i)**2;
    print(sum1)    
for11(5)

# for 12
def for112(n):
    multi=1
    for i in range(1.1,n+1,0.1):
        multi*=i;
    print(multi)    
for12(5)

# for13
def for13(n):
    sum1=k=0.0
    for i in range(1,n+1):
        k+=1
        sum1+=math.pow(-1,i-1)*(1+k/10)
    print(sum1)    
for13(2)

# for14
def for14(n):
    for i in range(1,n+1):
        print(i**2)
for14(5)

# for15
n=int(input("n = "))
def for15(a):
    kv=1
    for i in range(1,n+1):
        kv*=a
    print(kv)
for15(2)    

# for16
a=float(input("a = "))

def for16(n):
    for i in range(1,n+1):
        print(a**i)
for16(5)

# for17
a=float(input("a = "))
def for17(n):
    sum1=0
    for i in range(1,n+1):
        sum1+=a**i
    print(sum1)
for17(5)

# for18
a=float(input("a = "))
def for18(n):
    sum1=0
    for i in range(1,n+1):
        sum1+=(math.pow(-1,i-1))*math.pow(a,i)
        
    print(sum1)
for18(5)

# for19
n=int(input("n = "))
def for19():
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
for19()

# for20
n=int(input("n = "))
sum1=0
def for20():
    global sum1
    for i in range(1,n+1):
        fact=1
        for j in range(1,i+1):
            fact*=j
        sum1+=fact
    print(sum1)
for20()

# while 15

s=int(input("S som "))
def bank():
    sum2=0
    global s
    sum1=2*s
    p=int(input("foiz kiriting: "))
    i=1
    while i>0:
        a=s*p/100
        s+=a
        print(s)
        if s>=sum1:
            print(i,"-oy")
            exit()
        i+=1    
bank()

# while 16
n=10
def SportSmen():
    global n
    kun=30
    p=int(input("foiz kiriting: "))
    i=0
    while i<n:
        i+=1
        a=n*p/100
        n+=a
        print(n,"km")
        if n>=200:
            print(i,"kundan keyin 200km dan oshadi")
            exit()
SportSmen()            
        

# while17
def ButunQoldiq(n,m):
    counter=0
    while n>m:
        n-=m
        counter+=1
    print("butun = ",counter)
    print("qoldiq = ",n)
ButunQoldiq(15,4)

# while18
def ReverseNumber(n):
    while n>0:
        print(n%10,end="")
        n//=10
ReverseNumber(123)        

# while19
def SumNum(n):
    counter=summ=0
    while n>0:
        a=n%10
        n//=10
        summ+=a
        counter+=1
    print("raqam soni = ",counter)
    print("yig'indi = ",summ)        
SumNum(1231)        

# while20
def TwoTrueFalse(n):
    while n>0:
        a=n%10
        n//=10
        if a==2:
            c='2 raqami bor'
            break
        else:
            c='yoq'
    print(c)              
TwoTrueFalse(1324)        
'''

    
            
            
    

        


        

    

        
    
