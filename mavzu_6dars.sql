"""CREATE TABLE auther(
    id bigserial PRIMARY KEY,
    name VARCHAR(64),
    age SMALLINT
);
CREATE TABLE books(
    id bigserial PRIMARY KEY,
    name VARCHAR(64),
    page SMALLINT,
    price INT
);
CREATE TABLE userss(
    id bigserial PRIMARY KEY,
    name VARCHAR(64),
    email VARCHAR(128)
);
CREATE TABLE reviews(
    id bigserial PRIMARY KEY,
    body VARCHAR(64),
    star_sivon SMALLINT,
    user_id bigint REFERENCES users(id)
);

CREATE TABLE book_auther(
    id bigserial PRIMARY KEY,
    books_id bigint REFERENCES books(id),
    auther_id bigint REFERENCES auther(id)
);
CREATE TABLE savdo_n1(
    id bigserial PRIMARY KEY,
    books_auther_id bigint REFERENCES book_auther(id),
    users_id bigint REFERENCES users(id)
);

INSERT INTO auther(id,name, age) VALUES
(1,'geron',19),
(2,'otkir hoshimov',20),
(3,'pushkin',22);

INSERT INTO books(id,name,page,price) VALUES
(1,'matem',200,10),
(2,'oqish',120,15),
(3,'english',150,20);

INSERT INTO users(id,name,email) VALUES
(1,'ali','ali12@gmail.com'),
(2,'sarvar','sarvar12@gmail.com'),
(3,'nodir','nodir32@gmail.com');

INSERT INTO reviews(id,body,star_sivon,user_id) VALUES
(1,'yaxshi',4,6),
(2,'yomon',1,7),
(3,'alo',5,8);

INSERT INTO book_auther(id,books_id,auther_id) VALUES
(1,2,3),
(2,1,2),
(3,2,1);

INSERT INTO savdo_n1(id,books_auther_id,users_id) VALUES
(1,2,4),
(2,1,5),
(3,2,6);
"""


CREATE DATABASE maktab;
CREATE TABLE teachers(
    id bigserial PRIMARY KEY,
    name VARCHAR(64),
    specialty_fan VARCHAR(64));
CREATE TABLE students(
    id bigserial PRIMARY KEY,
    name VARCHAR(64),
    course SMALLINT);
CREATE TABLE groups(
    id bigserial PRIMARY KEY,
    name VARCHAR(64),
    student_id bigint REFERENCES students(id));
CREATE TABLE dars_jadvali(
    id bigserial PRIMARY KEY,
    student_id bigint REFERENCES groups(id),
    teachers_id bigint REFERENCES teachers(id),
    fan_name VARCHAR(255));
CREATE TABLE hafta_kun(
    id bigserial PRIMARY KEY,
    week_name VARCHAR(64),
    jadval_id bigint REFERENCES dars_jadvali(id));
INSERT INTO teachers(id,name,specialty_fan) VALUES
(1,'Xolmominov Yusuf','web dasturlash'),
(2,'olimov Sarvar','dasturlash'),
(3,'nosirov ali','fizika'),
(4,'malikov sardor','matematika');
INSERT INTO students(id,name,course) VALUES
(1,'Sardor',2),
(2,'diyor',1),
(4,'umid',3),
(3,'ali',4);
INSERT INTO groups(id,name,student_id) VALUES
(1,'130-22',3),
(2,'140-22',1),
(3,'830-21',4),
(4,'710-21',2);
INSERT INTO dars_jadvali(id,student_id,teachers_id,fan_name) VALUES
(1,1,4,'Matematika'),
(2,2,3,'fizika'),
(3,4,2,'dasturlash'),
(4,3,1,'web dasturlash');

INSERT INTO hafta_kun(id,week_name,jadval_id) VALUES
(1,'Dushanba',1),
(2,'Seshanba',3),
(3,'chorshanba',2),
(4,'payshanba',4);

CREATE DATABASE apteka;
CREATE TABLE users(
    id bigserial PRIMARY KEY,
    name VARCHAR(64));
CREATE TABLE sotuvchi(
    id bigserial PRIMARY KEY,
    name VARCHAR(64),
    level bigint);
CREATE TABLE dori(
    id bigserial PRIMARY KEY,
    name VARCHAR(64),
    muddat VARCHAR(128),
    narx bigint,
    user_id bigint REFERENCES users(id));
CREATE TABLE dorixona(
    id bigserial PRIMARY KEY,
    location VARCHAR(64),
    dori_id bigint REFERENCES dori(id),
    sotuvchi_id bigint REFERENCES sotuvchi(id)
);
INSERT INTO users(id,name) VALUES
(1,'sarvar'),
(2,'azim'),
(3,'diyor'),
(4,'begzod');
INSERT INTO sotuvchi(id,name,level) VALUES
(1,'dilshod',4),
(2,'farhod',5),
(3,'ali',3),
(4,'zafar',5);
INSERT INTO dori(id,name,muddat,narx,user_id) VALUES
(1,'Trimol','01/01/2024-01/06/2024',10000,2),
(2,'Taylolxot','10/01/2024-10/06/2025',15000,1),
(3,'Parasetamol','01/10/2024-01/02/2025',5000,3),
(4,'lorengosept','01/01/2024-01/06/2024',20000,4);
INSERT INTO dorixona(id,location,dori_id,sotuvchi_id) VALUES
(1,'chilonzor 5kv',2,1),
(2,'yunusobot 19kv',1,4),
(3,'chorsu',3,4),
(4,'olmazor',4,2);






