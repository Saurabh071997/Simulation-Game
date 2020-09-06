import pygame
import time
from random import randint,randrange

black = (0,0,0)
white = (255,255,255)

sunset = (253,72,47)
greenyellow = (154,255,0)
brightblue = (47,228,253)
orange = (255,113,0)
yellow = (255,236,0)
purple = (252,67,255)

colorChoices = [greenyellow, brightblue, orange, yellow, purple ]

pygame.init()

surfaceWidth = 900
surfaceHeight = 500

imageHeight = 50
imageWidth = 45

surface= pygame.display.set_mode((surfaceWidth, surfaceHeight))
pygame.display.set_caption('Flappy Bird')
#to set frames per second
clock= pygame.time.Clock()

img = pygame.image.load('birdie.png')

def score(count):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("Score : " + str(count), True, white )
    surface.blit(text, [0,0] )


    

def blocks(x_block, y_block, block_width, block_height, gap):
    colorChoice = colorChoices[randrange(0,len(colorChoices))]
    pygame.draw.rect(surface, colorChoice, [x_block, y_block, block_width, block_height ])
    pygame.draw.rect(surface, colorChoice, [x_block, y_block+block_height+gap, block_width, surfaceHeight ])


def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
            continue

        return event.key
    
    return None 
        

def makeTextObjs(text,font):
    textSurface = font.render(text, True ,sunset)        #second parameter is anti-aliasing, third is for color
    return textSurface,textSurface.get_rect()           # second variable allows us to get the rectangle that goes around the text

def msgSurface(text):
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    largeText = pygame.font.Font('freesansbold.ttf', 60)

    titleTextSurf , titleTextRect = makeTextObjs(text, largeText)     #Rect one is to place the text in rectangle to simplify the positioning of text
    titleTextRect.center = surfaceWidth/2, surfaceHeight/2
    surface.blit(titleTextSurf, titleTextRect)

    typTextSurf, typTextRect = makeTextObjs('Press any key to continue',smallText)
    typTextRect.center = surfaceWidth/2, ((surfaceHeight/2) + 100)          # +100 :so that second msg appears below the first one
    surface.blit(typTextSurf ,typTextRect)

    pygame.display.update()
    time.sleep(1)

    while replay_or_quit() == None:
        clock.tick()

    main()


    
def gameOver():
    msgSurface('You are so Fucked UP !! ')

    
def helicopter(x, y, image):
    surface.blit(img, (x,y))  #blit func to put something on screen


def main():
    x = 150
    y = 200 
    y_move = 0

    x_block = surfaceWidth
    y_block = 0

    block_width = 75
    block_height = randint(0,surfaceHeight/2)
    gap = imageHeight*3
    block_move = 4
    
    current_score = 0
    
    game_over = False

    while not game_over:
        for event in pygame.event.get():  #for loop gets all kind of events into event variable
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:       #to move bird down
                if event.key == pygame.K_UP:
                    y_move = -5              # -ve 5 means to go up in y-axis

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 5


        y += y_move
        
        surface.fill(black)  #to fill background with black color
        helicopter(x, y, img)
        

        blocks(x_block, y_block, block_width, block_height, gap)
        score(current_score)
        x_block -= block_move
        
        if y > surfaceHeight-40 or y<0:
            gameOver()

        if x_block < (-1*block_width):
            x_block = surfaceWidth
            block_height = randint(0, surfaceHeight/2)
           # current_score += 1

        if (x + imageWidth) > x_block:                                 # if bird hits upper block
            if x < (x_block + block_width):
                if y < block_height:
                    if (x - imageWidth) < (block_width + x_block):
                        gameOver()


        if (x + imageWidth) > x_block:
            if (y +imageHeight) > (block_height + gap):
                if x < (block_width + x_block) :
                    gameOver()


        if  x_block < (x - block_width ) < x_block + block_move:
            current_score += 1


        if 3<= current_score < 5:
            block_move = 6
            gap = imageHeight * 2.7

        if 5<= current_score <8:
            block_move = 7
            gap = imageHeight * 2.5

        if current_score>8:
            block_move= 8
            gap = imageHeight *2.3
            
        
        pygame.display.update()             #to update the screen   update with parameters update only specific section
                                                                    #and without parameters it update entire screen
        clock.tick(60) #60 frames per sec


main()
pygame.quit()
quit()

                                                                                                                              
