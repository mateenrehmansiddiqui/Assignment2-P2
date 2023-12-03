#PRE-PROCESSOR CLASS 

class PREPROCESSOR:

    def __init__(self, inputTextFile):
        self.inputTextFile = inputTextFile
        self.outputTextFile = 'outputFile.txt'
  

    def removeBlankLines(self):

        with open(self.inputTextFile, 'r') as file:

            dataInFileAsList = file.readlines()

            for eachLine in dataInFileAsList.copy():

                if eachLine == "\n":

                    dataInFileAsList.remove(eachLine)

            return dataInFileAsList
    
    
    def removeComments(self, linesList):

        for eachLine in linesList.copy():

            if "#" in eachLine:

                linesList.remove(eachLine)


        return linesList



    def removeImportStatements(self, linesList): 

        for eachLine in linesList.copy():

            if "import" in eachLine:

                linesList.remove(eachLine)

        return linesList
    
    
    def eliminateAnnotations(self, linesList): 

        for eachLine in linesList.copy():

            if "@" in eachLine:

                linesList.remove(eachLine)

        return linesList
    

    def fileWriteandRead(self, linesList):

        with open(self.outputTextFile, 'w') as file:

            file.writelines(linesList)

        with open(self.outputTextFile, 'r') as file:

            print(file.read())


    def fileGetter(self):

        return self.outputTextFile

