import string
import numpy as np
from PIL import Image

def prepare_key(key):
    # Remove whitespaces and convert to uppercase
    key = key.replace(" ", "").upper()

    # Remove duplicate characters while maintaining the order
    key = "".join(dict.fromkeys(key))

    # Add remaining characters (letters, numbers, and special characters) to the key
    remaining_chars = [chr(ch) for ch in np.arange(255,-1,-1).tolist() if chr(ch) not in key]
    key += "".join(remaining_chars)

    return key

def create_playfair_matrix(key):
    key = prepare_key(key)
    matrix = [['' for _ in range(16)] for _ in range(16)]
    char_index = 0

    for row in range(16):
        for col in range(16):
            if char_index < len(key):
                matrix[row][col] = key[char_index]
                char_index += 1

    return matrix


def prepare_message(message):
    message = message.upper()
    message = message.replace("J", "I")  # Replace 'J' with 'I'
    message = "".join(filter(str.isalnum, message))  # Remove non-alphanumeric characters

    # Make the message length even by adding an 'X' at the end if necessary
    if len(message) % 2 != 0:
        message += 'X'

    return message

def encrypt_playfair(message, key):
    matrix = create_playfair_matrix(key)
    message = prepare_message(message)

    encrypted_message = ""
    i = 0

    while i < len(message):
        char1 = message[i]
        i += 1
        char2 = message[i]
        i += 1

        row1, col1 = find_char_position(matrix, char1)
        row2, col2 = find_char_position(matrix, char2)

        if row1 == row2:
            encrypted_message += matrix[row1][(col1 + 1) % 8]
            encrypted_message += matrix[row2][(col2 + 1) % 8]
        elif col1 == col2:
            encrypted_message += matrix[(row1 + 1) % 8][col1]
            encrypted_message += matrix[(row2 + 1) % 8][col2]
        else:
            encrypted_message += matrix[row1][col2]
            encrypted_message += matrix[row2][col1]

    return encrypted_message

def decrypt_playfair(encrypted_message, key):
    matrix = create_playfair_matrix(key)

    decrypted_message = ""
    i = 0

    while i < len(encrypted_message):
        char1 = encrypted_message[i]
        i += 1
        char2 = encrypted_message[i]
        i += 1

        row1, col1 = find_char_position(matrix, char1)
        row2, col2 = find_char_position(matrix, char2)

        if row1 == row2:
            decrypted_message += matrix[row1][(col1 - 1) % 8]
            decrypted_message += matrix[row2][(col2 - 1) % 8]
        elif col1 == col2:
            decrypted_message += matrix[(row1 - 1) % 8][col1]
            decrypted_message += matrix[(row2 - 1) % 8][col2]
        else:
            decrypted_message += matrix[row1][col2]
            decrypted_message += matrix[row2][col1]

    return decrypted_message

def find_char_position(matrix, char):
    for row in range(8):
        for col in range(8):
            if matrix[row][col] == char:
                return row, col

image = Image.open('download.jpg')
np.asarray(image).shape

def channelSplit(image):
    return np.dsplit(image,image.shape[-1])

[B,G,R]=channelSplit(image)
G