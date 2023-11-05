import string


def prepare_key(key):
    key = key.replace(" ", "").upper()

    key = "".join(dict.fromkeys(key))

    remaining_chars = [ch for ch in string.ascii_uppercase +
                       string.digits + string.punctuation if ch not in key]
    key += "".join(remaining_chars)

    return key


def create_playfair_matrix(key):
    key = prepare_key(key)
    matrix = [['' for _ in range(8)] for _ in range(8)]
    char_index = 0

    for row in range(8):
        for col in range(8):
            if char_index < len(key):
                matrix[row][col] = key[char_index]
                char_index += 1

    return matrix


def prepare_message(message):
    message = message.upper()
    message = message.replace("J", "I")  # Replace 'J' with 'I'
    # Remove non-alphanumeric characters
    message = "".join(filter(str.isalnum, message))

    # Make the message length even by adding an 'X' at the end if necessary
    if len(message) % 2 != 0:
        message += 'X'

    return message


def find_char_position(matrix, char):
    for row in range(8):
        for col in range(8):
            if matrix[row][col] == char:
                return row, col


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


key = input("KEY : ")
key = "".join(key.upper().split(" "))
print("Key : ", key)
message = input("MESSAGE : ")
encrypted_message = encrypt_playfair(message, key)
print("Encrypted Message:", encrypted_message)

decrypted_message = decrypt_playfair(encrypted_message, key)
print("Decrypted Message:", decrypted_message)
