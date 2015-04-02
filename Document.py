__author__ = 'aferraz'

import string

class Document:
    text = ""
    arrWords = []

    def __init__(self, text):
        self.text = text;
        self.arrWords = self.removePunctuation(text).split()

    def numOfWords(self):
        return len(self.arrWords)

    def removePunctuation(self, text):
        exclude = set(string.punctuation)
        return ''.join(ch for ch in text if ch not in exclude)

    def termFrequency(self, word):
        return self.arrWords.count(word)
