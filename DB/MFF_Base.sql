 DROP DATABASE IF EXISTS Week_plane;
 CREATE DATABASE Week_plane;
 USE Week_plane;
 
 
 
 DROP TABLE IF EXISTS interests;
 CREATE TABLE interests (
 	id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, 
 	interest Varchar(255),
 	color Varchar(255),
 	created_at DATETIME DEFAULT NOW(),
 	updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP
     ) COMMENT 'Таблица Интересов';
    
 DROP TABLE IF EXISTS goals;
 CREATE TABLE goals (
	id BIGINT UNSIGNED NOT NULL auto_increment unique,
 	interest_id BIGINT UNSIGNED NOT NULL,
	goal VARCHAR(255),
	status ENUM ('Сделано','Не сделано') default 'Не сделано',
        created_at DATETIME DEFAULT NOW(),
 	updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
 	FOREIGN KEY (interest_id) REFERENCES interests(id),
 	INDEX goal (goal)
     ) COMMENT 'Цели интереса';
     
 DROP TABLE IF EXISTS date_interest;
 CREATE TABLE date_interest (
 	id BIGINT UNSIGNED NOT NULL auto_increment unique,
 	interest_id BIGINT UNSIGNED NOT NULL,
	dt DATE,
        created_at DATETIME DEFAULT NOW(),
 	updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
 	FOREIGN KEY (interest_id) REFERENCES interests(id),
 	INDEX dt (dt)
     ) COMMENT 'Дата цель';
     
 INSERT INTO interests(interest,color) VALUES 
 ('Пун-Пун','green'),
 ('Учеба','blue'),
 ('Тренировка','red'),
 ('Игра','yellow');
 
 INSERT INTO goals(interest_id,goal) VALUES 
 (1,'Сходить в кино'),
 (1,'отметить 14 февраля'),
 (2,'Сделать домашку'),
 (3,'Сходить на все тренировки за месяц'),
 (3,'Пойти на ММА'),
 (4,'Найти новую игру');

INSERT INTO date_interest(interest_id,dt) VALUES 
(3,'2021-02-01'),
(4,'2021-02-02'),
(3,'2021-02-04'),
(1,'2021-02-06'),
(2,'2021-02-07');

CREATE OR REPLACE VIEW  inter_goal AS SELECT a.interest , b.goal,b.status from  interests a left join goals b on a.id =b.interest_id ;

select * from inter_goal;

CREATE OR REPLACE VIEW  inter_date AS SELECT b.dt, a.interest from  interests a join date_interest b on a.id=b.interest_id ;

select * from inter_date;