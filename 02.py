import turtle

def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, level -1)
        t.left(60)
        koch_curve(t, length, level -1)
        t.left(120)
        koch_curve(t, length, level -1)
        t.left(60)
        koch_curve(t, length, level -1)

def koch_snowflake(t, length, level):
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)

def main(level):
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, 100)
    t.pendown()

    length = 300
    koch_snowflake(t, length, level)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    level = int(input("Введіть рівень рекурсії: "))
    main(level)