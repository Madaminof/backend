# lesson 8
# dictionary
# key(kalit) va valie(qiymatni) ni oz ichiga oladi
# key(kalit) -> ozgaruvchiga oxshab elon qlinadi string va integerda oladi, char belgilarini qabul qilmaydi
# key(kalit) -> dublikatga ruxsat bermaydi. value-> elementlari takrorlanishi mumkin va hohlagan belgini qabul qiladi
# dictionary (key:value) -> ni ozgartirsak boladi



'''
# example_1
d={"name":"samandar",
   "age":19,
    "city":"fergana"}
print("dictionary uzunligi = ",len(d))
print(d.get("name"))

for i in d.values(): # bu values methodi hamma value(qiymatini) ekranga chiqaradi
    print("value = ",i)

for i in d.keys():  # keys methodi barcha kalitlarini chiqaradi
    print("key = ",i)

for i in d.items():   # items methodi barcha kalit,qiymatni chiqaradi
    print("key,value = ",i)


myDic={"emp1":{"name":"bob","job":"dev"},
       "emp2":{"name":"kim","job":"dev"},
       "emp3":{"name":"sam","job":"dev"}}
for i in myDic.values():
    for j in i.values():
        print(j)
        break


D = {
    'emp1': {'name': 'Bob', 'job': 'Mgr'},
    'emp2': {'name': 'Kim', 'job': 'Dev'},
    'emp3': {'name': 'Sam', 'job': 'Cod'},
    'emp4': {'name': 'Hun', 'job': 'Dev'},
    'emp5': {'name': 'Jin', 'job': 'Hr'},
    'emp6': {'name': 'Pin', 'job': 'Mgr'},
    'emp7': {'name': 'Sam', 'job': 'Mgr'},
    'emp8': {'name': 'Bob', 'job': 'Dev'},
}
names=[]
hodims=[]
jobs=[]
names.append()
for i["name"] not in :
    hodims.append(i["name"])
    jobs.append(i["job"])
s=0

        
    
print(hodims)
print(jobs)
                  
                  
sampleDic={"class":{"student":{"name":"mike","marks":{"physics":70,"history":80}}}}

for i in sampleDic.values():
    for j in i.values():
        for k in range(len(j.values()),1,-1):
            print(j[k].values())
            
  '''
'''
# lesson8 dictionary
# example_1
d={"num1":3,
   "num2":9,
   "num3":2,
   "num4":5}

a=sorted(d.values())
print(a)

# example_2
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)

# example_3
n=8
d={}
for i in range(1,n+1):
    d[i]=i**2
print(d)

# example_4
s=0
d1 = {'a': 100, 'b': 200, 'c':300}
for i in d1.values():
    s+=i
print(s)

# example_5
d1 = {'a': 100, 'b': 200, 'c':300}
a=max(d1.values())
print(a)

# example_6
d1 = {'a': 100, 'b': 200, 'c':300}
a=min(d1.values())
print(a)

# example_7
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 200, 'b': 200, 'd':400}


result_dict = {}

for key, value in d1.items():
    result_dict[key] = result_dict.get(key, 0) + value
for key, value in d2.items():
    result_dict[key] = result_dict.get(key, 0) + value

print(result_dict)

# example_8
m=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
m1=[]
m2={}
for i in range(len(m)):
   
    m2.update(m[i])
        
for j in m2:
    print(m2[j])


# example_9
n = input("So'zni kiriting: ")
a = {}
for i in n:
    a[i] = a.get(i, 0) + 1

for key, value in a.items():
    print(f"{key} {value} ta")

# example_10
a="mexanizasiyalashtirilganmi"
s={}
s1=0
for i in a:
    s[i]=s.get(i,0)+1
    
for key, value in s.items():
   
    s1=max( s.values())
    print(f"{key}  {value} ta")

for key,value in s.items():
    if s1==value:
        print(f"{key}  {value}")


# m_1
keys=["ten","twenty","thirty"]
value=[10,20,30]
d={}
for i in range(len(keys)):
    d[keys[i]]=value[i]  
print(d)

n=int(input("n = "))
for i in d.values():
    if i==n:
        print("son bor")
        break
    else:
        print("yoq")
        break
   '''
    



    
    


            
       
                    


    
    
    
           

    


    
    
    
       

    
