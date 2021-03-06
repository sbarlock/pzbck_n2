import numpy as np


def char_position(lookup_text, char_value):
    """ Computes the position of a given char in a string
    The position is the index (starting from 0) in the sting if the char exsits. Otherwise, the function
    returns -1.

        Args:
            lookup_text (char array): String in which the char must be found
            char_value (char): The char to be found

        Returns:
            char_first_position (int): Index position of the first appearance of the char in the string
    """

    char_first_position = np.where(lookup_text == char_value)
    # If the char does not exist in the string return -1
    if len(char_first_position[0]) == 0:
        return -1
    # Else, return the first found position
    else:
        return char_first_position[0][0]


def encrypt_book(plain_text, secret_key):
    """ Encrypt a string following the method described in the book.

        Args:
            plain_text (string): String containig the plain text to be encrypted
            secret_key (string): String containing the secret key to encrypt with

        Returns:
            cipher_text (string): Encrypted plain text
    """

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


def crack_next_char(known_plain_text, cipher_text, secret_key):
    """ Crack the next char of a cipher text
    Knowing the secret key and the first n char of the plain text, determine char n+1 of plain text

        Args:
            known_plain_text (string): String containig the plain text alredy known (char [0 to n])
            cipher_text (string): String containing the full length cipher text
            secret_key (string): String containing the secret key to encrypt with

        Returns:
            current_trial_plain_text (string): String containig the plain text with an aditionnal char ([0 to n+1])
    """

    # The plain text char can only belong to the secret_key,
    # build a array containing all those possible chars.
    vocabulary = np.unique(np.array(list(secret_key)))
    # Cut cipher text to the length of known plain text plus one char to crack
    cipher_with_next_char = cipher_text[0:len(known_plain_text)+1]

    # Iterate through possible plain text chars and stop when the encypted plain text
    # is the same than the cipher text.
    for vocabulary_index in range(len(vocabulary)):
        current_trial_plain_text = known_plain_text + vocabulary[vocabulary_index]
        cracked_text = encrypt_book(current_trial_plain_text, secret_key)
        if cracked_text == cipher_with_next_char:
            return current_trial_plain_text


def crack_full_sentence(cipher_text, secret_key):
    """ Iteratively crack a cipher_text
    The first char of the plain text is known due to the cipher properties. The crack_next_char
    function is called iteratively, cracking one char at a time

        Args:
            cipher_text (string): String containing the full length cipher text
            secret_key (string): String containing the secret key to encrypt with

        Returns:
            known_plain_text (string): String containig the recovered plain text
    """

    known_plain_text = cipher_text[0]
    for i in range(len(cipher_text) - 1):
        known_plain_text = crack_next_char(known_plain_text, cipher_text, secret_key)
    return known_plain_text


if __name__ == '__main__':
    sentence_to_crack = 'tsdmueyuvrxIedqqfmdqweIyaaxtiyzrujqezxqdawgotw'
    known_secret_key = 'nymphsblitzquIckvexdwarfjog.'
    print(crack_full_sentence(sentence_to_crack, known_secret_key))
