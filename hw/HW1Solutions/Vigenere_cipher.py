"""
Assignment 1 question3 vigenere cipher solutions
"""
def vigenere_encrypt(plain, key):
    '''
    @plain: a python input string. The plain text.
    @key: a python input string. The key.

    @return: the cipher python string text.
    '''
    # To do
    ans = ""
    counter = 0
    for char in plain:
        ans += chr(ord('A') + (ord(char) + ord(key[counter]) - 2 * ord('A')) % 26)
        counter = (counter + 1) % len(key)
    return ans

def vigenere_decrypt(cipher, key):
    '''
    @cipher: a python input string. The cipher text.
    @key: a python input string. The key.

    @return: the plain python string text.
    '''
    # To do
    rev_key = ""
    for char in key:
        rev_key += chr(ord('A') + (ord('A') + 26 - ord(char)))
    return vigenere_encrypt(cipher, rev_key)



