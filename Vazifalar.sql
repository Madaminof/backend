'database yaratish'
CREATE DATABASE kampyuter;
'jadval yaratish'
CREATE TABLE noutbook(
    id SERIAL PRIMARY KEY,
    brand VARCHAR(30),
    model VARCHAR(30),
    cpu VARCHAR(30),
    frequency FLOAT,
    ram SMALLINT,
    os VARCHAR(30),
    price INT

);
'malumotlarni kiritish'
INSERT INTO noutbook(id,brand,model,cpu,frequency,ram,os,price) values
(21,'Asus','Zenbook','Intel Core i3',1.8,8,'Windows 10',530),
(22,'Asus','Lenovo','Intel Core i7',2.4,8,'Windows 10',770),
(23,'Asus','Vivobook 14','Intel Core i5',1.8,8,'Windows 10',650),
(24,'Asus','Zenbook 14','Intel Core i7',3.9,8,'Windows 10',700),
(25,'Asus','ASUS TUF','Intel Core i5',2.4,8,'Windows 10',450);


(1,'APPLE','Mackbook pro','M1',3.9,8,'Mackos',1000),
(2,'Apple','Mackbook Air','Intel Core i7',1,8.8,'Mackos',700),
(3,'Asus','Zenbook','Intel Core i5',1.8,4,'Windows 10',500),
(4,'Asus','Lenovo','Intel Core i7',2.4,4,'Windows 10',650),
(5,'Apple','Mackbook Air','Intel Core i5',4.2,16,'Mackos',800),
(6,'Apple','Mackbook Pro','M2',5.1,32,'Mackos',1500),
(7,'Acer','zenbook','Intel Core i3',1.9,4,'Windows 10',400),
(8,'HP','Victus','Intel Core i9',4.8,16,'Windows 11',800),
(9,'HP','Legion','Intel Core i7',2.4,16,'Windows 11',750),
(10,'Apple','Mackbook Pro','M3',5.1,32,'Mackos',2500),
(11,'Asus','Asus TUF Geming','Intel Core i9',3.2,16,'Windows 11',900),
(12,'Apple','Mackbook Pro','M1',4.2,8,'Mackos',1000),
(13,'Asus','Vivobook','Intel Core i5',1.8,8,'Windows 10',650),
(14,'Asus','Zenbook 14','Intel Core i7',3.9,16,'Windows 10',700),
(15,'Asus','Lenovo','Intel Core i7',2.4,4,'Windows 10',450),
(16,'Apple','Mackbook Air','Intel Core i7',3.9,16,'Mackos',500),
(17,'Apple','Mackbook Pro','M1 Pro',5.1,16,'Mackos',1500),
(18,'Acer','zenbook','Intel Core i5',1.8,8,'Windows 10',550),
(19,'HP','Victus','Intel Core i7',4.8,8,'Windows 11',850),
(20,'HP','Legion','Intel Core i9',3.6,16,'Windows 11',650);

'1-misol'
SELECT *
FROM noutbook
WHERE price = (SELECT MAX(price) FROM noutbook);

'2-misol'
SELECT *
FROM noutbook
WHERE price = (SELECT MIN(price) FROM noutbook);

'3-misol'
SELECT frequency
FROM noutbook
WHERE price>=400 and price<=1000 and cpu LIKE 'Intel%';

'4-misol'
SELECT COUNT(*) 
FROM noutbook
WHERE brand='Apple';

'5-misol'
SELECT * FROM noutbook
WHERE os='Windows 10' and ram=8 and brand='Asus' 
ORDER BY price;


'Y3 masala'

CREATE DATABASE universitet;
CREATE TABLE talaba(
    id SERIAL PRIMARY KEY,
    talaba_ismi VARCHAR(64),
    kursi SMALLINT,
    stipendiya INT
);

INSERT INTO talaba(id,talaba_ismi,kursi,stipendiya) values
(1,'Ali',2,550),
(2,'Sardor',1,400),
(3,'Diyor',4,550),
(4,'Javoh',2,650),
(5,'Begzod',4,550),
(6,'Yusuf',1,500),
(7,'Sarvar',3,500),
(8,'Temur',4,800),
(9,'Alijon',2,550),
(10,'Sanjar',1,400);

'1-misol:  har bir kursni 1taga oshiring va 4-kurslarni ochiring'
UPDATE talaba
SET kursi=kursi+1;

DELETE FROM talaba WHERE kursi>=4;

'2-misol har bir kursda nechta talaba borligini aniqlang'

SELECT COUNT(*) as kurs_1
FROM talaba
WHERE kursi=1


SELECT COUNT(*) as kurs_2
FROM talaba
WHERE kursi=2;


SELECT COUNT(*) as kurs_3
FROM talaba
WHERE kursi=3;


SELECT COUNT(*) as kurs_4
FROM talaba
WHERE kursi=4;