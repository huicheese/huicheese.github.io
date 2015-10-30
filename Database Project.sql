create table books(
ISBN char(15) primary key,
title char(50) not null,
authors char(100) not null,
publisher char(50) not null,
yearPublished int not null,
copiesLeft int not null,
price float not null,
bookformat char(9) not null,
keywords char(100),
subject char(100)
)

create table customers(
fullName char(100) not null,
loginName char(30) primary key,
pw char(50) not null,
majorCCN char(19),
address char(100) not null,
phoneNum char(25) 
)

create table ordered(
oid char(30) primary key,
ogid char(25),
loginName char(30),
ISBN char(15) not null,
order_date time not null,
order_status char(30) not null,
foreign key (loginName) references customers
)

create table feedback(
fid char(30) primary key,
loginName char(30),
ISBN char(15),
rating int check (rating<=10 and rating >=0) not null,
optionalComment char(1000),
useful int not null default 0,
veryUseful int not null default 0,
useless int not null default 0,
feedbackTime time,
foreign key (loginName) references customers,
foreign key (ISBN) references books
)

