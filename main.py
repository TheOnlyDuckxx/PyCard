# Point d’entrée du jeu
import pygame
import random
from card import Card  # On importe la classe depuis cards.py
from ui import Board

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Démo Combat - Jeu de Cartes")
WIDTH, HEIGHT = screen.get_size()

# Police
font = pygame.font.Font(None, 24)

# Créer un plateau de jeu
board = Board(WIDTH/3.5, HEIGHT/4, WIDTH/2.4, HEIGHT/2)
print(WIDTH, HEIGHT)
# Liste des noms de cartes
cards_text = ["Attaque", "Défense", "Hack", "Surcharge", "Analyse","Bob","Zulu"]
cards = []

# Générer 5 cartes aléatoires en bas de l'écran
spacing = 20
start_x = (WIDTH - (5 * (120 + spacing))) // 2
y_position = HEIGHT - 180 - 30

for i, card_name in enumerate(random.sample(cards_text, min(5, len(cards_text)))):
    cards.append(Card(start_x + i * (120 + spacing), y_position, card_name))

# Boucle principale
running = True
while running:
    screen.fill((30, 30, 30))
    mouse_pos = pygame.mouse.get_pos()
    board.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for card in cards:
                if card.hovered:
                    card.start_drag()

        elif event.type == pygame.MOUSEBUTTONUP:
            for card in cards:
                if board.on_board(card):
                    card.action() 
                    card.stop_drag(True)
                else:
                    card.stop_drag(False)

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # Met à jour les cartes
    for card in cards:
        card.check_hover(mouse_pos)
        card.move(mouse_pos)
        card.draw(screen, font)
        

    pygame.display.flip()

pygame.quit()
