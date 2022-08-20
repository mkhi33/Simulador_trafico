import pygame
from ui import draw_cars
import random
import math

import time

class Escenario2:
    def __init__(self):
        self.car = None
        self.cars = [
            {"carril1": []},
            {"carril2": []},
            {"carril3": []},
            {"carril4": []},
            {"entrada": []}
        ]
        self.velocidad_simulacion = 5
        self.cola = [(560, 300)]
        


    def run(self, panel3, pygame_gui, manager, window_surface):

        RANGE_SLIDER = (0, 500)
        RANGE_SLIDER2 = (0, 50)

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
        self.slider2 = pygame_gui.elements.UIHorizontalSlider(relative_rect=self.slider_layout2, start_value = self.slider_value2, value_range=RANGE_SLIDER2, manager = manager)
        self.label_slider_value2 = pygame_gui.elements.UILabel(relative_rect=self.label_slider_value_layout2, text = "%s"%self.slider_value2, manager= manager)

        # carriles
        self.label_carriles = pygame_gui.elements.UILabel(relative_rect=self.lbl_carriles_layout, text = 'Cantidad de carriles', manager= manager)
        self.dpd_cantidad_carriles = pygame_gui.elements.UIDropDownMenu(options_list=["1","2","3", "4"], starting_option = "4", relative_rect=self.dpd_carriles_layout, manager=manager)

        # velocidad de simulación
        self.label_velocidad = pygame_gui.elements.UILabel(relative_rect=self.lbl_velocidad_sim, text = 'Velocidad de simulación', manager= manager)
        self.slider3 = pygame_gui.elements.UIHorizontalSlider(relative_rect=self.slider_layout_3, start_value = self.velocidad_simulacion, value_range=(0,100), manager = manager)
        self.label_slider_value3 = pygame_gui.elements.UILabel(relative_rect=self.label_slider_value_layout_3, text = "%s%s"%(self.velocidad_simulacion, '%'), manager= manager)

        
        self.cortesia = False


    def getCantidadCarros(self):
        return len(self.cars[0]["carril1"]) + len(self.cars[1]["carril2"]) + len(self.cars[2]["carril3"]) + len(self.cars[3]["carril4"])
    
    def generarCarros(self, n, pygame, pygame_gui, window_surface, manager):


        self.generarCarrosEntrada(n, pygame, pygame_gui, window_surface, manager)
        objCar = draw_cars.Cars()
        if( self.getCantidadCarros() > self.slider_value1 or self.slider_value1 == 0):
            return

        for i in range(n):
            carril = math.ceil( random.random() * self.n_carriles )
            car_rect, image =  objCar.generarCarro(carril)
            car = pygame_gui.elements.UIImage(relative_rect=car_rect, image_surface = window_surface, manager = manager)
            car.set_image(image)

            data = {
                "index": i,
                "car": car,
                "carril":carril,
                "dimension":car_rect.size,
                "cortesia": math.ceil( random.random() * 100 )
            }

            self.cars[carril - 1]["carril%s"%carril].append(data)

            
    def generarCarrosEntrada(self, n, pygame, pygame_gui, window_surface, manager):

        objCar = draw_cars.Cars()

        if(len(self.cars[4]['entrada']) > self.slider_value2 or self.slider_value2 == 0):
            return

        if(len(self.cola) > 3):
            return

        for i in range(n):
            car_rect, image = objCar.generarCarroEntrada()
            car = pygame_gui.elements.UIImage(relative_rect=car_rect, image_surface = window_surface, manager = manager)
            car.set_image(image)
            
            data = {
                "index": i,
                "car": car,
                "carril":5,
                "dimension":car_rect.size,
                "cortesia": 0,
                "image": image
            }

            self.cars[4]["entrada"].append(data)

    def carrilLibre(self):
        carril = self.cars[0]["carril1"]
        for data in carril:
            carro = data["car"]
            posx = carro.relative_rect.x

            if(posx >= 400 and posx <= 800):
                return False

        return True


    def actualizarPos(self):

        self.actualizarCarril(1)
        self.actualizarCarril(2)
        self.actualizarCarril(3)
        self.actualizarCarril(4)
        self.actualizarCarril(5)

    def actualizarCarril(self, n):
        if(n == 5):
            carril = self.cars[n-1]["entrada"]
        else:
            carril = self.cars[n-1]["carril%s"%n]
        index = 0
        for data in carril:
            if(n == 5):
                posy = data['car'].get_relative_rect().top 
                posx = data['car'].get_relative_rect().left 
                w, h = data['dimension']
                if( posy <= 300 and not self.cortesia  ):
                    self.actualizarCola(data)
                else:
                    data['car'].set_position(position=(posx - self.velocidad_simulacion, posy + self.velocidad_simulacion))
                    self.cola = [(560, 300)]
                    self.cortesia = False
                    if(posy >= 350):
                        objCar = draw_cars.Cars()
                        image = objCar.girarImagen(data['image'], 1, True)
                        data['car'].set_image(image)
                        self.cars[0]["carril1"].append(data)
                        self.cars[4]["entrada"].remove(data)
                        self.actualizarCarril(1)
            else:


                posx = data['car'].get_relative_rect().left -self.velocidad_simulacion
                data['car'].set_position(position=(posx, data['car'].get_relative_rect().top))

    def actualizarCola(self, data, separacion = 95):
        nombreCarril = data['carril']
        carro = data['car']

        posy = data['car'].get_relative_rect().top
        posx = data['car'].get_relative_rect().left

        w, h = data['dimension'] # Dimensiones del último carro en la cola

        if self.carrilLibre():
            data['car'].set_position(position=(posx - self.velocidad_simulacion, posy + self.velocidad_simulacion))
            return data
        if( posy   >= self.cola[-1][1]):
            if not (posx, posy - separacion) in self.cola:
                self.cola.append((posx, posy-separacion))
        else:
            data['car'].set_position(position=(posx - self.velocidad_simulacion, posy + self.velocidad_simulacion))
        return data


    def actualizarCarriles(self, panel3):
        panel3.set_image(pygame.image.load('./resources/images/pista_2_%s.png'%self.n_carriles))

        



