import pygame 
pygame.init()
import random
font = pygame.font.Font(None, 204)
text = font.render("🍟", True,(0, 0, 0))

windows = pygame.display.set_mode((1370,714))

players = [pygame.Rect(925,225,100,200),
            pygame.Rect(725,225,100,200),
            pygame.Rect(525,225,100,200),
            pygame.Rect(325,225,100,200)] 


text_on_area = random.choice(players)
start_time = pygame.time.get_ticks()

score = 0
game = True
clock = pygame.time.Clock()

while game:
    windows.fill((9, 128, 251))
    windows.blit(text,(40,40))
    
    for p1 in players:
       pygame.draw.rect(windows,(0,0,255), p1)

    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time
    if elapsed_time > 1000:
        text_on_area = random.choice(players)
        start_time = pygame.time.get_ticks()
    windows.blit(text,(text_on_area.x,text_on_area.y))
 
    
    #pygame.draw.rect(windows,(0,0,255),player)
    #pygame.draw.rect(windows,(0,0,255),player1)
    #pygame.draw.rect(windows,(0,0,255),player2)
    #pygame.draw.rect(windows,(0,0,255),player3)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x,y = event.pos
            if text_on_area.collidepoint(x,y):
                score += 1
                print(score)
        elif event.type == pygame.KEYDOWN:
            print(20)
    pygame.display.update()
    clock.tick(60)
 