class CodeParser():

    #Parsing variables
    PORT = ''
    OPERATION = ''
    NUMBER = ''

    #Parsing libraries
    OPERATIONS = ['+', '-', '*', '/', '=']
    NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    WHITESPACE = ' '
    PORTS = ["THROTTLE", "TURN"]
    
    #Ports to be modified
    SPEED = 0
    ANGLE = 0
    
    def __init__(self, path="Racer.txt"):
        
        
    def main(self):
        
        #Open racer file
        self.racer = open(self.path, "r")

        #Break down symbols together
        self.lexeme = ''
        if self.racer.mode == "r":
            self.code = self.racer.readlines()
            for self.line in self.code:
                self.PORT = ''
                self.OPERATION = ''
                self.NUMBER = ''
                self.lexeme = ''
                for self.i, self.char in enumerate(self.line):
                    if self.char != self.WHITESPACE:
                       self.lexeme += self.char
                    if (self.i + 1 < len(self.line)):
                        if self.line[self.i + 1] == self.WHITESPACE or self.line[self.i + 1] == '\n':
                            if self.lexeme in self.PORTS:
                                self.PORT = self.lexeme
                            if self.lexeme in self.OPERATIONS:
                                self.OPERATION = self.lexeme
                            if bool([self.ele for self.ele in self.NUMBERS if(self.ele in self.lexeme)]):
                                self.NUMBER = self.lexeme
                            self.lexeme = ''
                    if (self.i == len(self.line) - 1):
                        if self.lexeme in self.PORTS:
                            self.PORT = self.lexeme
                        if self.lexeme in self.OPERATIONS:
                            self.OPERATION = self.lexeme
                        if bool([self.ele for self.ele in self.NUMBERS if(self.ele in self.lexeme)]):
                            self.NUMBER = self.lexeme
                        self.lexeme = ''
                        
                oprSwitch()
                print('Speed: %d' % self.SPEED)
                print('Angle: %d' % self.ANGLE)

    def addPort(self):
        
        if self.PORT == "THROTTLE":
            self.SPEED = self.SPEED + int(self.NUMBER)
            
        if self.PORT == "TURN":
            self.ANGLE = self.ANGLE + int(self.NUMBER)
        
    def subPort(self):

        if self.PORT == "THROTTLE":
            self.SPEED = self.SPEED - self.NUMBER
            
        if self.PORT == "TURN":
            self.ANGLE = self.ANGLE - self.NUMBER
        
    def mltPort(self):

        if self.PORT == "THROTTLE":
            self.SPEED = self.SPEED * self.NUMBER
            
        if self.PORT == "TURN":
            self.ANGLE = self.ANGLE * self.NUMBER
        
        
    def divPort(self):

        if self.PORT == "THROTTLE":
            self.SPEED = self.SPEED / self.NUMBER
            
        if self.PORT == "TURN":
            self.ANGLE = self.ANGLE / self.NUMBER

    def setPort(self):

        if self.PORT == "THROTTLE":
            self.SPEED = self.NUMBER
            
        if self.PORT == "TURN":
            self.ANGLE = self.NUMBER
        
    def oprSwitch(self):

        self.NUMBER = int(self.NUMBER)
        self.ANGLE = int(self.ANGLE)
        self.SPEED = int(self.SPEED)
        
        oprSwitcher = {
            1: mltPort,
            2: addPort,
            4: subPort,
            6: divPort,
            20: setPort
            }

        self.nOperation = ord(slef.OPERATION) - 41
        f = oprSwitcher.get(self.nOperation, "invalid operation")
        f()

green = CodeParser()
CodePartser.__init__
