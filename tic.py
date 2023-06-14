import pygame
from time import sleep

class Tile():
    def __init__(self,screen,id,row,column,w,h):
        self.screen = screen
        self.x = column * w
        self.y = row * h
        self.w = w
        self.h = h
        self.id = id
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.border = 2
        self.player = None

    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect, self.border)
        if self.player:
          text = 'X'
          if self.player == 2: text = 'O'
          font = pygame.font.SysFont(None,48)
          img = font.render(text,True,'red')
          self.rect.topleft = (self.x+(self.w // 2),self.y+(self.h // 2))
          self.rect.size = img.get_size()
          self.screen.blit(img,self.rect)

    def update(self,player):
        pos = pygame.mouse.get_pos()
        if self.player == None:
            if pos[0] >= self.x and pos[0] < self.x + self.w and pos[1] >= self.y and pos[1] < self.y + self.h:
                self.player = player
                self.draw() 
                return self.id
        return 0
    
def TicTiles(screen,w,h):
    tiles = []
    id = 0
    for row in [0,1,2]:
        for column in [0,1,2]:
            id += 1
            tiles.append(Tile(screen,id,row,column,w,h))
    return tiles

def TicTextCaption(screen,text):
  if screen:
    pygame.display.set_caption(text)

def TicText(screen,text):
  TicTextCaption(screen,text)
  pygame.display.update()

def TicGameOver(tiles):
  x = [tile.player for tile in tiles]
  winner = None
  draw = False
  # rows
  if x[0] != None and x[0] == x[1] and x[0] == x[2]: winner = x[0]
  if x[3] != None and x[3] == x[4] and x[3] == x[5]: winner = x[3]
  if x[6] != None and x[6] == x[7] and x[6] == x[8]: winner = x[6]
  # cols
  if x[0] != None and x[0] == x[3] and x[0] == x[6]: winner = x[0]
  if x[1] != None and x[1] == x[4] and x[1] == x[7]: winner = x[1]
  if x[2] != None and x[2] == x[5] and x[2] == x[8]: winner = x[2]
  # diagonals
  if x[0] != None and x[0] == x[4] and x[0] == x[8]: winner = x[0]
  if x[2] != None and x[2] == x[4] and x[2] == x[6]: winner = x[2]
  # Draw
  if winner == None and not None in x:
    draw = True
  return winner, draw

def TicEnd(screen,text):
  TicText(screen,text)
  font = pygame.font.SysFont(None,96)
  img = font.render(text,True,'white')
  rect = screen.get_rect()
  rect.topleft = (200,200)
  rect.size = img.get_size()
  screen.blit(img,rect)
  pygame.display.update()
   
def Tic():
  SCREEN_WIDTH = 900
  SCREEN_HEIGHT = 900

  TILE_WIDTH = SCREEN_WIDTH // 3
  TILE_HEIGHT = SCREEN_HEIGHT // 3

  #framerate
  FPS = 60
  clock = pygame.time.Clock()

  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  tiles = TicTiles(screen,TILE_WIDTH,TILE_HEIGHT)
  [tile.draw() for tile in tiles]

  player = 1
  TicText(screen,f'Next Player: {player}')

  run = True
  while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      if event.type == pygame.MOUSEBUTTONUP:
        x = [tile.update(player) for tile in tiles]
        if sum(x) > 0:
          if player == 1: player = 2
          else: player = 1
          TicText(screen,f'Next Player: {player}')
          pygame.display.update()
        winner,draw = TicGameOver(tiles)
        if draw: 
          TicEnd(screen,'Draw')
          run = False
          sleep(5)
        if winner: 
          TicEnd(screen,f'Winner: Player {winner}')
          run = False
          sleep(5)

  pygame.quit()


Tic()
