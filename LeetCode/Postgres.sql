" \! clear tozalash
  \dt+ (table_name) - tablni xotra joyini korsatadi
"
CREATE DATABASE n38;
CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    name varchar(64),
    lastname varchar(128),
    age SMALLINT DEFAULT 18 ,
    created_AT TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
INSERT INTO users(id,name,lastname,age) values(1,'ali','aliyev',20);


'QUERY lar'
SELECT*FROM users WHERE length(name)>5 and age>=20; 
DELETE *FROM users WHERE length(name)<6 and age>70;















