import pygame
from enum import Enum 
from tankClass import Tank #THIS THINGS JUST WOr
from bulletClass import Bullet
from globalVars import screen

#_____________________________________________all the variales_________________________________________
pygame.init()
bground = pygame.image.load('bground.jpg') #loading background image
gameover = pygame.image.load('gameover.jpg') #loading imaga for gameover screen
turn = pygame.mixer.Sound("turn.wav")
hit = pygame.mixer.Sound("probitie.wav")
destruction = pygame.mixer.Sound("destruction.wav")
mainloop = True #to start loop
tank1 = Tank('jaguar', 15,300, 300, 1, (255, 0, 0),3) #first tank (name,score's pos, tank's x, tank's y, speed, tuple for color, lives, default keys:arrows )
tank2 = Tank('T-34', 50,100, 100, 1, (0, 0, 255),3, pygame.K_d, pygame.K_a, pygame.K_w, pygame.K_s) # second tank, but keys are wasd
bullet1 = Bullet(tank1.x + int(tank1.width / 2), tank1.y + int(tank1.width / 2),(255, 123, 100)) # pos of tank + center of tank by its width and height, color
bullet2 = Bullet(tank2.x + int(tank2.width / 2), tank2.y + int(tank2.width / 2),(0,120,255)) # ↑
tanks = [tank1,tank2] #adding our instances to list
bullets = [bullet1,bullet2] # ↑


#_____________________________________________starting main loop of the game____________________________
while mainloop:
    for event in pygame.event.get(): # starting event listner
        if event.type == pygame.QUIT: # if clicked X button on caption
            mainloop = False #stopping main loop
        if event.type == pygame.KEYDOWN: #when some of the keys are pressed
            if event.key == pygame.K_ESCAPE: # if escape button is pressed
                mainloop = False #stopping main loop
            if event.key == pygame.K_RETURN: # return(enter) key
                if bullet1.drop == False: # if drop is false, then we appear(make it true)
                    bullet1.drop = True
                    bullet1.shoot(tank1) # shoot bullet from tank
            if event.key == pygame.K_SPACE: # the same thing with return button but with other instances
                if bullet2.drop == False:
                    bullet2.drop = True
                    bullet2.shoot (tank2)  
            for tank in tanks: # tracking whenever is button of direction is clicked by tank
                if event.key in tank.KEY.keys():
                    turn.play()
                    tank.change_direction(tank.KEY[event.key])
    if bullet1.colission(tank2) == True: #if bullet of tank1 hitted tank2
        hit.play()
        tank2.lives -= 1 #decrementing 1 life
        bullet1.drop = False # "disappearing" bullet
        bullet1.x, bullet1.y = tank1.x + int(tank1.width / 2), tank1.y + int(tank1.width / 2) #"giving back" bullet to the center of tank1
    if bullet2.colission(tank1) == True: #same thing from prev but vica versa
        hit.play()
        tank1.lives -= 1
        bullet2.drop = False
        bullet2.x, bullet2.y = tank2.x + int(tank2.width / 2), tank2.y + int(tank2.width / 2)
    for bullet in bullets: #if one of the bullets
        if bullet.out() == True: #if bullet shooted out of the screen
            bullet.drop = False # "disappearing" a bullet
    
                
    screen.blit(bground, (0, 0)) # settting background image

    for tank in tanks: #if one of a tanks
        tank.move() #move it in some direction
        tank.chances() #blitting lives' info which dependa on tank's left lives
        if tank.lives == 0: #if tank got zero lives
            destruction.play()
            bground=gameover #blitting background image by gameover image
            tank.dead() # just blitting over background image info which tank is destructed
            tank1.speed, tank2.speed = 0, 0 #stopping tanks
            tank1.width, tank2.width = 0, 0 #making tanks to "dissapear"
            tank1.color, tank2.color = (0,0,0), (0,0,0)
            for bullet in bullets: #if one of the bullets
                bullet.drop = False # "disappearing" a bullet
    bullet2.start(tank2.x + int(tank2.width / 2), tank2.y + int(tank2.width / 2)) #binding bullet to tank's pos
    bullet1.start(tank1.x + int(tank1.width / 2), tank1.y + int(tank1.width / 2)) # ↑
    pygame.display.flip() # Update the full display Surface to the screen
#_____________________________________________end of a main loop____________________________

pygame.quit() #when main loop stops this makes script to close