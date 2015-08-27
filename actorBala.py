import pilas
from pilas.actores import Actor

class Bala(Actor):
    def __init__(self, mapa, x=50, y=-50, imagen=None, velocidad=4):
        Actor.__init__(self, x=x, y=y)
        self.imagen = pilas.imagenes.cargar_grilla(imagen,1,1)
        self.x=x
        self.y=y
        self.eliminar_habilidad(pilas.habilidades.MoverseConElTeclado)
        self.mapa=mapa
        self.radio_colision=30
        self.escala=0.5
