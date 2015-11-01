create table books(
ISBN char(15),
title char(50) not null,
authors char(100) not null,
publisher char(50) not null,
yearPublished int not null,
stock int not null,
price float not null,
format ENUM('Hardcover','Softcover'),
keywords char(100),
subject char(100),
primary key(ISBN)
);

create table customers(
fullName char(100) not null,
loginID char(30),
pw char(50) not null,
majorCCN char(19),
address char(100) not null,
phoneNum char(25),
primary key (loginID)
);

create table orders(
oid char(30),
loginID char(30),
ISBN char(15) not null,
qty int not null,
order_date time not null,
order_status char(30) not null,
primary key (ISBN, oid),
foreign key (ISBN) references books(ISBN),
foreign key (loginID) references customers(loginID)
);

create table feedback(
loginID char(30) not null,
ISBN char(15) not null,
review ENUM ('0','1','2','3','4','5','6','7','8','9','10'),
optionalComment text,
feedback_date time not null,
primary key(loginID, ISBN),
foreign key (loginID) references customers(loginID),
foreign key (ISBN) references books(ISBN)
);

create table ratings(
ISBN char(15),
feedbackID char(30),
ratingID char(30),
rating ENUM ('0','1','2'),
primary key (ISBN, feedbackID, ratingID),
foreign key (feedbackID) references feedback(loginID),
foreign key (ratingID) references customers(loginID),
foreign key (ISBN) references feedback(ISBN)
);

#################### TRIGGER TO PREVENT STOCK AND PRICE FROM BEING NEGATIVE ##########################################
USE `triggertest`;  #replace triggertest with schema name here

DELIMITER $$

DROP TRIGGER IF EXISTS triggertest.books_BEFORE_INSERT$$  #replace triigertest with schema name
USE `triggertest`$$
CREATE DEFINER=`root`@`localhost` TRIGGER `triggertest`.`books_BEFORE_INSERT` BEFORE INSERT ON `books` FOR EACH ROW
BEGIN
	IF NEW.stock <0 THEN
		SET NEW.stock = 0;
	END IF;
    IF NEW.price <0 THEN
		SET NEW.price = 0;
	END IF;
END
$$
DELIMITER ;
######################################################################################################################

#####################Check if ratingID and feedbackID is the same#####################################################
USE `triggertest`;

DELIMITER $$

DROP TRIGGER IF EXISTS triggertest.ratings_BEFORE_INSERT$$
USE `triggertest`$$
CREATE DEFINER = CURRENT_USER TRIGGER `triggertest`.`ratings_BEFORE_INSERT` BEFORE INSERT ON `ratings` FOR EACH ROW
BEGIN
	IF NEW.ratingID = NEW.feedbackID THEN
		SET new.ratingID = null;
	END IF;
END
$$
DELIMITER ;
###################################################################################################################### 

### Some test codes ######
insert into ratings  value ('2125', 'c' , 'b' , '0') ;
insert into books value ('1', 'a','b','c', 1356,-77,-69, 'Hardcover','f','g');