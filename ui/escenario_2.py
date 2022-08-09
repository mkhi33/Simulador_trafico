import pygame
from ui import draw_cars
import random
import math

class Escenario2:
    def __init__(self):
        self.car = None
        self.cars = []
        self.velocidad_simulacion = 5
        


    def run(self, panel3, pygame_gui, manager, window_surface):

        RANGE_SLIDER = (0, 500)

        self.label_slider_layout1 = pygame.Rect(5, 50, 250, 50) 
        self.slider_layout1 = pygame.Rect(5, 90, 200, 15)
        self.label_slider_value_layout1 = pygame.Rect(210, 75, 50, 50) 
        self.slider_value1 = 25

        #slider para la cantidad de vehículos que entran a la autopista
        self.label_slider_layout2 = pygame.Rect(265, 50, 400, 50) 
        self.slider_layout2 = pygame.Rect(280, 90, 200, 15)
        self.label_slider_value_layout2 = pygame.Rect(485, 75, 50, 50) 
        self.slider_value2 = 10

        # número de carriles
        self.lbl_carriles_layout =  pygame.Rect(680, 50, 200, 50)
        self.dpd_carriles_layout = pygame.Rect(700, 90, 50, 20)
        self.n_carriles = 4

        # velocidad de simulación
        self.lbl_velocidad_sim = pygame.Rect(880, 50, 200, 50)
        self.slider_layout_3 = pygame.Rect(880, 90, 200, 15)
        self.label_slider_value_layout_3 = pygame.Rect(1085, 75, 50, 50)



        panel3.set_image(pygame.image.load('./resources/images/pista_2_4.png'))


        self.label_silder1 = pygame_gui.elements.UILabel(relative_rect=self.label_slider_layout1, text = 'cantidad de vehículos autopista', manager= manager)
        self.slider1 = pygame_gui.elements.UIHorizontalSlider(relative_rect=self.slider_layout1, start_value = self.slider_value1, value_range=RANGE_SLIDER, manager = manager)
        self.label_silder_value1 = pygame_gui.elements.UILabel(relative_rect=self.label_slider_value_layout1, text = "%s"%self.slider_value1, manager= manager)


        self.label_slider2 = pygame_gui.elements.UILabel(relative_rect=self.label_slider_layout2, text = 'cantidad de vehículos que entran a la autopista', manager= manager)
        self.slider2 = pygame_gui.elements.UIHorizontalSlider(relative_rect=self.slider_layout2, start_value = self.slider_value2, value_range=RANGE_SLIDER, manager = manager)
        self.label_slider_value2 = pygame_gui.elements.UILabel(relative_rect=self.label_slider_value_layout2, text = "%s"%self.slider_value2, manager= manager)

        # carriles
        self.label_carriles = pygame_gui.elements.UILabel(relative_rect=self.lbl_carriles_layout, text = 'Cantidad de carriles', manager= manager)
        self.dpd_cantidad_carriles = pygame_gui.elements.UIDropDownMenu(options_list=["1","2","3", "4"], starting_option = "4", relative_rect=self.dpd_carriles_layout, manager=manager)

        # velocidad de simulación
        self.label_velocidad = pygame_gui.elements.UILabel(relative_rect=self.lbl_velocidad_sim, text = 'Velocidad de simulación', manager= manager)
        self.slider3 = pygame_gui.elements.UIHorizontalSlider(relative_rect=self.slider_layout_3, start_value = self.velocidad_simulacion, value_range=(0,100), manager = manager)
        self.label_slider_value3 = pygame_gui.elements.UILabel(relative_rect=self.label_slider_value_layout_3, text = "%s%s"%(self.velocidad_simulacion, '%'), manager= manager)

        


    
    def generarCarros(self, n, pygame, pygame_gui, window_surface, manager):
        objCar = draw_cars.Cars()
        for i in range(n):
            carril = math.ceil( random.random() * self.n_carriles )
            car_rect, image =  objCar.generarCarro(carril)
            car = pygame_gui.elements.UIImage(relative_rect=car_rect, image_surface = window_surface, manager = manager)
            car.set_image(image)
            self.cars.append(car)
            

    def actualizarPos(self):
        for carro in self.cars:
            posx = carro.get_relative_rect().left - self.velocidad_simulacion
            carro.set_position(position=(posx, carro.get_relative_rect().top))


    def actualizarCarriles(self, panel3):
        panel3.set_image(pygame.image.load('./resources/images/pista_2_%s.png'%self.n_carriles))

        



