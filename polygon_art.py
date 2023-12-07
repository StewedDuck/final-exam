import turtle
import random


class polygon_art:
    def __init__(self, num_sides, size, orientation, location, color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360/self.num_sides)
        turtle.penup()

    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

class Draw:
    def __init__(self, num, size):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)
        self.num = num
        self.size = size
        num_sides = 0  # triangle, square, or pentagon
        if choice == 1:
            num_sides = 3
        elif choice == 2:
            num_sides = 4
        elif choice == 3:
            num_sides = 5
        elif choice == 4:
            num_sides = random.randint(3, 5)
        elif choice == 5:
            num_sides = 3
        elif choice == 6:
            num_sides = 4
        elif choice == 7:
            num_sides = 5
        elif choice == 8:
            num_sides = random.randint(3, 5)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        border_size = random.randint(1, 10)
        self.art = polygon_art(num_sides, size, orientation, location, color, border_size)


    def draw(self):
        for i in range(self.num):
            self.art.orientation = random.randint(0, 90)
            self.art.location = [random.randint(-300, 300), random.randint(-200, 200)]
            self.art.color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            self.art.border_size = random.randint(1, 10)
            if choice != 8:
                self.art.draw_polygon()
            if choice == 4:
                self.art.num_sides = random.randint(3, 5)
            if choice == 8:
                self.art.num_sides = random.randint(3, 5)
            reduction_ratio = 0.618
            # reposition the turtle and get a new location
            turtle.penup()
            if choice <= 4:
                turtle.forward(self.size * (random.randint(-7, 7) - reduction_ratio) / 2)
                turtle.left(90)
                turtle.forward(self.size * (random.randint(-7, 7) - reduction_ratio) / 2)
                turtle.right(90)
                self.art.location[0] = turtle.pos()[0]
                self.art.location[1] = turtle.pos()[1]
                self.art.size *= reduction_ratio
                self.art.draw_polygon()
                self.art.size = self.size
            elif choice >= 5 != 8:
                for j in range(2):
                    turtle.forward(self.size * (1 - reduction_ratio) / 2)
                    turtle.left(90)
                    turtle.forward(self.size * (1 - reduction_ratio) / 2)
                    turtle.right(90)
                    self.art.location[0] = turtle.pos()[0]
                    self.art.location[1] = turtle.pos()[1]
                    self.art.size = self.size * (reduction_ratio / (j+1))
                    self.art.draw_polygon()
                    self.art.size = self.size
            elif choice == 8:
                self.art.draw_polygon()
                for j in range(3):
                    turtle.forward(self.size * (1 - reduction_ratio) / 2)
                    turtle.left(90)
                    turtle.forward(self.size * (1 - reduction_ratio) / 2)
                    turtle.right(90)
                    self.art.location[0] = turtle.pos()[0]
                    self.art.location[1] = turtle.pos()[1]
                    self.art.size = self.size * (reduction_ratio / (j+1))
                    self.art.draw_polygon()
                    self.art.size = self.size
        turtle.done()


num = random.randint(5, 8)
size = random.randint(100, 150)
choice = int(input('Which art do you want to generate? Enter a number between 1 to 8,\n inclusive: '))
my_art = Draw(num, size)
my_art.draw()

