def main():

    #Open racer file
    racer = open("Racer.txt", "r")

    #Define symbols
    OPERATION = ['+', '-', '*', '/', '=']
    NUMBER = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    WHITESPACE = ' '


    #Break down symbols together
    lexeme = ''
    if racer.mode == "r":
        code = racer.readlines()
        for line in code:
            for i, char in enumerate(line):
                if char == OPERATION:
                    print(switch(char))
               #if char != WHITESPACE:
                   #lexeme += char
                #if (i + 1 < len(line)):
                    #if line[i + 1] == WHITESPACE:
                       #print(lexeme)
                        #lexeme = ''
        print(lexeme)

def switch(argument):
    def addPort()
    switcher = {
        '+': addPort,
        '-': subPort,
        '*': mltPort,
        '/': divPort
        }

    operand = switcher.get(argument, "invalid operation")
    return operand
        
def setPort(port, number):
    
    
    
if __name__== "__main__":
    main()
