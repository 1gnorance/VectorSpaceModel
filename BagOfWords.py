__author__ = 'aferraz'

import operator

class BagOfWords:
    bagOfWords = {}

    def __init__(self, bagOfDocuments):
        self.createBagOfWords(bagOfDocuments)

    def createBagOfWords(self, bagOfDocuments):
        i = 0
        for doc in bagOfDocuments.arrDocuments:
            words = doc.arrWords
            for word in words:
                if word in self.bagOfWords:
                    continue

                self.bagOfWords[word.lower()] = i
                i += 1


    def addDocToBagWords(self, doc):
        i = max(self.bagOfWords.iteritems(), key=operator.itemgetter(1))[0]
        words = doc.arrWords
        for word in words:
            if word in self.bagOfWords:
                continue

            self.bagOfWords[word.lower()] = i
            i += 1

    def len(self):
        return len(self.bagOfWords)

    def getPositionOfWord(self, word):
        return self.bagOfWords[word]

    def show(self):
        sorted_x = sorted(self.bagOfWords.items(), key=operator.itemgetter(1))
        print type(sorted_x)
        print sorted_x