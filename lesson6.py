# lesson6
import math
# rtoplamlar
# tuple and set
# tuple- indexlangan elementini ozgartirib bolmaydi, dublikatga ruxsat bor
#  del -> to'plamni butunlay o'chiradi
#  count()-> tuple ichda nechta bir xil element borligini aniqlaydi
#  index() -> element turgan ornini aniqlaydi
'''
# example_1
mytuple=('ali',20,True,12.1)
print(mytuple)
print(mytuple[:2])
# example_2
s="samandar"
print(s[::-1]) #revers, ::->start and stop default holda olib ketadi
# example_3
myTUPLE=(1,3,7,5,'apple',5)
print(myTUPLE.count(5))
print(len(myTUPLE))

#    LIST toplami
# list-> tartiblangan dublikatga ruxsat bor va elementnini ozgartirsa boladi


myList=['apple','banana','cherry','apple']
myList1=['nok','banana','orange']

print(len(myList))
myList[0]='olma' # edit qilish (ozgartirish)
print(myList)
# listga element qoshish -> append()
myList.append('tarvuz') # list oxrdan qoshadi

# insert() -> istalgan joydan element qoshish
myList.insert(0,'orange') #0- indexga qoshadi

#listga boshqa listni qoshish -> extend()
myList.extend(myList)
print(myList)

# listdan element o'chirish -> remove()
myList.remove('apple') # agar apple bir nechta bolsa 1-uchraganini o'chiradi

#listda pop() -> funksiyasi oxridan o'chiradi
myList.pop()

# sort() funksiyasi
myList.sort() # alifbo boycha yoki son bolsa kichikdan kattaga qarab saralaydi
print(myList)

# listdan nusxa olish:
myList=myList1.copy()
myList=myList1 # bir xil qiladi
'''
# vazifa lesson 6
# list
# example_1
myList=['apple','banana','cherry']
a=0
counter=0
for i in myList:
    for j in i:
        if j=='a':
           print(i)
           break

# example_2
myList=['apple','banana','cherry']
counter=0
for i in myList:
    for j in i:
        if j=='a':
            myList.remove(i)    
print(myList)

# example_3
def list_sum(sumList=[2,4,7,5]):
    s=0
    for i in sumList:
        s+=i
    print(s)
list_sum()

# example_4
def list_multi(sumList=[2,4,7,5]):
    s=1
    for i in sumList:
        s*=i
    print(s)
list_multi()
# example_5
def dublikat_remove(a=[1,2,3,4,1]):
    c=0
   for i in range(len(a)):
       for j in range(1,len(a)):
           if a[i]==a[j]:
               a.remove(i)
    print(a)          
       
dublikat_remove()        

# example_6
def twoDublicat(a=[1,2,3,4],b=[8,2,1]):
    c=True
    counter=0
    for i in a:
        for j in b:
            if i==j:
                counter+=1
                if counter>1:
                    c=True
                else:
                    c=False
                    
    print(c)                
twoDublicat()

# example_7
def juftRemove(a=[1,2,3,4,5]):
    for i in a:
        if i%2==0:
            a.remove(i)
    print(a)
juftRemove()

# example_8
def solution(a=[1,2,3,4,5]):
    b=int(input("son kirit: "))
    for i in a:
        if i==b:
            c=i
            
        else:
            c="son yoq"
    print(c)         
solution()

# example_9
def maxList(a=[1,2,3,4,5]): 
    print(max(a))
maxList()

# example_10
def minList(a=[1,2,3,4,5]): 
    print(min(a))
minList()

# example_11
def max2List(a=[1,2,3,4,5]):
    max2=0;
    s=max(a)
    for i in a:
        if s>i:
            max2=i
    print(max2)        
max2List()

# example_12
def min2List(a=[1,2,3,4,5]):
    min2=0
    s=min(a)
    for i in a:
        if s<=i and i!=s:
            min2=i
            break
    print(min2)        
min2List()

# example_13
def kvList(a=[1,2,3,4,5,6,7]):
    b=[]
    for i in a:
        i=i*i
        b.append(i)
    print(b)           
kvList()

# example_14
def list14(a=["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]):
    a[2][1][2].extend(["h", "i", "j"])
    print(a)
list14()

# example_15
def list15():
    a="apple banana cherry orange"
    b=[]
    n=int(input("uzunligini kiriting"))
    x=a.split()
    for i in x:
        if len(i)==n:
            b.append(i)
    print(b)         
list15()

# example_16
def list16():
    a = "salom python assalom python salom dunyo"
    sozlar = a.split()
    nechtaliklar = {}

    for i in sozlar:
        if i in nechtaliklar:
            nechtaliklar[i] += 1
        else:
            nechtaliklar[i] = 1

    for i, nechtalik in nechtaliklar.items():
        print(f"{i} {nechtalik} ta")
list16()

# example_17
def s_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
my_list = [5, 2, 8, 1, 3, 7, 4, 6]
s_sort(my_list)
print("Sorted list:", my_list)

# example_18
a=['a','b','c']
b=[]
for i in range(len(a)):
    for j in range(1,len(a)):
        if a[i]!=a[j]:
            
            c=a[i]+a[j]
         
            b.append(c)
print(b)

# example_19
a="salom alaykum talabalar"
maxx=0
soz=""
x=a.split()
for i in x:
    if maxx<len(i):
        maxx=len(i)
        soz=i
print(soz)

# TUPLE DOIR MASALALAR:
# m_1
def myTuple(a=[]):
    n=int(input("element soni = "))
    for i in range(n):
        x=int(input("element = "))
        a.append(x)
    tuplee=tuple(a)
    print(tuplee)
myTuple()

# m_2
def m(a=(1,3,4,5,6)):
    b=list(a)
    n=int(input("element = "))
    for i in b:
        if i==n:
            b.remove(i)  
    c=tuple(b)    
    print(c)
m()

# m_3
def reverse(a=(1,3,4,5,6)):
    b=list(a)
    print(a[::-1])
reverse()

# m_4
a=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
for i in a:
    for j in i:
        for k in range(len(a)):
            j[-1]=100
            break
print(a)            
    
# m_5
list1 = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
list2 = [t for t in original_list if t]

print(list2)

       
        
        
        
        
   

    





            

    
        
            
    
            
           
                
            
        
       
        





