__author__ = 'aferraz'

from scipy import sparse

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

        for docVector in self.docsVector:
            similaridade = docVector.dot(queryVector.transpose())[0, 0]
            self.similarity.append(similaridade)

    def printRank(self):
        i = 0
        for docVector in self.docsVector:
            print "Doc[" + str(i) + "] = " + str(self.similarity[i])
            i += 1