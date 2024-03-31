import psycopg2
from prettytable import PrettyTable
conn = psycopg2.connect(dbname='najottalim', host='localhost', port='5432', user='postgres', password='Samandar2004')
curr = conn.cursor()

"TABLE YARATISH"
"""def create_table(table_name):
    try:
        curr.execute(f"CREATE TABLE {table_name}(id serial primary key)")
    except Exception:
        print('Buanqa table mavjud!')
    else:
        print('Yaratildi')
create_table('')    """    

"TABLE OCHIRISH"
def drop_table(table_name):
    try:
        curr.execute(f"DROP TABLE {table_name}")
    except Exception:
        print('Buanqa table mavjud emas!')
    else:
        print('Ochirildi')
#drop_table('person')

"USTUN QOSHISH"
def add_column(table_name, column_name, data_type, exc=''):
    try:
        curr.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} {data_type} {exc}")
    except Exception as e:
        print(f'Xato malumot kiritildi!\n{e}')
    else:
        print('Done')
#add_column('person3', 'phones', 'VARCHAR(15)')
        
"USTUN OCHIRISH"
def drop_column(table_name,column_name):
    try:
        curr.execute(f"ALTER TABLE {table_name} DROP COLUMN {column_name}")   
    except Exception:
        print('column mavjud emas')
    else:
        print('column ochirildi') 
#drop_column('person2','phone')   

"USTUN OZGARTRISH"
def Change_Column_Name(table_name,old_column_name,new_column_name):
    try:
        curr.execute(f"ALTER TABLE {table_name} RENAME COLUMN {old_column_name} TO {new_column_name}")   
    except Exception:
        print('column ozgarmadi')
    else:
        print('column ozgartirildi') 
#Change_Column_Name('person3','phones','telefon')  


"USTUNNI TYPINI OZGARTIRISH"
def Change_Column_Type(table_name,column_name,data_type1):
    try:
        curr.execute(f"ALTER TABLE {table_name} ALTER COLUMN {column_name} TYPE {data_type1}")   
    except Exception:
        print('column DATA_TYPE ozgarmadi')
    else:
        print('column  DATA_TYPE ozgartirildi')  
#Change_Column_Type('person3','telefon','varchar(30)')                


"MALUMOT QOSHISH"
def insert_data(table_name, data):
    try:
        postgres_insert_query = f"INSERT INTO {table_name} (id, telefon) VALUES (1,'redmi');"
        curr.execute(postgres_insert_query, data)
        print("Ma'lumot muvaffaqiyatli kiritildi")

    except (Exception, psycopg2.Error) as error:
        print("Xatolik bor: ", error)

    else:
        print("insert qoshildi")    
data_to_insert = ('value1', 'value2', 'value3',)
#insert_data('person3', data_to_insert)


"UPDATE QILISH"
def Update1(table_name,column_name,value5):
    try:
        curr.execute(f"UPDATE {table_name} SET {column_name} = '{value5}' ")   
    except Exception:
        print('update bolmadi')
    else:
        print('UPDATE')  
#Update1('person3','telefon','samsung')        


"TABLE NI NOMINI OZGARTIRISH"
def Rename_Table(old_table_name,new_table_name):
    try:
        curr.execute(f"ALTER TABLE {old_table_name} RENAME TO {new_table_name}")   
    except Exception:
        print('table ozgarmadi')
    else:
        print('RENAME Qilindi')  
#Rename_Table('person3','person4')  


" like function"
def like_function(table_name,name):
    try:
        curr.execute(f"Select * from {table_name} WHERE {name} LIKE 'A%'")
    except Exception:
        print("ERROR!!!")
    else:
        print("✅")
#like_function('person3',)                


def insert1(t_name):
    curr.execute(f"select *from {t_name}")
    c_name=[i[0] for i in curr.description]
    input_data=[input(f"{i} kirit = ") for i in c_name]
    curr.execute(f"insert into {t_name} values {tuple(input_data)}")
#insert1("person1")    
    





"select"
#curr.execute(f"select *from person1")
#print(curr.fetchall())    hamma malumotni chiqaradi
#print(curr.fetchmany(1))  nechi kiritse shuncha malumot chiqaradi
#print(curr.fetchone())    1ta malumot chiqaradi



def select_pretty(table_name):
    table1=PrettyTable
    curr.execute(f"select *from {table_name}")
    data=curr.fetchall()
    table1.field_names([i[0] for i in curr.description])
    table1.add_rows(data)
    return table1
#select_pretty('person1')    














# 2-misol
def file_insert(table_name):
    curr.execute(f"select *from {table_name}")
    c=[i for i in curr]
    with open("files.txt", "w") as file:
        for line in c:
            file.write(str(line) + "\n")
#file_insert('cars')    





# 3-misol
def file_insert_table(table_name, file_name):
    with open(file_name, "r") as file:
        data = file.readlines()

   # c_names = data[0].strip().split('\t') 
    for line in data: 
        values = tuple(line.strip().split()) 
        query = f"INSERT INTO {table_name} (name,age,city) VALUES {values}"
        curr.execute(query)
#file_insert_table('file2', 'file2.txt')
            


#4-misol
def insert(t_name):
    curr.execute(f"select *from {t_name}")
    c_name=[i[0] for i in curr.description]
    input_data=[input(f"{i} kirit = ") for i in c_name]
    curr.execute(f"insert into {t_name} values {tuple(input_data)}")
#insert("cars")    
    


# name va color kiritilgan malumotni chiqarish
"""table=PrettyTable()    
def exmple1(table_name,column_name):
    try:
        curr.execute(f"select *from {table_name} where {column_name}='Town Car'")
        a=curr.fetchall()
    except Exception:
        print("bunday malumot topilmadi")
    else:
        print(curr.fetchall())
exmple1("cars","car_name")                    




conn.commit()
conn.close()

"""





def users_txt( txt_filename):
    try:
        curr.execute("SELECT country, COUNT(*) AS user_counts FROM userr GROUP BY country ORDER BY country;")
        user_counts = curr.fetchall()

        with open(txt_filename, "w") as file:
            for country, count in user_counts:
                file.write(f"{country}: {count}\n")
        
        print(f"Ma'lumot TXT fayliga yozld: {txt_filename}")
    except psycopg2.Error as e:
        print("Xato ro'y berdi:", e)
    else:
        print('bajarildi')    
#txt_filename = input("TXT fayl nomi: ")

#users_txt(txt_filename)


import psycopg2

def delete_user(user_id):
    try:
        curr.execute(f"SELECT * FROM userr WHERE id = {user_id};")
        user = curr.fetchone()

        if user:
            curr.execute(f"DELETE FROM userr WHERE id = {user_id};")
            conn.commit()
            print(" o'chirildi")
        else:
            print("foydlamvchi yoq")
    except psycopg2.Error as e:
        print("Xato ro'y berdi:", e)

user_id = input("delet id kiriting ")
delete_user(user_id)

