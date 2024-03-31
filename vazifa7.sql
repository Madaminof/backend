"""create database n38_sql

create table users(
    id bigserial primary key,
    name varchar(29),
    age int
);
insert into users(name, age) values
('Islombek', 17),
('Azizbek', 18),
('Bekzod', 17);


create table cars(
    id bigserial primary key ,
    model varchar(29),
    make varchar(29),
    price int
);

insert into cars(model, make, price) values
('Nexia2', 'GM', 7000),
('BMW X7', 'BMW', 150000),
('Malibu', 'GM', 35000);


create table savdo(
    id bigserial primary key ,
    users_id bigserial references users(id),
    cars_id bigserial references cars(id)
);

insert into savdo(users_id, cars_id) values
(1, 2),
(3, 1);"""
"""
CREATE TABLE sabject(
    id bigserial primary KEY,
    name VARCHAR(64));
CREATE TABLE group1(
    id bigserial primary KEY,
    name VARCHAR(64));
CREATE TABLE addres(
    id bigserial primary KEY,
    vil VARCHAR(64),
    tum VARCHAR(64),
    mfy VARCHAR(64));
CREATE TABLE imthon_turi(
    id bigserial primary KEY,
    name VARCHAR(64),
    ball bigint);
CREATE TABLE univer(
    id bigserial primary KEY,
    name VARCHAR(64),
    year bigint,
    addres_id5 bigint REFERENCES addres(id));
CREATE TABLE student(
    id bigserial primary KEY,
    name VARCHAR(64),
    age bigint,
    addres_id1 bigint REFERENCES addres(id),
    group_id1 bigint REFERENCES group1(id),
    univer_id1 bigint REFERENCES univer(id));
CREATE TABLE teacher(
    id bigserial primary KEY,
    name VARCHAR(64),
    age bigint,
    addres_id2 bigint REFERENCES addres(id),
    univer_id2 bigint REFERENCES univer(id));
CREATE TABLE dars_jadvali(
    id bigserial primary KEY,
    group_id2 bigint REFERENCES group1(id),
    teacher_id1 bigint REFERENCES teacher(id),
    subject_id1 bigint REFERENCES sabject(id),
    data1 VARCHAR(20),
    hafta_kuni VARCHAR(30));
CREATE TABLE imthon_jadvali(
    id bigserial primary KEY,
    group_id4 bigint REFERENCES group1(id),
    teacher_id2 bigint REFERENCES teacher(id),
    subject_id3 bigint REFERENCES sabject(id),
    data1 VARCHAR(20),
    imthon_turi_id bigint REFERENCES imthon_turi(id));
CREATE TABLE result(
    id bigserial primary KEY,
    imthon_id2 bigint REFERENCES imthon_turi(id),
    ball bigint
);
INSERT INTO sabject(id,name) VALUES
(1,'mat'),
(2,'fiz'),
(3,'englsh');
INSERT INTO addres(id,vil,tum,mfy) VALUES
(1,'far','uchkoprik','beshkapa'),
(2,'tosh','chilonzor','amur temur'),
(3,'anjon','shahrixon','ulugbek');
INSERT INTO group1(id,name) VALUES
(1,'140-22'),
(2,'130-22'),
(3,'230-20');
INSERT INTO imthon_turi(id,name,ball) VALUES
(1,'matem',5),
(2,'fizika',3),
(3,'englsh',4);
INSERT INTO univer(id,name,year,addres_id5) VALUES
(1,'TATU',1955,2),
(2,'FARDU',1978,1),
(3,'MED',1944,3);
INSERT INTO student(id,name,age,addres_id1,group_id1,univer_id1) VALUES
(1,'ali',22,1,1,3),
(2,'sardor',19,2,3,1),
(3,'donyor',21,3,2,1);
INSERT INTO teacher(id,name,age,addres_id2,univer_id2) VALUES
(2,'sarvar',32,2,2),
(1,'diyor',39,1,3),
(3,'vali',41,3,2);
INSERT INTO dars_jadvali(id,group_id2,teacher_id1,subject_id1,data1,hafta_kuni) VALUES
(3,1,2,3,'21/03','dushanba'),
(2,2,1,2,'27/05','seshanba'),
(1,3,3,1,'17/04','chorshanba');
INSERT INTO imthon_jadvali(id,group_id4,teacher_id2,subject_id3,data1,imthon_turi_id) VALUES
(3,2,1,2,'02/06/2024',1),
(2,3,2,1,'05/01/2024',2),
(1,3,3,3,'01/06/2024',3);
insert into result(id,imthon_id2,ball) values
(1,3,5),
(2,2,4),
(3,1,5);


CREATE TABLE course(
    id bigserial PRIMARY KEY,
    name VARCHAR(64)
);
CREATE TABLE student1(
    id bigserial PRIMARY KEY,
    name VARCHAR(64),
    age bigint,
    course_id bigint REFERENCES course(id)
);
INSERT INTO course(id,name) VALUES
(1,'matem'),
(3,'fizika'),
(2,'english'),
(4,'rus tili');


INSERT INTO student1(id,name,age) VALUES
(6,'ali',19),
(7,'bobur',22),
(9,'samandar',13);


SELECT *
FROM student1
LEFT JOIN course ON course.id = student1.course_id
WHERE student1.course_id IS NULL;
"""



"""
CREATE TABLE student(
    id bigserial PRIMARY KEY,
    first_name VARCHAR(64),
    last_name VARCHAR(64),
    age bigint
);

CREATE TABLE sinf(
    id bigserial PRIMARY KEY,
    sinf_name VARCHAR(64),
    student_id bigint REFERENCES student(id)
);



INSERT INTO student(id,first_name,last_name,age) VALUES
(6,'Diyor','aliyev',16),
(2,'Ali','Soliev',12),
(3,'Sarvar','Olimov',17),
(1,'Sanjar','Umarov',19),
(12,'Bobur','Qosimov',15);

INSERT INTO sinf(id,sinf_name,student_id) VALUES
(1,'10-sinf',1),
(3,'6-sinf',6),
(2,'10-sinf',2),
(4,'11-sinf',3),
(5,'8-sinf',12),
(6,'8-sinf',1);"""



CREATE TABLE mevalar1(
    id int PRIMARY KEY,
    name VARCHAR(64)
);

CREATE TABLE mevalar2(
    id int PRIMARY KEY,
    name VARCHAR(64)
);
INSERT INTO mevalar1(id,name) VALUES
(1,'olma'),
(2,'nok'),
(3,'shaftoli'),
(4,'banan');

INSERT INTO mevalar2(id,name) VALUES
(1,'tarvuz'),
(2,'uzum'),
(3,'shaftoli'),
(4,'olma');


INSERT INTO it_e(id,t_name,s_name) VALUES
(6,'Elmurod','Murod'),
(7,'Sanjar','hushnud'),
(8,'bunyod','hurshid'),
(9,'toyir','bobur');



SELECT s.*
FROM student s
LEFT JOIN course c ON s.course_id = c.id AND c.name = 'it'
WHERE c.id IS NULL;





create table english_e(
    id serial primary key,
    t_name varchar (20),
    s_name varchar (20)
);

create table it_e(
    id serial primary key,
    t_name varchar (20),
    s_name varchar (20)
;);


create table ru_e(
    id serial primary key,
    t_name varchar (20),
    s_name varchar (20)
);
SELECT it_e.s_name,english.s_name,ruskiy.s_name
FROM it_e
WHERE s_name NOT IN (SELECT s_name FROM english UNION SELECT s_name FROM ruskiy);

SELECT s_name
FROM it_e
WHERE s_name NOT IN (SELECT s_name FROM english UNION SELECT s_name FROM ruskiy);





-- hamma oquvchilarni chiqarish
select english.s_name, ruskiy. s_name, it_e.s_name 
from english full join ruskiy on ruskiy. s_name=english. s_name 
full join it_e on ruskiy.s_name=it_e.s_name;

-- hamma oqituvchilarni chiqarish
select english.t_name, ruskiy.t_ name, it_e.t_name 
from english full join ruskiy on ruskiy.t_name=english.t_name 
full join it_e on ruskiy.t_name=it e.t_name;

-- oqituvchilar sonini chiqarish
select count(*) from english 
full join ruskiy on ruskiy.t_name=english.t_name 
full join it_e on ruskiy.t_name=it_e.t_name;

-- oquvchilar sonini chiqarish
select count(*) from english 
full join ruskiy on ruskiy.s_name=english.s_name 
full join it_e on ruskiy.s_name=it_e.s_name;

-- it kursiga bormaydiganlari
select english.s_name as english,ruskiy.s_name as ruskiy,it_e.s_name as it
from english full join ruskiy on ruskiy.s_name=english.s_name 
full join it_e on ruskiy.s_name=it_e.s_name
where it_e.s_name is null;

-- english kursiga bormaydiganlari
select english.s_name as english,ruskiy.s_name as ruskiy,it_e.s_name as it
from english full join ruskiy on ruskiy.s_name=english.s_name 
full join it_e on ruskiy.s_name=it_e.s_name
where english.s_name is null;

-- rus tili kursiga bormaydiganlari
select english.s_name as english,ruskiy.s_name as ruskiy,it_e.s_name as it
from english full join ruskiy on ruskiy.s_name=english.s_name 
full join it_e on ruskiy.s_name=it_e.s_name
where ruskiy.s_name is null;


