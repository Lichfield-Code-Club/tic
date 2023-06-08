import turtle as t
from time import sleep

t.speed(10)
player=1
turn=1
flip=1
end=9
win=0
place = [10,10,10,10,10,10,10,10,10]
tiles = [(-200,200),(0,200),(200,200),(-200,0),(0,0),(200,0),(-200,-200),(0,-200),(200,-200)]
winner = 10
y=0
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
def turn():
  if flip==0:
    nought()
  else:
    cross()
  
t.shape('circle')
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

def play():
  global pos
  global end
  global y
  global tiles
  global place

  coord_num = pos -1
  if place[coord_num] == 10:
    t.goto(tiles[coord_num])
    turn()
    t.goto(0,0)
    place[coord_num] = end % 2
    y += 1
    end -= 1
  else:
    print("Sorry, I can't do that. ")
    end+=1

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

while end !=0:
  msg = ''
  pos = 0
  while pos == 0:
    print('1-9')
    no = input()
    pos = int(no)
    if pos > 9:
      pos = 0
      print('1-9 only')
  if y%2==0:
    flip=1
  else:
    flip =0
  play()
  WinCheck()
  if winner == 1:
    msg = "Player 1 wins!"
    end = 0
  elif winner == 0:
    msg = "Player 2 wins!"
    end = 0
  elif end == 0:
    msg = "it's a draw."
t.write(msg, move=False, align='center', font=('Arial', 32, 'normal')) 
sleep(5)