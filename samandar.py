
import psycopg2
from prettytable import PrettyTable
conn = psycopg2.connect(dbname='najottalim', host='localhost', port='5432', user='postgres', password='Samandar2004')
curr = conn.cursor()
#3 masala
def create_table(table_name):
    try:
        curr.execute(f"CREATE TABLE {table_name}(id serial primary key)")
    except Exception:
        print('Buanqa table mavjud!')
    else:
        print('Yaratildi')
#create_table('tablee')    

def drop_table(table_name):
    try:
        curr.execute(f"DROP TABLE {table_name}")
    except Exception:
        print('Buanqa table mavjud emas!')
    else:
        print('Ochirildi')
#drop_table('tablee')
        



#4 masala

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
#delete_user(user_id)





# 5-masala
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
txt_filename = input("TXT fayl nomi: ")

#users_txt(txt_filename)