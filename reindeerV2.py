# Computer Science CPT - Reindeer Game
# @author Ridam Loomba
# @date 2017/01/09
# @course ICS3C

# Main Program

import pygame
import random


# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN= (79,183,69)
GREY= (178,176,183)
#Define some variable
tree_x=20
tree_y=-300

class Gift(pygame.sprite.Sprite):
    #creates the imag eof the gift 
    def __init__ (self, colour, width, height):
        super().__init__()
        self.image= pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.colour= (random.randrange (0,255), random.randrange(0,255), random.randrange(0,255))

    def move_down (self):
        self.rectY= self.rectY+ random.randrange(2,4)
        if self.rectY >500:
            self.place_top

    def place_top(self):
        self.rectY = random.randrange(-300, -20)
        self.rectX = random.randrange(0, screen_width)


# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create screen
screen_width=1000
screen_height=600
screen = pygame.display.set_mode([screen_width, screen_height])

#List of gift sprites
gift_list= pygame.sprite.Group()

#List of all sprites
every_Sprite_list= pygame.sprite.Group()

for i in range (20):
    gift=Gift(WHITE,50,50)
    gift.rectX = random.randrange(300,400)
    gift.rectY = 0

    # Add the gift to the list of objects
    gift_list.add(gift)
    every_Sprite_list.add(gift)



#Set caption of game 
pygame.display.set_caption("Reindeer Game")
 
clock = pygame.time.Clock()

# Load and set up graphics.
# image taken from https://upload.wikimedia.org/wikipedia/commons/8/83/Christmas_trees.png
tree_image = pygame.image.load("tree02.png").convert()
tree_image.set_colorkey(WHITE)

done = False
#-----Main----- 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill (GREY)

# Update every sprite in sprite list 
    every_Sprite_list.update()
    
#Loop to draw grass on both sides of the screen 
    y_offset= 0
    while y_offset<1000:
        pygame.draw.rect(screen, GREEN, [0+y_offset,0,250,600])
        y_offset= y_offset + 750

# Draw the tree 

    for i in range (random.randrange (2,4)):
        tree_y=tree_y+1
        screen.blit(tree_image, [tree_x, tree_y])
        if tree_y>600:
            tree_y=-300

# Draw all the spites
    every_Sprite_list.draw(screen)

    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()

