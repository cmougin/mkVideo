# -*- coding: utf-8 -*-

print "début du programme..."
import pygame
from pygame.locals import *
import os
import time

# Before you can do much with pygame, you will need to initialize it
pygame.init()
clock = pygame.time.Clock()
 
def main():
    fenetre = pygame.display.set_mode((640, 480),FULLSCREEN,16)
    pygame.display.set_caption("Hello !")
    os.chdir("D:\\Dropbox\\src\\Python")
    h, m, s =time.localtime()[3:6]
    print "%d:%d:%d\n"%(h, m, s)
    img0 = pygame.image.load("0.jpg").convert()
    loop = True
    while loop:
        x, y = pygame.mouse.get_pos()
        x-= img0.get_width() / 2
        y-= img0.get_height() / 2
        fenetre.blit(img0, (x, y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
         # Actualisation de l'affichage
        pygame.display.update()
        # 10 fps
        clock.tick(10)
 
if __name__ == '__main__':
    main()
    print "fin du prg."