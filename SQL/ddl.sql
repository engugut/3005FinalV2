create table rooms
	(room_number			SERIAL, 
	 room_size				varchar(6),
	 available				boolean,
	 primary key (room_number)					
	);

create table equipment
	(equipment_id			SERIAL, 
	 equipment_type				varchar(20),
	 needs_maintenance				boolean,
	 primary key (equipment_id)					
	);
	
create table users
	(user_id			SERIAL, 
	 name			varchar(20) not null, 
	 height			int, 
	 weight			int,
	 gender			varchar(20),
	 fitness_goals  varchar(50),
	 weight_goal 	varchar(50),
	 time_goal		varchar(50),
	 health_metrics varchar(50),
	 primary key (user_id)
	);
	
create table trainers
	(trainer_id			SERIAL, 
	 name			varchar(20) not null, 
	 gender			varchar(20),
	 speciality		varchar(20),
	 primary key (trainer_id)
	);
	
create table adminstaff
	(admin_id			SERIAL, 
	 name			varchar(20) not null, 
	 equipment_id		int,
	 primary key (admin_id),
	 foreign key (equipment_id) references equipment
		on delete set null
	);

create table trainerschedule
	(trainer_id		int,
	 app_time_start		TIME NOT NULL,
	 app_time_end		TIME NOT NULL,
	 day_available			DATE,
	 room_number			int,
	 primary key (trainer_id),
	 foreign key (trainer_id) references trainers
		on delete set null,
	 foreign key (room_number) references rooms
		on delete set null
	);

create table userschedule
	(user_id		int,
	 app_time_start		TIME NOT NULL,
	 app_time_end		TIME NOT NULL,
	 day_available			DATE,
	 room_number			int,
	 primary key (user_id),
	 foreign key (user_id) references users
		on delete set null,
	 foreign key (room_number) references rooms
		on delete set null
	);

create table exercices
	(user_id		int, 
	 routines			varchar(50)[], 
	 fitness_ach		varchar(50)[],
	 health_metrics		varchar(50),
	 primary key (user_id),
	 foreign key (user_id) references users
		on delete set null
	);

create table classschedule
	(class_id		SERIAL,
	 trainer_id		int,
	 user_id		int[],
	 app_time_start		TIME NOT NULL,
	 app_time_end		TIME NOT NULL,
	 day_available			DATE,
	 room_number			int,
	 primary key (class_id),
	 foreign key (trainer_id) references trainers
		on delete set null,
	 foreign key (room_number) references rooms
		on delete set null
	);

create table payments
	(payment_id			SERIAL,
	 user_id			int,
	 card_number		varchar(30),
	 expire_date		DATE,
	 cvc				varchar(4),
	 paid				boolean,
	 primary key (payment_id),
	 foreign key (user_id) references users
		on delete set null
	);



