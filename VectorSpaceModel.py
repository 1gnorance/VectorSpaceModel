__author__ = 'aferraz'

from scipy import sparse
import operator

class VectorSpaceModel:
    docsVector = []
    similarity = []
    bagOfWords = None
    bagOfDocuments = None

    def __init__(self, bagOfWords, bagOfDocuments):
        self.bagOfWords = bagOfWords
        self.bagOfDocuments = bagOfDocuments
        self.createDocsVector()

    def createDocsVector(self):
        for doc in self.bagOfDocuments.arrDocuments:
            self.addDoc(doc)

    def getDocVector(self, index):
        return self.docsVector[index]

    def addDoc(self, doc):
        sparseDocArr = self.createVector(doc)
        self.docsVector.append(sparseDocArr)

    def createVector(self, doc):
        sparseDocArr = sparse.lil_matrix((1, self.bagOfWords.len()))

        words = doc.arrWords
        for word in words:
            sparseDocArr[0, self.bagOfWords.getPositionOfWord(word)] = doc.termFrequency(word)*self.bagOfDocuments.inverseDocumentFrequency(word)

        return sparseDocArr

    def rankDocs(self, query):
        queryVector = self.createVector(query)

        for i, docVector in enumerate(self.docsVector):
            similaridade = docVector.dot(queryVector.transpose())[0, 0]
            self.similarity.append((self.bagOfDocuments.arrDocuments[i], similaridade))

    def getRank(self):
        return sorted(self.similarity,key=lambda x: x[1], reverse=True)

    def printRank(self, limit=10):
        i = 0
        ordered = sorted(self.similarity,key=lambda x: x[1], reverse=True)
        for o in ordered:
            if i == limit:
                break
            print "Doc[" + str(i) + "] = " + str(ordered[i])
            i += 1