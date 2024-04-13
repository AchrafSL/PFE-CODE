CREATE SCHEMA DamsoStreamDB;
use DamsoStreamDB;

-- Operations : (insert, delete, update);

create table Client(
idCli integer NOT NULL,	
Email char(60),
Password char(60) ,
FirstName char(32) ,
LastName char(32) ,
status char(30) DEFAULT 'unverified' ,
primary key (idCli)
);

-- Primary Key Set automaticaly 
ALTER TABLE Client MODIFY idCli integer AUTO_INCREMENT; 
ALTER TABLE Client MODIFY Email char(60); 


-- Examples :
-- Insert values into the CLIENT table
INSERT INTO Client (FirstName, LastName, Email,Password) VALUES 
('usr0', '1st','usr0@gmail.com','0000'),
('usr1', '2nd','usr1@gmail.com','1111');

-- Delete values from the CLIENT table 
DELETE FROM client WHERE (`idCli` = '13');
DELETE FROM client WHERE (`idCli` = '14');

-- Update values of the CLIENT table
UPDATE Client SET 
    FirstName = 'NewFirstName',
    LastName = 'NewLastName',
    Email = 'newemail@example.com',
    Password = 'newpassword'
WHERE 
    idCli = 0;

-- and commit after finish
