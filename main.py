#coding:utf-8
__author__ = 'aferraz'

import string
from BagOfDocuments import BagOfDocuments
from BagOfWords import BagOfWords
from VectorSpaceModel import VectorSpaceModel
from Document import Document

print "------------------------------------"

bod = BagOfDocuments()
bod.addDoc(Document("Site oficial da campanha de Dilma Rousseff a reeleicao presidencial. Dilma presidente".lower()))
bod.addDoc(Document("Conheca a biografia e trajetoria politica de Dilma Rousseff".lower()))
bod.addDoc(Document("Entenda por que Dilma Rousseff nao pode ser vista como faxineira da corrupcao".lower()))
bod.addDoc(Document("O governo Dilma Rousseff começou sob o signo da corrupcao".lower()))
bod.addDoc(Document("Federais desmentem Dilma no JN, e revelam interferencia do governo para reduzir combate à corrupcao".lower()))
bod.addDoc(Document("Compare as propostas de governo de Dilma e Aecio".lower()))
bod.addDoc(Document("Dilma uma cadeirante que precisa de sua ajuda".lower()))
bod.addDoc(Document("Aecio um cartola do futebol".lower()))

bod.numberOfDocumentsThatContains("aecio")

bof = BagOfWords(bod)
vsm = VectorSpaceModel(bof, bod)
query = Document("presidente dilma corrupcao")
vsm.rankDocs(query)
vsm.printRank()