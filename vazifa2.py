import math
'''
# if1
a=int(input("a = "))
if a>0:
    print(a+1)
else:
    print(a)

# if2
a=int(input("a = "))
if a>0:
    print(a+1)
else:
    print(a-2)
    
# if3
a=int(input("a = "))
if a>0:
    print(a+1)
elif a<0:
    print(a-2)
else:
    a=10
    print(a)

# if4
a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
counter=0
if a>0 and b>0 and c>0:
    print(3)
elif a>0 and b>0 and c<0:
    print(2)
elif a>0 and b<0 and c>0:
    print(2)
elif a<0 and b>0 and c>0:
    print(2)
elif a>0 and b<0 and c<0:
    print(1)
elif a<0 and b>0 and c<0:
    print(1)
elif a<0 and b<0 and c>0:
    print(1)    
else:
    print("musbat son yoq")

# if5
a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
counter=0
if a>0 and b>0 and c>0:
    print("musbat ",3)
    print("manfiy ",0)
elif a>0 and b>0 and c<0:
   print("musbat ",2)
    print("manfiy ",1)
elif a>0 and b<0 and c>0:
   print("musbat ",2)
    print("manfiy ",1)
elif a<0 and b>0 and c>0:
    print("musbat ",2)
    print("manfiy ",1)
elif a>0 and b<0 and c<0:
    print("musbat ",1)
    print("manfiy ",2)
elif a<0 and b>0 and c<0:
   print("musbat ",1)
    print("manfiy ",2)
elif a<0 and b<0 and c>0:
    print("musbat ",1)
    print("manfiy ",2)  
else:
   print("musbat ",0)
    print("manfiy ",3)

# if6
a=int(input("a = "))
b=int(input("b = "))
print(max(a,b))

# if7
a=int(input("a = "))
b=int(input("b = "))
d=min(a,b)
print(d)

# if8
a=int(input("a = "))
b=int(input("b = "))
mak=max(a,b)
min1=min(a,b)
print(mak)
print(min1)

#if9
a=float(input("a = "))
b=float(input("b = "))
if a>b:
    a,b=b,a
    print("a = ",a)
    print("b = ",b)
else:
    print("a = ",a)
    print("b = ",b)

# if10
a=int(input("a = "))
b=int(input("b = "))
if a!=b:
    print(a+b)
else:  
    print(0)

# if11
a=int(input("a = "))
b=int(input("b = "))
if a!=b:
    print(max(a,b))
else:
    print(0)

# if12
a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
print(min(a,b,c))

#if 13
a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
if a>b and b>c:
    print(b)
elif a>c and c>b:
    print(c)
elif c>b and b>a:
    print(b)
elif c>a and a>b:
    print(a)
elif b>a and a>c:
    print(a)
elif b>c and c>a:
    print(c)

# if14
a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
print(min(a,b,c))
print(max(a,b,c))

#if15
a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
sum1=a+b
sum2=a+c
sum3=b+c
print(max(sum1,sum2,sum3))

# if16
a=float(input("a = "))
b=float(input("b = "))
c=float(input("c = "))
if a<b and b<c:
    print(a*2)
    print(b*2)
    print(c*2)
else:
    print(a*(-1))
    print(b*(-1))
    print(c*(-1))

#if 17
a=float(input("a = "))
b=float(input("b = "))
c=float(input("c = "))
if a<b and b<c or a>b and b>c:
   print(a*2)
   print(b*2)
   print(c*2)
   
else:
    print(a*(-1))
    print(b*(-1))
    print(c*(-1))

# if18
a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
if a==b:
   print(c)
elif a==c:
   print(b)
elif b==c:
   print(a)
   
# if19
a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
d=int(input("d = "))
if a==b and b==c:
   print(d)
elif a==b and b==d:
   print(c)
elif a==c and c==d:
   print(b)
elif c==b and b==d:
   print(a)   

# if20
a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
size1=math.fabs(a-b)
size2=math.fabs(a-c)
yaqn=min(size1,size2)
print(yaqn)
print(size1)

# if21
a=int(input("a = "))
if a==0:
   print(0)
else:
   print("ox = "a," "," oy = ",a)

# if22
ox=int(input("ox = "))
oy=int(input("oy = "))
if ox>0 and oy>0:
   print("1-chorak")
elif ox>0 and oy<0:
   print("4-chorak")
elif ox<0 and oy>0:
   print("2-chorak")
elif ox<0 and oy<0:
   print("3-chorak")

# if23
x1=int(input("x1 = "))
y1=int(input("y1 = "))
x2=int(input("x2 = "))
y2=int(input("y2 = "))
x3=int(input("x3 = "))
y3=int(input("y3 = "))

x4 = x1 + x3 - x2
y4 = y1 + y3 - y2
print(x4)
print(y4)

# if24
x=float(input("x = "))
if x>0:
   print(2*math.sin(x))
elif x<=0:
   print(x-6)

# if25
x=float(input("x = "))
if x<-2 or x>2:
   print(2*x)
else:
   print((-3)*x)

# if26
x=float(input("x = "))
if x<=0:
   print(-x)
elif x>0 and x<2:
   print(x**2)
elif x>=2:
   print(4)

# if27
x=float(input("x = "))
if x<0:
   print(0)
elif x%2==0:
   print(1)
elif x%2==1:
   print(-1)

# if28
y=int(input("yil = "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
   print("kabisa yili")
else:
   print("kabisa yili emas")

# if29
x=int(input("x = "))
if  x%2==0:
   a=" juft son"
   if x>0:
      print("musbat",a)
   elif x<0:
      print("manfiy",a)
if  x%2!=0:
   b=" toq son"
   if x>0:
      print("musbat",b)
   elif x<0:
      print("manfiy",b)      
    
# if30
x=int(input("x = "))
size=str(abs(x))
a=len(size)
if x%2==0:
   print(a," xonali juft son")
else:
   print(a," xona;i toq son")
      
# uchbur
a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))

if a+b>c and b+c>a and a+c>b:
    print("uchburchak hosil bo'ladi")
else:
    print("uchburchak emas")

# masala
x=int(input("x = "))
print("musbat" if x>0 else "manfiy" )
'''
# masala1
x=float(input("summa kiriting = "))
a=x%100
a1=x/100
if a>500:
    print(a1+1)
elif a<500:
    print(a1)
