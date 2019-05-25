"""
Reverse a String - Enter a string and the program will reverse it and print it out.

Pig Latin - Pig Latin is a game of alterations played on the English language game.
To create the Pig Latin form of an English word the initial consonant sound is transposed
to the end of the word and an ay is affixed.

Count Vowels - Enter a string and the program counts the number of vowels in the text.
For added complexity have it report a sum of each vowel found.

Check if Palindrome - Checks if the string entered by the user is a palindrome.
That is that it reads the same forwards as backwards.

Count Words in a String - Counts the number of individual words in a string.
For added complexity read these strings in from a text file and generate a summary.
"""


class MyString:
    """
    Class that store strings
    """
    @staticmethod
    def reverse(some_seq):
        """
        :param some_seq: Sequence
        :return: Sequence: reversed version
        """
        return some_seq[::-1]

    @staticmethod
    def count_vowels(vowel_str):
        """
        :param vowel_str: String
        :return: Integer: No. of vowels or 0
        """
        vowels = "aeiou"
        count = {char: 0 for char in vowels}
        for char in vowel_str:
            if char in vowels:
                count[char] += 1
        return count

    def is_palindrome(self, some_seq):
        """
        :param some_seq: sequence of anything
        :return: Boolean: palindrome check of sequence passed
        """
        return some_seq == self.reverse(some_seq)

    @staticmethod
    def count_words(word_str=None, file=None):
        """
        :param word_str:    A string
        :param file:      A file to be read
        """
        word_count = 0
        if word_str:
            word_count = len(word_str.split())
        if file:
            with open(file) as f_str:
                word_count = len(f_str.read().split())
        return word_count

    def find_in_iter(self, some_iter):
        """just an example for someone."""
        return self.str_iter(some_iter) if isinstance(some_iter, str) \
            else self.int_iter(some_iter) if isinstance(some_iter[0], int) else None

    @staticmethod
    def str_iter(iteration):
        """str"""

        def cond(sequence, con_str):
            """cond"""
            return [char for char in con_str if char in sequence]

        vowels = "a,e,i,o,u"
        return [word for word in iteration.lower().split(" ") if len(cond(vowels, word)) > 1]

    @staticmethod
    def int_iter(iteration):
        """int"""
        return [num for num in iteration if num > 5]

    @staticmethod
    def pig_latin(pig_str):
        """
        Pig Latin – Pig Latin is a game of alterations played on the English language game.
        To create the Pig Latin form of an English word the initial consonant sound is transposed
        to the end of the word and an ay is affixed
        """
        words = []
        vowels = 'aeiou'
        for word in pig_str.split():
            if len(word) > 2 and word[0] not in vowels:
                words.append(word[1:] + '-' + word[0] + 'ay')
            else:
                words.append(word + '-ay')
        return ' '.join(words)


if __name__ == '__main__':
    X = input("Type Something: ")
    STR = MyString()
    print("Reversed sequence is: ", STR.reverse(X))
    print("Amount of vowels are: ", STR.count_vowels(X))
    print("Is the word palindrome: ", STR.is_palindrome(X))
    print("Amount of words are: ", STR.count_words(X))
    print("The iterations are: ", STR.find_in_iter(X))
    print("The pig latins are: ", STR.pig_latin(X))
