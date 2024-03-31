"""
n=5
s=""
while n>=0:
    s+=str(n%2)
    n=n/2
print(s[::1]) 
a="dfdd"
print(a[::1])  """

def next_id(arr):
    a=sorted(arr)
    if a==arr:
        return len(arr)
    else:
        return 0
print(next_id([1,2,3,4]))    