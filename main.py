# Point d’entrée du jeu
import pygame
import random
from card import Card  # On importe la classe depuis cards.py

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Démo Combat - Jeu de Cartes")

# Police
font = pygame.font.Font(None, 24)

# Liste des noms de cartes
cards_text = ["Attaque", "Défense", "Hack", "Surcharge", "Analyse"]
cards = []

# Générer 5 cartes aléatoires en bas de l'écran
spacing = 20
start_x = (WIDTH - (len(cards_text) * (120 + spacing))) // 2
y_position = HEIGHT - 180 - 30

for i, card_name in enumerate(random.sample(cards_text, len(cards_text))):
    cards.append(Card(start_x + i * (120 + spacing), y_position, card_name))

# Boucle principale
running = True
while running:
    screen.fill((30, 30, 30))
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for card in cards:
                if card.hovered:
                    card.start_drag()

        elif event.type == pygame.MOUSEBUTTONUP:
            for card in cards:
                card.stop_drag()

    # Met à jour les cartes
    for card in cards:
        card.check_hover(mouse_pos)
        card.move(mouse_pos)
        card.draw(screen, font)

    pygame.display.flip()

pygame.quit()
