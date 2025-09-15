# Alex's Vet Centre

A command-line veterinary management system for tracking dogs, owners, and their relationships using an SQLite database.

---

## Table of Contents

- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Code Structure](#code-structure)
- [License](#license)

---

## Features

- Add, update, and delete dog records (name, breed, age, chip status, last checkup)
- Add, update, and delete owner records (name, location, date of birth, contact number)
- Link dogs to owners
- View reports of all dogs, owners, and dog-owner relationships
- Input validation for dates and contact numbers

---

## Setup

### Prerequisites

- Python 3.x
- SQLite3

### Installation

1. Clone this repository or download the files.
2. Ensure you have a SQLite database named `veterinaryDatabase.db` in the project directory.
3. Install any required dependencies (standard library only).

---

## Usage

Run the main program:

```sh
python AlexsVetCentre.py
```

Follow the on-screen prompts to manage the database.

### Menu Navigation

- **Main Menu**: Choose between Dog Information, Owner Information, Reports, or Exit.
- **Dog Information**: Add, update, or delete dog records.
- **Owner Information**: Add, update, or delete owner records.
- **Report**: View all dogs, owners, and dog-owner relationships.

---

## Database Schema

```sql
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
```

---

## Code Structure

- **AlexsVetCentre.py**: Main application logic
    - `main_menu()`: Main menu navigation
    - `dog_menu()`, `owner_menu()`: Submenus for dogs and owners
    - CRUD operations for dogs and owners
    - Input validation for dates and contact numbers
    - Reporting functions to display all records

---

## License

This project is for educational purposes.

---

**Feel free to copy and use this README for your project!**
