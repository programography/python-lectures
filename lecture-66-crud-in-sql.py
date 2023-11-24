show databases;

create database programography;

use programography;


create table ContactUs(Name varchar(50), Email varchar(50), message text);

insert into ContactUs values("hlo", "hlo@gmail.com", "this is hlo text");

show tables;

select * from ContactUs;

update ContactUs set Email = "thisismyemail@gmail.com" where Name = "moriss";

update ContactUs set message = "this is new messsage by update" where Name = "hlo";
-- CRUD-- 


delete from ContactUs where Name = "moriss";


set sql_safe_updates = 0;




