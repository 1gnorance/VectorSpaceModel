__author__ = 'aferraz'

import math

class BagOfDocuments:

    arrDocuments = []

    def addDoc(self, document):
        self.arrDocuments.append(document)

    def numOfDocuments(self):
        return len(self.arrDocuments)

    def inverseDocumentFrequency(self, word):
        return math.log10(self.numOfDocuments()/(self.numberOfDocumentsThatContains(word)+1))

    def numberOfDocumentsThatContains(self, word):
        result = [i for i,doc in enumerate(self.arrDocuments) if doc.termFrequency(word) > 0]
        return len(result)