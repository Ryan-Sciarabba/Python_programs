port = ''
operation = ''
number = ''
speed = 0
angle = 0

def main():

    global port
    global operation
    global number
    
    #Open racer file
    racer = open("Racer.txt", "r")

    #Define symbols
    OPERATIONS = ['+', '-', '*', '/', '=']
    NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    WHITESPACE = ' '
    PORTS = ["THROTTLE", "TURN"]
    
    #Break down symbols together
    lexeme = ''
    if racer.mode == "r":
        code = racer.readlines()
        for line in code:
            port = ''
            operation = ''
            number = ''
            lexeme = ''
            for i, char in enumerate(line):
                if char != WHITESPACE:
                   lexeme += char
                if (i + 1 < len(line)):
                    if line[i + 1] == WHITESPACE or line[i + 1] == '\n':
                        if lexeme in PORTS:
                            port = lexeme
                        if lexeme in OPERATIONS:
                            operation = lexeme
                        if bool([ele for ele in NUMBERS if(ele in lexeme)]):
                            number = lexeme
                        lexeme = ''
                if (i == len(line) - 1):
                    if lexeme in PORTS:
                        port = lexeme
                    if lexeme in OPERATIONS:
                        operation = lexeme
                    if bool([ele for ele in NUMBERS if(ele in lexeme)]):
                        number = lexeme
                    lexeme = ''
                    
            oprSwitch()
            print('Speed: %d' % speed)
            print('Angle: %d' % angle)

def addPort():
    global port
    global speed
    global angle
    global number
    
    print("Speed: ", int(speed), " Number: ", number)
    
    if port == "THROTTLE":
        speed = speed + number
        
    if port == "TURN":
        angle = angle + number

def subPort():
    global port
    global speed
    global angle
    global number
    
    if port == "THROTTLE":
        speed = speed - number
        
    if port == "TURN":
        angle = angle - number
    
def mltPort():
    global port
    global speed
    global angle
    global number
    
    if port == "THROTTLE":
        speed = speed * number
        
    if port == "TURN":
        angle = angle * number

def divPort():
    global port
    global speed
    global angle
    global number

    if port == "THROTTLE":
        speed = speed / number
        
    if port == "TURN":
        angle = angle / number

def setPort():
    global port
    global speed
    global angle
    global number

    if port == "THROTTLE":
        speed = number
        
    if port == "TURN":
        angle = number
    
def oprSwitch():

    global number
    global angle
    global speed
    
    number = int(number)
    angle = int(angle)
    speed = int(speed)

    print("Op speed: ", speed)
    oprSwitcher = {
        1: mltPort(),
        2: addPort(),
        4: subPort(),
        6: divPort(),
        20: setPort()
        }

    global operation
    nOperation = ord(operation) - 41
    oprSwitcher.get(nOperation, "invalid operation")
    
main()
