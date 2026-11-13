CREATE DATABASE student_dbms;

USE student_dbms;

CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    course VARCHAR(50),
    semester INT
);
