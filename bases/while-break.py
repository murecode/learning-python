import random

goal = 20
player1 = 0
player2 = 0

# Mientras sea verdad se ejecuta
while True:
  advance_player1 = random.randint(1,5)
  advance_player2 = random.randint(1,5)

  player1 += advance_player1
  player2 += advance_player2

  print(f"Player1 -> avanza:{advance_player1} total_pasos:{player1}")
  print(f"Player2 -> avanza:{advance_player2} total_pasos:{player2}")

  # Condicion de salida 
  if player1 >= goal or player2 >= goal:
    break

if player1 > player2:
  print("Gandor Player1")
elif player2 > player1:
  print("Ganador Player2")
else:
  print("Empate")






