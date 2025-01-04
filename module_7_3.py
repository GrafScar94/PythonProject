import io
from pprint import pprint

class WordsFinder:
    def __init__(self, *files):
        file_names = []
        for i in files:
            file_names.append(i)
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punct = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for txt in self.file_names:
            list_of_words = []
            with open(txt, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for char in line:
                        if char in punct:
                            words = line.replace(char, '')
                        else:
                            words = line
                    list_of_words += words.split()
            all_words.update({txt: list_of_words})
        return all_words

    def find(self, word):
        dict_ = {}
        for txt in self.file_names:
            words = self.get_all_words()[txt]
            for i in range(len(words)):
                if word.lower() == words[i]:
                    dict_.update({txt: i+1})
                    break
        return dict_

    def count(self, word):
        dict_ = {}
        for txt in self.file_names:
            words = self.get_all_words()[txt]
            dict_.update({txt: words.count(word.lower())})
        return dict_




finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))

