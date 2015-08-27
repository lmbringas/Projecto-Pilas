import pilas
import random
import math

class Habilidad(object):
    """Representa una habilidad que un actor puede aprender."""

    def __init__(self, receptor):
        self.receptor = receptor

    def actualizar(self):
        pass

    def eliminar(self):
        pass


class MoverseConElTeclado(Habilidad):

    CUATRO_DIRECCIONES = 4
    OCHO_DIRECCIONES = 8


    def __init__(self, receptor, control=None, direcciones=OCHO_DIRECCIONES, velocidad_maxima=4,
                 aceleracion=1, deceleracion=0.1, con_rotacion=False, velocidad_rotacion=1, marcha_atras=True):


        Habilidad.__init__(self, receptor)
        pilas.escena_actual().actualizar.conectar(self.on_key_press)

        if control == None:
            self.control = self.receptor.escena.control
        else:
            self.control = control

        self.direcciones = direcciones

        self.velocidad = 0
        self.deceleracion = deceleracion
        self._velocidad_maxima = velocidad_maxima
        self._aceleracion = aceleracion
        self.con_rotacion = con_rotacion
        self.velocidad_rotacion = velocidad_rotacion
        self.marcha_atras = marcha_atras

    def set_velocidad_maxima(self, velocidad):
        self._velocidad_maxima = velocidad

    def get_velocidad_maxima(self):
        return self._velocidad_maxima

    def get_aceleracion(self):
        return self._aceleracion

    def set_aceleracion(self, aceleracion):
        self._aceleracion = aceleracion

    velocidad_maxima = property(get_velocidad_maxima, set_velocidad_maxima, doc="Define la velocidad maxima.")
    aceleracion = property(get_aceleracion, set_aceleracion, doc="Define la acelaracion.")

    def on_key_press(self, evento):

        c = self.control

        if self.con_rotacion:

            if c.izquierda:
                self.receptor.rotacion -= self.velocidad_rotacion * self.velocidad_maxima
            elif c.derecha:
                self.receptor.rotacion += self.velocidad_rotacion * self.velocidad_maxima

            if c.arriba:
                self.avanzar(+1)
            elif c.abajo:
                if self.marcha_atras:
                    self.avanzar(-1)
                else:
                    self.decelerar()
            else:
                self.decelerar()

            rotacion_en_radianes = math.radians(-self.receptor.rotacion + 90)
            dx = math.cos(rotacion_en_radianes) * self.velocidad
            dy = math.sin(rotacion_en_radianes) * self.velocidad
            if not(self.receptor.mapa.es_punto_solido(self.receptor.x + dx, self.receptor.y + dy)):
                self.receptor.x += dx
                self.receptor.y += dy

        else:
            pass

    def decelerar(self):
        if self.velocidad > self.deceleracion:
            self.velocidad -= self.deceleracion
        elif self.velocidad < -self.deceleracion:
            self.velocidad += self.deceleracion
        else:
            self.velocidad = 0

    def avanzar(self, delta):
        self.velocidad += self.aceleracion * delta

        if self.velocidad > self.velocidad_maxima:
            self.velocidad = self.velocidad_maxima
        elif self.velocidad < - self.velocidad_maxima / 2:
            self.velocidad = - self.velocidad_maxima / 2
