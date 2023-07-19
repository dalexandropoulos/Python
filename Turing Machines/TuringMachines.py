# The Buzy Beaver

import sys
import time

# ANSI escape codes for different text colors
ansi_colors = {
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'light_gray': '\033[37m',
    'dark_gray': '\033[90m',
    'white': '\033[97m',
    'reset': '\033[0m'
}

class TuringMachine: 
    def __init__(self,instactions):
        self.instractions = instactions
        self.instractions_set = 1
        self.tape = [0]
        self.index = 0

    def nextstep(self):
        # Reading the tape
        read_value = self.tape[self.index]

        # Calculating
        a = 2 * self.instractions_set -2 ; b = 2 * self.instractions_set -1
        write_value = int(self.instractions[a][0]) if read_value == 0 else int(self.instractions[b][0])
        move_value = int(self.instractions[a][1]) if read_value == 0 else int(self.instractions[b][1])
        self.instractions_set = int(self.instractions[a][2]) if read_value == 0 else int(self.instractions[b][2])
        # printc(self.tape,"green",0)
        # print("Read value:",read_value,". Write Value:",write_value, ". Move Value:", move_value, ". Next State:", self.instractions_set, ". Index:", self.index)
        
        # Writing to tape
        self.tape[self.index] = write_value

        # Moving
        if self.index == 0 and move_value == 0:
            self.tape.insert(0,0)
        elif self.index == len(self.tape)-1 and move_value == 1:
            self.tape.append(0)
            self.index = self.index -1 + 2 * move_value
        else:
            self.index = self.index -1 + 2 * move_value
        
        if self.instractions_set == 0 or self.instractions_set > len(self.instractions)/2: 
            tm.printtape()
            print("halt", end=' ')
            sum=0
            for i in range(0, len(self.tape)):
                sum += self.tape[i]
            print(sum)
            sys.exit()
    
    def printtape(self):
        for i in range(0, len(self.tape)):
            if self.index == i:
                printc(self.tape[i],'red',1)
            else:
                if self.tape[i] == 0:
                    printc(self.tape[i],'dark_gray',1)
                else:
                    printc(self.tape[i],'light_gray',1)
        print()


def printc(text, color, end):
    print(ansi_colors[color],text, ansi_colors['reset'],sep='', end='') if end == 1 else print(ansi_colors[color],text, ansi_colors['reset'], sep='')


# Setup Turing Machine
instractions2 = ["112", "102", "101", "110"]
instractions3 = ["112", "110", "013", "112", "103", "101"]
instractions4 = ["112", "102", "101", "003", "110", "104", "114", "011"]
instractions5 = ["102", "101", "113", "112", "101", "114", "101", "115", "110", "013"]
instractions =  ["102", "101", "113", "112", "101", "114", "101", "115", "110", "013"]
tm = TuringMachine(instractions)

print("Turing Machine",end=' ')
printc(tm.instractions,"red",0)
print()

tm.printtape()
while True:
    tm.nextstep()
    tm.printtape()
    # time.sleep(1)

