import pygame

pygame.init()
pygame.display.flip()

image = pygame.image.load('images/test.png').convert()
image = pygame.transform.scale(image, (50, 100))
image_rect = image.get_rect()