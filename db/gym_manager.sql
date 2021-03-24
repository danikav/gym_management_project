DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    membertype VARCHAR(255)
);

CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date VARCHAR(255),
    time VARCHAR(255),
    capacity INT,
    details TEXT, 
    peak BOOLEAN
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    class_id INT REFERENCES classes(id) ON DELETE CASCADE
);