
# 
"""s='(('
result=True
for i in range(0,len(s),2):
    for j in range(1,len(s),2):
        if s[i]!=s[j]:
            if s[i]=='(':
                if s[j]==')':
                    result=True
                else:
                    result=False    
            elif s[i]=='[':
                if s[j]==']':
                    result=True 
                else:
                    result=False
            elif s[i]=='{':
                if s[j]=='}':
                    result=True
                else:
                    result=False
        else:
            result=False            
print(result)                                           
          
def isValid(s):
    result=True
    for i in range(0,len(s),2):
        for j in range(1,len(s),2):
            if s[i]!=s[j]:
                if s[i]=='(':
                    if s[j]==')':
                        result=True
                    else:
                        result=False    
                elif s[i]=='[':
                    if s[j]==']':
                        result=True 
                    else:
                        result=False
                elif s[i]=='{':
                    if s[j]=='}':
                        result=True
                    else:
                        result=False
    return result
print(isValid(s))      """


# Marge two list sort
"""
l1=[1,2,4]
l2=[1,3,4,5]

l3=l1+l2
print(sorted(l3))        """

"""
l1=[0,0,1,1,2,2,3,3,4,4,5,5]
s1=set(l1)
l2=list(s1)
len1=len(l1)-len(l2)
for i in range(len1):
    l2.append('_')
print(l2)"""

nums=[3,2,2,3]
val=3
s=0
l=[]
for i in nums:
    if i!=val:
        l.append(i)
for i in nums:
    if i==val:
        s+=1
for i in range(s):
    l.append('_')
#print(l)


"""
word = "abcdefd"
ch = "d"
index1=word.index(ch)
a1=word[:-index1]
a2=word[index1+1:]
revrs=a1[::-1]
print(revrs+a2)"""

"""
nums = [1,2,3,2]
result=[]
for i in nums:
    if nums.count(i)==1:
        result.append(i)
print(sum(result))    """
"""
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
s=0
for i in grid:
    for j in i:
        if j<0:
            s+=1
print(s)           """

"""
c=0
r=""
s="abcABC123  fd  efef efe"
a=s.split()
b=a[::-1]
for i in b:
    r+=i+" "
print(r.strip())   """
 

def RemoveDublicate(nums):
    result=[]
    for num in nums:
        if num not in result:
            result.append(num)
    return result
print(RemoveDublicate([1,1,2,3,3,4,2,5]))
        





