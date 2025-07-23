import turtle
import random
colors = ["blue", "pink", "purple", "black", "red"]
turtles = []

startY = 100

#create turts
for hue in colors:
  turtle_racer = turtle.Turtle()
  turtle_racer.color(hue)
  turtle_racer.shape("turtle")
  turtle_racer.penup()
  turtle_racer.goto(0, startY)
  startY -= 20
  turtles.append(turtle_racer)

#draw finish line
finishLine = turtle.Turtle()
finishLine.penup()
finishLine.goto(100, 100)
finishLine.pendown()
finishLine.goto(100, 0)

#start race
winner = None
while not winner:
  for turt in turtles:
        turt.fd(random.randint(1, 10))
        if turt.xcor() >= 100:
          winner = turt
          