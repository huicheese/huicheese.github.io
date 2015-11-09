create table books(
    ISBN char(15),
    title char(50) NOT NULL,
    authors char(100) NOT NULL,
    publisher char(50) NOT NULL,
    yearPublished int(4) NOT NULL,
    stock int NOT NULL CHECK(stock>=0),
    price float NOT NULL CHECK(price>=0),
    format char(9) CHECK(format='Hardcover'OR format='Softcover'),
    keywords char(100),
    subject char(100),
    PRIMARY KEY (ISBN)
);


create table customers(
    fullName char(100) NOT NULL,
    loginID char(30) NOT NULL,
    pw char(50) NOT NULL,
    majorCCN char(19),
    address char(100) NOT NULL,
    phoneNum char(25),
    PRIMARY KEY (loginID)
);


create table has_orders(
    oid INTEGER PRIMARY KEY AUTOINCREMENT,
    loginID char(30),
    order_date time NOT NULL,
    order_status char(30) CHECK(order_status ='Pending Order'
                                OR order_status='Payment Received'
                                OR order_status='Shipped'
                                OR order_status='Canceled'
                                OR order_status='Returned'),
    FOREIGN KEY (loginID) REFERENCES customers(loginID)
);

    
create table order_items(
    oid INTEGER,
    ISBN char(15) NOT NULL,
    qty int NOT NULL CHECK (qty >=0),
    primary key (ISBN, oid),
    foreign key (ISBN) references books(ISBN),
    FOREIGN KEY (oid) REFERENCES has_orders(oid)
);



create table feedback(
    loginID char(30) not null,
    ISBN char(15) not null,
    review INTEGER CHECK(review>=1 AND review <=10),
    optionalComment text,
    feedback_date time not null,
    primary key(loginID, ISBN),
    foreign key (loginID) references customers(loginID),
    foreign key (ISBN) references books(ISBN)
);

create table ratings(
    ISBN char(15),
    feedbackID char(30) CHECK(feedbackID != ratingID),
    ratingID char(30),
    rating INTEGER CHECK (rating>=0 AND rating <=2),
    primary key (ISBN, feedbackID, ratingID),
    foreign key (ratingID) references customers(loginID),
    foreign key (feedbackID) references customers(loginID),
    foreign key (ISBN) references books(ISBN)
);

drop table books;
drop table customers;
drop table feedback;
drop table ratings;
drop table has_orders;
drop table order_items;


insert into customers VALUES ('full name','loginID','password', 'majorCCN','address','696969696969');
insert into customers VALUES ('full name','loginID2','password', 'majorCCN','address','696969696969');
insert into books VALUES ('b','title','author','publisher', 1999, 9, 99, 'Hardcover', 'keyword','subject');
insert into has_orders(loginID,order_date,order_status) VALUES ('loginID',1999-02-15,'Shipped');
insert into feedback VALUES ('loginID','b',1,'wow this book sucks',1999-09-11);
insert into order_items VALUES (1, 'b',1);
insert into ratings VALUES ('b','loginID','loginID2',0);

select * from books;
select * from customers;