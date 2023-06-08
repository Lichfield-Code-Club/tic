import turtle as t
from time import sleep

t.speed(10)
player=1
turn=1
flip=1
end=9
win=0
place = [10,10,10,10,10,10,10,10,10]
pace = [1,10,20,30,40,50,60,70,80,90]
tiles = [(-200,200),(0,200),(200,200),(-200,0),(0,0),(200,0),(-200,-200),(0,-200),(200,-200)]
winner =0
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
    place[coord_num] = end %2
    y += 1
  else:
    print("Sorry, I can't do that. ")
    end+=1

def WinCheck():
  global place
  global winner
  global end
  
  # Player 1
  if sum(place[:3])==0 or sum(place[3:6])==0 or sum(place[6:8])==0: # rows
    winner=2
    end=2
  if place[0]+place[3]+place[6]==0 or place[1]+place[4]+place[7]==0  or place[2]+place[5]+place[8]==0: # columns
    winner=2
    end=1
  if place[0] + place[4] + place[8] == 0 or place[2] + place[4] + place[7] == 0: # diagonals
    winner=2
    end=1

  # Player 2
  if sum(place[:3])==3 or sum(place[3:6])==3 or sum(place[6:8])==3: # rows
    winner=1
    end=2
  if place[0]+place[3]+place[6] == 3 or place[1]+place[4]+place[7] == 3 or place[2]+place[5]+place[8] == 3: # columns
    winner=1
    end=1
  if place[0] + place[4] + place[8] == 3 or place[2] + place[4] + place[7] == 3: # diagonals
    winner=1
    end=1

while end !=0:
  print('1-9')
  no = input()
  pos = int(no)
  if y%2==0:
    flip=1
  else:
    flip =0
  play()
  WinCheck()
  if winner>=1:
    print("Player", winner, "wins!")
    end = 0
  elif end == 0:
    print("it's a draw.")
sleep(5)