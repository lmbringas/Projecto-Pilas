import pilas
import random
from pilas.actores import Actor
import personaje,auto
from Coche import CocheMoviendo
from pistola import Arma
from movimiento import MoverseConElTeclado
from ladron import Choro
from actorBala import Bala

#-------------------El Juego ---------------------------------------------------
class MiJuego(pilas.escena.Base):

    def iniciar(self):
        self.mapa=pilas.actores.MapaTiled('mapa.tmx',x=0,y=0)
        self.defTextos() # Tablero

        #------------- Variables que voy usar en el juego-----------
        self.municionn=9
        self.foo=False # Variables que uso para vereficar si toca o no una tecla o si esta o no dentro del auto tambien si tiene la habilidad de disparar
        self.estaAdentro=False
        self.dispara=False
        self.sabeDisparar=False
        self.actres=[]
        self.enemigos=[]
        self.creado=True
        self.conta=0
        #------------ Genero actores ----------------------
        self.miActor=personaje.MiActor(self.mapa,x=90,y=-150,imagen='Personajes/Maton.png',velocidad=1) # Llamo a un personaje principal el policia
        self.coche=auto.Autito(self.mapa,x=90,y=-600,imagen='Personajes/autos.png',velocidad=10) # este es el auto al que se puede subir
        self.unAuto=CocheMoviendo(x=90,y=-200, imagen='Personajes/autos.png',velocidad=10) # el auto que va estar dando vuelta la ciudad
        self.unArma=Arma(x=180,y=-410,imagen='Personajes/Pistolita.png',velocidad=0) # es un actor que le da habilidad de poder disparar cuando colisiona con el
        self.actres.append(self.miActor)
        self.generarEnemigos()

        #----------------Colisiones y evento de  teclas----------------------
        pilas.mundo.colisiones.agregar(self.actres, self.coche, self.cuandoCo)
        pilas.mundo.colisiones.agregar(self.actres,self.unArma,self.aprendeDisparar)
        pilas.eventos.pulsa_tecla.conectar(self.tocaElTeclado)
        self.pulsa_tecla_escape.conectar(self.ir_a_menu)
        pilas.mundo.agregar_tarea_siempre(1,self.vericador)

    def vericador(self):
        if self.estaAdentro:
            self.distanciaa(self.coche)

        else:
            self.distanciaa(self.miActor)

        if len(self.enemigos)==0:
            import menu
            pilas.cambiar_escena(menu.TerminaElJuego())

    def distanciaa(self,actorCoche):
        if len(self.enemigos)<=10:
            if self.creado:
                self.tex=pilas.actores.Texto('Distancia:',x=-250,y=-200)
                self.distancia=pilas.actores.Puntaje( x=-175, y=-200, color=pilas.colores.blanco)
                self.creado=False

            for j in range(len(self.enemigos)):
                if actorCoche.distancia_con(self.enemigos[j])<=700:
                    self.ladron=self.enemigos[j]
                    dis=self.distancia.obtener()
                    self.distancia.aumentar(actorCoche.distancia_con(self.enemigos[j])-dis)


    def defTextos(self):
        self.ladroQueFaltan=pilas.actores.Puntaje( x=45, y=200, color=pilas.colores.blanco)
        tex1=pilas.actores.Texto('Faltan:',x=-15,y=200)
        self.ladroQueAgarraste=pilas.actores.Puntaje(x=300, y=200, color=pilas.colores.blanco)
        tex2=pilas.actores.Texto('Agarraste:',x=220,y=200)

    def generarEnemigos(self):
        cantidad=[10,15,30,35]
        direccion=['derecha','izquierda','abajo','arriba']
        lugarX=[150,400,500,839,850,1000,1300,1642,1999,2000,2300,2500,2700,3100]
        lugarY=[-157,-186,-500,-1002,-1371,-1500,-1900,-2000,-2200,-2500,-2700,2800,-3100]
        for x in range(random.choice(cantidad)):
            self.enemigos.append(Choro(self.mapa,x=random.choice(lugarX),y=random.choice(lugarY),imagen='Personajes/ladron2.png',
                                       velocidad=random.randint(1,4),policia=self.miActor,ir=random.choice(direccion)))

        self.ladroQueFaltan.aumentar(len(self.enemigos))
        self.miActor.enemigos=self.enemigos
        self.coche.enemigos=self.enemigos

    def cuandoCo(self,miActor,coche):
        if self.foo:
            self.dispara=False
            miActor.eliminar()
            coche.aprender(MoverseConElTeclado,con_rotacion=True,velocidad_maxima=6)
            coche.aprender(pilas.habilidades.SiempreEnElCentro)
            self.estaAdentro=True
            pilas.mundo.colisiones.agregar(coche,self.enemigos,self.eliminarEnemigoConAuto)

    def aprendeDisparar(self,miActor,unArma): #Cuando colisiona el policia con el arma aprende a disparar
        if not(self.municionn==0):
            self.miActor.aprender(pilas.habilidades.Disparar,municion=pilas.actores.Bala,\
                                  grupo_enemigos=self.enemigos,frecuencia_de_disparo=2,cuando_dispara=self.restarMunicion,offset_origen_actor=(0,-5),\
                                  cuando_elimina_enemigo=self.eliminarEnemigo)
            self.unArma.eliminar()
            self.dispara=True
            self.sabeDisparar=True
            self.tarea=pilas.mundo.agregar_tarea_siempre(0.1,self.dondeDisparar)
            tex3=pilas.actores.Texto('Municion:',x=-250,y=200)
            self.laMunicion=pilas.actores.Puntaje( x=-175, y=200, color=pilas.colores.blanco)
            self.laMunicion.aumentar(self.municionn+1)
            pilas.mundo.agregar_tarea_siempre(60,self.generadorMuniciones)
        else:
            pass

    def tocaElTeclado(self,e): #Verifica cuando haya presionado las tecla E(entrar) o W(salir)
        if e.codigo==pilas.simbolos.w and self.estaAdentro:
            self.foo=False
            self.coche.eliminar_habilidad(pilas.habilidades.SiempreEnElCentro)
            self.miActor=personaje.MiActor(self.mapa,self.coche.x+10,self.coche.y+10,imagen='Personajes/Maton.png',velocidad=1)
            self.actres.append(self.miActor)
            self.coche.eliminar_habilidad(MoverseConElTeclado)
            self.estaAdentro=False

            if self.hayEnemigos:
                for x in range(len(self.enemigos)):
                    self.enemigos[x].posicionePolic=self.miActor
                self.miActor.enemigos=self.enemigos

            if self.sabeDisparar: # Verifico que sepa disparar mi actor
                self.dispara=True

            if not(self.municionn<0): # si la municion no es 0 y sabe disparar entonces aprende la habilidad
                if self.sabeDisparar and self.dispara:
                    self.miActor.aprender(pilas.habilidades.Disparar,municion=pilas.actores.Bala,\
                                  grupo_enemigos=self.enemigos,frecuencia_de_disparo=2,cuando_dispara=self.restarMunicion,offset_origen_actor=(0,-5),\
                                  cuando_elimina_enemigo=self.eliminarEnemigo)
            else:
                self.dispara=False # No va disparar

        if e.codigo==pilas.simbolos.e and self.foo==False:
            self.foo=True

        if e.codigo==pilas.simbolos.p:
            pilas.escena.pausar()

    def ir_a_menu(self, evento):
        import menu
        pilas.cambiar_escena(menu.JuegoCompleto())

    def generadorMuniciones(self):
        self.balas=Bala(mapa=self.mapa,imagen='Personajes/municion.png', x=90,y=-150)#x=1600,y=1520)
        pilas.mundo.colisiones.agregar(self.actres,self.balas,self.recargarMunicion)
        self.hayMunicion=False


    def recargarMunicion(self,miActor,balas):
        antes = self.municionn
        balas.eliminar()
        if self.municionn>0:
            self.municionn+=9
            self.laMunicion.aumentar(abs(self.municionn-antes))

        elif self.municionn<0:
            self.municionn+=10
            self.laMunicion.aumentar(self.municionn+1)
        else:
            pass
        self.miActor.aprender(pilas.habilidades.Disparar,municion=pilas.actores.Bala,\
                                  grupo_enemigos=self.enemigos,frecuencia_de_disparo=2,cuando_dispara=self.restarMunicion,offset_origen_actor=(0,-5),\
                                  cuando_elimina_enemigo=self.eliminarEnemigo)
        self.dispara=True

    def restarMunicion(self):
        if self.municionn==0:
            self.miActor.eliminar_habilidad(pilas.habilidades.Disparar)
            self.dispara=False
            self.laMunicion.aumentar(-1)
            self.municionn=-1
        elif self.municionn>0:
            self.municionn-=1
            self.laMunicion.aumentar(-1)
        else:
            pass

    def eliminarEnemigo(self,bala,ladrones):
        bala.eliminar()
        ladrones.eliminar()
        self.ladroQueFaltan.aumentar(-1)
        self.ladroQueAgarraste.aumentar(1)
        self.miActor.enemigos=self.enemigos
        self.coche.enemigos=self.enemigos

    def eliminarEnemigoConAuto(self,auto,ladrones):
        ladrones.eliminar()
        self.ladroQueFaltan.aumentar(-1)
        self.ladroQueAgarraste.aumentar(1)

    def dondeDisparar(self): #Obtiene donde poder disparar
        if self.dispara and self.sabeDisparar:
            if pilas.escena_actual().control.izquierda:
                self.miActor.obtener_habilidad(pilas.habilidades.Disparar).angulo_salida_disparo=90
            elif pilas.escena_actual().control.derecha:
                self.miActor.obtener_habilidad(pilas.habilidades.Disparar).angulo_salida_disparo=270
            elif pilas.escena_actual().control.arriba:
                self.miActor.obtener_habilidad(pilas.habilidades.Disparar).angulo_salida_disparo=0
            elif pilas.escena_actual().control.abajo:
                self.miActor.obtener_habilidad(pilas.habilidades.Disparar).angulo_salida_disparo=-180
            else:
                pass
        else:
            pass

    def hayEnemigos(self):
        if len(self.enemigos)==0:
            return False
        else:
            return True
