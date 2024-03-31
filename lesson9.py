# lesson9
#dict oson usullari
'''
#m1
n=int(input())
a={son:son**2 for son in range(1,n+1)}
print(a)

#m2
d={'a':100,'b':200,'c':300}
a=[x**2 if x==200 else x for x in d.values() if x>150]
 #print    shart     else    loop
print(a)

#m3
n=int(input())
a={son: son**2 for son in range(1,n+1)}
print(a)


#m4
d1 = {'a': 100, 'b': 200, 'c': 300, 'v': 'sdvfw', 'j': 12, 'f': 'dfe'}
c=0
for i in d1.values():
    if type(i)==int:
        c+=i
print(c)

s=0
a={i: i if type(i)==int else  for i in d1.values()  }
print(a)
 



a="mexanizasiyalashtirilganmi"
b={i: a.count(i)  for i in a }
print(b)
'''
# vazifa:
#m1

def ortaArif(a=[1, 1, 3, 4, 4, 5, 6, 7],b=[0, 1, 2, 3, 4, 4, 5, 7, 8]):
    len1=len(a)
    len2=len(b)
    sum1=0
    sum2=0
    for i in a:
        sum1+=i
    arif1=sum1/len1
    for j in b:
        sum2+=j
    arif2=sum2/len2
    s=(arif1+arif2)/2
    print(s)
ortaArif()

#m2
a=[1, 4, 3, 9]
b=[]
n=str(input("n = "))
for i in a:
    b.append(n+str(i))
print(b)

#m3
my_list = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]

max_sum = max(my_list, key=sum)

print("Berilgan list:", my_list)
print("Eng katta yi'gindisi bo'lgan sublist:", max_sum)


#m4
a=[1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
c=0
for i in a:
    if type(i)==int:
        c+=1
        
print(c)        
   
#m5
a=[2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2]
b={i: a.count(i)  for i in a  }
c=0
for i in b.values():
    if c<i:
        c=i
print(c)
for i,j in b.items():
    if j==c:
        print(i,j)

#m6
def increment(lst):
   
    num = int(''.join(map(str, lst))) + 1
   
    result = [int(digit) for digit in str(num)]
    
    return result

print(increment([1, 2, 3])) 
print(increment([9]))      
print(increment([9, 9, 9, 9]))

#m7
b=[]
n=int(input("n = "))
for i in range(n):
    i=int(input("son = "))
    b.append(i**2)
print(b)

#m8
a=[1, 4, 3, 9]
b=['chelsea', 'real', 'barca', 'MU']
c=[]
for i in range(len(a)):
    c.append(b[i]+str(a[i]))
print(c)

# 2. Berilgan strdagi raqamlar yigindisini toping
# input: 'sfb9wue8qfu5q2' output: 24
a='sfb9wue8qfu5q2'
b=[]
c=0
for i in a:
    if i.isdigit():
        b.append(int(i))       
for i in b:
    c+=i
print(c)    
        
            
        

    
    

    

        
    
    
   
    



    

