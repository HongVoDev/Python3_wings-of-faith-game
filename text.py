#------System imports-----
import pygame
import sys
import time
import random
import pygame.freetype
from constants import generalConstants as gc
from constants import imagePathConstants as ipc
import textEffect as te

class Text(te.TextEffect):
    
    def display_button(self, surf, choice1, choice2, ic, ac):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()        
        
        if (450 > mouse[0] > 50 and 360 > mouse[1] > 280):
            pygame.draw.rect(surf, ac,(50, 280, 400, 80))
            self.display_center_word_wrap(choice2,(0,0,0), 250, 300, surf, 370)
            if click[0] == 1:
                return 2
        elif (450 > mouse[0] > 50 and 200 > mouse[1] > 120):
            pygame.draw.rect(surf, ac,(50, 120, 400, 80))
            self.display_center_word_wrap(choice1,(0,0,0), 250, 140, surf, 370)
            if click[0] == 1:
                return 1 
        else:
            pygame.draw.rect(surf, ic,(50, 120, 400, 80))
            pygame.draw.rect(surf, ic,(50, 280, 400, 80))
            self.display_center_word_wrap(choice1,(0,0,0), 250, 140, surf, 370)
            self.display_center_word_wrap(choice2,(0,0,0), 250, 300, surf, 370)
  
    def display_choices(self, surf):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if (self.display_button(surf, self.first_choice[1], self.second_choice[1],
                            gc.LIGHT_GREY, gc.WHITE) == 1):
                return 1
            elif (self.display_button(surf, self.first_choice[1], self.second_choice[1],
                            gc.LIGHT_GREY, gc.WHITE) == 2):
                return 2
            pygame.display.update()
    
    def display_text_box(self, surf, text):
        chat_box = ipc.Chat_Box
        chat_box = \
                 pygame.transform.scale(chat_box, (490, 150))
        surf.blit(chat_box, (gc.TEXTBOX_POS))
        self.word_wrap(surf, text)
        self.display_text(surf, "OK", 450, 470)
        
