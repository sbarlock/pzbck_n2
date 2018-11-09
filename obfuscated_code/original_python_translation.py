import numpy as np


def encrypt_book(plain_text):
    secret_key = 'nymphsblitzquIckvexdwarfjob'
    internal_key = secret_key
    n = 28
    i = 0
    cipher_text = ''

    secret_key_array = np.array(list(secret_key))

    while i < len(plain_text):
        plain_char_pos_in_secret = np.where(secret_key_array == plain_text[i])[0][0]
        internal_char_pos_in_secret = np.where(secret_key_array == internal_key[i % len(internal_key)])[0][0]
        z = (plain_char_pos_in_secret + internal_char_pos_in_secret) % n
        cipher_text = cipher_text + secret_key[z]

        if plain_char_pos_in_secret+1 == n:
            internal_key = cipher_text
        i += 1
    return cipher_text


if __name__ == '__main__':
    test_wd = 'tadum'
    test_wd_enc = encrypt_book(test_wd)
    print(test_wd_enc)
    print(str(len(test_wd)) + '/' + str(len(test_wd_enc)))

#aim find: tsdmueyuvrxIedqqfmdqweIyaaxtiyzrujqezxqdawgotw