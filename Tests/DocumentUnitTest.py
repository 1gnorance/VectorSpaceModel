__author__ = 'aferraz'

import unittest
import string
from Document import Document

class BagOfDocumentsUnitTest(unittest.TestCase):

    def test_numOfWords(self):
        d = Document("teste teste teste.zica teste")
        self.assertEqual(d.numOfWords(),5, "Contagem de palavras")

    def test_removePunctuation(self):
        d = Document(".,!?")
        self.assertEqual(d.numOfWords(),0, "Remocao de pontuacao")

    def test_termFrequency(self):
        d = Document("teste teste teste.zica teste")
        self.assertEqual(d.termFrequency("teste"),4, "Term frequency")

if __name__ == '__main__':
    unittest.main()
