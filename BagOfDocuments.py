__author__ = 'aferraz'

import math

class BagOfDocuments:

    arrDocuments = []

    def addDoc(self, document):
        self.arrDocuments.append(document)

    def numOfDocuments(self):
        return len(self.arrDocuments)

    def inverseDocumentFrequency(self, word):
<<<<<<< Updated upstream
        return math.log10(self.numOfDocuments()/(self.numberOfDocumentsThatContains(word)+1))
=======
        return math.log10(float(self.numOfDocuments()+1)/self.numberOfDocumentsThatContains(word))
>>>>>>> Stashed changes

    def numberOfDocumentsThatContains(self, word):
        result = [i for i, doc in enumerate(self.arrDocuments) if doc.termFrequency(word) > 0]
        return len(result)