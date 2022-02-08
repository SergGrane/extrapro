# Create a class that performs statistical processing of a text file - counting characters, words, sentences, etc.
# Determine the required attributes-data and attributes-methods in class for working with the text file.

import os.path


class TextFileproc:

    """
    performs statistical processing of a text file
    - counting characters, words, sentences
    """

    def __init__(self, file_name: str):
        """
        constructor for opening and reading file
        :param file_name:
        """
        if not os.path.isfile(file_name):
            raise FileExistsError('No such file')
        self.f1 = open(file_name, 'r')
        self.st = ''
        for line in self.f1:
            self.st += line
        self.f1.close()

    def char_count(self):
        """
         counting chars in file
        :return:
        """

        return len(self.st.replace(' ', ''))

    def word_count(self):
        """
         counting words in file
        :return:
        """
        return len(self.st.split())

    def sentense_count(self):
        """
        counting sentences in file
        :return:
        """
        res = self.st.replace('!', '.')
        res = res.replace('?', '.')
        return len(res.split('.')) - 1

    def __str__(self):
        return self.st


if __name__ == '__main__':
        try:
            f = (TextFileproc('test.txt'))
            print(f)
            print(f.char_count())
            print(f.word_count())
            print(f.sentense_count())
        except Exception as error:
            print(error)

