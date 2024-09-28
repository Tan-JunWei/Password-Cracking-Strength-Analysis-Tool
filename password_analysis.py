import getpass
import hashlib
import time
import sys
from pyfiglet import Figlet
from colorama import Fore, Style
import threading
import itertools

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
    hashed_password = hash_password(password) # password is hashed and only revealed if found in dictionary
    start_time = time.time()

    # Create a thread to display a spinner animation
    stop_event = threading.Event()
    spinner_thread = threading.Thread(target=spinner_animation, args=(stop_event,1))
    spinner_thread.start()
    
    with open(dictionary_file, "r", encoding="utf-8", errors="ignore") as dictionary_file:
        for index, word in enumerate(dictionary_file):
            word = word.strip()
            hashed_word = hash_password(word)
            
            if hashed_word == hashed_password:
                # Stop the spinner animation
                stop_event.set()
                spinner_thread.join()
                
                print(Fore.CYAN + "\nDictionary attack complete!" + Style.RESET_ALL)
                print(f"\nPassword found: {word} ({index +1} attempts)")
                end_time = time.time()
                print(f"Time taken: {end_time - start_time:.2f} seconds")

                return True

    # If the password is not found in the dictionary
    stop_event.set()
    spinner_thread.join()
    end_time = time.time()
    print(f"\n{Fore.GREEN}Password not found in dictionary. Time taken: {end_time - start_time:.2f} seconds. Trying brute force attack...\n" + Style.RESET_ALL)
    return False

def brute_force_attack(password: str, min_length: int, max_length: int):
    hashed_password = hash_password(password)
    character_set = "abcdefghijklmnopqrstuvwxyz0123456789" 
    start_time = time.time()

    # Create a thread to display a spinner animation
    stop_event = threading.Event()
    spinner_thread = threading.Thread(target=spinner_animation, args=(stop_event,2))
    spinner_thread.start()

    for password_length in range(min_length, max_length + 1):
        # Generate all combinations for the current length
        for combination in itertools.product(character_set, repeat=password_length):
            attempt = ''.join(combination)
            hashed_attempt = hash_password(attempt)

            if hashed_attempt == hashed_password:
                stop_event.set()
                spinner_thread.join()

                print(Fore.CYAN + "\nBrute force attack complete!" + Style.RESET_ALL)
                print("Password found:", attempt)
                end_time = time.time()
                print(f"Time taken: {end_time - start_time:.2f} seconds")
                password_found = True
                break 
        else:
            continue
        break 

    return password_found

def spinner_animation(stop_event,num):
    spinner = ['-', '\\', '|', '/']
    if num == 1:
        while not stop_event.is_set():
            for symbol in spinner:
                sys.stdout.write(f'\r{Fore.RED}{symbol} Dictionary attack in progress...' + Style.RESET_ALL)
                sys.stdout.flush()
                time.sleep(0.1)
    elif num == 2:
        while not stop_event.is_set():
            for symbol in spinner:
                sys.stdout.write(f'\r{Fore.RED}{symbol} Brute force attack in progress...' + Style.RESET_ALL)
                sys.stdout.flush()
                time.sleep(0.1)

def password_analysis():
    '''
    Password analysis function that calls the dictionary_attack function
    '''
    password = getpass.getpass("Enter password to check: ")
    # Dictionary attack
    dictionary_path = "rockyou.txt"
    password_found = dictionary_attack(password, dictionary_path) 

    if not password_found: # If password was not found in dictionary, start a brute force attack
        # Set minimum and maximum password lengths 1-10 in this case
        min_length = 1
        max_length = 10
        brute_force_attack(password, min_length, max_length)

    return password_found

count = 0
while True:
    if count == 0:
        password_cracked = password_analysis()

    if password_cracked:
        count += 1
        choice = input("Do you want to check another password (y/n)? ").lower()
        print() 

        while choice not in ["y", "n"]:
            choice = input("Invalid choice. Do you want to check another password (y/n)? ").lower()
            print()

        match choice:
            case "y":
                password_analysis()
            case "n":
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Try again.")