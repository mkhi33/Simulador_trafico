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
                },
            "car_13":                 {
                    'dim': (138,71), 
                    'image': pygame.image.load('./resources/images/cars/car-13.png')
            },
            "car_14":                 {
                    'dim': (138,54), 
                    'image': pygame.image.load('./resources/images/cars/car-14.png')
            },
            "car_15":                 {
                    'dim': (138,58), 
                    'image': pygame.image.load('./resources/images/cars/car-15.png')
            },
            "car_16":                 {
                    'dim': (138,47), 
                    'image': pygame.image.load('./resources/images/cars/car-16.png')
            },
            "car_17":                 {
                    'dim': (138,56), 
                    'image': pygame.image.load('./resources/images/cars/car-17.png')
            },
            "car_18":                 {
                    'dim': (138,60), 
                    'image': pygame.image.load('./resources/images/cars/car-18.png')
            },
            "car_19":                 {
                    'dim': (138,47), 
                    'image': pygame.image.load('./resources/images/cars/car-19.png')
            },
            "car_20":                 {
                    'dim': (138,55), 
                    'image': pygame.image.load('./resources/images/cars/car-20.png')
            },
            "car_21":                 {
                    'dim': (138,59), 
                    'image': pygame.image.load('./resources/images/cars/car-21.png')
            },
            "car_22":                 {
                    'dim': (138,53), 
                    'image': pygame.image.load('./resources/images/cars/car-22.png')
            },
            "car_23":                 {
                    'dim': (138,63), 
                    'image': pygame.image.load('./resources/images/cars/car-23.png')
            },
            "car_24":                 {
                    'dim': (138,47), 
                    'image': pygame.image.load('./resources/images/cars/car-24.png')
            },
        }

        self.pos_start = {
            "carril_1": (1199, 400),
            "carril_2": (1199, 467),
            "carril_3": (1199, 534),
            "carril_4": (1199, 601),
        }

        self.pos_start_1 = {
            "carril_1": (-150, 420), # carril derecho a las 9
            "carril_2": (1199, 340), # carril izquierdo a las 9 1199
            "carril_3": (573, -145), # carril derecho en las 12
            "carril_4": (640, 686), # carril izquierdo a las 12
            "carril_5": (670, 700), # carril derecho a las 6
            "carril_6": (605, 700), # carril izquierdo a las 6
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

        # Seleccionar un carril aleatoriamente


        # seleccionar un carro aleatoriamente
        r = 1

        if(carril == 1):
            r = self.getRandom(24, 12)
        elif carril == 2:
            r = self.getRandom(12, 0)
        elif carril == 3:
            r = self.getRandom(12, 0)
        elif carril == 4:
            r = self.getRandom(12, 0)
        elif carril == 5:
            r = self.getRandom(12, 0)
        elif carril == 6:
            r = self.getRandom(12, 0)




        car = self.cars["car_" + str(r)]
        w, h = car["dim"]
        x, y = self.pos_start_1["carril_" + str(carril)]
        
        if carril == 4:
            #print((x,y,w,h))
            pass
        image = self.girarImagen(car["image"], carril)
        car_rect = pygame.Rect(x, y, w, h)
        return car_rect, image

    def girarImagen(self, image, carril):
        if carril == 3:
            return pygame.transform.rotate(image, angle=90)
        if carril == 4:
            return pygame.transform.rotate(image, angle=-90)
        return image

    def getRandom(self, max, min):
        return math.ceil(random.random() * (max - min) + min)



