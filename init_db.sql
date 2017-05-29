create table admin.post (
	id serial not null primary key,
	title text not null,
	body text,
	img text,
	posted_at timestamp default now()
);

create unique index on admin.post (id);
create index on admin.post (title);
create index on admin.post (body);
create index on admin.post (posted_at);


CREATE table admin.exercise (
	id bigserial not null primary key,
	title text,
	category text not null,
	file_path text not null,
	uploaded_at timestamp default now()
);

create unique index on admin.exercise (id);
create index on admin.exercise (category);
create index on admin.exercise (uploaded_at);



CREATE TABLE admin.success (
    id serial not null primary key,
    full_name text not null,
    school_year int not null,
    university text not null,
    promoted boolean default false

)

;
create unique index on admin.success (id);
create index on admin.success (school_year);
create index on admin.success (full_name);
create index on admin.success (promoted) where (promoted = true);


CREATE TABLE admin.newsletter (
    id serial not null primary key,
    email text not null,
    registered_at TIMESTAMP;
);

create unique index on admin.newsletter (id);
create index on admin.newsletter (email);
create index on admin.newsletter (registered_at);