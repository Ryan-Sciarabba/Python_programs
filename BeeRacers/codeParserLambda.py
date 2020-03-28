from Bee_Memory import VM
import pickle

class CodeParser():

    bee = VM()
        
    def __init__(self, path):

        #Set line number to zero and initialize stack
        self.lineNum = 0
        self.functionLine = []
        
        #Open bee code file
        beeCode = open(path, "r")
        self.userCode = beeCode.readlines()
        beeCode.close()

        #Remove whitespace
        line = 0
        while line < len(self.userCode):
            terms = self.userCode[line].split()
            if len(terms) == 0:
                self.userCode.pop(line)
            else:
                line += 1
        
        #Save bee code as binary
        #binPath = path.replace(".txt", ".bin")
        #pickle.dump(self.userCode, open(binPath, "wb")
        #binPath.close()

        #Create bee VM
        self.bee.print_ram()
                    
    def parse(self):

        while self.lineNum < len(self.userCode):

            terms = self.userCode[self.lineNum].split()
            print(terms)

            if terms[0] == "add":
                if terms[1] == "SPEED":
                    self.bee.add(0, int(terms[2]))
                elif terms[1] == "ANGLE":
                    self.bee.add(1, int(terms[2]))

            elif terms[0] == "sub":
                if terms[1] == "SPEED":
                    self.bee.sub(0, int(terms[2]))
                elif terms[1] == "ANGLE":
                    self.bee.sub(1, int(terms[2]))

            elif terms[0] == "mpy":
                if terms[1] == "SPEED":
                    self.bee.mpy(0, int(terms[2]))
                elif terms[1] == "ANGLE":
                    self.bee.mpy(1, int(terms[2]))

            elif terms[0] == "div":
                if terms[1] == "SPEED":
                    self.bee.div(0, int(terms[2]))
                elif terms[1] == "ANGLE":
                    self.bee.div(1, int(terms[2]))

            elif terms[0] == "set":
                if terms[1] == "SPEED":
                    self.bee.mov(0, int(terms[2]))
                elif terms[1] == "ANGLE":
                    self.bee.mov(1, int(terms[2]))

            elif terms[0] == "jmp":
                self.jmp(terms)

            elif terms[0] == "fly":
                self.fly()

            elif terms[0] == "lst":
                self.lst(terms)

            elif terms[0] == "lte":
                self.lte(terms)

            elif terms[0] == "grt":
                self.grt(terms)

            elif terms[0] == "gte":
                self.gte(terms)

            elif terms[0] == "eqt":
                self.eqt(terms)

            elif terms[0] == "nte":
                self.nte(terms)

            elif terms[0] == "err":
                self.error(terms)

            elif terms[0] == "nop":
                self.wait(terms)
                
            elif terms[0] == "end":
                self.popFunction()
                
            self.lineNum += 1

    def jmp(self, terms):

        for lineNum, line in enumerate(self.userCode):
            line = self.userCode[lineNum].split()
            print("Linenum: ", lineNum, "Terms: ", terms)
            if line[0] == terms[1]:
                self.pushFunction()
                self.lineNum = lineNum
                return
            
    #def fly(self):

        #REMOVE COLLISION FROM BEE FOR SET TIME PERIOD
        #INCREASE SIZE OF BEE SPRITE AND DEPTH OF SHADOW THEN GO BACK TO NORMAL

    def portToNum(self, terms):
        for i, _ in enumerate(terms):
            if terms[i] == "SPEED":
                terms[i] = self.acceleration[0]
            if terms[i] == "ANGLE":
                terms[i] = self.acceleration[1]

    def lst(self, terms):
        self.portToNum(terms)
        if int(terms[1]) < int(terms[2]):
            for lineNum, line in enumerate(self.userCode):
                line in self.userCode[lineNum].split()
                if line[0] == terms[4]:
                    self.pushFunction()
                    self.lineNum = lineNum
                    return

    def lte(self, terms):
        self.portToNum(terms)
        if int(terms[1]) <= int(terms[2]):
            for lineNum, line in enumerate(self.userCode):
                line in self.userCode[lineNum].split()
                if line[0] == terms[4]:
                    self.pushFunction()
                    self.lineNum = lineNum
                    return
                
    def grt(self, terms):
        self.portToNum(terms)
        if int(terms[1]) > int(terms[2]):
            for lineNum, line in enumerate(self.userCode):
                line in self.userCode[lineNum].split()
                if line[0] == terms[4]:
                    self.pushFunction()
                    self.lineNum = lineNum
                    return
                
    def gte(self, terms):
        self.portToNum(terms)
        if int(terms[1]) >= int(terms[2]):
            for lineNum, line in enumerate(self.userCode):
                line in self.userCode[lineNum].split()
                if line[0] == terms[4]:
                    self.pushFunction()
                    self.lineNum = lineNum
                    return
                
    def eqt(self, terms):
        self.portToNum(terms)
        if int(terms[1]) == int(terms[2]):
            for lineNum, line in enumerate(self.userCode):
                line in self.userCode[lineNum].split()
                if line[0] == terms[4]:
                    self.lineNum = lineNum
                    return
                
    def nte(self, terms):
        self.portToNum(terms)
        if int(terms[1]) != int(terms[2]):
            for lineNum, line in enumerate(self.userCode):
                line in self.userCode[lineNum].split()
                if line[0] == terms[4]:
                    self.pushFunction()
                    self.lineNum = lineNum
                    return

    def error(self, terms):
        for i in (1, len(terms)):
            print(terms[i])
        #vm.error()

    def wait(self, terms):
        vm.wait(terms[1])

    def pushFunction(self):
        self.functionLine.append(self.lineNum)

    def popFunction(self):
        if(not(self.functionLine)):
            self.lineNum = self.functionLine[(len(self.functionLine) - 1)]
            self.functionLine.pop()
