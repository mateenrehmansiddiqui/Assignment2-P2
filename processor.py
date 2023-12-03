#PROCESSOR CLASS

class PROCESSOR:

    def __init__(self, inputTextFile):
        self.inputTextFile = inputTextFile
        self.outputTextFile = 'outputFile2.txt'


    def bufferMethod(self):

        bufferLinearArray = []

        with open(self.inputTextFile.fileGetter(), 'r') as file:

            for i in file.read():

                if i == "\n":

                    pass

                else:
                    
                    bufferLinearArray.append(i)

            bufferLinearArray.append("$")

        return bufferLinearArray
    

    
    def fileWriteandRead(self, buffer):

        with open(self.outputTextFile, 'w') as file:

            file.write(str(buffer))

        print("".join(buffer))



    def fileGetter(self):

        return self.outputTextFile
