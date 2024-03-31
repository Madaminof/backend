
import psycopg2

conn = psycopg2.connect(dbname='python_wuth', host='localhost', port='5432', user='postgres', password='Samandar2004')
curr = conn.cursor()

def create_table(table_name):
    try:
     curr.execute('CREATE TABLE {table_name}(id serial primary key, name varchar(20))')
    except Exception:
       print("bunday table bor")
    else:
       print("yaratildi")
create_table('person1')       
     

def drop_table(table_name):
    try:
     curr.execute('DROP TABLE {table_name}')
    except Exception:
       print("bunday table mavjud emas")
    else:
       print("o'chirildi")   
#drop_table('python1')





conn.commit()
conn.close()