import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (300, 300)
screen = pygame.display.set_mode(size)

all_sprites_list = pygame.sprite.Group()

class Tile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("tile.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    #def draw_layout(self, layout):
        #for row in layout:
            #for col in row:
               #if layout[row][col] == 1:
                   # self.rect.x = col * 20
                   # self.rect.y = row * 20
                   # all_sprites_list.add(self)

class Maze():
    def __init__(self,layout):
        for i in range(len(layout)):
            for j in range(len(layout[i])):
                if layout[i][j] == 1:
                    tile = Tile()
                    tile.rect.x = j * 20
                    tile.rect.y = i * 20
                    all_sprites_list.add(tile)
         
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

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #maze = Maze()
    #maze.rect.x = 10
    #maze.rect.y = 10
    #all_sprites_list = pygame.sprite.Group()
    #all_sprites_list.add(maze)

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
