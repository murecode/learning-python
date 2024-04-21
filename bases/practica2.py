import random
import turtle

canva = turtle.Screen()
canva.title("🏁Carrera")
canva.bgcolor("lightblue")
canva.setup(width=800, height=600)

player_1 = turtle.Turtle()
player_1.shape("turtle")
player_1.color("blue")
player_1.penup()
player_1.goto(-300, 50)
player_1.speed()

player_2 = turtle.Turtle()
player_2.shape("turtle")
player_2.color("red")
player_2.penup()
player_2.goto(-300, -50)
player_2.speed()

goal = 300

while True:
  p1_advance = random.randint(10,20)
  p2_advance = random.randint(10,20)

  player_1.forward(p1_advance)
  player_2.forward(p2_advance) 

  if player_1.xcor() >= goal or player_2.xcor() >= goal:
    break

if player_1.xcor() > player_2.xcor():
  print("Gandor Player1")
elif player_2.xcor() > player_1.xcor():
  print("Ganador Player2")
else:
  print("Empate")


canva.exitonclick()