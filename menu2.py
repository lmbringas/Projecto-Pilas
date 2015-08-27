import pilas


#-------------------Menu del juego---------------------------------------------------
class JuegoCompleto(pilas.escena.Base):
    def iniciar(self):
        pilas.fondos.Fondo('Fondos/choro.jpg')
        self.opcioness()
        self.titulo()

    def opcioness(self):
        opciones = [
		    ('Iniciar Juego', self.comenzar),
		    ('Instruciones',self.instruciones),
            ('Salir', self.salir)]
        self.menu = pilas.actores.Menu(opciones)

    def titulo(self):
        tit=pilas.actores.Actor('Fondos/titulo2.png')
        tit.escala=5
        tit.escala=[1]
        tit.rotacion=[360]
        tit.y=100
        tit.x=10

    def instruciones(self):
        pilas.cambiar_escena(Instruciones())

    def comenzar(self):
    	import test
        pilas.cambiar_escena(test.MiJuego())

    def salir(self):
        pilas.terminar()

#-------------------Instruciones---------------------------------------------------
class Instruciones(pilas.escena.Base):

    def iniciar(self):
        pilas.fondos.Fondo('Fondos/choro.jpg')
        tex=pilas.actores.Texto('Este un juego es en base a lo que paso 4 dic 2013 en Cordoba.\n\n El cual se trata de atrapar a una cierta cantidad de ladrones.\n\n Se utiliza la letra E para poder entrar al coche,\n\n la letra W para salir , con las flechas te moves , barra espaciadora disparar,\n\n con P pones pausa y despausar con Esc y con Esc sin estar en pausa volves al menu \n\n Muchas Gracias por jugarlo\n\n\n Para volver pulsar Esc')
        tex.magnitud=30
        tex.escala=0.5
        self.pulsa_tecla_escape.conectar(self.ir_a_menu)

    def ir_a_menu(self,eventos):
         pilas.cambiar_escena(JuegoCompleto())
