import pygame
import numpy as np

class GameEvent():
    def __int__(self, event_type, data):
        self.type = event_type
        self.data = data

    def set_allowed_event():
        pygame.event.set_allowed([pygame.KEYDOWN, pygame.quit])

    def events():
        closed = False
        quit = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closed = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        quit = True
        return {"quir_to_main_menu":quit, "closed":closed, "clicked":pygame.mouse.get_pressed()[0], "mouse_pos": np.array(pygame.mouse.get_pos())}