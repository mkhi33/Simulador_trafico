# tamaño de la imagen (ancho, alto)
import pygame
import random
import math
class Cars:
    def __init__(self):

        self.cars = {
            "car_1": {
                'dim': (138,63),
                'image': pygame.image.load('./resources/images/cars/car-1.png'),
            },
            "car_2": {
                'dim': (138,75),
                'image': pygame.image.load('./resources/images/cars/car-2.png'),
            },
            "car_3":
                {
                    'dim': (138,52), 
                    'image': pygame.image.load('./resources/images/cars/car-3.png')
                },
            "car_4":
                {
                    'dim': (138,63), 
                    'image': pygame.image.load('./resources/images/cars/car-4.png')
                },
            "car_5":
                {
                    'dim': (138,58), 
                    'image': pygame.image.load('./resources/images/cars/car-5.png')
                },
            "car_6":
                {
                    'dim': (138,46), 
                    'image': pygame.image.load('./resources/images/cars/car-6.png')
                },
            "car_7":
                {
                    'dim': (138,48), 
                    'image': pygame.image.load('./resources/images/cars/car-7.png')
                },
            "car_8":
                {
                    'dim': (138,51), 
                    'image': pygame.image.load('./resources/images/cars/car-8.png')
                },
            "car_9":
                {
                    'dim': (138,54), 
                    'image': pygame.image.load('./resources/images/cars/car-9.png')
                },
            "car_10":
                {
                    'dim': (138,57), 
                    'image': pygame.image.load('./resources/images/cars/car-10.png')
                },
            "car_11":
                {
                    'dim': (138,61), 
                    'image': pygame.image.load('./resources/images/cars/car-11.png')
                },
            "car_12":
                {
                    'dim': (138,60), 
                    'image': pygame.image.load('./resources/images/cars/car-12.png')
                }
        }

        self.pos_start = {
            "carril_1": (1199, 400),
            "carril_2": (1199, 467),
            "carril_3": (1199, 534),
            "carril_4": (1199, 601),
        }

        self.pos_start_1 = {
            "carril_1": (0, 420), # carril derecho a las 9
            "carril_2": (1199, 340), # carril izquierdo a las 9
            "carril_3": (573, 145), # carril derecho en las 12
            "carril_4": (670, 145), # carril izquierdo a las 12
            "carril_4": (670, 700), # carril derecho a las 6
            "carril_4": (605, 700), # carril izquierdo a las 6
        }


    # Carros en el carril 4:
    def draw_cars_4(self, screen, pygame):
        colors = {
            "red": (255, 0, 0),
            "green": (0, 255, 0),
        }
        x, y = ( 1192, 166 )
        pygame.draw.rect(screen, colors['red'], (1024/2, 500, 138,63) )

    def generarCarro(self, carril = 1):

        # seleccionar un carro aleatoriamente
        r = math.ceil(random.random() * 12)

        car = self.cars["car_" + str(r)]
        w, h = car["dim"]
        x, y = self.pos_start["carril_" + str(carril)]
    
        
        car_rect = pygame.Rect(x, y, w, h)
        return car_rect, car["image"]

    # Para el escenario 2 ya que es una carretera doble via con intersecciones se debe de generar de otra forma

    def generarCarro1(self, carril = 1):

        r = math.ceil(random.random() * 12)
        car = self.cars["car_" + str(r)]
        w, h = car["dim"]
        x, y = self.pos_start_1["carril_" + str(carril)]

        image = car["image"]
        if carril == 1:
            image = pygame.transform.rotate(image, angle=180)

        car_rect = pygame.Rect(x, y, w, h)
        return car_rect, image


