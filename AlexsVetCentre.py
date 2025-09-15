import sqlite3
from datetime import datetime

vetDB = sqlite3.connect("veterinaryDatabase.db")
cursor = vetDB.cursor()


# CREATE TABLE dogs(dogID INTEGER PRIMARY KEY, name TEXT, breed TEXT, age INTEGER, chip BOOLEAN, checkup DATE)

# CREATE TABLE owners(ownerID INTEGER PRIMARY KEY, name TEXT, location TEXT, dob DATE, contactNumber INTEGER,
# email TEXT)

# CREATE TABLE dogOwner(dogID INTEGER, ownerID INTEGER)


def main_menu():
    print('\n*** MAIN MENU ***\n1. Dog Information\n2. Owner Information\n3. Report\n4. Exit')
    try:
        choice = int(input('> '))
    except ValueError:
        main_menu()
    else:
        if choice == 1:
            dog_menu()
        elif choice == 2:
            owner_menu()
        elif choice == 3:
            report()
        elif choice == 4:
            exit_answer = (input('Are you sure (yes or no)?\n> '))
            while exit_answer.lower() != 'yes' and exit_answer.lower() != 'no':
                print('Yes or No?')
                exit_answer = (input('\nAre you sure (yes or no)?\n> '))
            if exit_answer.lower() == 'yes':
                vetDB.close()
            elif exit_answer.lower() == 'no':
                main_menu()
        else:
            main_menu()


def dog_menu():
    print("\n*** DOG INFORMATION ***\n1. Add\n2. Update\n3. Delete\n4. Exit")
    try:
        choice = int(input('\n> '))
    except ValueError:
        dog_menu()
    else:
        if choice == 1:
            dog_add()
        elif choice == 2:
            dog_update()
        elif choice == 3:
            dog_delete()
        elif choice == 4:
            main_menu()
        else:
            dog_menu()


def dog_add():
    print('\n** Add **')
    name = input('\nName > ')
    breed = input('Breed > ')
    age = int(input('Age > '))
    chip = input('Chip (yes or no) > ')
    while chip.lower() != 'yes' and chip.lower() != 'no':
        chip = input('yes or no\n> ')
    if chip.lower() == 'yes':
        chip_bool = True
    else:
        chip_bool = False
    checkup = input('Last checkup (dd/mm/yy) > ')
    formatted_date = date_validation(checkup)
    while formatted_date == 'ERROR':
        checkup = input('Last checkup (dd/mm/yy) > ')
        formatted_date = date_validation(checkup)
    cursor.execute('''
        INSERT INTO dogs(name, breed, age, chip, checkup) VALUES(?, ?, ?, ?, ?)''',
                   (name, breed, age, chip_bool, checkup))
    vetDB.commit()
    print('\nDog added successfully')
    main_menu()


def dog_update():
    print('\n** Update **')
    try:
        dog_id = int(input('\nDog ID > '))
    except ValueError:
        print('Enter dog ID number')
        dog_update()
    else:
        # checking that the dog exists in the database
        cursor.execute('''
        SELECT * FROM dogs WHERE dogID = ?''', (dog_id,))
        dog_list = cursor.fetchone()
        if dog_list is None:
            print('This dog does not exist')
            dog_update()
        # VERIFY OWNER INFORMATION BEFORE CONTINUING
        # checking the information related to that dog ID, so you know what information you are updating
        print('Is this your dog (yes or no) >', dog_list[1], dog_list[2])
        confirm = input('\n> ')
        while confirm.lower() != 'yes' and confirm.lower() != 'no':
            print('yes or no')
            confirm = input('> ')
        if confirm.lower() == 'no':
            dog_update()
        # asking what information they would like to update and then going through that respective process
        field = input('What do you want to update?\n1. Name\n2. Breed\n3. Age\n4. Chip\n5. Last Checkup\n6. Exit\n> ')
        while field not in ('1', '2', '3', '4', '5', '6'):
            field = input(
                'What do you want to update?\n1. Name\n2. Breed\n3. Age\n4. Chip\n5. Last Checkup\n6. Exit> ')
        if field == '1':
            new_name = input('\nNew name > ')
            cursor.execute('''
            UPDATE dogs SET name = ? WHERE dogID = ? ''', (new_name, dog_id))
        elif field == '2':
            new_breed = input('\nNew Breed >')
            cursor.execute('''
            UPDATE dogs SET breed = ? WHERE dogID = ? ''', (new_breed, dog_id))
        elif field == '3':
            new_age = input('\nNew Age >')
            cursor.execute('''
            UPDATE dogs SET age = ? WHERE dogID = ? ''', (new_age, dog_id))
        elif field == '4':
            new_chip_status = input('Chip (yes or no) > ')
            while new_chip_status.lower() != 'yes' and new_chip_status.lower() != 'no':
                new_chip_status = input('yes or no\n> ')
            if new_chip_status.lower() == 'yes':
                chip_bool = True
            else:
                chip_bool = False
            cursor.execute('''
            UPDATE dogs SET chip = ? WHERE dogID = ? ''', (chip_bool, dog_id))
        elif field == '5':
            latest_checkup = input('Last checkup (dd/mm/yy) > ')
            formatted_date = date_validation(latest_checkup)
            while formatted_date == 'ERROR':
                latest_checkup = input('Last checkup (dd/mm/yy) > ')
                formatted_date = date_validation(latest_checkup)
            cursor.execute('''
            UPDATE dogs SET checkup = ? WHERE dogID = ? ''', (latest_checkup, dog_id))
        elif field == '6':
            dog_menu()
        main_menu()


def dog_delete():
    print('\n** Delete **')
    try:
        dog_id = int(input('\nDog ID > '))
    except ValueError:
        print('Enter dog ID number')
        dog_update()
    else:
        # checking that the dog exists in the database
        cursor.execute('''
        SELECT * FROM dogs WHERE dogID = ?''', (dog_id,))
        dog_list = cursor.fetchone()
        if dog_list is None:
            print('This dog does not exist')
            dog_delete()
        # VERIFY OWNER INFORMATION BEFORE CONTINUING
        # checking the information related to that dog ID, so you know what information you are deleting
        print('Is this your dog (yes or no) >', dog_list[1], dog_list[2])
        confirm = input('\n> ')
        while confirm.lower() != 'yes' and confirm.lower() != 'no':
            print('yes or no')
            confirm = input('> ')
        if confirm.lower() == 'no':
            dog_delete()
        confirm_delete = input(
            'Are you sure you want to delete this information, it will be permanent? (yes or no)\n> '
        )
        while confirm_delete.lower() != 'yes' and confirm_delete.lower() != 'no':
            print('yes or no')
            confirm = input('> ')
        if confirm.lower() == 'no':
            dog_menu()
        else:
            cursor.execute('''
            DELETE FROM dogs WHERE dogID = ?''', (dog_id,))
            vetDB.commit()
            main_menu()


def owner_menu():
    print("\n*** OWNER INFORMATION ***\n1. Add\n2. Update\n3. Delete\n4. Exit")
    try:
        choice = int(input('> '))
    except ValueError:
        owner_menu()
    else:
        if choice == 1:
            owner_add()
        elif choice == 2:
            owner_update()
        elif choice == 3:
            owner_delete()
        elif choice == 4:
            main_menu()
        else:
            owner_menu()


def owner_add():
    print('\n** Add **')
    try:
        contact_number = int(input('\nContact Number > '))
    except ValueError:
        print('Contact Number must be only digits of length 11 with no spaces')
        owner_add()
    else:
        if len(str(contact_number)) != 10:
            print('Contact number must be 11 digits long with no spaces')
            owner_add()
        name = input('Name > ')
        location = input('Address > ')
        dob = input('Date of Birth (dd/mm/yy) > ')
        formatted_date = date_validation(dob)
        while formatted_date == 'ERROR':
            dob = input('Date of Birth (dd/mm/yy) > ')
            formatted_date = date_validation(dob)
        cursor.execute('''
        INSERT INTO owners(name, location, dob, contactNumber) VALUES(?, ?, ?, ?)''',
                       (name, location, dob, contact_number))
        vetDB.commit()
        print('Owner added successfully')
        owner_menu()


def owner_update():
    print('** Update **')
    try:
        owner_id = int(input('Owner ID > '))
    except ValueError:
        print('Enter owner ID number')
        owner_update()
    else:
        # checking that the owner exists in the database
        cursor.execute('''
        SEARCH * FROM owners WHERE ownerID = ?''', (owner_id,))
        owner_list = cursor.fetchone()
        if owner_list is None:
            print('This owner does not exist')
            owner_update()
        # checking that name and location is the person, so you know you are updating correct data
        owner_menu()


def owner_delete():
    # if owner is deleted all dogs linked to that owner must be deleted too
    print('** Delete **')
    owner_menu()


def date_validation(date):
    try:
        formatted_date = datetime.strptime(date, '%d/%m/%y')
        present = datetime.now()
        if formatted_date > present:
            print('Date must be in the past')
            formatted_date = 'ERROR'
    except ValueError:
        print('Enter in the form dd/mm/yy')
        formatted_date = 'ERROR'
    return formatted_date

def print_all_dogs():
    cursor.execute("SELECT * FROM dogs")
    dogs = cursor.fetchall()
    if not dogs:
        print("No dogs found in the database.")
    else:
        print("\n--- All Dogs ---")
        for dog in dogs:
            print(f"ID: {dog[0]}, Name: {dog[1]}, Breed: {dog[2]}, Age: {dog[3]}, Chip: {dog[4]}, Last Checkup: {dog[5]}")

def print_all_owners():
    cursor.execute("SELECT * FROM owners")
    owners = cursor.fetchall()
    if not owners:
        print("No owners found in the database.")
    else:
        print("\n--- All Owners ---")
        for owner in owners:
            print(f"OwnerID: {owner[0]}, Name: {owner[1]}, Location: {owner[2]}, DOB: {owner[3]}, Contact Number: {owner[4]}, Email: {owner[5]}")

def print_all_dogOwners():
    cursor.execute("SELECT * FROM dogOwner")
    dogOwners = cursor.fetchall()
    if not dogOwners:
        print("No dog owners found in the database.")
    else:
        print("\n--- All Dog Owners ---")
        for dogOwner in dogOwners:
            print(f"DogID: {dogOwner[0]}, OwnerID: {dogOwner[1]}")

def report():
    print_all_dogs()
    print_all_owners()
    print_all_dogOwners()
    main_menu()


# ADD A FUNCTION FOR VALIDATING OWNER INFORMATION FOR VALIDATION


main_menu()
