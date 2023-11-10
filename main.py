"""
author: assaf dor
description:
    paramter encrypt: receives input encrypts it and put in a file.
    paramter decrypt: decrypts encrypted cypher in file and prints it.
"""
import sys

encryption_table = {
    'A': '56', 'J': '45', 'S': '64', 'b': '13', 'k': '32', 't': '91',
    '.': '100', 'B': '57', 'K': '46', 'T': '65', 'c': '14', 'l': '33',
    'u': '92', ';': '101', 'C': '58', 'L': '47', 'U': '66', 'd': '15',
    'm': '34', 'v': '93', "'": '102', 'D': '59', 'M': '48', 'V': '67',
    'e': '16', 'n': '35', 'w': '94', '?': '103', 'E': '40', 'N': '49',
    'W': '68', 'f': '17', 'o': '36', 'x': '95', '!': '104', 'F': '41',
    'O': '60', 'X': '69', 'g': '18', 'p': '37', 'y': '96', ':': '105',
    'G': '42', 'P': '61', 'Y': '10', 'h': '19', 'q': '38', 'z': '97',
    'H': '43', 'Q': '62', 'Z': '11', 'i': '30', 'r': '39', ' ': '98',
    'I': '44', 'R': '63', 'a': '12', 'j': '31', 's': '90', ',': '99',
}

decryption_table = {value: key for key, value in encryption_table.items()}


def encrypt(message):
    encrypted_message = []
    for char in message:
        if char in encryption_table:
            encrypted_message.append(encryption_table[char])
    return ','.join(encrypted_message)


def decrypt(encrypted_message):
    decrypted_message = ''
    encrypted_chars = encrypted_message.split(',')
    for char_code in encrypted_chars:
        if char_code in decryption_table:
            decrypted_message += decryption_table[char_code]
    return decrypted_message


def main():
    if len(sys.argv) != 2:
        print("wrong data input, input encrypt/decrypt")
        print(sys.argv)
        return

    operation = sys.argv[1]

    if operation == 'encrypt':
        message = input("Enter a message to encrypt: ")
        encrypted_message = encrypt(message)
        with open("encrypted_msg.txt", 'w') as file:
            file.write(encrypted_message)
        print(f"Encrypted message saved in 'encrypted_msg.txt'")
    elif operation == 'decrypt':
        with open("encrypted_msg.txt", 'r') as file:
            encrypted_message = file.read()
        decrypted_message = decrypt(encrypted_message)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid operation. Use 'encrypt' or 'decrypt'.")


if __name__ == '__main__':
    main()
