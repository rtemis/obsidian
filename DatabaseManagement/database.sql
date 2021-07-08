-- Create main tables --

-- Employee control --
CREATE TABLE employee_table (
	employeeid serial PRIMARY KEY,
	firstname VARCHAR(255) NOT NULL,
	lastname VARCHAR(255) NOT NULL,
	password character varying(50) NOT NULL,
	hire_date DATE NOT NULL
	);

-- Client control --
CREATE TABLE client_table (
	clientid serial PRIMARY KEY,
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
	document character varying(50) NOT NULL,
	birthday DATE NOT NULL,
	client_since DATE NOT NULL DEFAULT CURRENT_DATE
	);

-- Item control --
CREATE TABLE items_table (
	itemid serial PRIMARY KEY,
	stockid SECO
	name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
	document character varying(50) NOT NULL,
	birthday DATE NOT NULL,
	client_since DATE NOT NULL DEFAULT CURRENT_DATE
	);

-- Repairs control --
CREATE TABLE repairs_table (
	clientid serial PRIMARY KEY,
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
	document character varying(50) NOT NULL,
	birthday DATE NOT NULL,
	client_since DATE NOT NULL DEFAULT CURRENT_DATE
	);
