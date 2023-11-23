show databases;

create database programography;

use programography;


create table ContactUs(Name varchar(50), Email varchar(50), message text);


insert into ContactUs values("moris", "moris@gmail.com", "this is moris message");

update ContactUs set Email = "krissmoris@gmail.com" where Name = "moris";

show tables;

select * from ContactUs;

delete from ContactUs where Name = "kriss";

-- CRUD -- 


SET SQL_SAFE_UPDATES = 0;





