__author__ = 'aferraz'

import unittest
from Document import Document
from VectorSpaceModel import VectorSpaceModel
from BagOfDocuments import BagOfDocuments
from BagOfWords import BagOfWords

class VectorSpaceModelUnitTest(unittest.TestCase):

    def test_rankDocs(self):
        d1 = Document("news about")
        d2 = Document("news about organic food campaign")
        d3 = Document("news of presidential campaign")
        d4 = Document("news of presidential campaign presidential candidate ")
        d5 = Document("news of organic food campaign campaign campaign campaign")

        bod = BagOfDocuments()
        bod.addDoc(d1)
        bod.addDoc(d2)
        bod.addDoc(d3)
        bod.addDoc(d4)
        bod.addDoc(d5)

        bow = BagOfWords(bod)

        vsm = VectorSpaceModel(bow, bod)
        query = Document("news about presidential campaign")
        vsm.rankDocs(query)
        vsm.printRank()

if __name__ == '__main__':
    unittest.main()
