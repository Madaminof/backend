import psycopg2
from prettytable import PrettyTable
conn = psycopg2.connect(dbname='backend', host='localhost', port='5432', user='postgres', password='Samandar2004')
curr = conn.cursor()


# 1-misol
"prettytable orqali table dagi malumotlarni terminalga chiqarish "
def print_table(table_name):
    curr.execute(f"SELECT * FROM {table_name}")
    data = curr.fetchall()
    c_names = [desc[0] for desc in curr.description]
    pt = PrettyTable(c_names)
    for row in data:
        pt.add_row(row)
    print(pt)
#print_table('cars')



# 2-misol
    "tabledagi malumotlarni.txt file ga yozish "
def file_insert(table_name):
    curr.execute(f"select *from {table_name}")
    c=[i for i in curr]
    with open("files.txt", "w") as file:
        for line in c:
            file.write(str(line) + "\n")
#file_insert('cars')    



# 3-misol
".txt file da malumotlar berilgan(name, age, city) shu malumorlarni table yaratib table ichiga joylash"
def file_insert_table(table_name, file_name):
    with open(file_name, "r") as file:
        data = file.readlines()
    for line in data: 
        values = tuple(map(str.strip, line.strip().split(',')))
        sorov = f"INSERT INTO {table_name} (name,age,city) VALUES {values}"
        curr.execute(sorov)
#file_insert_table('file2', 'file2.txt')


#4-misol
"insert funksiyasini qaytadan yozish"
def insert(t_name):
    curr.execute(f"select *from {t_name}")
    c_name=[i[0] for i in curr.description]
    input_data=[input(f"{i} kirit = ") for i in c_name]
    curr.execute(f"insert into {t_name} values {tuple(input_data)}")
#insert("cars")    
    

# 5-misol    
"file dagi malumotlarni prettytable orqali chiqarinig"    

def print_table(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    a='name', 'age', 'city'
    pt = PrettyTable(a)
    
    for i in lines:
        values = i.strip().split(',')
        pt.add_row(values)
    print(pt)
print_table('file2.txt')
    
    
              
        
