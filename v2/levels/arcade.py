import pygame
import random

#Modules initialize
pygame.init()

#Screen
screen = pygame.display.set_mode((800, 600))

#Enemys
enemysNumber = random.randrange(5, 10)
enemysHit = [False] * enemysNumber
enemysDead = []
enemysXPosList = []
enemysYPosList = []
enemysYChange = []

#Score
font = pygame.font.Font("freesansbold.ttf", 32)
scoreValue = 0
scoreMaxValue = 0

#Show score
def showScore(x, y):
    score = font.render("Score: " + str(scoreValue), True, (255, 255, 255))
    screen.blit(score, (x, y))
def showMaxScore(x, y):
    score = font.render("Max score: " + str(scoreMaxValue), True, (255, 255, 255))
    screen.blit(score, (x, y))

#Enemy creating
def enemyMaker():
    for _ in range(enemysNumber):
        eXp = random.randint(100, 668)
        eYp = random.randint(0, 100)
        enemysXPosList.append(eXp)
        enemysYPosList.append(eYp)

def showEnemy(enemyImg):
    for _ in range(enemysNumber):
        screen.blit(enemyImg, (enemysXPosList[_], enemysYPosList[_]))