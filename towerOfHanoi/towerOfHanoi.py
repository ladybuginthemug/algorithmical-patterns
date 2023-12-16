import turtle
import os

class Stack:
    def __init__(self, name):
        self.items = []
        self.name = name

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return self.name


class TowerOfHanoi:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        self.tower_a = Stack('Tower A')
        self.tower_b = Stack('Tower B')
        self.tower_c = Stack('Tower C')
        self.move_count = 0

        for i in range(num_disks, 0, -1):
            self.tower_a.push(i)

        # Set up Turtle window
        turtle.speed(0)
        turtle.hideturtle()
        turtle.title("Towers of Hanoi")
        turtle.delay(0)

        # Create a folder for screenshots
        os.makedirs("turtle_img", exist_ok=True)

        # Draw initial state and save the first canvas
        self.draw_hanoi_state()

    def move_disk(self, source, target):
        disk = source.pop()
        target.push(disk)
        self.move_count += 1
        print(f"Move disk {disk} from {source.name} to {target.name}")
        self.draw_hanoi_state()

    def hanoi_recursive(self, n, source, target, holding):
        if n > 0:
            # Move n-1 disks from source to holding (temporary) peg using target as auxiliary
            self.hanoi_recursive(n - 1, source, holding, target)
            # Move the nth disk from source to target peg
            self.move_disk(source, target)
            # Move the n-1 disks from holding peg to target peg using source as the second holding peg
            self.hanoi_recursive(n - 1, holding, target, source)

    def draw_hanoi_state(self):
        turtle.clear()
        peg_positions = {'A': (-150, -50), 'B': (0, -50), 'C': (150, -50)}

        for peg, disks in {'A': self.tower_a.items, 'B': self.tower_b.items, 'C': self.tower_c.items}.items():
            self.draw_peg(*peg_positions[peg], 100)
            for i, disk in enumerate(disks):
                self.draw_disk_with_offset(peg_positions[peg][0], -50 + i * 20, disk * 35, 20)

        turtle.update()
        self.save_canvas()

    def draw_peg(self, x, y, height):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

        turtle.forward(5)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
        turtle.forward(5)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

    def draw_disk_with_offset(self, x, y, width, height):
        turtle.penup()
        turtle.goto(x - width/2, y)
        turtle.pendown()

        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

    def save_canvas(self):
        canvas = turtle.getcanvas()
        canvas.postscript(file=f"turtle_img/move_{self.move_count:03d}.eps")
        self.convert_eps_to_png()

    def convert_eps_to_png(self):
        eps_file = f"turtle_img/move_{self.move_count:03d}.eps"
        png_file = f"turtle_img/move_{self.move_count:03d}.png"

        from PIL import Image
        image = Image.open(eps_file)
        image.save(png_file, 'png')
        os.remove(eps_file)

    def solve(self):
        print("Initial state:")
        print(f"Tower A: {self.tower_a.items}")
        print(f"Tower B: {self.tower_b.items}")
        print(f"Tower C: {self.tower_c.items}")

        self.hanoi_recursive(self.num_disks, self.tower_a, self.tower_c, self.tower_b)

        print(f"\nNumber of moves: {self.move_count}")
        print("Final state:")
        print(f"Tower A: {self.tower_a.items}")
        print(f"Tower B: {self.tower_b.items}")
        print(f"Tower C: {self.tower_c.items}")

# Example: Solve Tower of Hanoi with 3 disks
hanoi = TowerOfHanoi(3)
hanoi.solve()

# Close the turtle graphics window on click
turtle.exitonclick()
