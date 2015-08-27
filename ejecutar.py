import pilas
import menu

pilas.iniciar(pantalla_completa=True,gravedad=(0, 0))
pilas.mundo.motor.ocultar_puntero_del_mouse()
pilas.cambiar_escena(menu.JuegoCompleto())
pilas.ejecutar()
