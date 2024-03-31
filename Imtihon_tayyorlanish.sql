-- POSTGRES DATABASES

--:  1-example: distinct-(unikal) dublicat qiladi;
SELECT distinct car_name,price FROM cars
WHERE color='Black';

--: 2-example: ORDER BY (Sort qilish) Osish yoki kamayish yoki alifbo tartibida
SELECT * FROM cars
WHERE color='Blue'
ORDER BY year Desc;

--: 3-example: LIMIT-(bu kesib olish) 
SELECT *from cars
WHERE year='2000'
LIMIT 10;

--: 4-example: LIKE(biror qiymat bilan boshlanadgan yoki tugaydigan)
SELECT * from cars
WHERE car_name LIKE 'A%';

--: 5-example: IN-(ichida bor yoqligini tekshiradi) - bir vaqtta bir nechta shartni tekshiradi;
SELECT * from cars
WHERE car_name in('GX','Camry Solara','A5','X6 M');

--: 6-example: BETWEEN-(orasida degani) 
SELECT *from cars
WHERE year BETWEEN '1990' and '2020'  ORDER by price;

--: 7-example: JOINS (birlashtirish) INNER JOIN
SELECT cars.car_name,cars.price,avto.car_name,avto.price from cars
INNER JOIN avto ON cars.year=avto.year
WHERE cars.car_name LIKE 'A%' and avto.car_name LIKE 'A%' 
LIMIT 30;

--: 8-example: LEFT JOIN
SELECT * FROM cars
LEFT JOIN avto ON cars.id=avto.id
LIMIT 20;

--: 9-example: RIGHT JOIN 
SELECT cars.id,cars.car_name,avto.car_name FROM cars
RIGHT JOIN avto ON cars.car_name=avto.car_name
LIMIT 20;

--: 10-example FULL JOIN-()
SELECT FROM cars
FULL JOIN avto ON cars.price=avto.car_name
LIMIT 10;








