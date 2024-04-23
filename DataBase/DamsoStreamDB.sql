
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
    image_Name VARCHAR(255),
    Offer_price DECIMAL(10, 2),
    name VARCHAR(255),
	PRIMARY KEY (idOffer)
);

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



-- this table should store orders temporary and remove data when submiting the data
-- aka filling Order and OrderOffers
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

























-- Examples :

INSERT INTO  OFFERS (description,image_Name,Offer_price,name) VALUES
('netflix account offer description','tswira d netflix',200,'Netflix acocunts');
-- Example 2
INSERT INTO OFFERS (description, image_Name, Offer_price, name) 
VALUES ('Spotify Premium offer description', 'spotify_image.jpg', 150, 'Spotify Premium');

-- Example 3
INSERT INTO OFFERS (description, image_Name, Offer_price, name) 
VALUES ('Amazon Prime subscription offer description', 'amazon_image.jpg', 100, 'Amazon Prime');

-- Example 4
INSERT INTO OFFERS (description, image_Name, Offer_price, name) 
VALUES ('Hulu subscription offer description', 'hulu_image.jpg', 120, 'Hulu Subscription');

SELECT COUNT(*) AS OffersNumber FROM OFFERS;











