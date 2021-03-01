DROP DATABASE IF EXISTS MFF_Base;
CREATE DATABASE MFF_Base;
USE MFF_Base;


-- 0. Юзеры(клубы,тренеры,руководители, врачи и т.д.)
-- 
-- 1.Клубы
-- название
-- кратное название
-- ОПФ
-- ИНН
-- ОГРН
-- КПП
-- руководитель
-- тренеры
-- аттестационный статус
-- 
-- 2.Аттестация
-- клуб
-- заявления
-- учредительные документы
-- стадион
-- документы на стадион
-- 
-- 
-- 3. КДК
-- юзер
-- дела
-- санкция
-- дата
-- решение
-- 
-- 4.КДЭ
-- юзер
-- дела
-- санкция
-- дата
-- решение
-- 
-- 5.Штат клуба
-- лицензия
-- 
-- 
-- 6. Стадионы
-- название
-- кратное название
-- ОПФ
-- ИНН
-- ОГРН
-- КПП
-- руководитель
-- тренеры
-- аттестационный статус



DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    users_type VARCHAR(255),
    created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP
    ) COMMENT 'Общая таблица юзеров';
   
-- delimiter // 
-- drop trigger if exists auto_add//
-- CREATE TRIGGER auto_add after insert ON users
-- FOR each row 
-- begin
-- 	if new.users_type = 'Клуб'
-- 		then INSERT INTO clubs (club_id) VALUES (new.id);
-- 		INSERT INTO attestation (club_id) VALUES (new.id);		
--   	end if;
-- END//
-- delimiter ;
   
DROP TABLE IF EXISTS clubs;
CREATE TABLE clubs (
	club_id BIGINT UNSIGNED NOT NULL,
	name VARCHAR(255),
	phone VARCHAR(255),
	email VARCHAR(255),
	shrt_name VARCHAR(255),
	o_p_f VARCHAR(255),
	jur_addr VARCHAR(255),
	fact_addr VARCHAR(255),
	site VARCHAR(255),
	inn VARCHAR(255),
	kpp VARCHAR(255),
	okpo VARCHAR(255),
	ogrn VARCHAR(255),
	bank_name VARCHAR(255),
	cor_ac VARCHAR(255),
	check_ac VARCHAR(255),
	bik VARCHAR(255),
	ustav VARCHAR(255),
	reg_in_min_just VARCHAR(255),
	reg_in_tax VARCHAR(255),
	creat_club VARCHAR(255),
	creat_rucovod VARCHAR(255),
	ofice VARCHAR(255),
    first_registration DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (club_id) REFERENCES users(id)
    ) COMMENT 'профили Клубов';
   
DROP TABLE IF EXISTS club_state;
CREATE TABLE club_state (
	user_id BIGINT UNSIGNED NOT null,
	club_id BIGINT UNSIGNED NOT NULL,
	name VARCHAR(255),
	phone VARCHAR(255),
	email VARCHAR(255),
	second_name VARCHAR(255),
	patrom VARCHAR(255),
	name_of_state VARCHAR(255),
	doc_of_study VARCHAR(255),
	licence VARCHAR(255),
    first_registration DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (user_id) REFERENCES users(id),
	FOREIGN KEY (club_id) REFERENCES clubs(club_id)
	
    ) COMMENT 'Штат Клуба';
   

-- --
-- --DROP TABLE IF EXISTS attestation;
-- --CREATE TABLE attestation (
-- --	id  BIGINT UNSIGNED NOT NULL unique AUTO_INCREMENT,
-- --	club_id BIGINT UNSIGNED NOT NULL,
-- --	`year` int default DATE_FORMAT(NOW(), "%Y"), 
-- --	status tinyint default '0',
-- ---- 	stadium_status tinyint default '0',
-- --	FOREIGN KEY (club_id) REFERENCES users(id)
-- --    ) COMMENT 'Аттестация статус';
-- --
-- --
-- --DROP TABLE IF EXISTS attestation_docs;
-- --CREATE TABLE attestation_docs (
-- --	id  BIGINT UNSIGNED NOT NULL,
-- --	application_1 tinyint default '0' COMMENT 'Заявление о процедуре аттестации',
-- --	application_2 tinyint default '0'COMMENT 'О проведении политики ',
-- --	application_3 tinyint default '0'COMMENT 'Соблюдение регламентов',
-- --	application_4 tinyint default '0'COMMENT 'Список сотрудников',
-- --	application_5 tinyint default '0'COMMENT 'Гарантийное письмо',
-- --	charter tinyint default '0' COMMENT 'Устав',
-- --	p_cr_sc tinyint default '0' COMMENT 'Протокол о создании школы',
-- --	p_el_head tinyint default '0' COMMENT 'Протокол о назначении директора',
-- --	reg_in_tax tinyint default '0' COMMENT 'Регистрация в налоговой',
-- --	reg_in_MJ tinyint default '0' COMMENT 'Регистрация в Мин Юсте',
-- --	FOREIGN KEY (id) REFERENCES attestation(id),
-- --    ) COMMENT 'Документы для аттестации';
-- --   
-- ---- delimiter // 
-- ---- drop trigger if exists auto_chanch_status//
-- ---- CREATE TRIGGER auto_chanch_status after insert ON attestation_docs
-- ---- FOR each row 
-- ---- begin
-- ---- 	if 	application_1 = '1' AND application_2='1' AND application_3='1' AND application_4='1' AND application_5='1'
-- ---- 		charter='1' and p_cr_sc='1' and p_el_head='1' and reg_in_tax='1' and reg_in_MJ='1'
-- ---- 			then UPDATE attestation SET status = '1' WHERE attestation_docs.id=attestation.id;	
-- ----   	end if;
-- ---- END//
-- ---- delimiter ;
-- --   
-- --DROP TABLE IF EXISTS stadiums;
-- --CREATE TABLE stadiums (
-- --	id  BIGINT UNSIGNED NOT NULL unique AUTO_INCREMENT,
-- --	name VARCHAR(255),
-- --	in__Reg_stad tinyint default '0' COMMENT 'В реестре объектов спорта',
-- --	conf_in_expluatation tinyint default '0' COMMENT 'Введен в эксплуатацию',
-- --	instr_pub_order tinyint default '0' COMMENT 'Инструкция по обеспечению безопасности',
-- --	instr_pub_order_date_until Date,
-- --	act_categ tinyint default '0' COMMENT 'Акт обследования и категорирования',
-- --	act_categ_date_until Date,
-- --	statd_plan tinyint default '0' COMMENT 'План стадиона',
-- --    ) COMMENT 'Стадион';
-- --    
-- --DROP TABLE IF EXISTS club_stadium;
-- --CREATE TABLE club_stadium (
-- --	id BIGINT UNSIGNED NOT NULL unique AUTO_INCREMENT,
-- --	club_id  BIGINT UNSIGNED NOT NULL,
-- --	stad_id BIGINT UNSIGNED NOT NULL,
-- --	cntr_on_stad tinyint default '0' COMMENT 'Контракт на стадион',
-- --	cntr_on_stad_date_until date,
-- --	FOREIGN KEY (club_id) REFERENCES clubs(club_id),
-- --	FOREIGN KEY (stad_id) REFERENCES stadiums(id),
-- --    ) COMMENT 'Стадион';
-- --
-- ---- drop procedure if exists update_club_stadium;
-- ---- delimiter //
-- ---- create procedure update_club_stadium()
-- ---- begin
-- ---- 	set i=select count(id) from club_stadium
-- ---- 	declare c INT DEFAULT 1;
-- ---- 	WHILE c<i DO
-- ---- 		if (select cntr_on_stad_date_until from club_stadium where id=c)<NOW()
-- ---- 		then UPDATE club_stadium SET cntr_on_stad = '0' WHERE id=c
-- ---- 		END IF;
-- ---- 	SET c=c+1;
-- ---- 	END WHILE;
-- ---- END// 
-- ---- delimiter ;    
-- ----    
-- ----    
-- ---- DELIMITER // 
-- ---- DROP EVENT IF EXISTS update_club_stadium// 
-- ---- CREATE EVENT update_club_stadium
-- ---- ON SCHEDULE EVERY 1 DAY STARTS '2021-02-18 00:00:00'
-- ---- ON COMPLETION PRESERVE ENABLE 
-- ---- DO
-- ---- 	CALL update_club_stadium ()//
-- ---- END// 
-- ---- DELIMITER ; 
-- ----     
