
import pilas

#pilas.iniciar(pantalla_completa=True,gravedad=(0, 0))
#pilas.mundo.motor.ocultar_puntero_del_mouse()

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
            ('Configuraciones',self.configuraciones),
            ('Salir', self.salir)]
        self.menu = pilas.actores.Menu(opciones)

    def titulo(self):
        tit=pilas.actores.Actor('Fondos/titulo2.png')
        tit.escala=5
        tit.escala=[1]
        tit.rotacion=[360]
        tit.y=100
        tit.x=10

    def configuraciones(self):
        pilas.cambiar_escena(Configuraciones())

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

class Configuraciones(pilas.escena.Base):
    def iniciar(self):
        pilas.fondos.Fondo('Fondos/choro.jpg')
        opciones=[('Pantalla Completa',self.fullscrenn),
        ('Modo Ventana',self.modoVentana),
        ('Volver',self.volver)
        ]
        self.menu = pilas.actores.Menu(opciones)
        self.pulsa_tecla_escape.conectar(self.ir_a_menu)
        self.titulo()
        pilas.avisar('Pulse el boton de Esc para volver menu.')

    def titulo(self):
        tit=pilas.actores.Texto('Configuraciones')
        tit.x=-70
        tit.magnitud=35
        tit.y=300
        tit.y=[150]

    def fullscrenn(self):
        pilas.atajos.modo_pantalla_completa()

    def modoVentana(self):
        pilas.atajos.modo_ventana()

    def ir_a_menu(self,eventos):
         pilas.cambiar_escena(JuegoCompleto())

    def volver(self):
        pilas.cambiar_escena(JuegoCompleto())

#------------Cuando Termina El Juego
class TerminaElJuego(pilas.escena.Base):
    def iniciar(self):
        pilas.avisar("Pulse el boton de Esc para volver menu.")
        pilas.fondos.Fondo('Fondos/final.jpg')
        self.pulsa_tecla_escape.conectar(self.salir)
        self.textGanador()
        self.pulsa_tecla_escape.conectar(self.ir_a_menu)

    def ir_a_menu(self,eventos):
         pilas.cambiar_escena(JuegoCompleto())

    def textGanador(self):
        tit=pilas.actores.Texto('Ciudad libre de delincuentes')
        tit.magnitud=35
        tit.y=300
        tit.y=[150]
        text=pilas.actores.Texto('La ciudad a quedado libre de\n bandalos gracias a su astucia.')
        text.x=400
        text.x=[50]
    def salir(self,eventos):
        pilas.cambiar_escena(JuegoCompleto())

#pilas.cambiar_escena(JuegoCompleto())
#pilas.ejecutar()
