import math

a=int(input("kv tomonni kirit:\n"))
print(a*a)

# masala 3
a=int(input("a = "))
b=int(input("b = "))

s=a*b
p=2*(a+b)

print("s = ",s)
print("p = ",p)

# masala 4
d=int(input("d = "))
l=math.pi*d
print(l)

#masala 5
a=int(input("a = "))
v=a**3
s=6*a**2
print(v)
print(s)

#masala 6
a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
v=a*b*c
s=2*(a*b+b*c+c*a)
print(v)
print(s)

#masala 7
r=int(input("r = "))
l=2*math.pi*r
s=math.pi*r**2
print("l = ",l,"  s = ",s)

#masala 8
a=int(input("a = "))
b=int(input("b = "))
print("orta arif = ",(a+b)/2)

#masala 9
a=int(input("a = "))
b=int(input("b = "))
print("orta geometrik = ", math.sqrt(a*b))

#masala 10
a=int(input("a = "))
b=int(input("b = "))
print("sum = ",a+b)
print("multi = ",a*b)
print("kvad = ",a**2," ",b**2)

#masala 11
a=int(input("a = "))
b=int(input("b = "))
print("sum = ",a+b)
print("multi = ",a*b)
print(math.fabs(a)," ",math.fabs(b))

#masala 12
a=int(input("a = "))
b=int(input("b = "))
c=math.sqrt(a**2+b**2)
p=a+b+c
print(c)
print(p)

#masala 13
r1=int(input("r1 = "))
r2=int(input("r2 = "))
s1=math.pi*r1
s2=math.pi*r2
s3=math.pi*(r1-r2)
print("s1 = ",s1,"  s2 = ",s2,"  s3 = ",s3)

#masala 14
l=int(input("l = "))
r=l/2*math.pi
s=math.pi*r**2
print(r)
print(s)

#masala 15
s=int(input("s = "))
r=math.sqrt(l/math.pi)
l=2*math.pi*r
d=l/math.pi
print("r = ",r)
print("d = ",d)

#masala 16
x1=int(input("x1 = "))
x2=int(input("x2 = "))
masofa = math.fabs(x2-x1)
print(masofa)

#masala 17
a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
print("ac uzunligi = ",math.fabs(c-a))
print("bc uzunligi = ",math.fabs(c-b))

#masala 18
a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
ac=math.fabs(c-a)
bc=math.fabs(c-b)
print(ac*bc)

#masala 19
 # Tomon uzunliklarini hisoblash
""" x1=int(input("x1 = "))
 x2=int(input("x2 = "))
 x3=int(input("x3 = "))
 x4=int(input("x4 = "))

    AB = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    BC = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    CD = math.sqrt((x4 - x3)**2 + (y4 - y3)**2)
    DA = math.sqrt((x1 - x4)**2 + (y1 - y4)**2)
    # Perimeterni hisoblash
    P = AB + BC + CD + DA
    # yuzasi
 S = 0.5 * abs((x1*y2 + x2*y3 + x3*y4 + x4*y1) - (y1*x2 + y2*x3 + y3*x4 + y4*x1))
print("p = ",P)
print("s = ",S)
"""
#masala 20
x1=int(input("x1 = "))
x2=int(input("x2 = "))
y1=int(input("y1 = "))
y2=int(input("y2 = "))
print("tek_oras_masofa = ",math.sqrt((x2-x1)**2+(y2-y1)**2))


#masala 22
a=int(input("a = "))
b=int(input("b = "))
t=a
a=b
b=t
print(a)
print(b)

#masala 23
a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
t=a
a=b
b=c
c=a
a=t

print(a)
print(b)
print(c)

#masala 24
a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
a, c, b = c, b, a

print(a)
print(b)
print(c)

#masala 25
x=int(input("x = "))
y=3*x**5-6*x**2-7
print(y)

#masala 26
x=int(input("x = "))
y=4*(x-3)**5-7*(x-3)**3+2
print(y)

#masala 27
a=int(input("a = "))
print(a**2," ",a**4)

#masala 28
a=int(input("a = "))
print(a**2," ",a**3," ",a**5," ",a**10)

#masala 29
a=int(input("burchak gradus = "))
rad=a*math.pi/180
print(rad)

#masala 30
rad=int(input("radian = "))
gradus=rad*180/math.pi
print(gradus)

#masala 31
Tf=int(input("faranget = "))
Tc=(Tf-32)*5/9
print(Tc)

#masala 32
Tc=int(input("faranget = "))
Tf=(Tc-32)*5/9
print(Tf)

#masala 33
x=int(input("x kg = "))
a=int(input("x  som = "))
kg1=a/x
y=int(input("y = "))
kgy=y*a/x
print(kg1)
print(kgy)

#masala 34
x=int(input("x kg = "))
a=int(input("x  som = "))
y=int(input("y kg = "))
b=int(input("b  som = "))
kg1Sh=a/x
kg1K=b/y
print(math.fabs(kg1Sh-kg1K))

#masala 35
v=int(input("v = "))
u=int(input("u = "))
t1=int(input("t1 = "))
t2=int(input("t2 = "))
s=(v*t1-u*t2)
print(s)

#masala 36
v1=int(input("v1 = "))
v2=int(input("v2 = "))
t=int(input("t = "))
s1=v1*t
s2=v2*t
s=s1+s2
print(s)

#masala 37
v1=int(input("v1 = "))
v2=int(input("v2 = "))
t=int(input("t = "))
s1=v1*t
s2=v2*t
s=s1-s2
print(s)

#masala 38
a=int(input("a = "))
b=int(input("b = "))
x=-b/a
print(x)

#masala 39
a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
D=b**2-4*a*c
x1=(-b+math.sqrt(D))/2*a
x2=(-b-math.sqrt(D))/2*a

print(x1)
print(x2)









