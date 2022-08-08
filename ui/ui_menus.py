import pygame_gui
import pygame
from pygame_gui.core import ObjectID
from pygame_gui.elements import UIButton

# Construye una ventana con el layout de la interfaz
def esqueleto(WIDTH, HEIGHT, manager):

    
    scen1_layout_rect = pygame.Rect( WIDTH/4 + 30, 5, 150, 40)
    scen2_layout_rect = pygame.Rect(WIDTH/4 + 180, 5, 150, 40)
    scen3_layout_rect = pygame.Rect( WIDTH/4 + 330, 5, 150, 40)
    about = pygame.Rect(WIDTH/4 + 480, 5, 150, 40)

    panel1_layout = pygame.Rect(WIDTH/4, 0, 655, 50)
    panel2_layout = pygame.Rect(0, 55, WIDTH, 80)
    panel3_layout = pygame.Rect(0, 145, WIDTH, HEIGHT - 145)
    
    panel1 = pygame_gui.elements.UIPanel(relative_rect=panel1_layout, starting_layer_height=0, manager=manager,
                                        object_id=ObjectID(
                                            class_id='@panel1', object_id='#panel1'),    
                                        )

    scen1_button = UIButton(relative_rect=scen1_layout_rect,
                            text='Escenario 1',
                            manager=manager,
                            object_id=ObjectID(class_id='@menu_buttons', object_id='#scen1_button'),

                        )

    scen2_button = UIButton(relative_rect=scen2_layout_rect,
                            text='Escenario 2',
                            manager=manager,
                            object_id=ObjectID(class_id='@menu_buttons',
                                            object_id='#scen1_button'))

    scen3_button = UIButton(relative_rect=scen3_layout_rect,
                            text='Escenario 3',
                            manager=manager,
                            object_id=ObjectID(class_id='@menu_buttons',
                                            object_id='#scen1_button'))
    about_button = UIButton(relative_rect=about,
                            text='Acerca de',
                            manager=manager,
                            object_id=ObjectID(class_id='@menu_buttons',
                                            object_id='#about_button'))


    panel2 = pygame_gui.elements.UIPanel(relative_rect=panel2_layout, starting_layer_height=0, manager=manager,
                                        object_id=ObjectID(
                                            class_id='@panel2', object_id='#panel2'),    
                                        )


    panel3 = pygame_gui.elements.UIPanel(relative_rect=panel3_layout, starting_layer_height=0, manager=manager, object_id=ObjectID(object_id="panel3", class_id = "@panel3"))
    return scen1_layout_rect, scen2_layout_rect, scen3_layout_rect, about, panel1_layout, panel2_layout, panel3_layout, panel1, scen1_button, scen2_button, scen3_button, about_button, panel2, panel3
