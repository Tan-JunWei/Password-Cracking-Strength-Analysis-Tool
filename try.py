import math
import re

def password_strength(password: str) -> str:
    '''
    Password entropy formula:
    E = log2(R^L)
    where E is 
    '''
    password_length = len(password)
    possible_pool_size = 0

    # r"" prefix specifies a raw string literal in Python
    if re.search(r"\d", password): # contains digits
        possible_pool_size += 10
    if re.search(r"[a-z]", password):
        possible_pool_size += 26
    if re.search(r"[A-Z]", password):
        possible_pool_size += 26
    if re.search(r"\W", password):
        possible_pool_size += 32
    
    password_entropy = password_length * math.log2(possible_pool_size)
    print(password_entropy)


password_strength("1Bankruptcies2&%")