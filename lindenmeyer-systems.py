import turtle
import random

def hexagonal_gosper():
    return {
        "axiom": ['F','X'],
        "rules": {
            'X': ['X', '+', 'Y', 'F', '+', '+', 'Y', 'F', '-', 'F', 'X', '-', '-', 'F', 'X', 'F', 'X', '-', 'Y', 'F', '+'],
            'Y': ['-', 'F', 'X', '+', 'Y', 'F', 'Y', 'F', '+', '+', 'Y', 'F', '+', 'F', 'X', '-', '-', 'F', 'X', '-', 'Y']
        },
        "moves": {
            '+': [{"turn": -60}],
            '-': [{"turn": 60}],
            'F': [{"forward": 1}]
        }
    }

def draw_lsystem(t, instructions, distance):
    angle = random.choice([15, 30, 45, 60, 75, 90, 105, 120, 135, 150])
    for cmd in instructions:
        if cmd == 'F':
            t.forward(distance)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)

def create_lsystem(num_generations, axiom, rules):
    instructions = axiom
    for i in range(num_generations):
        new_instructions = []
        for cmd in instructions:
            if cmd in rules:
                new_instructions.extend(rules[cmd])
            else:
                new_instructions.append(cmd)
        instructions = new_instructions
    return instructions

system = hexagonal_gosper()
instructions = create_lsystem(6, system["axiom"], system["rules"])

t = turtle.Turtle()

draw_lsystem(t, instructions, 10)
turtle.done()
