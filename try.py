import itertools

character_set = "abcdefghijklmnopqrstuvwxyz0123456789" 

# Set minimum and maximum password lengths
min_length = 4
max_length = 6 


for password_length in range(min_length, max_length + 1):
    # Generate all combinations for the current length
    for combination in itertools.product(character_set, repeat=password_length):
        candidate = ''.join(combination)  

        if candidate == target_password:
            print("Password found:", candidate)
            break  # Exit inner loop if the password is found
    else:
        continue 
    break 

