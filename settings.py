import pygame

#win
width = 1000
height = 800
run = True
block = False
start = True
game = False

#player settings
x = 100
y = 480
playerWidth = 150
playerHeight = 200
speed = 4
score = 0
lives = 5

#move
go = None
tic = 0

#block settings
blockX = 500
blockY = 0
blockSize = 20
blockSpeed = 1.5
count = 0

#images
stayRight = pygame.image.load('textures/stay/stayRight.png')
apple = pygame.image.load('textures/apple/apple.png')
goRight = [pygame.image.load('textures/goRight/right1.png'), pygame.image.load('textures/goRight/right2.png')]
goLeft = [pygame.image.load('textures/goLeft/left1.png'), pygame.image.load('textures/goLeft/left2.png')]
eat = pygame.image.load('textures/eat/eat2.png')
heart = pygame.image.load('textures/apple/heart.png')
cloud1 = pygame.image.load('textures/background/cloud1.jpg')
player = stayRight