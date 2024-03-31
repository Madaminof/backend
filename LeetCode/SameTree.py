l1=[1,2,3]
l2=[1,2,3,4]
s1=""
s2=""
for i in l1:
    s1+=str(i)
for j in l2:
    s2+=str(j)
if len(l1)!=len(l2):
    print(False)
elif s1==s2:
    print(True)
else:
    print(False)            


nums=[2,11,10,1,3]
k=10
s=0
for i in nums:
    if i<k:
        s+=1
print(s)        
    

nums = [2,1,3]    
nums[1],nums[2]=nums[2],nums[1]
print(nums)
s = "Hello, my name is John"
s1=0
for i in s.split():
    s1+=1
print(s1) 


s = ["H","a","n","n","a","h"]
print(s[::-1])
s3=[]
s1=""
for i in s:
    s1+=i
s2=s1[::-1]
for i in s2:
    s3.append(i)
print(s3)    

s1="asdfghjkl"
a="alaska"
for i in a:
    if i in s1:
        print(True)
    else:
        print(False)    

