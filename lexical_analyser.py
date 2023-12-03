#LEXICAL ANALYSER 


class LEXICAL_ANALYZER:


    def __init__(self, inputTextFile):

        self.inputTextFile = inputTextFile
        self.keywords = ["and", "as", "assert", "break", "class", "continue", "def", 
                         "del", "elif", "else", "except", "False", "finally", "for", 
                         "from", "global", "if", "import", "in", "is", "lambda", "None", 
                         "nonlocal", "not", "or", "pass", "raise", "return", "True", "try", 
                         "while", "with", "yield"]
        self.operators = ["+", "-", "*", "/", "%", "=", "+=", "-=", "*=", "/=", "==", "!=", "<", ">", "<=", ">=", "and", "or", "not", "in", "is"]
        self.punctuators = ["{", "}", "[", "]", "(", ")", ",", ";", ":", "."]



    def findingLexemes(self):

        with open(self.inputTextFile.fileGetter(), 'r') as file:
    
            listInFile = file.read()
    
            evalOutputAsList = eval(listInFile)

            empty = ''

            matched = []

            for i in evalOutputAsList:

                if i.isalpha() or i == '_':

                    empty = empty + i

                elif empty:

                    matched.append(empty)
                    empty = ''

                    if i in self.operators or i in self.punctuators or i.isnumeric():

                        matched.append(i)

                else:
                    
                    if i in self.operators or i in self.punctuators or i.isnumeric():

                        matched.append(i)

        for lexeme in matched:

            print("Lexeme: " + lexeme)


                    



                    


