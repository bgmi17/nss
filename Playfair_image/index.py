import numpy as np
from PIL import Image
from functools import reduce

def unique(list1):
    ans = reduce(lambda re, x: re+[x] if x not in re else re, list1, [])
    return ans

def create_key(key):
    key = unique(key)
    for i in np.arange(255,-1,-1).tolist():
        if i not in key:
            key.append(i)
    key = np.asarray(key).reshape((16,16))
    return key

def find_char_position(matrix, char):
    for row in range(16):
        for col in range(16):
            if matrix[row][col] == char:
                return row, col

def encrypt_playfair(message, key):
    matrix = create_key(key)
    encrypted_message = []
    i = 0

    while i < len(message):
        char1 = message[i]
        i += 1
        char2 = message[i]
        i += 1
        row1, col1 = find_char_position(matrix, char1)
        row2, col2 = find_char_position(matrix, char2)

        if row1 == row2:
            encrypted_message.append(matrix[row1][(col1 + 1) % 16])
            encrypted_message.append(matrix[row2][(col2 + 1) % 16])
        elif col1 == col2:
            encrypted_message.append(matrix[(row1 + 1) % 16][col1])
            encrypted_message.append(matrix[(row2 + 1) % 16][col2])
        else:
            encrypted_message.append(matrix[row1][col2])
            encrypted_message.append(matrix[row2][col1])

    return encrypted_message

import random
key = [random.randint(0,255) for i in range(255)]
print(key)

image = Image.open('/content/download.jpg')
image = image.resize((224,224))
image = np.asarray(image)












Image.fromarray(image)
def channelSplit(image):
    return np.dsplit(image,image.shape[-1])

[B,G,R]=channelSplit(image)
b = np.asarray(encrypt_playfair(B.reshape((-1)).tolist(),key)).reshape((224,224))
g = np.asarray(encrypt_playfair(G.reshape((-1)).tolist(),key)).reshape((224,224))
r = np.asarray(encrypt_playfair(R.reshape((-1)).tolist(),key)).reshape((224,224))

image = np.array(np.dstack((b,g,r)),dtype=np.uint8)
Image.fromarray(image)

def decrypt_playfair(encrypted_message, key):
    matrix = create_key(key)

    decrypted_message = []
    i = 0

    while i < len(encrypted_message):
        char1 = encrypted_message[i]
        i += 1
        char2 = encrypted_message[i]
        i += 1

        row1, col1 = find_char_position(matrix, char1)
        row2, col2 = find_char_position(matrix, char2)

        if row1 == row2:
            decrypted_message.append(matrix[row1][(col1 - 1) % 16])
            decrypted_message.append(matrix[row2][(col2 - 1) % 16])
        elif col1 == col2:
            decrypted_message.append(matrix[(row1 - 1) % 16][col1])
            decrypted_message.append(matrix[(row2 - 1) % 16][col2])
        else:
            decrypted_message.append(matrix[row1][col2])
            decrypted_message.append(matrix[row2][col1])

    return decrypted_message

[B,G,R]=channelSplit(image)
print(B.shape)
b = np.asarray(decrypt_playfair(B.reshape((-1)).tolist(),key)).reshape((224,224))
g = np.asarray(decrypt_playfair(G.reshape((-1)).tolist(),key)).reshape((224,224))
r = np.asarray(decrypt_playfair(R.reshape((-1)).tolist(),key)).reshape((224,224))

image = np.array(np.dstack((b,g,r)),dtype=np.uint8)
Image.fromarray(image)