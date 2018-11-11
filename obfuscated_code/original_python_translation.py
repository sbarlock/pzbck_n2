import numpy as np


def char_position(lookup_text, char_value):
    char_first_position = np.where(lookup_text == char_value)
    if len(char_first_position[0]) == 0:
        return -1
    else:
        return char_first_position[0][0]


def encrypt_book(plain_text):
    secret_key = 'nymphsblitzquIckvexdwarfjog.'
    internal_key = secret_key
    n = 28
    i = 0
    cipher_text = ''

    secret_key_array = np.array(list(secret_key))

    while i < len(plain_text):
        plain_char_pos_in_secret = char_position(secret_key_array, plain_text[i])
        internal_char_pos_in_secret = char_position(secret_key_array, internal_key[i % len(internal_key)])
        z = (plain_char_pos_in_secret + internal_char_pos_in_secret) % n
        cipher_text = cipher_text + secret_key[z]

        if plain_char_pos_in_secret+1 == n:
            internal_key = cipher_text
        i += 1
    return cipher_text


def crack_next_char(known_plain_text, cipher_text, vocabulary):
    cipher_with_next_char = cipher_text[0:len(known_plain_text)+1]
    cracked_text = known_plain_text + '$'

    for vocabulary_index in range(len(vocabulary)):
        current_trial_plain_text = known_plain_text + vocabulary[vocabulary_index]
        cracked_text = encrypt_book(current_trial_plain_text)
        if cracked_text == cipher_with_next_char:
            return current_trial_plain_text


def crack_full_sentence(cipher_text, vocabulary):
    known_plain_text = cipher_text[0]
    for i in range(len(cipher_text) - 1):
        # print(known_plain_text)
        known_plain_text = crack_next_char(known_plain_text, cipher_text, vocabulary)
    return known_plain_text


if __name__ == '__main__':
    sentence_to_crack = 'tsdmueyuvrxIedqqfmdqweIyaaxtiyzrujqezxqdawgotw'
    print(crack_full_sentence(sentence_to_crack,
                              np.unique(np.array(list('nymphsblitzquIckvexdwarfjog.')))))