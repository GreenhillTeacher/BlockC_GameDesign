import pygame, time
pygame.init()

wind=pygame.display.set_mode((700,700))
pygame.display.set_caption("Testing")

#create different FNTS

TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('comicsans', 40)
INST_FNT=pygame.font.SysFont('comicsans', 15)


text=TITLE_FNT.render("Greenhill",1,(0,255,150))
wind.fill((255,255,255))
wind.blit(text, (150,50))
text1=MENU_FNT.render("Instructions",1,(200,25,150))
wind.blit(text1, (150,200))
message="the key t play this game is play and play and play"
text=INST_FNT.render(message,1,(0,0,0))
wind.blit(text, (50,250))
pygame.display.update()

pygame.time.delay(10000)