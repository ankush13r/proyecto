#!/usr/bin/env python

class Robot:
    
    def __init__(self, nombre,color,energia,inteligenicia, encendido):
        self.__nombre = nombre
        self.__color = color
        self.__energia = energia
        self.__inteligencia= inteligenicia
        self.__encendido = encendido

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self,nombre):
        self.__nombre = nombre

    def get_color(self):
        return self.color

    def set_color(self,color):
        self.color = color

    def get_energia(self):
        return self.__energia

    def set_energia(self,__energia):
        self.__energia = __energia

    def get_inteligencia(self):
        return self.__inteligencia
    
    def setinteligenica(self, inteligenica):
        self.__inteligencia = inteligenica
    
    def __str__(self):
        return "\tRobot\n----------------------\nNombre: "+ self.__nombre + ",\tColor: "+ self.__color +",\tEnergia: "+ str(self.__energia) + ",\tInteligencia : "+str(self.__inteligencia)

    def se_pinta(self,color):
        self.color = color

    def habla(self):
        self.__energia = self.__energia - 10

    def mueve(self):
        self.__energia = self.__energia - 20
        
    def reposta_energía(self):
        self.__energia = 100

    def lee(self):
        self.__inteligencia = self.__inteligencia + 50

    def apaga(self):
        self.__energia = 100
        self.__inteligencia = 100
        
        self.__encendido = False
        return "Se ha apagado el robot"
    def enciende(self):
        self.__encendido = True
        return "Se ha encendido el robot"


robot = Robot("Ankush", "brown", 100,100, False)

print(robot)


