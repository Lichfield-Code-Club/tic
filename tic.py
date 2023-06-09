import turtle as t
from time import sleep

def cross():
  t.pendown()
  t.left(45)
  for x in range(4):
   t.forward(140)
   t.backward(140)
   t.left(90)
  t.left(45)
  t.penup()
def nought():
  t.forward(100)
  t.pendown()
  t.left(90)
  t.circle(100)
  t.penup()
  
def Board():
  #t.shape('circle')
  t.penup()
  t.goto(-300,-300)
  t.pendown()
  t.goto(300,-300)
  t.goto(300,300)
  t.goto(-300,300)
  t.goto(-300,-300)
  t.goto(-100,-300)
  t.left(90)
  t.forward(600)
  t.right(90)
  t.forward(200)
  t.right(90)
  t.forward(600)
  for x in range(2):
      t.left(90)
      t.forward(200)
  t.left(90)
  t.forward(600)
  t.right(90)
  t.forward(200)
  t.right(90)
  t.forward(600)
  t.penup()
  t.goto(0,0)
  t.speed(10)

def TileIndex(x,y):
  global tiles

  # First row
  if x >= -300 and x < -100 and y > 100: return 0
  if x >= -100 and x < 100  and y > 100: return 1
  if x >=  100 and y > 100: return 2

  # second row
  if x >= -300 and x < -100 and y < 100 and y > -100: return 3
  if x >= -300 and x < 100  and y < 100 and y > -100: return 4
  if x >= 100  and y < 100  and y > -100: return 5

  # third row
  if x >= -300 and x < -100 and y < 300: return 6
  if x >= -300 and x < 0 and y < 300: return 7
  if x >= 100  and y < 300: return 8

  print("Shouldn't reach this point")
  return 9 # will cause 'list index out of range'

def play(x,y):
  global tiles
  global place
  global player

  tile_index = TileIndex(x,y)
  if place[tile_index] == 10:
    t.goto(tiles[tile_index])
    if player == 0:
      nought()
    else:
      cross()
    t.goto(0,0)
    place[tile_index] = player
    if player: player = 0 # Switch player
    else: player = 1
  else:
    print("Sorry, I can't do that. ")

def Checker(player,total):
  global place
  global winner
  global end
  
  if place[0]+place[1]+place[2] == total or place[3]+place[4]+place[5] == total or place[6]+place[7]+place[8] == total: # rows
    winner=player
    end=0
  if place[0]+place[3]+place[6] == total or place[1]+place[4]+place[7] == total or place[2]+place[5]+place[8] == total: # columns
    winner=player
    end=0
  if place[0] + place[4] + place[8] == total or place[2] + place[4] + place[6] == total: # diagonals
    winner=player
    end=0

def WinCheck():
  global winner
  Checker(1,3)
  if winner != 1:
    Checker(0,0)

def PlayGame(x,y):
  global places
  msg = ''
  play(x,y)
  WinCheck()
  if winner == 1:
    msg = "Player 1 wins!"
  elif winner == 0:
    msg = "Player 2 wins!"
  elif not 10 in place : # all squares used
    msg = "it's a draw."
  if len(msg):
    t.write(msg, move=False, align='center', font=('Arial', 32, 'normal')) 

t.speed(10)
player=1
place = [10,10,10,10,10,10,10,10,10]
window_height = 900
window_width = 900
tiles = [(-200,200),(0,200),(200,200),(-200,0),(0,0),(200,0),(-200,-200),(0,-200),(200,-200)]
winner = 10
window = t.Screen()
window.setup(window_width,window_height)
window.onclick(PlayGame)
Board()
t.mainloop()