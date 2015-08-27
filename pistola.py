import pilas
from pilas.actores import Actor

class Arma(Actor):
    def __init__(self,x,y,imagen,velocidad):
        Actor.__init__(self,x=x,y=y)
        self.imagen=pilas.imagenes.cargar_imagen(imagen)
        self.eliminar_habilidad(pilas.habilidades.MoverseConElTeclado)
