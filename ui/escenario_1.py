import pygame
from ui import draw_cars
import random
import math

from pygame_gui.core import ObjectID
from pygame_gui.elements import UIButton

from core.modelo.escenario1.semaforo import Semaforo
from core.modelo.escenario1.rutas import Rutas

class Escenario1:
    def __init__(self):
        self.car = None
        self.cars = [
            {"carril1": []},
            {"carril2": []},
            {"carril3": []},
            {"carril4": []},
            {"carril5": []},
            {"carril6": []},
        ]
        self.velocidad_simulacion = 5
        self.mostrar_semaforos = True
        self.n_carriles = 6


        # instancias del modelo
        self.semaforo = Semaforo()
        self.semaforo.carril['carril2']['cola'] = [(570, 489)]
        self.semaforo.carril['carril3']['cola'] = [(573, 400)]
        self.semaforo.carril['carril4']['cola'] = [(573, 496)]

    def run(self, panel3, pygame_gui, manager, window_surface):
        RANGE_SLIDER = (0, 500)

        self.label_slider_layout1 = pygame.Rect(5, 50, 250, 50) 
        self.slider_layout1 = pygame.Rect(5, 90, 200, 15) 
        self.label_slider_value_layout1 = pygame.Rect(210, 75, 50, 50) 
        self.slider_value1 = 25


        # Semaforos
        self.semaforo_1_layout = pygame.Rect(546, 370, 52, 52)
        self.semaforo_2_layout = pygame.Rect(680, 370, 52, 52)
        self.semaforo_3_layout = pygame.Rect(610, 489, 52, 52)
        self.semaforo_4_layout = pygame.Rect(610, 300, 52, 52)

        self.semaforo_1 = pygame_gui.elements.UIImage(relative_rect=self.semaforo_1_layout, image_surface = window_surface, manager = manager)
        self.semaforo_2 = pygame_gui.elements.UIImage(relative_rect=self.semaforo_2_layout, image_surface = window_surface, manager = manager)
        self.semaforo_3 = pygame_gui.elements.UIImage(relative_rect=self.semaforo_3_layout, image_surface = window_surface, manager = manager)
        self.semaforo_4 = pygame_gui.elements.UIImage(relative_rect=self.semaforo_4_layout, image_surface = window_surface, manager = manager)


        # cargar imagenes de los semaforos
        imagen1, imagen2, imagen3, imagen4 = self.semaforo.obtenerImagenes()

        self.semaforo_1.set_image(pygame.image.load(imagen1))
        self.semaforo_2.set_image(pygame.image.load(imagen2))
        self.semaforo_3.set_image(pygame.image.load(imagen3))
        self.semaforo_4.set_image(pygame.image.load(imagen4))

        # agregar las referencias al modelo
        self.semaforo.semaforoPygame.append(self.semaforo_1)
        self.semaforo.semaforoPygame.append(self.semaforo_2)
        self.semaforo.semaforoPygame.append(self.semaforo_3)
        self.semaforo.semaforoPygame.append(self.semaforo_4)




        # Cambiar por switch para activar o desactivar semaforos
        self.btn_layout_semaforo = pygame.Rect(280, 80, 180, 40)

        self.btn_semaforo = UIButton(relative_rect=self.btn_layout_semaforo,
                                text='Desactivar semaforos',
                                manager=manager,
                                object_id=ObjectID(class_id='@btn_semaforo', object_id='#btn_semaforo'),

                            )

        # velocidad de simulación
        self.lbl_velocidad_sim = pygame.Rect(480, 50, 200, 50)
        self.slider_layout_3 = pygame.Rect(480, 90, 200, 20)
        self.label_slider_value_layout_3 = pygame.Rect(680, 75, 50, 50)
        self.slider_value3 = 5

        panel3.set_image(pygame.image.load('./resources/images/pista_1.1.png'))

        self.label_silder1 = pygame_gui.elements.UILabel(relative_rect=self.label_slider_layout1, text = 'cantidad de vehículos autopista', manager= manager)
        self.slider1 = pygame_gui.elements.UIHorizontalSlider(relative_rect=self.slider_layout1, start_value = self.slider_value1, value_range=RANGE_SLIDER, manager = manager)
        self.label_silder_value1 = pygame_gui.elements.UILabel(relative_rect=self.label_slider_value_layout1, text = "%s"%self.slider_value1, manager= manager)


        # velocidad de simulación
        self.label_velocidad = pygame_gui.elements.UILabel(relative_rect=self.lbl_velocidad_sim, text = 'Velocidad de simulación', manager= manager)
        self.slider_velocidad = pygame_gui.elements.UIHorizontalSlider(relative_rect=self.slider_layout_3, start_value = self.slider_value3, value_range=(0,100), manager = manager)
        self.label_slider_value3 = pygame_gui.elements.UILabel(relative_rect=self.label_slider_value_layout_3, text = "%s%s"%(self.slider_value3, '%'), manager= manager)
    
        self.cola = []
    def setSemaforo(self):
        self.mostrar_semaforos = not self.mostrar_semaforos

        self.semaforo_1.visible = self.mostrar_semaforos
        self.semaforo_2.visible = self.mostrar_semaforos
        self.semaforo_3.visible = self.mostrar_semaforos
        self.semaforo_4.visible = self.mostrar_semaforos
        if not self.mostrar_semaforos:
            self.btn_semaforo.set_text('Activar semaforos')

        else:
            self.btn_semaforo.set_text('Desactivar semaforos')

    def generarCarros(self, n, pygame, pygame_gui, window_surface, manager):
        objCar = draw_cars.Cars()
        for i in range(n):

            carril = math.ceil( random.random() * self.n_carriles )

            if carril == 4 and len(self.semaforo.carril['carril4']['cola']) >2:
                return
            if carril == 3 and len(self.semaforo.carril['carril3']['cola']) >2:
                return
            if carril == 2 and len(self.semaforo.carril['carril2']['cola']) >4:
                return
            if carril == 1 and len(self.semaforo.carril['carril1']['cola']) >4:
                return
                
            car_rect, image =  objCar.generarCarro1(carril)
            car = pygame_gui.elements.UIImage(relative_rect=car_rect, image_surface = window_surface, manager = manager)
            car.set_image(image)

            data = {
                "index": i,
                "car": car,
                "carril":carril,
                "dimension":car_rect.size,

            }

            self.cars[carril - 1]["carril%s"%carril].append(data)
    


    def obtenerUltimoCarroCarril(self, carril):
        return carril[-1]

    

    def actualizarCarril(self, n):


        carril = self.cars[n-1]["carril%s"%n]

        index = 0

        for data in carril:
            

            if(n == 1): # Para el carril 1
                posx = data['car'].get_relative_rect().left
                if(self.semaforo.carril['carril1']['color'] == 'rojo' and not (posx > 600) ):
                    self.cars[n - 1]["carril1"][index] = self.actualizarColaSemaforoCarril1(data)
                else:
                    self.semaforo.carril['carril1']['cola'] = [(600, 370)]
                    data['car'].set_position(position=(posx + self.velocidad_simulacion, data['car'].get_relative_rect().top))
                    self.cars[n - 1]["carril1"][index] = data
            elif(n == 2): # Para el carril 2
                posx = data['car'].get_relative_rect().left

                if ( self.semaforo.carril['carril2']['color'] == 'rojo' and not (posx <= 550)):
                    self.cars[n - 1]["carril2"][index] = self.actualizarColaSemaforoCarril2(data)
                else:
                    self.semaforo.carril['carril2']['cola'] = [(550, 489)]
                    data['car'].set_position(position=(posx - self.velocidad_simulacion, data['car'].get_relative_rect().top))
            elif(n == 3): # Para el carril 3
                posy = data['car'].get_relative_rect().top

                if(self.semaforo.carril['carril4']['color'] == 'rojo') and (posy <= 300): # Error en el nombre de variables del semaforo (carril3  )
                    self.cars[n - 1]["carril3"][index] = self.actualizarColaSemaforoCarril3(data)
                else:

                    self.semaforo.carril['carril3']['cola'] = [(573, 400)] # Reiniciar la cola
                    data['car'].set_position(position=(data['car'].get_relative_rect().left, posy + self.velocidad_simulacion))
            
            elif(n == 4):

                posy = data['car'].get_relative_rect().top
                if(self.semaforo.carril['carril3']['color'] == 'rojo') and (posy >=  496):
                    self.cars[n - 1]["carril4"][index] = self.actualizarColaSemaforoCarril4(data)
                else:
                    self.semaforo.carril['carril4']['cola'] = [(573, 496)]
                    data['car'].set_position(position=(data['car'].get_relative_rect().left, posy - self.velocidad_simulacion))
                      
            index += 1

    def actualizarColaSemaforoCarril4(self, data, separacion = 50):

        nombreCarril = data['carril']
        carro = data['car']

        posy = data['car'].get_relative_rect().top


        w, h = data['dimension'] # Dimensiones del último carro en la cola
        separacion = w + separacion

        if(self.semaforo.carril['carril4']["cola"] and posy   <= self.semaforo.carril['carril4']["cola"][-1][1]):
            if(not (573, posy+separacion) in self.semaforo.carril['carril4']["cola"]):
                self.semaforo.carril['carril4']['cola'].append((573, posy+ separacion))
        else:
            data['car'].set_position(position=(data['car'].get_relative_rect().left, posy - self.velocidad_simulacion))
        return data




    def actualizarPos(self):

        self.actualizarCarril(1)
        self.actualizarCarril(2)
        self.actualizarCarril(3)
        self.actualizarCarril(4)



    def actualizarSemaforo(self):
        self.semaforo.cambiarAmarillo()

    def actualizarColaSemaforoCarril1(self, data, separacion = 50):
        
        
        nombreCarril = data['carril']
        carro = data['car']

        posx = data['car'].get_relative_rect().left

        w, h = data['dimension'] # Dimensiones del último carro en la cola
        separacion = w + separacion
        if( self.semaforo.carril['carril1']["cola"] and (posx  + separacion >= self.semaforo.carril['carril1']["cola"][-1][0])):
            if not (posx, 370) in self.semaforo.carril['carril1']['cola']:
                self.semaforo.carril['carril1']['cola'].append((posx, 370))

        else:
            data['car'].set_position(position=(posx + self.velocidad_simulacion, data['car'].get_relative_rect().top))

        return data



    def actualizarColaSemaforoCarril2(self, data, separacion = 50):

        nombreCarril = data['carril']
        carro = data['car']

        posx = data['car'].get_relative_rect().left

        w, h = data['dimension'] # Dimensiones del último carro en la cola
        separacion = w + separacion

        if( self.semaforo.carril['carril2']["cola"] and (posx - separacion <= self.semaforo.carril['carril2']["cola"][-1][0])):
            if not (posx, 489) in self.semaforo.carril['carril2']['cola']:
                self.semaforo.carril['carril2']['cola'].append((posx, 489))

        else:
            data['car'].set_position(position=(posx - self.velocidad_simulacion, data['car'].get_relative_rect().top))

        return data
    def actualizarColaSemaforoCarril3(self, data, separacion = 50):

        nombreCarril = data['carril']
        carro = data['car']


        posy = data['car'].get_relative_rect().top

        w, h = data['dimension'] # Dimensiones del último carro en la cola
        separacion = w + separacion

        
        if(self.semaforo.carril['carril3']["cola"] and posy + separacion >= self.semaforo.carril['carril3']["cola"][-1][1]):
            self.semaforo.carril['carril3']['cola'].append((573, posy))
        else:
            data['car'].set_position(position=(data['car'].get_relative_rect().left, posy + self.velocidad_simulacion))
        return data



                
            
