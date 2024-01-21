create table department (
	dept_id mediumint primary key auto_increment,
    dept_name varchar(50),
    description text
	);

create table employee (
	employee_id mediumint primary key auto_increment,
    dept_id mediumint,
	last_name varchar(50),
    first_name varchar(50),
    birth_date date,
    wage double,
    foreign key (dept_id) references department (dept_id)
		on delete set null
    );

create table work_slot (
	slot_id mediumint primary key auto_increment,
    start_time time,
    end_time time,
    day varchar(10)
    );
    
create table employee_work_slot (
	slot_id mediumint,
    employee_id mediumint,
    primary key (slot_id, employee_id),
    foreign key (slot_id) references work_slot (slot_id)
		on delete cascade,
    foreign key (employee_id) references employee (employee_id)
		on delete cascade
	);

create table employee_check_in (
	check_in_id mediumint primary key auto_increment,
    employee_id mediumint,
    date date,
    check_in time,
    check_out time,
    foreign key (employee_id) references employee (employee_id)
		on delete cascade
    );

create table exhibit (
	exhibit_id mediumint primary key auto_increment,
    manager_id mediumint,
    theme varchar(50),
    description text,
    foreign key (manager_id) references employee (employee_id)
		on delete set null
	);

create table artist (
	artist_id mediumint primary key auto_increment,
    last_name varchar(50),
    first_name varchar(50),
    birth_date date,
    death_date date,
    nationality varchar(50),
    biography text
	);

create table piece (
	piece_id mediumint primary key auto_increment,
    artist_id mediumint,
    exhibit_id mediumint,
    name varchar(50),
    description text,
    year int,
    foreign key (artist_id) references artist (artist_id)
		on delete set null,
	foreign key (exhibit_id) references exhibit (exhibit_id)
		on delete set null
	);

create table visitor (
	visitor_id mediumint primary key auto_increment,
    last_name varchar(30),
    first_name varchar(30),
    email varchar(50),
    phone_num bigint,
    birth_date date
    );

create table visit_slot (
	slot_id mediumint primary key auto_increment,
    time time
    );
    
create table reservation (
	visitor_id mediumint,
    slot_id mediumint,
    date date,
    primary key (visitor_id, slot_id, date),
    visitor_count tinyint,
    foreign key (visitor_id) references visitor (visitor_id)
		on delete cascade,
	foreign key (slot_id) references visit_slot (slot_id)
		on delete cascade
    );

create table ticket (
	ticket_id mediumint primary key auto_increment,
    type varchar(50),
    price double
    );

create table visit (
	visit_id mediumint primary key auto_increment,
    ticket_id mediumint,
    visitor_id mediumint,
    receptionist_id mediumint,
    check_in time,
    date date,
    foreign key (ticket_id) references ticket (ticket_id)
		on delete set null,
	foreign key (visitor_id) references visitor (visitor_id)
		on delete set null,
	foreign key (receptionist_id) references employee (employee_id)
		on delete set null
    );