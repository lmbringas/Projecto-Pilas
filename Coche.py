import pilas
from pilas.actores import Actor
from pilas.comportamientos import Comportamiento

class CocheMoviendo(Actor):

    def __init__(self,x,y,imagen=None,velocidad=None):
        Actor.__init__(self,x=x,y=y,)
        self.estado=1
        self.imagen=pilas.imagenes.cargar_imagen(imagen)
        self.x=x
        self.y=y
        self.velocidad=velocidad
        self.eliminar_habilidad(pilas.habilidades.MoverseConElTeclado)
        self.rotacion = pilas.interpolar(180,duracion=0.1)
        pilas.mundo.agregar_tarea_siempre(27,self.siempre)

    def siempre(self):

        if self.estado==1:
            self.y = pilas.interpolar(-3196, duracion=25)
            self.estado=2

        elif self.estado==2:
            self.rotacion=pilas.interpolar(90,duracion=1.5)
            self.x=pilas.interpolar(3106,duracion=25)
            self.estado=3

        elif self.estado==3:
            self.rotacion=pilas.interpolar(0,duracion=2)
            self.y=pilas.interpolar(-144,duracion=25)
            self.estado=4

        elif self.estado==4:
            self.rotacion=pilas.interpolar(270,duracion=0.8)
            self.x=pilas.interpolar(85,duracion=25)
            self.estado=5

        elif self.estado==5:
            self.rotacion=pilas.interpolar(180,duracion=2)
            self.y = pilas.interpolar(-3209, duracion=25)
            self.estado=2
