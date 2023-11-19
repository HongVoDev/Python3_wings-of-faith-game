#------System imports-----
import pygame
import sys
import time
import random
import text as tx
from constants import storyConstants as sc

class Scene:
    def __init__(self, story_list):
        self.background_image = story_list[0]
        self.background_image =\
            pygame.transform.scale(self.background_image, (500, 500))
        self.texts = story_list[1]
        self.first_choice = story_list[2]
        self.second_choice = story_list[3]
        self.text_object = tx.Text(self.texts, self.first_choice, self.second_choice)

    def display_scene(self, screen):
        # Display background image
        screen.blit(self.background_image, (0, 0))
        # Display texts
        font = pygame.font.SysFont('Berlin Sans FB',30)
        self.text_object.display_text_box(screen, self.texts)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                self.handle_user_input(event, screen)
        pygame.display.update()

    def transition_scene(self, screen, choice):
        screen.blit(pygame.transform.scale(choice[2], (500, 500)), (0, 0))
        self.text_object.display_text_box(screen, choice[1])
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for i, choice_position in enumerate([(450, 470, 460,480)]):
                            if (pygame.Rect(choice_position)).collidepoint(mouse_pos):
                                next_chapter = sc.story_dict.get(choice[0])
                                if (choice[0] < 9):                                    
                                    next_scene = Scene(next_chapter)
                                    next_scene.display_scene(screen)
                                else:
                                    screen.blit(next_chapter[0], (0, 0))
                                    ending_text = tx.Text(next_chapter[1], '', '')
                                    
                                    #screen.blit(ending_text.textDropShadow(next_chapter[1]), (5, 200))
                                    ending_text.ending_word_wrap(screen, next_chapter[1], 10, 200)
                                    pygame.display.update()
                                    
        
    def handle_user_input(self, event, screen):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
            # Check if any choice was clicked
            for i, choice_position in enumerate([(450, 470, 460,480)]):
                if (pygame.Rect(choice_position)).collidepoint(mouse_pos):
                    screen.blit(self.background_image, (0, 0))
                    if (self.text_object.display_choices(screen) == 1):
                        self.transition_scene(screen, self.first_choice)
                    elif (self.text_object.display_choices(screen) == 2):
                        self.transition_scene(screen, self.second_choice)
                    pygame.display.update()

                    

# Create the game window
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Wings Of Faith")
pygame.init()

# Create a new scene
story_list_1 = sc.story_dict.get(1)
scene1 = Scene(story_list_1)

# Game loop
scene1.display_scene(screen)
