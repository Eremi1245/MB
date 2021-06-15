--  INSERT INTO users (id,users_type) VALUES (1,'Стадион'),(2,'Клуб');
--  -- 
--  insert into clubs (club_id,name ,phone ,email ,shrt_name ,
--  o_p_f ,jur_addr ,fact_addr ,site,inn ,kpp ,okpo ,ogrn ,bank_name ,
--  cor_ac ,check_ac ,bik,ustav ,reg_in_min_just ,
--  reg_in_tax,creat_club,creat_rucovod,ofice)
--  values (2,'fdsf','fdsf','fdsf','fdsf','fdsf','fdsf','fdsf','fdsf',1234,1234,1234,1234,'dfdfs',1234,1234,1234,
--  1,1,1,1,1,1);
--  
--  insert into stadiums (stad_id ,name ,shrt_name ,o_p_f ,jur_addr ,
--  phone ,site ,email ,inn ,kpp ,okpo ,ogrn,in__Reg_stad ,
--  conf_in_expluatation ,instr_pub_order ,instr_pub_order_date_until ,
--  act_categ,act_categ_date_until ,statd_plan ,category_RFS)
--  values (1,'fsdfs','fsdfs','fsdfs','fsdfs','fsdfs','fsdfs','fsdfs',1234,123,123,123,
--  1,1,1,'2021-06-18',1,'2021-06-18',1,'hgfhf');
--  -- 
--  
--  insert into attestation (club_id,`year`,application_1 ,
--  application_2 ,application_3,application_4 ,
--  application_5 ,stadium ,document)
--  values (2,2020,1,1,1,1,1,1,'contract');
-- 
-- -- 
-- update attestation 
-- set document_until='2021-06-18';
-- CREATE OR REPLACE VIEW info_about_all_users as 
-- select a.id,
-- (case when a.users_type='Клуб' then b.shrt_name else c.shrt_name end) name,
-- (case when a.users_type='Клуб' then b.site else c.site end) site,
-- (case when a.users_type='Клуб' then b.email else c.email end) email,
-- (case when a.users_type='Клуб' then b.club_status else c.status end) status
-- from users a left join clubs b on a.id=b.club_id 
-- left join stadiums c on a.id=c.stad_id ;

-- 
-- select * from info_about_all_users;

-- insert into kdk (date_meeting,notes) values ('2021-06-11',"Пробуем создать заседание");


-- CREATE OR REPLACE VIEW total_club_info as 
-- c.club_id , c.name ,c.shrt_name , c.o_p_f ,c.jur_addr, 
-- c.fact_addr , c.site, c.phone, c.inn , c.kpp ,c.okpo ,c.ogrn from clubs c; 


-- CREATE OR REPLACE VIEW attet_club_info as
-- select a.club_id ,b.`year` , b.att_status ,a.club_status , 
-- b.stadium , b.stadium_status , b.document ,b.document_until ,
-- b.application_1 ,b.application_2 ,b.application_3 ,b.application_4 ,
-- b.application_5 from clubs a left join attestation b on a.club_id = b.club_id ;

select * from attet_club_info;