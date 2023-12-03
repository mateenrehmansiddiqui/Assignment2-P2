#MAIN CLASS FOR MAKING OBJECTS AND CALLING METHODS

from pre_processor import PREPROCESSOR
from processor import PROCESSOR
from lexical_analyser import LEXICAL_ANALYZER


ObjectPreProcessor = PREPROCESSOR(r"/Users/mateen_siddiqui/Desktop/University/P2 - COMP111/Programming II Assignment 2/input1.txt")
removeBlankLines = ObjectPreProcessor.removeBlankLines()
removeComments = ObjectPreProcessor.removeComments(removeBlankLines)
removeImportStatements = ObjectPreProcessor.removeImportStatements(removeComments)
removeAnnotations = ObjectPreProcessor.eliminateAnnotations(removeImportStatements)
ObjectPreProcessor.fileWriteandRead(removeAnnotations)
print()
ObjectProcessor = PROCESSOR(ObjectPreProcessor)
bufferMethod = ObjectProcessor.bufferMethod()
ObjectProcessor.fileWriteandRead(bufferMethod)
print()
ObjectLexicalAnalyser = LEXICAL_ANALYZER(ObjectProcessor)
ObjectLexicalAnalyser.findingLexemes()