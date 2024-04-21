import turtle

# Config
canva = turtle.Screen()
canva.bgcolor("white")
cursor = turtle.Turtle()
cursor.speed(1)

# Dubujar cuadrado
for _ in range(5):
  cursor.forward(150)
  cursor.right(144)

canva.exitonclick()