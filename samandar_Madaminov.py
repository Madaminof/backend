# MADAMINOV SAMANDAR  ID-20004
#  variant-A

#1
a={1, 45, 78, 4}
b={7, 4, 78, 1}
d=[]
c=0
for i in a:
    for j in b:
        if i==j:
            d.append(j)
c=min(d)
print(c)

#2
a="Python 22 django3sndsiH20KNK34 "
c=0
b=list(a)
d=[]
for i in a:
    if i.isdigit():
        d.append(i)
        c+=int(i)
print(d)
print(c)        


#m3
a="Assalom"
b=set(a.lower())
list1=list(b)
len1=len(list1)
print(list1)
print(len1)



#m4
n=int(input("n = "))
dict1={}
for i in range(1,n+1):
    dict1[i]=i**2
print(dict1)    
    

#m5
a=10,20,3,0,2,5
b=4,9,8,10,0,2
c=set({})
for i in a:
    for j in b:
        if i==j:
            c.add(j)
v=sorted(list(c))
print(v)

