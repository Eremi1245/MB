--  INSERT INTO users (id,users_type) VALUES (1,'�������'),(2,'����');
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
CREATE OR REPLACE VIEW info_about_all_users as 
select a.id,
(case when a.users_type='����' then b.shrt_name else c.shrt_name end) name
from users a left join clubs b on a.id=b.club_id 
left join stadiums c on a.id=c.stad_id ;

-- CREATE OR REPLACE VIEW info_about_all_users as 
-- select a.id,
-- (case when a.users_type !='����' then c.shrt_name  end) name
-- from users a join stadiums c on a.id=c.stad_id ;

select * from info_about_all_users;