# lesson10 -> SET collections

# set kop elementni 1ta ozgaruvchga saqlashda ishlatladi
# set unordred tartblanmagan, indexlanmagan
# 2ta bir xil qiymat mumkin emas
# ozgartrish mumkin emas, lekin yang element qoshish mumkin
# figurali qavs blan yaratladi {}
# element qoshish -> add()
# update() -> setga boshqa setni qoshish uchun ishlatladi
# remove() -> ochrish
#  discard() -> removga oxshash
# pop() -> oxrdagb elementni ochradi
# intersection() -> bir xilni yangi setga oladi, kesishmasni oladi
# subset -> 2ta set bor kichigi subset
# superset -> 2ta set bor kattasi supperset boladi
# disjoint set -> 2ta set bor bir biriga tegshli bolmasa true aks holda false qaytaradi

# setni + tarafi elementlarni sort qilib beradi aftomatik ravishda



# m1
'''

def t(a):
    if type(a)==set or type(a)==tuple:
        print("true")
    else:
        print("false")
t(())
'''
'''
#m1 2usul
def t1(a):
    if a in None:
        return 'None'
    elif type(a) in [tuple,set]:
        return True
    else:
        return False
    a=(1,2)
    print(t1(a))    
    
#m2
set1={10,20,30,40,50}
set2={30,40,50,60,70}
set3=[]
for i in set1:
    for j in set2:
        if i==j:
           set3.append(i)
print(set(set3))           

# example_1
set1={10,20,30,40,50}
set2={30,40,50,60,70}
a1=list(set1)
a2=list(set2)
a3=[]

for i in a2:
    a1.append(i)
print(a1)
for i in a1:
    if a1.count(i)==1:
        a3.append(i)
print(set(a3))

# example_2
s1={10,20,30}
s2={20,40,50}
a1=list(s1)
a2=list(s2)
a3=[]
for i in a1:
    for j in a2:
        if i==j:
            a1.remove(i)
print(a1)


# example_3
set1={"yellow","orange","black"}
list1=["blue","green","red"]
s1=list(set1)

for i in s1:
    list1.append(i)

print(set(list1))    


# example_4
s1={5,20,30}
s2={20,40,6}
a1=list(s1)
a2=list(s2)
a=a1[0]
print(a)
for i in a1:
    for j in a2:
        if i==j:
            if a>i:
                a=i
print(a)

#example_5
set1={5,10,15,20,30}
list1=list(set1)
b=True
n=int(input("n = "))
for i in range(len(list1)):
    if list1[i]==n:
        b=True
    else:
        b=False
print(b)

a = 'qwebfuqewyfyupqweihdfiwqenvdfbvyer'
print(a.replace('w','l'))
c=''
for i in a:
    if i !='w':
        c+=i
    else:
        c+='l'
print(c)

# m1
a = "Lorem Ipsum is simply dummy text of the printing and typesetting industry"
b=a.split()
d=sorted(b,key=lambda x :x[0].lower())
print(d)



dict1 = {1: 'ABC', 2: 'SXD', 3: 'HJK', 4: 'OIU', 5: 'YHB', 6: 'IKM'}
#{1: 'SXD', 2: 'ABC', 3: 'OIU', 4: 'HJK', 5: 'YHB'}
for i in range(1,len(dict1),2):
    dict1[i],dict1[i+1]=dict1[i+1],dict1[i]
print(dict1)    
    '''
a=[2,4,6,8,9,45,7,1,5]
n=int(input("n = "))
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==n:
            print([a[i],a[j]])
            
        
    












































        
    
            
            
           
      


         
        
        

