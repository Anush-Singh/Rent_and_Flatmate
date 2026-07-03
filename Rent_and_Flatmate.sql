--Rent and Flatmate Application
/*
CREATE DATABASE RentFlatmateDB;
USE RentFlatmateDB;
*/
--User
CREATE TABLE users (
    id INT IDENTITY(1,1) PRIMARY KEY,
    full_name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(MAX),
    role VARCHAR(20)
);
--listings
CREATE TABLE listings (
    id INT IDENTITY(1,1) PRIMARY KEY,
    owner_id INT,
    location VARCHAR(100),
    rent INT,
    available_from DATE,
    room_type VARCHAR(50),
    furnishing_status VARCHAR(50),
    filled BIT DEFAULT 0
);
--tenant profile
CREATE TABLE tenant_profiles (
    id INT IDENTITY(1,1) PRIMARY KEY,
    tenant_id INT,
    preferred_location VARCHAR(100),
    budget_min INT,
    budget_max INT,
    move_in_date DATE
);
--Score
CREATE TABLE compatibility_scores (
    id INT IDENTITY(1,1) PRIMARY KEY,
    tenant_id INT,
    listing_id INT,
    score INT,
    explanation VARCHAR(MAX)
);
--Internet Request
CREATE TABLE interest_requests (
    id INT IDENTITY(1,1) PRIMARY KEY,
    tenant_id INT,
    listing_id INT,
    status VARCHAR(20)
);
--chat
CREATE TABLE chat_messages (
    id INT IDENTITY(1,1) PRIMARY KEY,
    sender_id INT,
    receiver_id INT,
    message VARCHAR(MAX),
    sent_at DATETIME DEFAULT GETDATE()
);