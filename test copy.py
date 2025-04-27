def caesar_cipher(text, shift, mode='encrypt'):
    """Encrypt or decrypt using Caesar cipher."""
    result = ''
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encrypt' else -shift
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char
    return result

def vigenere_cipher(text, key, mode='encrypt'):
    """Encrypt or decrypt using Vigenere cipher."""
    key = key.lower()
    result = ''
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            shift = shift if mode == 'encrypt' else -shift
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

def get_user_input():
    """Handle user input for cipher selection and mode."""
    cipher_type = input("Choose cipher ('Caesar' or 'Vigenere'): ").strip().lower()
    mode = input("Would you like to 'encrypt' or 'decrypt'? ").strip().lower()
    message = input("Enter your message: ")

    if cipher_type == "caesar":
        shift = input("Enter shift value (integer): ")
        if shift.isdigit():
            result = caesar_cipher(message, int(shift), mode)
        else:
            result = "Invalid shift value. Please enter an integer."
    
    elif cipher_type == "vigenere":
        key = input("Enter keyword (letters only): ")
        if key.isalpha():
            result = vigenere_cipher(message, key, mode)
        else:
            result = "Invalid keyword. Please enter alphabetic characters only."
    
    else:
        result = "Invalid cipher choice. Please choose 'Caesar' or 'Vigenere'."

    print(f"Your {cipher_type} {mode}ed message: {result}")

# Start the interactive session
get_user_input()