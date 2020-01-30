class CodeParser():

    #Parsing variables
    PORT = ''
    OPERATION = ''
    NUMBER = ''
    JUMP = ''
    FUNC = ''
    FUNCTIONS = []

    path = ''
    speed = 0
    angle = 0

    #Parsing libraries (or "keywords" if you wanna not sound like an arrogant prick)
    OPERATIONS = ['+', '-', '*', '/', '=']
    NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    WHITESPACE = ' '
    PORTS = ["THROTTLE", "TURN"]


    #Initialize the CodeParser
    def __init__(self, path):
        self.path = "Racer.txt"
        self.SPEED = 0
        self.ANGLE = 0

        #Open racer file
        self.racer = open(self.path, "r")

        #Read lines in
        if self.racer.mode == "r":
            self.code = self.racer.readlines()

        self.analyzer()


    #Analyze
    def analyzer(self):

        for self.lineNum, self.line in enumerate(self.code):
            self.terms = self.line.split()
            if len(self.terms) == 3:   
                self.PORT = self.terms[0]
                self.OPERATION = self.terms[1]
                self.NUMBER = self.terms[2]

                #Parse the line of code   
                self.oprSwitch()

            if len(self.terms) == 2:
                self.JUMP = self.terms[0]
                self.FUNC = self.terms[1]
                print("Jumping")
                self.jump()

            if len(self.terms) == 1:
                self.FUNCTIONS.append(self.terms[0])
            print(self.speed)
                
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

    #Function to jump to spcific line
    def jump(self):
        
        for num, i in enumerate(self.code):
            if self.FUNC == i:
                self.line = num
        self.lineNum = 0

#This is just for testing and running the code
green = CodeParser("racer.txt")
CodeParser.__init__
