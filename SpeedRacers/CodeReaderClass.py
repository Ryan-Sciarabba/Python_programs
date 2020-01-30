class CodeParser():

    #Parsing variables
    PORT = ''
    OPERATION = ''
    NUMBER = ''

    #Parsing libraries (or "keywords" if you wanna not sound like an arrogant prick)
    OPERATIONS = ['+', '-', '*', '/', '=']
    NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    WHITESPACE = ' '
    PORTS = ["THROTTLE", "TURN"]


    #Initialize the CodeParser
    def __init__(self, path):
        self.SPEED = 0
        self.ANGLE = 0

        #Open racer file
        self.racer = open(self.path, "r")

        #Read lines in
        if self.racer.mode == "r":
            self.code = self.racer.readlines()


    #Analyze
    def analyzer(self):

        #Break down lines into individual parts
        lexeme = ''
        
            #For each line in the .txt file reset all stored variables then...
            for line in self.code:
                self.PORT = ''
                self.OPERATION = ''
                self.NUMBER = ''
                lexeme = ''

                #For each character in the line...
                for i, char in enumerate(line):

                    #If the character does not equal whitespace add it to the word
                    if char != WHITESPACE:
                       lexeme += char

                    #If the character index is less than the length of the line and...
                    if (i + 1 < len(line)):

                        #If the character after i is whitespace or a newline check if the word is in "keywords"
                        if line[i + 1] == WHITESPACE or line[i + 1] == '\n':
                            if lexeme in PORTS:
                                self.PORT = lexeme
                            if lexeme in OPERATIONS:
                                self.OPERATION = lexeme
                            if bool([ele for ele in NUMBERS if(ele in lexeme)]):
                                self.NUMBER = lexeme

                            #Reset the word stored
                            lexeme = ''
                            
                    #If the index of the character is one less than the length of the line check if the word is in "keywords"
                    if (i == len(line) - 1):
                        if lexeme in PORTS:
                            self.PORT = lexeme
                        if lexeme in OPERATIONS:
                            self.OPERATION = lexeme
                        if bool([ele for ele in NUMBERS if(ele in lexeme)]):
                            self.NUMBER = lexeme

                        #Reset the word stored
                        lexeme = ''

                #Parse the line of code   
                self.oprSwitch()

                
                print('Speed: %d' % self.SPEED)
                print('Angle: %d' % self.ANGLE)
                
            self.racer.close()


    #Function to add number to port
    def addPort(self):
        
        if self.PORT == "THROTTLE":
            self.SPEED = self.SPEED + int(self.NUMBER)
            
        if self.PORT == "TURN":
            self.ANGLE = self.ANGLE + int(self.NUMBER)


    #Function to subtract number from port 
    def subPort(self):

        if self.PORT == "THROTTLE":
            self.SPEED = self.SPEED - self.NUMBER
            
        if self.PORT == "TURN":
            self.ANGLE = self.ANGLE - self.NUMBER


    #Function to multply port by number
    def mltPort(self):

        if self.PORT == "THROTTLE":
            self.SPEED = self.SPEED * self.NUMBER
            
        if self.PORT == "TURN":
            self.ANGLE = self.ANGLE * self.NUMBER

        
    #Function to divide port by number    
    def divPort(self):

        if self.PORT == "THROTTLE":
            self.SPEED = self.SPEED / self.NUMBER
            
        if self.PORT == "TURN":
            self.ANGLE = self.ANGLE / self.NUMBER


    #Function to set port to number
    def setPort(self):

        if self.PORT == "THROTTLE":
            self.SPEED = self.NUMBER
            
        if self.PORT == "TURN":
            self.ANGLE = self.NUMBER


    #Switch to correct function
    def oprSwitch(self):

        #Cast variables to ints
        self.NUMBER = int(self.NUMBER)
        self.ANGLE = int(self.ANGLE)
        self.SPEED = int(self.SPEED)

        #Switcherrrrr
        oprSwitcher = {
            1: self.mltPort,
            2: self.addPort,
            4: self.subPort,
            6: self.divPort,
            20: self.setPort
            }

        #Turn ascii operation into numeral and then go to the switch
        self.nOperation = ord(self.OPERATION) - 41
        f = oprSwitcher.get(self.nOperation, "invalid operation")
        f()

#This is just for testing and running the code
#green = CodeParser()
#CodeParser.__init__
