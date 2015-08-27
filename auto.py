import pilas
from pilas.actores import Actor
from pilas.comportamientos import Comportamiento

class Autito(Actor):
    def __init__(self, mapa, x=50, y=-50, imagen=None, velocidad=4,enemigos=[4,8,8,8,8,8,8,8,8,8,8,8,8,8,8,4]):
        Actor.__init__(self, x=x, y=y)
        self.imagen = pilas.imagenes.cargar_grilla(imagen,1,1)
        self.x=x
        self.y=y
        self.eliminar_habilidad(pilas.habilidades.MoverseConElTeclado)
        self.mapa=mapa
        self.radio_de_colision=24
        self.enemigos=enemigos
        self.creado=False
        #self.figura_de_colision=pilas.fisica.Rectangulo(50, 90,40, True)
        #self.imitar(a)
