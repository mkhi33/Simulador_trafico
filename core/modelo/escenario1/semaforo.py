import threading
import time
import pygame
import sys
class Semaforo:
    # Modelo para cambio de semaforo
    def __init__(self, tAmarillo = 3, tSemaforo=5):
        self.tAmarillo = tAmarillo
        self.tSemaforo = tSemaforo

        # Definir las propiedades de los semaforos para cada carril
        self.carril = {
            "carril1": {
                "color": "rojo",
                "cola": []
            },
            "carril2": {
                "color": "rojo",
                "cola": []
            },
            "carril3": {
                "color": "rojo",
                "cola": []
            },
            "carril4": {
                "color": "verde",
                "cola": []
            }
        }

        self.cambiando = threading.Event()
        self.cambiando.set()
        self.bandera = True

        self.semaforoPygame = []

        # Inicializar el semaforo para cada carril
        self.t = threading.Thread(target=self.run, args=(self.cambiando,))

        self.t.start()


    def cambiarSemaforo(self):
        for carril in self.carril:
            color = self.carril[carril]["color"]
            if carril == "carril4" and color == "amarillo":
                self.carril[carril]["color"] = "rojo"
                self.carril['carril1']['color'] = 'verde'
            if carril == "carril1" and color == "amarillo":
                self.carril[carril]["color"] = "rojo"
                self.carril['carril2']['color'] = 'verde'
            if carril == "carril2" and color == "amarillo":
                self.carril[carril]["color"] = "rojo"
                self.carril['carril3']['color'] = 'verde'





    def actualizarSemaforoPygame(self):
        if(self.semaforoPygame):
            imagen1, imagen2, imagen3, imagen4 = self.obtenerImagenes()
            self.semaforoPygame[0].set_image(pygame.image.load(imagen1))
            self.semaforoPygame[1].set_image(pygame.image.load(imagen2))
            self.semaforoPygame[2].set_image(pygame.image.load(imagen3))
            self.semaforoPygame[3].set_image(pygame.image.load(imagen4))
    

    def cambiarAmarillo(self):

        for carril in self.carril.keys():
            color = self.carril[carril]["color"]
            if color == "verde":
                self.carril[carril]["color"] = "amarillo"

    def obtenerImagenes(self):
        path = './resources/images/semaforo'

        semaforo1 = "%s/%s.png"%(path, self.carril["carril1"]["color"])
        semaforo2 = "%s/%s.png"%(path, self.carril["carril2"]["color"])
        semaforo3 = "%s/%s.png"%(path, self.carril["carril3"]["color"])
        semaforo4 = "%s/%s.png"%(path, self.carril["carril4"]["color"])
        return (semaforo1, semaforo2, semaforo3, semaforo4)

    def run(self, cambiando):
        cont = 1
        while cambiando.is_set():
            time.sleep(self.tSemaforo) # cambiar a amarillo cada 10 segundos
            self.cambiarAmarillo()
            self.actualizarSemaforoPygame()
            time.sleep(self.tAmarillo) # Actualizar semaforos cada 3 segundos
            if cont == 4:
                self.carril['carril4']['color'] = 'verde'
                self.carril['carril3']['color'] = 'rojo'
                self.carril['carril2']['color'] = 'rojo'
                self.carril['carril1']['color'] = 'rojo'
                cont = 1
                
            else:
                self.cambiarSemaforo()
                cont+=1
            self.actualizarSemaforoPygame()
            



            if(not self.bandera):
                self.cambiando.clear()
                break
            
            # finalizar el bucle con sys
                





