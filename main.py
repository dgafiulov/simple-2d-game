import pygame
from settings import *
import random
import time

pygame.init()

win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.flip()
pygame.font.init()

f1 = pygame.font.Font(None, 40)
f2 = pygame.font.Font(None, 150)
f3 = pygame.font.Font(None, 60)
f4 = pygame.font.Font(None, 120)
finalText = f2.render('Ты проиграл!', 1, (0, 0, 0))
pullText = f3.render('нажмите куда угодно', 1, (255, 0, 0))
startText = f4.render('Глиста ест яблоки!', 1, (0, 255, 0))

pygame.display.set_caption('Глиста!')

win.fill((255, 255, 255))

while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	if start == True and game == False:
		win.blit(startText, (100, 100))
		win.blit(pullText, (250, 250))
		if event.type == pygame.MOUSEBUTTONDOWN:
			start = False
			game = True
	if game:
		win.fill((0, 168, 243))
		win.blit(cloud1, (100, 100))
		win.blit(cloud1, (700, 300))
		win.blit(cloud1, (350, 50))

		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT] and x > 0 and block == False:
			x = x - speed
			go = 'left'
		if keys[pygame.K_RIGHT] and x + playerWidth < width + 33 and block == False:
			x = x + speed
			go = 'right'
		if keys[pygame.K_RIGHT] == False and keys[pygame.K_LEFT] ==  False and block == False:
			go = 'stay'
		if blockX > x and blockX < x + playerWidth:
			player = eat
		if go == 'right':
			player = goRight[tic]
		if go == 'left':
			player = goLeft[tic]

		if blockY > height - 128:
			blockY = -100
			blockX = random.randint(0, width - blockSize)
			count += 1
			lives -= 1
			
		if count == 5:
			blockSpeed += 0.5
			count = 0
			speed += 0.8

		if blockY > y + 20 and blockY < y + 30:
			if blockX > x and blockX < x + playerWidth:
				score += 1
				count += 1
				blockY = -100
				blockX = random.randint(0, width - blockSize)
				if player == eat:
					player = stayRight

		#for i in range(count):
			#win.blit(apple, (width - blockSize - (i * 30), 10))
		for j in range(lives):
			win.blit(heart, (width - blockSize - (j * 30), 10))

		if lives <= 0:
			win.blit(finalText, (100, 100))
			win.blit(pullText, (250, 250))
			block = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				run = False

		scoreText = f1.render(str(score), False, (0, 0, 0))
		win.blit(scoreText, (10, 10))

		win.blit(player, (x, y))

		win.blit(apple, (blockX, blockY))

		pygame.draw.rect(win, (0, 255, 50), (0, 672, width, height - 672))

		tic += 1

		blockY += blockSpeed

		if tic > 1:
			tic = 0  

	pygame.display.update()
	pygame.display.flip()
	clock.tick(32)