import string

print("Caeser Cipher Running!")

alphabet_list = list(string.ascii_lowercase)

user_input = "hellozz"
offset = 53

def encrypt_msg(msg):
    print("Encrypting")

    cipher_text = ""

    for letter in msg:

        letter_index = alphabet_list.index(letter)


        cipher_offset = letter_index + offset

        while cipher_offset >= len(alphabet_list)-1:
            cipher_offset -= len(alphabet_list)

        cipher_letter = alphabet_list[cipher_offset]

        cipher_text += cipher_letter

    return cipher_text

def decrypt_msg(msg):
    print("Decrypting")
    plain_text = ""

    for letter in msg:
        cipher_text_index = alphabet_list.index(letter)

        cipher_offset = cipher_text_index - offset

        while cipher_offset <= 0:
            cipher_offset += len(alphabet_list)

        plain_text_letter = alphabet_list[cipher_offset]

        plain_text += plain_text_letter

    return plain_text


cipher_text = encrypt_msg(user_input)

print("-> {}".format(cipher_text))
print("-> {}".format(decrypt_msg(cipher_text)))
