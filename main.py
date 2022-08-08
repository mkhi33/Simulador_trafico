import pygame
import pygame_gui
import time

from pygame_gui.core import ObjectID
from pygame_gui.elements import UIButton

from ui import draw_cars
from ui import escenario_1
from ui import escenario_2
from ui import ui_menus

# Constantes
WIDTH = 1200
HEIGHT = 700

COLORS = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
}

# Inicialización básica de pygame
pygame.init()
pygame.display.set_caption('Simulador de tráfico')
window_surface = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.Surface((WIDTH, HEIGHT))
background.fill(pygame.Color('#ffffff'))

manager = pygame_gui.UIManager((WIDTH, HEIGHT),'./ui/theme.json')

# Fin inicialización básica de pygame

# Dibujar los elementos de pantalla principal

esc1 = escenario_1.Escenario1()
esc2 = escenario_2.Escenario2()

scen1_layout_rect, scen2_layout_rect, scen3_layout_rect, about, panel1_layout, panel2_layout, panel3_layout, panel1, scen1_button, scen2_button, scen3_button, about_button, panel2, panel3 = ui_menus.esqueleto(WIDTH, HEIGHT, manager)

# Fin de elementos en pantalla




def selectOption(option):
    if option == 'scen1':
        esc1.run(panel3, pygame_gui, manager, window_surface)

        scen1_button.select()
        scen2_button.unselect()
        scen3_button.unselect()
        about_button.unselect()
    elif option == 'scen2':

        esc2.run(panel3, pygame_gui, manager, window_surface)


        scen1_button.unselect()
        scen2_button.select()
        scen3_button.unselect()
        about_button.unselect()
    elif option == 'scen3':
        scen1_button.unselect()
        scen2_button.unselect()
        scen3_button.select()
        about_button.unselect()
    elif option == 'about':
        scen1_button.unselect()
        scen2_button.unselect()
        scen3_button.unselect()
        about_button.select()
        panel3.set_image(pygame.image.load('./resources/images/acerca_de.png'))

    else:
        print('Opcion no valida')

def limpiar_manager():
    manager.clear_and_reset()
    scen1_layout_rect, scen2_layout_rect, scen3_layout_rect, about, panel1_layout, panel2_layout, panel3_layout, panel1, scen1_button, scen2_button, scen3_button, about_button, panel2, panel3 = ui_menus.esqueleto(WIDTH, HEIGHT, manager)


clock = pygame.time.Clock()
is_running = True
count = 0



while is_running:
    time_delta = clock.tick(60)/1000.0


    if scen2_button.is_selected:
        count += 1
        esc2.actualizarPos()
        if(count >= 50):
            esc2.generarCarros(1, pygame, pygame_gui, window_surface, manager)
            count = 0
    if scen1_button.is_selected:
        count += 1
        esc1.actualizarPos()
        if(count >= 50):
            esc1.generarCarros(1, pygame, pygame_gui, window_surface, manager)
            count = 0

        

    for event in pygame.event.get():

        # Eventos
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == scen1_button:
                manager.clear_and_reset()
                scen1_layout_rect, scen2_layout_rect, scen3_layout_rect, about, panel1_layout, panel2_layout, panel3_layout, panel1, scen1_button, scen2_button, scen3_button, about_button, panel2, panel3 = ui_menus.esqueleto(WIDTH, HEIGHT, manager)
                selectOption('scen1')

            elif event.ui_element == scen2_button:
                manager.clear_and_reset()
                scen1_layout_rect, scen2_layout_rect, scen3_layout_rect, about, panel1_layout, panel2_layout, panel3_layout, panel1, scen1_button, scen2_button, scen3_button, about_button, panel2, panel3 = ui_menus.esqueleto(WIDTH, HEIGHT, manager)
                selectOption('scen2')

            elif event.ui_element == scen3_button:
                manager.clear_and_reset()
                scen1_layout_rect, scen2_layout_rect, scen3_layout_rect, about, panel1_layout, panel2_layout, panel3_layout, panel1, scen1_button, scen2_button, scen3_button, about_button, panel2, panel3 = ui_menus.esqueleto(WIDTH, HEIGHT, manager)
                selectOption('scen3')

            elif event.ui_element == about_button:
                manager.clear_and_reset()
                scen1_layout_rect, scen2_layout_rect, scen3_layout_rect, about, panel1_layout, panel2_layout, panel3_layout, panel1, scen1_button, scen2_button, scen3_button, about_button, panel2, panel3 = ui_menus.esqueleto(WIDTH, HEIGHT, manager)
                selectOption('about')

        # Eventos para los escenarios

        if scen1_button.is_selected:
            # Eventos para el escenario 1
            if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:

                # Eventos para el escenario 2

                if event.ui_element == esc1.slider1:
                    esc1.slider_value1 = event.value
                    esc1.label_silder_value1.set_text(": %s"%esc1.slider_value1)

                elif event.ui_element == esc1.slider_velocidad:
                    esc1.velocidad_simulacion = event.value
                    esc1.label_slider_value3.set_text("%s %s"%(esc1.velocidad_simulacion, '%'))
            
            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == esc1.btn_semaforo:
                    esc1.setSemaforo()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event)
            

        elif scen2_button.is_selected:
            # Eventos para el escenario 2
            if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:

                # Eventos para el escenario 2

                if event.ui_element == esc2.slider1:
                    esc2.slider_value1 = event.value
                    esc2.label_silder_value1.set_text(": %s"%esc2.slider_value1)

                elif event.ui_element == esc2.slider2:
                    esc2.slider_value2 = event.value
                    esc2.label_slider_value2.set_text(": %s"%esc2.slider_value2)
                elif event.ui_element == esc2.slider3:
                    esc2.velocidad_simulacion = event.value
                    esc2.label_slider_value3.set_text("%s %s"%(esc2.velocidad_simulacion, '%'))
            elif event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if event.ui_element == esc2.dpd_cantidad_carriles:
                    esc2.n_carriles = int(event.text)
                    esc2.actualizarCarriles(panel3)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event)
        manager.process_events(event)
        

    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    
    manager.draw_ui(window_surface)
    
    pygame.display.update()


