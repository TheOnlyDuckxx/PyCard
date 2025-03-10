# Définition des cartes et effets

import pygame

# Paramètres des cartes
CARD_WIDTH, CARD_HEIGHT = 120, 180
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (200, 50, 50)

class Card:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.original_x = x
        self.original_y = y
        self.name = name
        self.width = CARD_WIDTH
        self.height = CARD_HEIGHT
        self.hovered = False
        self.dragging = False

    def draw(self, screen, font):
        """Affiche la carte."""
        color = RED if self.dragging else (WHITE if self.hovered else GRAY)
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height), border_radius=10)

        # Afficher le nom de la carte
        text_surface = font.render(self.name, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        """Vérifie si la souris est au-dessus de la carte."""
        x, y = mouse_pos
        self.hovered = self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height
        if self.hovered:
            self.width, self.height = CARD_WIDTH + 20, CARD_HEIGHT + 20  # Agrandir
        else:
            self.width, self.height = CARD_WIDTH, CARD_HEIGHT  # Remettre à la taille normale

    def start_drag(self):
        """Commence le drag de la carte."""
        self.dragging = True

    def move(self, mouse_pos):
        """Déplace la carte avec la souris."""
        if self.dragging:
            self.x, self.y = mouse_pos[0] - self.width // 2, mouse_pos[1] - self.height // 2

    def stop_drag(self, onboard):
        """Relâche la carte et la remet à sa position initiale."""
        self.dragging = False
        if onboard==False:
            self.x, self.y = self.original_x, self.original_y

    #Réalise l'action de la carte
    def action(self):
        print("Action réalisée avec succès")
        