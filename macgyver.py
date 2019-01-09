import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (300, 300)
screen = pygame.display.set_mode(size)


treasure_list = ["aiguille.png", "ether.png", "tube_plastique.png"]
all_sprites_list = pygame.sprite.Group()

class Tile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("tile.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

##class Maze():
##    def __init__(self,layout):
##        for row in layout:
##            for col in row:
##               if layout[row][col] == 1:
##                   tile = Tile()
##                   tile.rect.x = col * 20
##                   tile.rect.y = row * 20
##                   all_sprites_list.add(self)
##????TypeError: list indices must be integers or slices, not list????

class Maze():
    def __init__(self,layout):
        for i in range(len(layout)):
            for j in range(len(layout[i])):
                if layout[i][j] == 1:
                    tile = Tile()
                    tile.rect.x = j * 20
                    tile.rect.y = i * 20
                    all_sprites_list.add(tile)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
class Gardien(Player):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("gardien.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 280
        self.rect.y = 240
        all_sprites_list.add(self)

class Macgyver(Player):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("macgyver.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 40
        all_sprites_list.add(self)

class Treasure(pygame.sprite.Sprite):
    def __init__(self, picture):
        super().__init__()
        self.image = pygame.image.load(picture).convert()
        #key = surface.get_colorkey()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
     
pygame.display.set_caption("Help MacGyver escape!")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
structure = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                 [1,1,0,0,0,0,1,0,0,0,0,0,0,0,1],
                 [0,0,0,0,1,1,1,0,0,0,0,0,0,0,1],
                 [1,0,1,0,0,1,0,0,0,0,0,1,1,0,1],
                 [1,0,0,0,0,0,0,0,1,0,0,1,1,0,1],
                 [1,0,1,0,0,0,0,0,0,0,0,0,1,0,1],
                 [1,1,1,1,1,1,0,0,0,0,0,0,1,0,1],
                 [1,0,0,0,1,1,0,0,1,0,0,0,1,1,1],
                 [1,0,0,0,0,0,0,0,1,0,0,0,1,0,1],
                 [1,0,0,0,0,0,0,1,1,0,0,0,0,0,1],
                 [1,0,1,1,1,1,1,1,1,0,1,0,0,0,1],
                 [1,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
                 [1,0,0,1,1,1,0,0,0,0,0,0,1,0,0],
                 [1,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

maze = Maze(structure)

macgyver = Macgyver()

gardien = Gardien()

for item in treasure_list:
    treasure = Treasure(item)
    treasure.rect.x = random.randint(0,14)*20
    treasure.rect.y = random.randint(0,14)*20
    while pygame.sprite.spritecollideany(treasure, all_sprites_list, False):
        treasure.rect.x = random.randint(0,14)*20
        treasure.rect.y = random.randint(0,14)*20
    all_sprites_list.add(treasure)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    all_sprites_list.draw(screen)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
