# Alexs-Vet-Centre
This project is a command-line veterinary management system for tracking dogs, owners, and their relationships using an SQLite database. It allows users to add, update, delete, and report on dog and owner information.

Features
Add, update, and delete dog records (name, breed, age, chip status, last checkup).
Add, update, and delete owner records (name, location, date of birth, contact number).
Link dogs to owners.
View reports of all dogs, owners, and dog-owner relationships.
Input validation for dates and contact numbers.

Getting Started
Prerequisites
Python 3.x
SQLite3

Setup
Clone this repository or download the files.

Ensure you have a SQLite database named veterinaryDatabase.db in the project directory. 

For information the database SQL structure is:

CREATE TABLE dogs(
    dogID INTEGER PRIMARY KEY,
    name TEXT,
    breed TEXT,
    age INTEGER,
    chip BOOLEAN,
    checkup DATE
);

CREATE TABLE owners(
    ownerID INTEGER PRIMARY KEY,
    name TEXT,
    location TEXT,
    dob DATE,
    contactNumber INTEGER,
    email TEXT
);

CREATE TABLE dogOwner(
    dogID INTEGER,
    ownerID INTEGER
);

Install dependencies (if any).

Running
Run the main program:

Follow the on-screen prompts to manage the database.

File Structure
AlexsVetCentre.py: Main application logic.
veterinaryDatabase.db: SQLite database file.

Usage
Navigate menus using number inputs.
Add, update, or delete dogs and owners.
Generate reports to view all records.

License
This project is for educational purposes.

Additional Information
Please see screenshot below of my database and its contents for example.
<img width="1145" height="1046" alt="image" src="https://github.com/user-attachments/assets/cde15280-6ec0-470b-a782-94360cb5b70b" />
