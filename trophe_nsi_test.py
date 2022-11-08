#menu
import pygame, sys
from pygame.locals import *
from trophee_jeu1 import *
from annexe import *
from trophee_jeu4 import *


pygame.init()
pygame.key.set_repeat(10)


impact = pygame.font.SysFont('Impact', 60)
little_impact = pygame.font.SysFont('Impact', 30)

#mode, menu = 0, 

mode = [0, 0]
niveau = ['Aucun niveau selectionné']
texte_niveau = ["Aucun niveau n'est sélectionné"]

hauteur = [800]
longueur = [1500]

#création fenetre
pygame.display.set_caption("Test_Jeux")
fenetre = pygame.display.set_mode((1500, 800), )
position_fenetre = fenetre.get_rect()



class bouton:
    def __init__(self, hauteur, longueur, x, y, couleur, texte, multi_y):
        self.hauteur = hauteur
        self.longueur = longueur
        self.x = x
        self.y = y
        self.couleur = couleur
        self.texte = texte
        self.rectangle = pygame.draw.rect(fenetre, self.couleur, (self.x, self.y, self.longueur, self.hauteur))
        self.multi_y = multi_y
        
    def apparition(self): 
        pygame.draw.rect(fenetre, self.couleur, (self.x, self.y, self.longueur, self.hauteur))
        text = impact.render(self.texte, True, (0,0,0))
        text_rect = text.get_rect(center=(self.x + self.longueur/2, self.y + self.hauteur/2))
        fenetre.blit(text, text_rect)
    
    def adaptation_taille(self, new_hauteur, new_longueur):
        self.y = new_hauteur / self.multi_y
        self.longueur = new_longueur / 5
        self.hauteur = new_hauteur / 4.705882353
        
     
def mode_menu():
    fenetre = pygame.display.set_mode((1500, 800), )
    fenetre.fill([250, 250, 250])
    bouton_menu = []
    play_button = bouton(170, 300, 24, 24, (50, 100, 200), 'Jouer', 33)
    bouton_menu.append(play_button)
    level_button = bouton(170, 300, 24, 218, (50, 100, 200), 'Niveau', 3.669724771)
    bouton_menu.append(level_button)
    help_button = bouton(170, 300, 24, 412, (50, 100, 200), 'Aide', 1.941747573)
    bouton_menu.append(help_button)
    leave_button = bouton(170, 300, 24, 606, (50, 100, 200), 'Quitter', 1.320132013)
    bouton_menu.append(leave_button)
    font = pygame.font.Font(pygame.font.get_default_font(), 25)
    text = font.render(texte_niveau[0], True, (0, 0, 0))
    fenetre.blit(text, dest=(375, 140))
    text = font.render(niveau[0], True, (0, 0, 0))
    fenetre.blit(text, dest=(375, 80))
    
    for boutons in bouton_menu:
        boutons.adaptation_taille(hauteur[0], longueur[0])
        boutons.apparition()
        
    for event in pygame.event.get() :
        if event.type == pygame.VIDEORESIZE:
            longueur[0], hauteur[0] = event.size
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                
                if play_button.rectangle.collidepoint(event.pos):
                    mode[0] = 2
                    
                if level_button.rectangle.collidepoint(event.pos):
                    mode[0] = 1
                    
                if help_button.rectangle.collidepoint(event.pos):
                    mode[0] = 3
                    
                if leave_button.rectangle.collidepoint(event.pos):
                     pygame.display.quit()
                     sys.exit()
                     
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
            
    pygame.display.flip()
        
def mode_level():
    fenetre = pygame.display.set_mode((1500, 800), )
    fenetre.fill([250, 250, 250])
    bouton_level = []
    jeu1_button = bouton(170, 300, 24, 24, (50, 100, 200), 'Jeu1', 33)
    bouton_level.append(jeu1_button)
    jeu2_button = bouton(170, 300, 24, 218, (50, 100, 200), 'Jeu2', 3.669724771)
    bouton_level.append(jeu2_button)
    jeu3_button = bouton(170, 300, 24, 412, (50, 100, 200), 'Casse brique', 1.941747573)
    bouton_level.append(jeu3_button)
    return_button = bouton(170, 300, 24, 606, (50, 100, 200), 'Retour', 1.320132013)
    bouton_level.append(return_button)
    
    for boutons in bouton_level:
        boutons.adaptation_taille(hauteur[0], longueur[0])
        boutons.apparition()
        
    for event in pygame.event.get() :
        if event.type == pygame.VIDEORESIZE:
            longueur[0], hauteur[0] = event.size
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                
                if jeu1_button.rectangle.collidepoint(event.pos):
                    mode[1] = 1
                    mode[0] = 0
                    niveau[0] = "mangeballe"
                    texte_niveau[0] = "Un jeu qui consiste à manger les autres"
                    
                if jeu2_button.rectangle.collidepoint(event.pos):
                    mode[1] = 2
                    mode[0] = 0
                    niveau[0] = "teamball"
                    texte_niveau[0] = "Un jeu demandant de la réflexion, en combat d'équipe"
                    
                if jeu3_button.rectangle.collidepoint(event.pos):
                    mode[1] = 3
                    mode[0] = 0
                    niveau[0] = "casse brique"
                    texte_niveau[0] = "Un jeu de dextérité où vous devez cassez des briques sans perdre votre balles" 
                    
                if return_button.rectangle.collidepoint(event.pos):
                     mode[0] = 0
                     
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
            
    pygame.display.flip()

def play():
    mode[0] = 0
    if mode[1] == 0:
        texte_niveau[0] = 'Veillez selectionnez un niveau'
    if mode[1] == 1:
        mangeballe()
    elif mode[1] == 2:
        teamball()
    elif mode[1] == 3:
        texte_niveau[0] = 'momentanément indisponible'

def aide():
    mode[0] = 0
    if mode[1] == 0:
        texte_niveau[0] = 'Veillez selectionnez un niveau'
    if mode[1] == 1:
        regle1()
    elif mode[1] == 2:
        regle2()
    elif mode[1] == 3:
        texte_niveau[0] = 'momentanément indisponible'

while True:
    if mode[0] == 0:
        mode_menu()
    if mode[0] == 1:
        mode_level()
    if mode[0] == 2:
        play()
    if mode[0] == 3:
        aide()
