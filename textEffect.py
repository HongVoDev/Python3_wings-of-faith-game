#------System imports-----
import pygame
import sys
import time
import random
import pygame.freetype
from constants import generalConstants as gc
from constants import imagePathConstants as ipc

pygame.init()
class TextEffect:
    
    def __init__(self, text, first_choice, second_choice):
        global font
        font = pygame.font.SysFont(gc.MONOSPACE, gc.MONOSPACE_FONT_SIZE)
        self.text = text
        self.first_choice = first_choice
        self.second_choice = second_choice

    def display_text_animation(self, gameDisplay, string, x, y, speed, color):
        text = ''
        for i in range(len(string)):
            text += string[i]
            text_surface = font.render(text, True, color)      

            text_rect = text_surface.get_rect()
            text_rect= (x,y)
            gameDisplay.blit(text_surface, text_rect)
            pygame.display.update()
            pygame.time.wait(speed)
        gameDisplay.blit(text_surface, text_rect)

    def word_wrap(self, surf, text, color = (0, 0, 0)):
        font = pygame.freetype.SysFont(gc.MONOSPACE, gc.MONOSPACE_FONT_SIZE)
        font.origin = True
        words = text.split(' ')
        width, height = surf.get_size()
        line_spacing = font.get_sized_height() + 5
        x, y = gc.TEXT_START_X_POS, gc.TEXT_START_Y_POS + line_spacing
        space = font.get_rect(' ')
        for word in words:
            bounds = font.get_rect(word)
            if x + bounds.width + bounds.x >= width - 5:
                x, y = gc.TEXT_START_X_POS, y + line_spacing
            if x + bounds.width + bounds.x >= width:
                raise ValueError("word too wide for the surface")
            if y + bounds.height - bounds.y >= height:
                raise ValueError("text to long for the surface")
            self.display_text_animation(surf, word, x, y, gc.TEXT_DISPLAY_SPEED, color)
            x += bounds.width + space.width                        
        return x, y
    
    
    def ending_word_wrap(self, surf, text, x, y, color = (255, 255, 255)):
        font = pygame.freetype.SysFont(gc.MONOSPACE, gc.MONOSPACE_FONT_SIZE)
        font.origin = True
        words = text.split(' ')
        width, height = surf.get_size()
        line_spacing = font.get_sized_height() + 5
        x, y = x, y + line_spacing
        space = font.get_rect(' ')
        myfont = pygame.font.SysFont(gc.MONOSPACE, gc.MONOSPACE_FONT_SIZE)
        for word in words:
            bounds = font.get_rect(word)
            if x + bounds.width + bounds.x >= width - 5:
                x, y = gc.TEXT_START_X_POS, y + line_spacing
            if x + bounds.width + bounds.x >= width:
                raise ValueError("word too wide for the surface")
            if y + bounds.height - bounds.y >= height:
                raise ValueError("text to long for the surface")
            text_surface = myfont.render(word, True, gc.BLACK)      

            text_rect = text_surface.get_rect()
            text_rect= (x,y)
            surf.blit(text_surface, text_rect)
            pygame.display.flip()
            pygame.display.update()
            x += bounds.width + space.width            

        return x, y
    
    def text_object(self, text):
        textSurface = self.font.render(text, True, gc.DARK_GREY)
        return textSurface, textSurface.get_rect()
    
    def display_text(self, surf, text, x, y):
        text_surface = font.render(text, True, gc.BLACK)      

        text_rect = text_surface.get_rect()
        text_rect= (x,y)
        surf.blit(text_surface, text_rect)
        pygame.display.update()
        
    def display_center_word_wrap(self, text, colour, x, y, screen, allowed_width):
        # first, split the text into words
        words = text.split()
        # now, construct lines out of these words
        lines = []
        while len(words) > 0:
            # get as many words as will fit within allowed_width
            line_words = []
            while len(words) > 0:
                line_words.append(words.pop(0))
                fw, fh = font.size(' '.join(line_words + words[:1]))
                if fw > allowed_width:
                    break
            # add a line consisting of those words
            line = ' '.join(line_words)
            lines.append(line)
        # now we've split our text into lines that fit into the width, actually
        # render them
        # we'll render each line below the last, so we need to keep track of
        # the culmative height of the lines we've rendered so far
        y_offset = 0
        for line in lines:
            fw, fh = font.size(line)
            # (tx, ty) is the top-left of the font surface
            tx = x - fw / 2
            ty = y + y_offset
            font_surface = font.render(line, True, colour)
            screen.blit(font_surface, (tx, ty))
            y_offset += fh
   
