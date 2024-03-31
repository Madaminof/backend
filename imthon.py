#1
'''
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
print(b)

#m4
n=int(input("n = "))
dict1={}
for i in range(1,n+1):
    dict1[i]=i**2
print(dict1)    
    '''
"""
#m5
a=10,20,3,0,2,5
b=4,9,8,10,0,2
c=set({})
for i in a:
    for j in b:
        if i==j:
            c.add(j)
v=sorted(list(c))
print(v)"""
class Vaqt():
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second


class Hour(Vaqt):
    def add_5_hour(self):
        if self.hour > 24:
            h = (self.hour - 24) + 5
            print(f"{h}:{self.minute}:{self.second}")
        else:
            h = self.hour + 5
            print(f"{h}:{self.minute}:{self.second}")


class minut(Vaqt):
    def add_5_minute(self):
        if self.minute > 60:
            h = (self.hour - 60) + 5
            print(f"{h}:{self.minute}:{self.second}")
        else:
            h = self.hour + 5
            print(f"{h}:{self.minute}:{self.second}")

class sekund(Vaqt):
    def add_5_minute(self):
        if self.minute > 60:
            h = (self.hour - 60) + 5
            print(f"{h}:{self.minute}:{self.second}")
        else:
            h = self.hour + 5
            print(f"{h}:{self.minute}:{self.second}")            



vaqt = Vaqt(4, 8, 56)
h = Hour(vaqt)
h.add_5_hour()


