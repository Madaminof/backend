# example_6
'''
def reversFloat(a=[('item1',25.1),('item2',15.2),('item3',30.3)]):
    b=[]
    c=[]
    for i in a:
       # print(i)
    for j in range(len(i)):
        print(i[::-1])
reversFloat()

# exmple_1
def toqList(a=['salom','alekum','talaba']):
    b=[]
    for i in a:
        if len(i)%2==1:
            b.append(i)
    print(b)    
toqList()
'''
# example_2
def tubList(a=[1,2,3,4,5,6,7,8,9,10,11]):
    b=[]
    c=[]
    s=0
    for i in a:
        for j in range(1,i+1):
            if i%j==0:
                s+=1
        if s==2:
            b.append(i)
        else:
            c.append(i)
                
       
    print(b)
    print(c)
tubList()
'''
# example_3
def meva(a=['apple','banana','cherry']):
    n=str(input("meva kiriting: "))
    for i in a:
        if i==n:
            print("bu meva bor")
            break
        else:
            a.append(n);
            break
    print(a)        
meva()        
   
# example_4
def sonMedium(a=[1,2,3,4,5,6]):
    count=len(a)
    summ=0
    for i in a:
        summ+=i
    ortacha=int(summ/count)
    print(ortacha)
sonMedium()


# example_5
def num(a=[1,2,3,4,5,6]):
    max1=a[0]
    min1=a[0]
    for i in range(len(a)):
        if max1<a[i]:
            max1=a[i]
        if min1>a[i]:
            min1=a[i]
    multi=max1*min1
    print(multi)     
num()

# example_6
def endSort(a=['salom','alaykum','talaba']):
    sorted_list = sorted(a, key=lambda a: a[-1])
    print(sorted_list)
endSort()

# example_7
def nums(a=[1,2,3,4,5],b=[1,2,6,7,8,3]):
    c=[]
    for i in a:
        for j in b:
            if i==j:
                c.append(i)
    print(c)            
nums()

# example_8
def twoRemove(a=['sava','arra','hello','salom']):
    sort_list = [word for word in a if word.count('a') != 2]
    print(sort_list)
twoRemove()

# example_9
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

# example_10
def m10(a=[1, 3, 5, 7, 9, 10],b=[2, 4, 6, 8]):
    
    a.remove(a[-1])
    for i in b:
        a.append(i)
    print(a)    
m10()    
    '''


        
    
        
        

