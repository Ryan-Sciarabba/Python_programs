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

            oprSwitch()
            print('Speed: %d' % speed)
            print('Angle: %d' % angle)

def addPort():
    global port
    def speed():
        global speed
        global number
        speed = speed + number
    def angle():
        global angle
        global number
        angle = angle + number
                
    addSwitcher = {
        "THROTTLE": speed(),
        "TURN": angle()
        }

    addSwitcher.get(port, "invalid port")

def subPort():
    print("In subPort")
    global port
    global speed
    print(speed)
    def speed():
        global speed
        global number
        print(speed)
        speed = speed - number
    def angle():
        global angle
        global number
        angle = angle - number
                
    subSwitcher = {
        "THROTTLE": speed(),
        "TURN": angle()
        }

    subSwitcher.get(port, "invalid port")
    
def mltPort():
    global port
    def speed():
        global speed
        global number
        speed = speed * number
    def angle():
        global angle
        global number
        angle = angle * number
                
    mltSwitcher = {
        "THROTTLE": speed(),
        "TURN": angle()
        }

    mltSwitcher.get(port, "invalid port")

def divPort():
    global port
    def speed():
        global speed
        global number
        speed = speed / number
    def angle():
        global angle
        global number
        angle = angle / number
                
    divSwitcher = {
        "THROTTLE": speed(),
        "TURN": angle()
        }

    divSwitcher.get(port, "invalid port")

def setPort():
    global port
    def speed():
        global speed
        global number
        speed = number
    def angle():
        global angle
        global number
        angle = number
                
    setSwitcher = {
        "THROTTLE": speed(),
        "TURN": angle()
        }

    setSwitcher.get(port, "invalid port")
    
def oprSwitch():
    
    oprSwitcher = {
        1: mltPort(),
        2: addPort(),
        4: subPort(),
        6: divPort(),
        20: setPort(),
        }

    global operation
    nOperation = ord(operation) - 41
    print(nOperation)
    oprSwitcher.get(nOperation, "invalid operation")
    
main()
