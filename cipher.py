import streamlit as st

st.write('hey there')

def caesar_cipher(text, shift, mode='Encrypt'):
    """Encrypt or decrypt using Caesar cipher."""
    result = ''
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'Encrypt' else -shift
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

cypher_types = ["Caesar", "Vigenere"]
cipher_type = st.selectbox("Choose a Cipher Type:", cypher_types)

encrypt_mode = st.radio("Select an action:", ["Encrypt", "Decrypt"])

user_message = st.text_input("What is the message?")

if cipher_type == "Caesar":
    shift = st.number_input("Enter a number between 0 and 25:", 
                            min_value=0,
                            max_value=25)
    if shift == 0:
        st.warning('A number of 0 does not provide a good encryption')
    result = caesar_cipher(user_message, shift, encrypt_mode)
    st.header("Your encrypted message is")
    st.subheader(result)
else:
    
    result = "Invalid cipher choice. Please choose 'Caesar' or 'Vigenere'."

# def get_user_input():
#     """Handle user input for cipher selection and mode."""
#     cipher_type = input("Choose cipher ('Caesar' or 'Vigenere'): ").strip().lower()
#     mode = input("Would you like to 'encrypt' or 'decrypt'? ").strip().lower()
#     message = input("Enter your message: ")

    

#     print(f"Your {cipher_type} {mode}ed message: {result}")