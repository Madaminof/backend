# lesson 3   case:
import math
# case 1
"""""
kun=int(input("kunni kiriting: "))
if kun==1:
    print("dushanba")
elif kun==2:
    print("seshanba")
elif kun==3:
    print("chorshanba")
elif kun==4:
    print("payshanba")
elif kun==5:
    print("juma")
elif kun==6:
    print("shanba")
elif kun==7:
    print("yakshanba")
else:
    print("bunday hafta mavjud emas!")

#case 2
baho=int(input("bahoni kiriting: "))
if baho==1:
    print("yomon")
elif baho==2:
    print("qoniqarsiz")
elif baho==3:
    print("qoniqarli")
elif baho==4:
    print("yaxshi")
elif baho==5:
    print("a'lo")
else:
    print("xato")

# case 3
month=int(input("input month: "))
if month>=1 and month<=3:
    print("winter")
elif month>=4 and month<=6:
    print("Spring")
elif month>=7 and month<=9:
    print("Summer")
elif month>=10 and month<=12:
    print("Autumn")
else:
    print("exseption")

# case 4
month=int(input("input month: "))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print("31 kun bor")
elif month==4 or month==6 or month==9 or month==11:
    print("30 kun bor")
elif month==2:
    print("28 kun bor ")
else:
    print("not month ")

# case 5
a=float(input("son: "))
b=float(input("son: "))

amal=int(input("butun son: "))
if amal==1:
    print(a+b)
elif amal==2:
    print(a-b)
elif amal==3:
    print(a/b)
elif amal==4:
    print(a*b)
else:
    print("exseption")

# case 6
amal=float(input(" son: "))
a=int(input("butun son: "))
if a==1:
    print("dm ",a/10," m ga teng")
elif a==2:
    print("km ", a/1000," m ga teng")
elif a==3:
    print("m ", a," m ga teng")
elif a==4:
    print("mm ",a*1000," m ga teng" )
elif a==5:
    print("sm ",a*100,"m ga teng")
else:
    print("exseption")

# case 7
weight=int(input(" og'irlik: "))
a=int(input(" son: "))
if a==1:
    print("kg ",a," kg ga teng")
elif a==2:
    print("milligramm ", a*1**6," kg ga teng")
elif a==3:
    print("gramm ", a/1000," kg ga teng")
elif a==4:
    print("tonna ",a*1000," kg ga teng" )
elif a==5:
    print("sentner ",a*100,"kg ga teng")
else:
    print("exseption")

# case 8
d=int(input(" day: "))
m=int(input(" month: "))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print(d,"//",month,"//2023")
elif month==4 or month==6 or month==9 or month==11:
    print(d,"//",month,"//2023")
elif month==2:
    print(d,"//",month,"//2023")
else:
    print("not month ")

# case 9
day=int(input(" day: "))
month=int(input(" month: "))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    if day==31:
        day=1;
        print(day,"//",month+1)
    else:
        print(day+1,"//",month)
elif month==4 or month==6 or month==9 or month==11:
    if day==30:
        day=1
        print(day,"//",month+1)
    else:
        print(day+1,"//",month)
    
elif month==2:
    if day==28:
        day=1
        print(day,"//",month+1)
    else:
        print(day+1,"//",month)
else:
    print("not month ")

# case 10
y=str(input("yonalish: "))
k=int(input("kamanda: "))
if y=="s":
    if k==0:
        print("shimol ga harakatni davom ettir")
    elif k==1:
        print("shimol ga chapga buril")
    elif k==2:
        print(y,"shimol ga onggga buril")
    else:
        print("error")
elif y=="j":
    if k==0:
        print("janub ga harakatni davom ettir")
    elif k==1:
        print("janub ga chapga buril")
    elif k==2:
        print(y,"janub ga onggga buril")
    else:
        print("error")        
elif y=="q":
    if k==0:
        print("sharq ga harakatni davom ettir")
    elif k==1:
        print("sharq ga chapga buril")
    elif k==2:
        print(y,"sharq ga onggga buril")
    else:
        print("error")
elif y=="g":
    if k==0:
        print("garb ga harakatni davom ettir")
    elif k==1:
        print("garb ga chapga buril")
    elif k==2:
        print(y,"garb ga onggga buril")
    else:
        print("error")
else:
    print("xato")

# case 12
a=int(input("son: "))
r=int(input("radius: "))

if a==1:
    print(r)
elif a==2:
    print("diametr = ",2*r)
elif a==3:
    print("uzunlik = ",2*math.pi*r)
elif a==4:
    print("yuza = ", math.pi*r**2)
else:
    print("error")
# case 13
a=int(input("son: "))
b=int(input("katet: "))

if a==1:
    print(b)
elif a==2:
    c=b*math.sqrt(2)
    print("gipatenuza = ",c)
elif a==3:
    h=c/2
    print("balandlik = ",h)
elif a==4:
    print("yuza = ", c*h/2)
else:
    print("error")

# case 14
a=int(input("son: "))
b=int(input("tomoni: "))

if a==1:
    print(b)
elif a==2:
    r1=b*math.sqrt(3)/6
    print("ichki chiz ay radiusi = ",r1)
elif a==3:
    print("tashqi chiz ay radiusi = ",2*r1)
elif a==4:
    print("yuza = ",b**2*math.sqrt(3)/3)
else:
    print("error")
    """
