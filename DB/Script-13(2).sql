DROP DATABASE IF EXISTS MFF_Base;
CREATE DATABASE MFF_Base;
USE MFF_Base;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    users_type VARCHAR(255),
    created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP
    ) COMMENT 'Общая таблица юзеров';
   
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
	inn BIGINT,
	kpp BIGINT,
	okpo BIGINT,
	ogrn BIGINT,
	bank_name VARCHAR(255),
	cor_ac BIGINT,
	check_ac BIGINT,
	bik BIGINT,
	ustav tinyint,
	reg_in_min_just tinyint,
	reg_in_tax tinyint,
	creat_club tinyint,
	creat_rucovod tinyint,
	ofice tinyint,
    first_registration DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (club_id) REFERENCES users(id)
    ) COMMENT 'профили Клубов';
    
DROP TABLE IF EXISTS club_state;
CREATE TABLE club_state (
	user_id BIGINT UNSIGNED NOT null,
	club_id BIGINT UNSIGNED NOT NULL,
	name VARCHAR(255),
	second_name VARCHAR(255),
	patrom VARCHAR(255),
	phone VARCHAR(255),
	email VARCHAR(255),
	name_of_state VARCHAR(255),
	doc_of_study tinyint default '0',
	licence VARCHAR(255),
	licence_under date,
    first_registration DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (user_id) REFERENCES users(id),
	FOREIGN KEY (club_id) REFERENCES clubs(club_id)
	
    ) COMMENT 'Штат Клуба';
   
DROP TABLE IF EXISTS stadiums;
CREATE TABLE stadiums (
	stad_id BIGINT UNSIGNED NOT null,
	name VARCHAR(255),
	shrt_name VARCHAR(255),
	o_p_f VARCHAR(255),
	jur_addr VARCHAR(255),
	phone VARCHAR(255),
	site VARCHAR(255),
	email VARCHAR(255),
	inn bigint,
	kpp bigint,
	okpo bigint,
	ogrn bigint,
	in__Reg_stad tinyint default '0' COMMENT 'В реестре объектов спорта',
	conf_in_expluatation tinyint default '0' COMMENT 'Введен в эксплуатацию',
	instr_pub_order tinyint default '0' COMMENT 'Инструкция по обеспечению безопасности',
	instr_pub_order_date_until Date,
	act_categ  tinyint default '0' COMMENT 'Акт обследования и категорирования',
	act_categ_date_until Date,
	statd_plan  tinyint default '0' COMMENT 'План стадиона',
	category_RFS VARCHAR(255) default 'no category',
	status VARCHAR(255) default 'not allowed to compete',
    first_registration DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (stad_id) REFERENCES users(id)
    ) COMMENT 'Стадионы';
    
delimiter // 
drop trigger if exists auto_chanch_status_stad_after_insert//
CREATE TRIGGER auto_chanch_status_stad_after_insert after insert ON stadiums 
FOR each row 
	begin
		if 	in__Reg_stad = '1' AND conf_in_expluatation='1' AND instr_pub_order='1' AND act_categ='1' AND statd_plan='1'
			and instr_pub_order_date_until>now() and act_categ_date_until>now() and category_RFS != 'no category'
		then UPDATE stadiums SET status = 'admitted to the competition';	
		end if;
END//
delimiter ;
