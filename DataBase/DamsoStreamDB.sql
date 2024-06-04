
CREATE SCHEMA DamsoStreamDB;
use DamsoStreamDB;

-- Operations : (insert, delete, update);

-- USER TABLE :
create table USER(
idCli integer NOT NULL AUTO_INCREMENT,	
Email char(60),
Password char(60) ,
FirstName char(32) ,
LastName char(32) ,
status char(30) DEFAULT 'unverified' ,
role char(30) DEFAULT 'client',
Date_Joined DATETIME , 
whatsapp char(30),
pfpName char(255) DEFAULT 'user583abc_1649114257.png',
primary key (idCli)
);


-- OFFERS TABLE :
-- Filled with informations given by the admin (can be edited by the admin in the admin page)
CREATE TABLE OFFERS(
    idOffer INT AUTO_INCREMENT,
    description TEXT,
    image_Name VARCHAR(255) DEFAULT 'default-product-image.png',
    Offer_price DECIMAL(10, 2),
    name VARCHAR(255),
    duration INT,
	PRIMARY KEY (idOffer)
);

-- ALTER TABLE OFFERS
-- ADD COLUMN duration INT;

-- ORDERS TABLE :
-- Filled with information derived from the user's cart
CREATE TABLE Orders (
    idOrder INT AUTO_INCREMENT,
    idCli INT,
    StatOfTreatment VARCHAR(50) DEFAULT 'Pending Treatment',
    PaymentStat VARCHAR(50) DEFAULT 'Pending Payment',
    TotalPrice DECIMAL(10, 2),
    PRIMARY KEY (idOrder),
    FOREIGN KEY (idCli) REFERENCES USER(idCli)
);

-- The list of order offers will be found in the OrderOffers(table) in a form 
-- of rows under the same idOrder

-- OrderOffers :
CREATE TABLE OrderOffers (
    OrderOffers_Id INT AUTO_INCREMENT,
    idOrder INT,
    idOffer INT,
    PRIMARY KEY (OrderOffers_Id),
    FOREIGN KEY (idOrder) REFERENCES Orders(idOrder),
    FOREIGN KEY (idOffer) REFERENCES OfferS(idOffer)
);



-- this table should store offers(selected) temporary and remove data after submiting
-- the data
-- aka filling Order and OrderOffers (after clicking send order in cart page)
-- Cart page vary from every usr 
-- and it's filled with data comming from ( offers page ) 

-- Cart TABLE :
CREATE TABLE CART (
    idCart INT AUTO_INCREMENT PRIMARY KEY,
    idCli INT,
    fullPrice DECIMAL(10, 2),
    FOREIGN KEY (idCli) REFERENCES USER(idCli)
);

-- The list of order offers will be found in the CartOffers(table) in a form 
-- of rows under the same idCart

-- CartOffers TABLE :
CREATE TABLE CartOffers (
    CartOffer_id INT AUTO_INCREMENT ,
    idCart INT,
    idOffer INT,
	PRIMARY KEY (cartOffer_id),
    FOREIGN KEY (idCart) REFERENCES CART(idCart),
    FOREIGN KEY (idOffer) REFERENCES OFFERS(idOffer)
);

-- Subscription TABLE :
CREATE TABLE Subscription (
    idSubscription INT AUTO_INCREMENT,
    idCli INT,
    idOffer INT,
    subscriptionStatus VARCHAR(50) DEFAULT 'Active',
    startDate DATE,
    endDate DATE,
	PRIMARY KEY (idSubscription),
	FOREIGN KEY (idOffer) REFERENCES OFFERS(idOffer),
    FOREIGN KEY (idCli) REFERENCES USER(idCli)
);

-- Comment table :
CREATE TABLE COMMENT (
    idComment integer AUTO_INCREMENT,
    idOffer integer NOT NULL,
    idCli integer NOT NULL,
    comment_TEXT VARCHAR(10000) NOT NULL, -- need to make the usr only write 10 000  char max
    Date_written DATE, -- when inserting a comment
	PRIMARY KEY(idComment),
    FOREIGN KEY (idOffer) REFERENCES offers(idOffer),
    FOREIGN KEY (idCli) REFERENCES user(idCli)
); 

-- Selection par :
SELECT * FROM comment
WHERE idOffer = id
ORDER BY Date_witten DESC
LIMIT 0,100;

-- Insertion :
INSERT INTO COMMENT (idOffer, idCli,comment_TEXT,Date_witten )
VALUES (idOffer_V, idCli_V, commentaire_V, currentDate_V);



-- email or idUSER to update role
UPDATE USER SET role = 'admin' where idCli = 2

 SELECT o.idOrder,o.idCli, o.StatOfTreatment, o.PaymentStat, o.TotalPrice, 
usr.FirstName,usr.LastName, usr.Email, usr.WhatsApp 
 FROM ORDERS o, USER usr 
 WHERE o.idCli = usr.idCli 
 AND o.StatOfTreatment = 'Pending Treatment';
 
 
 



















-- Examples :
-- Values of duration is in DAYS

-- Example 1
INSERT INTO OFFERS (description, Offer_price, name,duration) 
VALUES ('Netflix account offer description', 200, 'Netflix accounts',150);

-- Example 2
INSERT INTO OFFERS (description, Offer_price, name,duration) 
VALUES ('Spotify Premium offer description', 150, 'Spotify Premium',150);

-- Example 3
INSERT INTO OFFERS (description, Offer_price, name,duration) 
VALUES ('Amazon Prime subscription offer description', 100, 'Amazon Prime',150);

-- Example 4
INSERT INTO OFFERS (description, Offer_price, name,duration) 
VALUES ('Hulu subscription offer description', 120, 'Hulu Subscription',150);

SELECT COUNT(*) AS OffersNumber FROM OFFERS;




-- Select Client Orders and for each order there is a select (for offers)
-- A list of orders and for each order there is a list of offers (just offers names )





