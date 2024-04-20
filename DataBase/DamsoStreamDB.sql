
CREATE SCHEMA DamsoStreamDB;
use DamsoStreamDB;

-- Operations : (insert, delete, update);

create table USER(
idCli integer NOT NULL,	
Email char(60),
Password char(60) ,
FirstName char(32) ,
LastName char(32) ,
status char(30) DEFAULT 'unverified' ,
role char(30) DEFAULT 'client',
Date_Joined DATETIME , 
whatsapp char(30),
primary key (idCli)
);

-- Primary Key Set automaticaly 
ALTER TABLE USER MODIFY idCli integer AUTO_INCREMENT; 
ALTER TABLE USER MODIFY Email char(60); 


-- Examples :
-- Insert values into the CLIENT table
INSERT INTO Client (FirstName, LastName, Email,Password) VALUES 
('usr0', '1st','usr0@gmail.com','0000'),
('usr1', '2nd','usr1@gmail.com','1111');

-- Delete values from the CLIENT table 
DELETE FROM USER WHERE (`idCli` = '1');
DELETE FROM USER WHERE (`idCli` = '3');
DELETE FROM USER WHERE (`idCli` = '2');


-- Update values of the CLIENT table
UPDATE Client SET 
    FirstName = 'NewFirstName',
    LastName = 'NewLastName',
    Email = 'newemail@example.com',
    Password = 'newpassword'
WHERE 
    idCli = 0;

-- and commit after finish
