CREATE DATABASE db0905assignment01;
USE db0905assignment01;
SET time_zone = '+09:00';

CREATE TABLE customer(
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50) NOT NULL,
    phone VARCHAR(30) NOT NULL,
    email VARCHAR(100) UNIQUE,
    prefcontact ENUM('phone', 'kakao', 'email') DEFAULT 'kakao',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE species(
    species_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE 
);

CREATE TABLE breed (
  breed_id INT PRIMARY KEY AUTO_INCREMENT,
  species_id INT NOT NULL,
  name VARCHAR(80) NOT NULL,
  FOREIGN KEY (species_id) REFERENCES species(species_id)
);

CREATE TABLE pet (
  pet_id INT PRIMARY KEY AUTO_INCREMENT,
  customer_id INT NOT NULL,
  breed_id INT NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
  FOREIGN KEY (breed_id) REFERENCES breed(breed_id),
  name VARCHAR(80) NOT NULL,
  sex ENUM('M','F','U') DEFAULT 'U',
  birth_date DATE NULL
);

CREATE TABLE room_type (
  room_type_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(80) NOT NULL,
  base_price INT,
  for_type ENUM('dog', 'cat', 'etc')
);

CREATE TABLE room (
  room_id INT PRIMARY KEY AUTO_INCREMENT,
  room_type_id INT NOT NULL,
  name VARCHAR(80) NOT NULL UNIQUE,
  is_available BOOLEAN DEFAULT TRUE,
  FOREIGN KEY (room_type_id) REFERENCES room_type(room_type_id)
);

CREATE TABLE service (
  service_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  price INT NOT NULL,
  category ENUM('grooming','walk','training','vet','other') DEFAULT 'other'
);

CREATE TABLE reservation (
  reservation_id INT PRIMARY KEY AUTO_INCREMENT,
  customer_id INT NOT NULL,
  room_id INT NOT NULL,
  pet_id INT NOT NULL,
  service_id INT NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
  FOREIGN KEY (room_id) REFERENCES room(room_id),
  FOREIGN KEY (pet_id) REFERENCES pet(pet_id),
  FOREIGN KEY (service_id) REFERENCES service(service_id),
  status ENUM('pending','confirmed','checked_in','checked_out','cancelled') DEFAULT 'pending'
);