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
	stockid INT NOT NULL,
	name VARCHAR(255),
	itemtype VARCHAR(4),
	description VARCHAR(255),
	imgurl VARCHAR(255),
	buyprice FLOAT,
	sellprice FLOAT,
	discount FLOAT
	);
-- Item type codes --
--- WATL - luxury watches
--- WATN - normal watches
--- JWLL - fine jewellery
--- JWLF - fashion jewellery
--- GIFT - gifts

CREATE TABLE watches_table (
    itemid INT PRIMARY KEY,
    stockid INT NOT NULL,
    -- image bucket for specific item
    clockwork VARCHAR(255),
    calibre VARCHAR(255),
    casematerial VARCHAR(255),
    caseshape VARCHAR(255),
    casewidth VARCHAR(255),
    casedepth VARCHAR(255),
    glasstype VARCHAR(255),
    dial VARCHAR(255),
    dialcolour VARCHAR(255),
    bracelet VARCHAR(255),
    clasp VARCHAR(255),
    features VARCHAR(255),
    batterycharge INT,
    service INT,
    diamondsnumber INT,
    diamondscarat INT,
    diamondsquality VARCHAR(255),
    numbercoloured INT,
    colours VARCHAR(255),

    CONSTRAINT fk_itemid
        FOREIGN KEY (itemid)
            REFERENCES items_table(itemid)
    );

CREATE TABLE jewellery_table (
    itemid INT PRIMARY KEY,
    stockid INT NOT NULL,

    design VARCHAR(255),
    clasptype VARCHAR(255),
    chainlength VARCHAR(255),
    ringsize VARCHAR(255),
    ringwidth VARCHAR(255),

    colour VARCHAR(255),
    clarity VARCHAR(255),
    cut VARCHAR(255),
    quality VARCHAR(255),

    material VARCHAR(255),
    materialgroup VARCHAR(255),
    alloy INT,
    unitweight FLOAT,

    CONSTRAINT fk_itemid
        FOREIGN KEY (itemid)
            REFERENCES items_table(itemid)
    );

CREATE TABLE gifts_table (
    itemid INT PRIMARY KEY,
    stockid INT NOT NULL,

    articlegroup VARCHAR(255),
    articlekind VARCHAR(255),
    brand VARCHAR(255),
    productline VARCHAR(255),
    collection VARCHAR(255),

    CONSTRAINT fk_itemid
        FOREIGN KEY (itemid)
            REFERENCES items_table(itemid)
    );


-- Repairs control --
CREATE TABLE repairs_table (
	repairid serial PRIMARY KEY,
	clientid VARCHAR(255) NOT NULL,
	description VARCHAR(255) NOT NULL,

	document character varying(50) NOT NULL,
	birthday DATE NOT NULL,
	client_since DATE NOT NULL DEFAULT CURRENT_DATE
	CONSTRAINT fk_customer
	    FOREIGN KEY (clientid)
	        REFERENCES client_table(clientid)
	);

-- History control --
CREATE TABLE history_table  (
    movementid serial PRIMARY KEY,
    movementdate DATE,
    itemid INT,
    description VARCHAR(255),

    CONSTRAINT fk_itemid
        FOREIGN KEY (itemid)
            REFERENCES items_table(itemid)
    );