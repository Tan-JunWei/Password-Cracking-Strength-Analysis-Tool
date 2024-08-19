import getpass
import hashlib
import time
import sys
from pyfiglet import Figlet
from colorama import Fore, Style

fig = Figlet(font='standard') 
print(fig.renderText('Password Analysis'))

def hash_password(password: str) -> str:
    '''
    Hashes the given password using the specified hashing algorithm SHA-256.
    
    Args:
        password (str): The password to hash

    Returns:
        str: The hexadecimal representation of the hash
    '''
    hash_obj = hashlib.sha256()
    # Update the hash object with the password encoded to bytes
    hash_obj.update(password.encode('utf-8'))
    # Return the hexadecimal representation of the hash
    return hash_obj.hexdigest()

def dictionary_attack(password: str, dictionary_file: str):
    '''
    This function checks if the password is in the dictionary "rockyou.txt"
    It hashes each word in the dictionary and compares it to the hashed password

    Args:
        password (str): The password to check
        dictionary_file (str): The path to the dictionary file
    '''
    hashed_password = hash_password(password)

    # Record start time
    start_time = time.time()
    
    try:
        with open(dictionary_file, "r", encoding="utf-8", errors="ignore") as dictionary_file:
            for word in dictionary_file:
                word = word.strip()
                hashed_word = hash_password(word)
                
                if hashed_word == hashed_password:
                    print(f"Password found: {word}")
                    # Record end time
                    end_time = time.time()
                    print(f"Time taken: {end_time - start_time:.2f} seconds")
                    return
    
    except FileNotFoundError:
        # If the dictionary file is not found, print an error message
        print(f"File not found: {dictionary_file}")

    end_time = time.time()
    # If the password is not found in the dictionary, print a message
    print("Password not found in dictionary")
    print(f"Time taken: {end_time - start_time:.2f} seconds")

def password_analysis():
    '''
    Password analysis function that calls the dictionary_attack function
    '''
    password = getpass.getpass("Enter password to check: ")
    # Dictionary attack
    dictionary_path = "rockyou.txt"
    dictionary_attack(password, dictionary_path)

count = 1

while True:
    if count == 1:
        password_analysis()
        count += 1

    else:
        choice = input("Do you want to check another password? (y/n) ").lower()
        match choice:
            case "y":
                password_analysis()
            case "n":
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Try again.")