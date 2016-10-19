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