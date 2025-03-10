# Interface utilisateur (affichage des cartes, boutons…)
import pygame
from card import Card

class Board:
    def __init__(self, x, y, width, height, color=(255, 255, 255)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=10)

    def on_board(self, card):
        """Vérifie si la carte est lâchée sur le plateau."""
        return self.rect.colliderect(pygame.Rect(card.x, card.y, card.width, card.height))