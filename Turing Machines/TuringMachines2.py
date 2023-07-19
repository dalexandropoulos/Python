from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys

# The Busy Beaver

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
    def __init__(self, instructions):
        self.instructions = instructions
        self.instruction_set = 1
        self.tape = [0]
        self.index = 0

    def next_step(self):
        # Reading the tape
        read_value = self.tape[self.index]

        # Calculating
        a = 2 * self.instruction_set - 2
        b = 2 * self.instruction_set - 1
        write_value = int(self.instructions[a][0]) if read_value == 0 else int(self.instructions[b][0])
        move_value = int(self.instructions[a][1]) if read_value == 0 else int(self.instructions[b][1])
        self.instruction_set = int(self.instructions[a][2]) if read_value == 0 else int(self.instructions[b][2])

        # Writing to tape
        self.tape[self.index] = write_value

        # Moving
        if self.index == 0 and move_value == 0:
            self.tape.insert(0, 0)
        elif self.index == len(self.tape) - 1 and move_value == 1:
            self.tape.append(0)
            self.index = self.index - 1 + 2 * move_value
        else:
            self.index = self.index - 1 + 2 * move_value

        if self.instruction_set == 0 or self.instruction_set > len(self.instructions) / 2:
            self.print_tape()
            print("halt", end=' ')
            total_sum = 0
            for i in range(0, len(self.tape)):
                total_sum += self.tape[i]
            print(total_sum)
            sys.exit()

    def print_tape(self):
        for i in range(0, len(self.tape)):
            if self.index == i:
                self.print_c(self.tape[i], 'red', 1)
            else:
                if self.tape[i] == 0:
                    self.print_c(self.tape[i], 'dark_gray', 1)
                else:
                    self.print_c(self.tape[i], 'light_gray', 1)
        print()

    @staticmethod
    def print_c(text, color, end):
        print(ansi_colors[color], text, ansi_colors['reset'], sep='', end='') if end == 1 else print(
            ansi_colors[color], text, ansi_colors['reset'], sep='')


def save_turing_machine_image(tape_states):
    image_width = len(tape_states[0]) * 20
    image_height = len(tape_states) * 20
    img = Image.new('RGB', (image_width, image_height), color='white')
    draw = ImageDraw.Draw(img)

    for step, tape_state in enumerate(tape_states):
        for i, cell in enumerate(tape_state):
            color = 'black' if cell == 1 else 'white'
            draw.rectangle([i * 20, step * 20, (i + 1) * 20, (step + 1) * 20], fill=color)

    img.save('turing_machine_result.png')


def create_turing_machine_animation(tape_states):
    fig = plt.figure()

    def animate(frame):
        plt.clf()
        plt.imshow(tape_states[frame], cmap='gray', vmin=0, vmax=1)

    ani = animation.FuncAnimation(fig, animate, frames=len(tape_states), interval=200)
    ani.save('turing_machine_animation.gif', writer='pillow')


# Setup Turing Machine
instructions = ["112", "110", "013", "112", "103", "101"]
tm = TuringMachine(instructions)

# List to store tape states during computation
tape_states = []

# Continue the computation until the Turing Machine halts
while True:
    # Save the current tape state to the list
    tape_states.append(list(tm.tape))

    # Perform one step of the Turing Machine's computation
    tm.next_step()

    # Check if the Turing Machine halts
    if tm.instruction_set == 0 or tm.instruction_set > len(tm.instructions) / 2:
        tape_states.append(list(tm.tape))  # Save the final tape state
        break

# Save the final tape state as an image
save_turing_machine_image(tape_states)

# Create an animated GIF from the tape_states
create_turing_machine_animation(tape_states)
