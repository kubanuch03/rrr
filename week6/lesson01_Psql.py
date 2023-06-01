#postgreSQL

# https://sql.toad.cz/?keyword=default


#===================================
# sudo -u postgres psql = вход
# \l = все БД
# \c restoran = переходит на БД
# \d = все таблицы
# \dt = все таблицы
# \d category = свойства category
# \c postgres = выход
# 
# 
# 


#===================================

# CREATE DATABASE restoran;
# CREATE TABLE category(id serial primary key,name varchar(50)); = задаем тип 
# CREATE TABLE menu(id serial primary key,name varchar(100));
# INSERT INTO category(name) VALUES('vtoroe'),('myasnoe'),('rubnoe'),('salat');
# SELECT * FROM category;
# create table food(id serial primary key,name varchar(250),price integer,id_category int,id_menu int, foreign key (id_category)references category (id),foreign key (id_menu) references menu (id));
# SELECT * from menu;
# SELECT name,price from food
# SELECT name as title,price from food;
# SELECT * from food WHERE id_menu=1;
# SELECT COUNT(*) from food where id_menu=2;
# SELECT 3+5
# SELECT CURRENT_TIMESTAMP;
# ALTER TABLE food RENAME COLUMN id_catedory to id_category;
# ALTER TABLE food DROP COLUMN id_menu;
# ALTER TABLE food ADD COLUMN id_menu INT FOREIGN KEY menu (id);
# ALTER TABLE food ADD COLUMN id_menu INT;
# ALTER TABLE food ADD CONSTRAINT menu_id FOREIGN KEY (id_menu) REFERENCES menu(id);
# select max (price) from food;
# select avg (price) from food;
# select min (price) from food;
# drop table megacom;
# CREATE TABLE employee(id serial primary key,first_name varchar(50),name varchar (50),addres varchar(50),phone_number varchar(50), salary varchar(50), department_id int, position_id int); 
# select  distinct (employee.first_name) from employee; = delete duplicate
# ORDER BY = сортировка 
# UPDATE employee SET age = 25; = редактировать запись
# UPDATE employee SET age = 25 where id in (1,2,3); = редактировать запись
# select * from employee where salary =56000 or department_id = 1;
# select * from employee where name LIKE '%a'; = последнее а
# select * from employee where salary:: text LIKE '__6___'; = последнее а
# SELECT name, SUM(salary) FROM employee GROUP BY name;
# SELECT name, SUM(salary) FROM employee GROUP BY name HAVING COUNT (nme)<2;
# 
# 
# select e.id, e.first_name, e.name, d.title AS position FROM employee as e 
# INNER JOIN position as d on e.position_id=d.id ORDER BY ID;


# select e.id, e.first_name, e.name, d.title AS department, p.title as position FROM employee as e 
# INNER JOIN position as p on e.position_id=p.id INNER JOIN department as d ON e.department_id=d.id;
# 
'''
insert into new_employee01(first_name,last_name,department,title,title)select e.first_name, e.last_name,d.title as department ,p.title as position from employee as e JOIN department d ON e.department_id=d.id JOIN position p ON e.Position_id=p.id ;


select * from employee where salary BETWEEN 30000 and 70000;




select * from employee where first_name LIKE '% (SELECT title from department whereid =1)%';



create FUNCTION summ_five() returns integer as 'select 5+5 as result;' language sql;
create FUNCTION update_pos() returns integer as $$ update position set title=x where id = 1; select 1 $$ language sql;
create FUNCTION multiple_two(food) returns integer as 'select $1.price*2;' LANGUAGE SQL;
'''



