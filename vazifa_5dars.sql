"""CREATE TABLE person(
    id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age SMALLINT
);

CREATE TABLE address(
    id INT PRIMARY KEY,
    vil VARCHAR(50),
    tum VARCHAR(50),
    mfy VARCHAR(50),
    person_id INT,
    FOREIGN KEY (person_id) REFERENCES person(id)
);

INSERT INTO address(id,vil,tum,mfy,person_id) values
(11,'Fargona','beshariq','xonobod',10),
(6,'andijon','shahrixon','poloxon',7);

INSERT INTO person(id,first_name,last_name,age) VALUES
(7,'Sardor','aliyev',23),
(10,'jamshid','suyunov',18);
"""

'2-misol'

'1-addres tatble yaratamz
 2-pochta_index table yaratamz
 3- school table yaratamz
 4- asosiy person table '


 CREATE TABLE address1 (
    id bigserial PRIMARY KEY,
    vil VARCHAR(64),
    tum VARCHAR(64),
    mfy VARCHAR(64),
    uy bigint);
CREATE TABLE pochta_index1 (
    id bigserial PRIMARY KEY,
    pochta_code bigint);
CREATE TABLE school1 (
    id bigserial PRIMARY KEY,
    name VARCHAR(64),
    address VARCHAR(64),
    type_school VARCHAR(64));
CREATE TABLE person1 (
    id bigserial PRIMARY KEY,
    name VARCHAR(64),
    age SERIAL,
    addres_index1 bigint,
    addres_id bigint,
    school_id bigint,
    CONSTRAINT fk_addres_index1 FOREIGN KEY (addres_index1) REFERENCES pochta_index1(id),
    CONSTRAINT fk_addres_id FOREIGN KEY (addres_id) REFERENCES address1(id),
    CONSTRAINT fk_school_id FOREIGN KEY (school_id) REFERENCES school1(id)
);
INSERT INTO address1(id,vil,tum,mfy,uy) VALUES
(1,'Fargona','beshariq','xonobod',234),
(2,'andijon','shahrixon','poloxon',121),
(3,'namangan','pop','xojabod',10),
(4,'Toshkent','yunusobot','amur temur',105);

INSERT INTO pochta_index1(id,pochta_code) VALUES
(2,25743),(3,5743),(4,28643);

INSERT INTO school1(id,name,address,type_school) VALUES
(2,'8-maktab','fargona','orta talim'),
(3,'33-maktab','andijon','litsey'),
(1,'121-maktab','toshkent','xususiy');

INSERT INTO person1(id,name,age,addres_index1,addres_id,school_id) VALUES
(1,'Samandar',19,2,4,2),
(2,'Abbos',20,3,2,3),
(3,'Donyor',18,4,1,1);



CREATE TABLE user(
    id bigserial PRIMARY KEY,
    name varchar(30),
    age bigint,
    country varchar(30)
);
INSERT INTO userr(id,name,age,country) VALUES
(1,'ali',20,'newyork'),
(2,'salim',19,'washinton'),
(3,'ali',32,'toshkent'),
(4,'salim',12,'fargona'),
(5,'ali',17,'andijon'),
(6,'salim',12,'qarshi');


INSERT INTO shoes(id,name,price) VALUES
(1,'nike',25),
(2,'zara',15),
(3,'adidas',30);


INSERT INTO savdo(id,user_id,p_id) VALUES
(1,2,3),
(2,3,1),
(3,2,1);


import csv
import psycopg2

def user_csv(database_name, csv_filename):
    try:
      

     
        cursor.execute("SELECT * FROM users ORDER BY country, id;")
        users = cursor.fetchall()

      
        with open(csv_filename, "w", newline="") as file:
            writer = csv.writer(file)

            # Header qismi yozish
            writer.writerow(["id", "name", "age", "country"])

            # Foydalanuvchilarni yozish
            for user in users:
                writer.writerow(user)
        
        print(f"Ma'lumotlar CSV fayliga yozildi: {csv_filename}")
    except psycopg2.Error as e:
        print("Xato ro'y berdi:", e)
    finally:
        # Ulanishni yopish
        if connection:
            cursor.close()
            connection.close()


database_name = input("Ma'lumotlar bazasining nomini kiriting: ")
csv_filename = input("CSV fayl nomini kiriting: ")

export_users_to_csv(database_name, csv_filename)
