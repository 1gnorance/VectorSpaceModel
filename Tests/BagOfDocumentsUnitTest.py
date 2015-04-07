__author__ = 'aferraz'

import unittest
from Document import Document
from BagOfDocuments import BagOfDocuments

class BagOfDocumentsUnitTest(unittest.TestCase):

    def test_inverseDocumentFrequency(self):
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

        idf = bod.inverseDocumentFrequency("news")
        self.assertAlmostEqual(idf, 0.0791812460476, 4)

if __name__ == '__main__':
    unittest.main()
