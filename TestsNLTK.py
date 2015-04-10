__author__ = 'aferraz'

import nltk
#C:\Users\h162524\AppData\Roaming\nltk_data
#nltk.download()
#print nltk.corpus.gutenberg.fileids()
#print nltk.corpus.machado.fileids()

machado001 = nltk.Text(nltk.corpus.machado.words('contos/macn001.txt'))
print len(machado001)
print machado001.concordance("fluminense")