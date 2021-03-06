DROP DATABASE IF EXISTS MFF_Base;
CREATE DATABASE MFF_Base;
USE MFF_Base;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    users_type VARCHAR(255),
    created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP
    ) COMMENT '����� ������� ������';
   
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
	cor_ac VARCHAR(255),
	check_ac VARCHAR(255),
	bik BIGINT,
	ustav tinyint default 0,
	reg_in_min_just tinyint default 0,
	reg_in_tax tinyint default 0,
	creat_club tinyint default 0,
	creat_rucovod tinyint default 0,
	ofice tinyint default 0,
	club_status VARCHAR(255) default 'not allowed to compete',
    first_registration DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (club_id) REFERENCES users(id)
    ) COMMENT '������� ������';
    
delimiter // 
drop trigger if exists club_stat//
CREATE TRIGGER club_stat BEFORE insert ON clubs
FOR each row 
	begin
		if 	new.ustav=1 AND new.reg_in_min_just  = 1 AND new.reg_in_tax=1 AND new.creat_club=1 
		AND new.creat_rucovod=1 and new.ofice = 1
		then SET new.club_status = 'admitted to the competition';	
		end if;
END//
delimiter ;

delimiter // 
drop trigger if exists update_club_stat//
CREATE TRIGGER update_club_stat BEFORE update ON clubs
FOR each row 
	begin
		if 	new.ustav=1 AND new.reg_in_min_just  = 1 AND new.reg_in_tax=1 AND new.creat_club=1 
		AND new.creat_rucovod=1 and new.ofice = 1
		then SET new.club_status = 'admitted to the competition';	
		end if;
END//
delimiter ;
   
CREATE OR REPLACE VIEW total_club_info as 
select c.club_id , c.name ,c.shrt_name , c.o_p_f ,c.jur_addr, 
c.fact_addr , c.site, c.phone, c.inn , c.kpp ,c.okpo ,c.ogrn from clubs c; 


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
    ) COMMENT '���� �����';
   
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
	in__Reg_stad tinyint default 0 COMMENT '� ������� �������� ������',
	conf_in_expluatation tinyint default 0 COMMENT '������ � ������������',
	instr_pub_order tinyint default 0 COMMENT '���������� �� ����������� ������������',
	instr_pub_order_date_until Date,
	act_categ  tinyint default 0 COMMENT '��� ������������ � ���������������',
	act_categ_date_until Date,
	statd_plan  tinyint default 0 COMMENT '���� ��������',
	category_RFS VARCHAR(255) default 'no category',
	status VARCHAR(255) default 'not allowed to compete',
    first_registration DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (stad_id) REFERENCES users(id)
    ) COMMENT '��������';
    
delimiter // 
drop trigger if exists stadium_status//
CREATE TRIGGER stadium_status BEFORE insert ON stadiums
FOR each row 
	begin
		if 	new.in__Reg_stad=1 AND new.conf_in_expluatation  = 1 AND new.instr_pub_order=1 AND new.act_categ=1 
		AND new.statd_plan=1 and new.instr_pub_order_date_until>now() and new.act_categ_date_until>now() 
		and new.category_RFS != 'no category'
		then SET new.status = 'admitted to the competition';	
		end if;
END//
delimiter ;

delimiter // 
drop trigger if exists update_stadium_status//
CREATE TRIGGER update_stadium_status before update ON stadiums
FOR each row 
	begin
		if 	new.in__Reg_stad=1 AND new.conf_in_expluatation  = 1 AND new.instr_pub_order=1 AND new.act_categ=1 
		AND new.statd_plan=1 and new.instr_pub_order_date_until>now() and new.act_categ_date_until>now() 
		and new.category_RFS != 'no category'
		then SET new.status = 'admitted to the competition';	
		end if;
END//
delimiter ;

DROP TABLE IF EXISTS attestation;
CREATE TABLE attestation (
	id  BIGINT UNSIGNED NOT NULL unique AUTO_INCREMENT,
	club_id BIGINT UNSIGNED NOT NULL,
	club_status tinyint default 0 COMMENT '������ ����� ������������� �� �����',
	`year` int,
	application_1 tinyint default 0 COMMENT '��������� � ��������� ����������',
	application_2 tinyint default 0 COMMENT '� ���������� �������� ',
	application_3 tinyint default 0 COMMENT '���������� �����������',
	application_4 tinyint default 0 COMMENT '������ �����������',
	application_5 tinyint default 0 COMMENT '����������� ������',
	stadium BIGINT UNSIGNED NOT NULL,
	stadium_status tinyint default 0 COMMENT '������ �������� ������������� �� ��������',
	document VARCHAR(255) default 'None',
	document_until Date default '0000-00-00',
	att_status tinyint default 0,
	FOREIGN KEY (club_id) REFERENCES clubs(club_id),
	FOREIGN KEY (stadium) REFERENCES stadiums(stad_id)
	) COMMENT '����������';


CREATE OR REPLACE VIEW status_club_info as select club_id,club_status 
from clubs;

CREATE OR REPLACE VIEW status_stad_info as select stad_id,status 
from stadiums;

CREATE OR REPLACE VIEW info_about_all_users as 
select a.id,
(case when a.users_type='����' then b.shrt_name else c.shrt_name end) name,
(case when a.users_type='����' then b.site else c.site end) site,
(case when a.users_type='����' then b.email else c.email end) email,
(case when a.users_type='����' then b.club_status else c.status end) status
from users a left join clubs b on a.id=b.club_id 
left join stadiums c on a.id=c.stad_id;


delimiter // 
drop trigger if exists autofill//
CREATE TRIGGER autofill before insert ON attestation
FOR each row 
	begin
		set @a=new.club_id ;
		set @b=new.stadium;
		if (select club_status from status_club_info where club_id=@a) = 'admitted to the competition' then 
		SET new.club_status = 1;
		end if;
		if (select status from status_stad_info where stad_id=@b) = 'admitted to the competition' then 
		SET new.stadium_status = 1;
		end if;
		if new.club_status=1 and new.application_1=1 and new.application_2=1 and new.application_3=1 and 
		new.application_4 and 
		new.application_5=1 and new.stadium_status=1 and new.document_until>now() then 
		set new.att_status=1;
		end if;
END//
delimiter ;


delimiter // 
drop trigger if exists autofill_2//
CREATE TRIGGER autofill_2 before update ON attestation
FOR each row 
	begin
		if new.club_status=1 and new.application_1=1 and new.application_2=1 and new.application_3=1 and 
		new.application_4 and 
		new.application_5=1 and new.stadium_status=1 and new.document_until>now() then 
		set new.att_status=1;
		end if;
END//
delimiter ;



DROP TABLE IF EXISTS KDK;
CREATE TABLE KDK (
	id  BIGINT UNSIGNED NOT NULL unique AUTO_INCREMENT,
	date_meeting date NOT null unique,
	notes text,
	first_registration DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP
	) COMMENT '���';

-- CREATE INDEX date_meeting ON KDK(date_meeting);


DROP TABLE IF EXISTS Cases;
CREATE TABLE Cases (
	id  BIGINT UNSIGNED NOT NULL unique AUTO_INCREMENT,
	meeting_id BIGINT UNSIGNED NOT NULL,
	date_meeting date NOT null ,
	case_number VARCHAR(255),
	time_meeting time default '12:00:00',
	potential_art VARCHAR(255),
	notes text,
	first_registration DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (meeting_id) REFERENCES KDK(id),
	FOREIGN KEY (date_meeting) REFERENCES KDK(date_meeting)
	) COMMENT '����';

CREATE INDEX case_number ON Cases(case_number);

DROP TABLE IF EXISTS ClubMembersOfMeeting;
CREATE TABLE ClubMembersOfMeeting (
	id  BIGINT UNSIGNED NOT NULL unique AUTO_INCREMENT,
	case_id BIGINT UNSIGNED NOT NULL,
	club_member_id BIGINT UNSIGNED NOT NULL,
	first_registration DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (case_id) REFERENCES Cases(meeting_id),
	FOREIGN KEY (club_member_id) REFERENCES clubs(club_id)
	) COMMENT '��������� ���������';

DROP TABLE IF EXISTS MembersOfMeeting;
CREATE TABLE MembersOfMeeting (
	id  BIGINT UNSIGNED NOT NULL unique AUTO_INCREMENT,
	case_id BIGINT UNSIGNED NOT NULL,
	member_id BIGINT UNSIGNED NOT NULL,
	first_registration DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (case_id) REFERENCES Cases(meeting_id),
	FOREIGN KEY (member_id) REFERENCES club_state(user_id)
	) COMMENT '��������� ���������';


DROP TABLE IF EXISTS Notifications_Cases;
CREATE TABLE Notifications_Cases (
	id  BIGINT UNSIGNED NOT NULL unique AUTO_INCREMENT,
	case_id BIGINT UNSIGNED NOT NULL,
	notification text,
	first_registration DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (case_id) REFERENCES Cases(meeting_id)
	) COMMENT '�����������';


DROP TABLE IF EXISTS Decisions_Cases;
CREATE TABLE Decisions_Cases (
	id  BIGINT UNSIGNED NOT NULL unique AUTO_INCREMENT,
	case_id BIGINT UNSIGNED NOT NULL,
	decision text,
	first_registration DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY (case_id) REFERENCES Cases(meeting_id)
	) COMMENT '�������';
	

CREATE OR REPLACE VIEW attet_club_info as
select a.club_id ,b.`year` , b.att_status ,a.club_status , 
b.stadium , b.stadium_status , b.document ,b.document_until ,
b.application_1 ,b.application_2 ,b.application_3 ,b.application_4 ,
b.application_5 from clubs a left join attestation b on a.club_id = b.club_id ;