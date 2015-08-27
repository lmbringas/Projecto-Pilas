import pilas
from pilas.actores import Actor
from pilas.comportamientos import Comportamiento

VELOCIDAD = 100

NORTE = 0
SUR = 2
ESTE = 1
OESTE = 3


class MiActor(Actor):

    def __init__(self, mapa, x=50, y=-50, imagen="Maton.png", velocidad=None,enemigos=[4,8,8,8,8,8,8,8,8,8,8,8,8,8,8,4]):
        Actor.__init__(self, x=x, y=y)
        self.imagen = pilas.imagenes.cargar_grilla(imagen, 3, 4)
        self.x=x
        self.y=y
        self.mapa = mapa
        self.enemigos=enemigos
        self.direccion = pilas.actores.personajes_rpg.SUR
        self.hacer(Esperando())
        self.velocidad = velocidad
        self.creado=False


    def definir_cuadro(self, indice):
        self.imagen.definir_cuadro(indice)
        self.definir_centro((17, 29))

    def actualizar(self):
        pilas.escena_actual().camara._set_x(self.x)
        pilas.escena_actual().camara._set_y(self.y)

class Esperando(Comportamiento):

    def iniciar(self, receptor):
        self.receptor = receptor
        if (self.receptor.direccion == pilas.actores.personajes_rpg.NORTE):
            self.receptor.definir_cuadro(1)
        elif (self.receptor.direccion == pilas.actores.personajes_rpg.ESTE):
            self.receptor.definir_cuadro(4)
        elif (self.receptor.direccion == pilas.actores.personajes_rpg.SUR):
            self.receptor.definir_cuadro(7)
        elif (self.receptor.direccion == pilas.actores.personajes_rpg.OESTE):
            self.receptor.definir_cuadro(10)

    def actualizar(self):
        if pilas.escena_actual().control.izquierda:
            self.receptor.hacer(Caminando())
        elif pilas.escena_actual().control.derecha:
            self.receptor.hacer(Caminando())
        elif pilas.escena_actual().control.arriba:
            self.receptor.hacer(Caminando())
        elif pilas.escena_actual().control.abajo:
            self.receptor.hacer(Caminando())

class Caminando(Esperando):
    """Representa al personaje caminando por el escenario."""

    def __init__(self):
        self._repeticion_cuadro = 3

        self.cuadros = [[1,1,1,1,0,0,0,0,1,1,1,1,2,2,2,2],
                        [4,4,4,4,3,3,3,3,4,4,4,4,5,5,5,5],
                        [7,7,7,7,6,6,6,6,7,7,7,7,8,8,8,8],
                        [10,10,10,10,9,9,9,9,10,10,10,10,11,11,11,11]]

        self.paso = 0

    def iniciar(self, receptor):
        self.receptor = receptor

    def actualizar(self):
        self.avanzar_animacion()

        dx = 0
        dy = 0

        if pilas.escena_actual().control.izquierda:
            dx = self.receptor.velocidad * -1
            self.receptor.direccion = pilas.actores.personajes_rpg.OESTE
        elif pilas.escena_actual().control.derecha:
            dx = self.receptor.velocidad
            self.receptor.direccion = pilas.actores.personajes_rpg.ESTE
        elif pilas.escena_actual().control.arriba:
            dy = self.receptor.velocidad
            self.receptor.direccion = pilas.actores.personajes_rpg.NORTE
        elif pilas.escena_actual().control.abajo:
            dy = self.receptor.velocidad * -1
            self.receptor.direccion = pilas.actores.personajes_rpg.SUR
        else:
            self.receptor.hacer(Esperando())

        if not(self.receptor.mapa.es_punto_solido(self.receptor.x + dx, self.receptor.y + dy)):
            self.receptor.x += dx
            self.receptor.y += dy

    def avanzar_animacion(self):
        """Cambia el cuadro de animacin."""
        self.paso += 1

        if self.paso >= len(self.cuadros[self.receptor.direccion]):
            self.paso = 0

        self.receptor.definir_cuadro(self.cuadros[self.receptor.direccion][self.paso])

