"""
Caesar cipher
Implement a Caesar cipher, both encoding and decoding. The key is an integer
from 1 to 25. This cipher rotates the letters of the alphabet (A to Z). The
encoding replaces each letter with the 1st to 25th next letter in the alphabet
(wrapping Z to A). So key 2 encrypts "HI" to "JK", but key 20 encrypts "HI" to
"BC". This simple "substitution cipher" provides almost no
security, because an attacker who has the encoded message can either use
frequency analysis to guess the key, or just try all 25 keys.
"""


class Caesar:
    """Caesar Class"""

    def __init__(self):
        # noinspection SpellCheckingInspection
        self.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.translated = ''
        self.key = 'key'
        self.message = 'message'

    def __crypt(self, mode):
        for symbol in self.message.upper():
            if symbol in self.letters:
                num = self.letters.find(symbol)
                if mode == 'encrypt':
                    num += self.key
                elif mode == 'decrypt':
                    num -= self.key

                if num >= len(self.letters):
                    num -= len(self.letters)
                elif num < 0:
                    num += len(self.letters)

                self.translated += self.letters[num]
            else:
                self.translated += symbol

        return self.translated

    def encrypt(self, message, key=0):
        """
        :param message:
        :param key:
        :return:
        """
        self.translated = ''
        self.key = key
        self.message = message
        return self.__crypt('encrypt')

    def decrypt(self, message, key=0):
        """
        :param message:
        :param key:
        :return:
        """
        self.translated = ''
        self.key = key
        self.message = message
        return self.__crypt('decrypt')


if __name__ == '__main__':
    CIPHER = Caesar()
    print(CIPHER.encrypt(message='Secret message.', key=13))
    # noinspection SpellCheckingInspection
    print(CIPHER.decrypt(message='FRPERG ZRFFNTR.', key=13))
