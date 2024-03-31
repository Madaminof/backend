# POSTGRES DATABASES

#  1-example: distinct-(unikal) dublicat qiladi;
import psycopg2
from prettytable import PrettyTable
conn = psycopg2.connect(dbname='backend', host='localhost', port='5432', user='postgres', password='Samandar2004')
curr = conn.cursor()


def delete_user(database_name, user_id):
    try:
        curr.execute(f"SELECT * FROM {database_name} WHERE id = {user_id};")
        user = curr.fetchone()
        if user:
            curr.execute(f"DELETE FROM {database_name} WHERE id = {user_id};")
            conn.commit()
            print("Foydalanuvchi o'chirildi")
        else:
            print("Bu foydalanuvchi yoq")
    except psycopg2.Error as e:
        print("Xato:", e)
    finally:
        if conn:
            curr.close()
            conn.close()

database_name = input("malumot kirting: ")
user_id = input("id kiriting: ")

delete_user(database_name, user_id)
