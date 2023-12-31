#Libraries
import pygame
import random
import math
import os

#Python files for the levels
from levels import arcade

#Saving score
save = open(os.path.join("saves", "score.txt"), "r")

#Assets pathing
icon_path = os.path.join("assets", "general", "icon.png")
background_path = os.path.join("assets", "general", "background.png")
levels_path = os.path.join("assets", "home", "levels.png")
options_path = os.path.join("assets", "home", "options.png")
start_path = os.path.join("assets", "home", "start.png")
home_path = os.path.join("assets", "general", "home.png")
spaceship8_path = os.path.join("assets", "spaceships", "8.png")
enemy1_path = os.path.join("assets", "enemys", "1.png")
bullet_path = os.path.join("assets", "general", "bullet.png")

#Assets loading
icon = pygame.image.load(icon_path)
background = pygame.image.load(background_path)
levels = pygame.image.load(levels_path)
options = pygame.image.load(options_path)
start = pygame.image.load(start_path)
home_ico = pygame.image.load(home_path)
spaceship8 = pygame.image.load(spaceship8_path)
enemy1 = pygame.image.load(enemy1_path)
bullet = pygame.image.load(bullet_path)

#Object for home buttons
class homeButtonsObj():
    def screen(self):
        screen.blit(background, (0, 0))
    def buttons(self, img1, img2, img3, x, y):
        screen.blit(img1, (x, y))
        screen.blit(img2, (x, (y + 64)))
        screen.blit(img3, (x, (y + 128)))
        
#Function to show for player
def player(img,x, y):
    screen.blit(img, (x, y))

#Function to get mouse position
def mousePosition():
    mousePos = 0
    if event.type == pygame.MOUSEBUTTONDOWN:
        mousePos = pygame.mouse.get_pos()
    return mousePos

#Object for home_ico
class homeIco():
    def __init__(self):
        self.houseClicked = "no"
    def show(self, x, y):
        self.x = x
        self.y = y
        screen.blit(home_ico, (self.x, self.y))
    def homeClicked(self):
        houseIco_rect = start.get_rect(topleft=(self.x, self.y))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if houseIco_rect.collidepoint(mousePosition()):
                self.houseClicked = "yes"
            else:
                self.houseClicked = "no"
#Object to detect if mouse clicks on the buttons
class clicking():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.screen = "home"
    def startClicked(self):
        start_rect = start.get_rect(topleft=(self.x, self.y))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_rect.collidepoint(mousePosition()):
                self.screen = "start"
                arcade.scoreValue = 0
    def levelsClicked(self):
        levels_rect = levels.get_rect(topleft=(self.x, (self.y + 64)))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if levels_rect.collidepoint(mousePosition()):
                self.screen = "levels"
    def optionsClicked(self):
        options_rect = options.get_rect(topleft=(self.x, (self.y + 128)))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if options_rect.collidepoint(mousePosition()):
                self.screen = "options"

#Collision detect for bullet and enenyms
def iscollison(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

#Bullet shooting
def fire(img, x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(img, (x + 8, y + 8))

#System initialize
pygame.init()
screen = pygame.display.set_mode((800, 600)) #(208,108)
pygame.display.set_caption("The space fighter")
pygame.display.set_icon(icon)
running = True
home = clicking(336, 264)
house = homeIco()
homeButtons = homeButtonsObj()
playerX = 368
playerY = 500
playerXChange = 0
playerYChange = 0
arcade.enemyMaker()
bulletX = 0
bulletY = 0
bullet_state = "ready"
arcade.scoreMaxValue = int(save.readline().strip())

#»»»»»»»»» Program Core
while running:
#»»»»»»»»» Screen drawing
    screen.blit(background, (0, 0))
#»»»»»»»»» Checking for pressed buttons
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save.seek(0)
            if int(save.readline().strip()) < arcade.scoreMaxValue:
                save2 = open(os.path.join("saves", "score.txt"), "w")
                save2.write(str(arcade.scoreMaxValue))
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXChange -= 0.55
            if event.key == pygame.K_RIGHT:
                playerXChange += 0.55
            if event.key == pygame.K_UP:
                playerYChange -= 0.45
            if event.key == pygame.K_DOWN:
                playerYChange += 0.45
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    bulletY = playerY
                    fire(bullet, bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXChange = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerYChange = 0
#»»»»»»»»» Checking for mouse position
    mousePosition()
#»»»»»»»»» Checking the screen we're in
    if home.screen == "home":
        arcade.showMaxScore(10, 10)
#»»»»»»»»» Assembling the buttons at home screen
        homeButtons.buttons(start, levels, options, 320, 264)
#»»»»»»»»» Checking for pressed buttons
        home.startClicked()
        home.levelsClicked()
        home.optionsClicked()
#»»»»»»»»» Checking the screen we're in
    elif home.screen == "start":
        arcade.showScore(10, 10)
#»»»»»»»»» Assembling house button/checking if it's pressed
        house.show(750, 20)
        house.homeClicked()
        if house.houseClicked == "yes":
            for _ in range(arcade.enemysNumber):
                arcade.enemysXPosList[_] = random.randint(0, 768)
                arcade.enemysYPosList[_] = random.randint(0, 100)
            home.screen = "home"
        homeButtons.screen
#»»»»»»»»» Player cords changing
        playerX += playerXChange
        playerY += playerYChange
        if playerX > 768:
            playerX = 768
        if playerX < 0:
            playerX = 0
        if playerY > 568:
            playerY = 568
        if playerY < 0:
            playerY = 0
#»»»»»»»»» Giving cords to the enemys
        for _ in range(arcade.enemysNumber):
            arcade.enemysYChange.append(0)
        for _ in range(arcade.enemysNumber):
            arcade.enemysYChange[_] = random.uniform(0.05, 0.15)
            arcade.enemysYPosList[_] += arcade.enemysYChange[_]
        for _ in range(arcade.enemysNumber):
            collision = iscollison(arcade.enemysXPosList[_], arcade.enemysYPosList[_], bulletX, bulletY)
            if collision:
                bulletY = 480
                bullet_state = "ready"
                arcade.enemysHit[_] = True
#»»»»»»»»» Check to see if bullet is fired
        if bullet_state == "fire":
            fire(bullet, bulletX, bulletY)
            bulletY -= 1.3
#»»»»»»»»» Check to see if bullet is ready
            if bulletY <= 0:
                bulletY = 500
                bullet_state = "ready"
#»»»»»»»»» Calling the enemys to the game
        arcade.showEnemy(enemy1)
#»»»»»»»»» Calling the player spaceship to the space
        for _ in range(arcade.enemysNumber):
            if arcade.enemysHit[_]:
                arcade.enemysXPosList[_] = random.randint(0, 768)
                arcade.enemysYPosList[_] = random.randint(0, 100)
                arcade.enemysHit[_] = False
                arcade.scoreValue += 1
        player(spaceship8, playerX, playerY)
        for _ in range(arcade.enemysNumber):
            if arcade.enemysYPosList[_] >= 568:
                for _ in range(arcade.enemysNumber):
                    arcade.enemysXPosList[_] = random.randint(0, 768)
                    arcade.enemysYPosList[_] = random.randint(0, 100)
                    if arcade.scoreValue > arcade.scoreMaxValue:
                        arcade.scoreMaxValue = arcade.scoreValue
                home.screen = "home"
#»»»»»»»»» Checking the screen we're in
    elif home.screen == "levels":
#»»»»»»»»» Assembling house button/ checking if it's pressed
        house.show(750, 20)
        house.homeClicked()
        if house.houseClicked == "yes":
            home.screen = "home"
        homeButtons.screen
#»»»»»»»»» Checking the screen we're in
    elif home.screen == "options":
#»»»»»»»»» Assembling house button/ checking if it's pressed
        house.show(750, 20)
        house.homeClicked()
        if house.houseClicked == "yes":
            home.screen = "home"
        homeButtons.screen
#»»»»»»»»» Screen updating for redraw
    pygame.display.update()