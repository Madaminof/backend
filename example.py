# m1
'''
a="phyton22django3nbdbdjsvj20bbm34"
b=[]
s=0
c=list(a)
for i in c:
    if i.isdigit():
        b.append(i)
print(b)
for i in b:
    s+=int(i)
print(s)


#m1
a={1,521,2,5,45,78,4}
b={7,8,456,45,12,78,521}
d=[]
c=0
for i in a:
    for j in b:
        if i==j:
            d.append(j)
c=min(d)
print(c)

#m3
a="assalom"
print(set(a))

#m4
n=int(input("n = "))
b={}
for i in range(1,n+1):
    b[i]=i**2
print(b)    
    
        


#m5
a=1,2,3,4,7,9,3
b=0,5,8,3,4,9
a1=list(a)
b1=list(b)
c=set({})
for i in a1:
    for j in b1:
        if i ==j:
            c.add(j)
v=sorted(list(c))
print(v)

#m6
a={22:"sardor"}
b={26:"ali"}
c=0
for i,j in a.items():
    for l,k in b.items():
        if i>l:
            print(l,k)
        else:
            print(i,j)
   
#m7
a="Mgh8HTnkY@hnj90"
b=""
c=[]
for i in a:
    if i==i.upper():
        b+=i
for i in b:
    if i.isalpha():
        c.append(i)
print(c)        


#m8
a=13249570
x=''
b=str(a)
for raqam in b:
        if raqam == '4':
            x+= '7'
        elif raqam == '7':
            x += '4'
        else:
            x += raqam
    
natija = int(x)
print(natija)

#m9
a="phytonwgdjheodowosddsco" # o nech marta qatnashgan
c=0
for i in a:
    if i=='o':
        c+=1
print(c)        
  '''
def kamayish_tartibida_chiqarish(qator1, qator2):
    sonlar1 = list(map(int, qator1.split(',')))
    sonlar2 = list(map(int, qator2.split(',')))

    natija = []
    for son in sonlar1 + sonlar2:
        if (son in sonlar1 and son not in sonlar2) or (son in sonlar2 and son not in sonlar1):
            natija.append(son)

    natija_kamayish = sorted(natija)
    print(' '.join(map(str, natija_kamayish)))

# Test
qator1 = "5,4,7,8,90,100,20,3,0,2,5"
qator2 = "1,5,0,20,100,4,9,8,90,0"
kamayish_tartibida_chiqarish(qator1, qator2)


































    
