from lvl1 import *
from lvl2 import * 
from lvl3 import *
from lvl4 import *
import pygame as pg

# Ajuste básico
pg.init()
screen = pg.display.set_mode((1000, 800))
pg.display.set_caption("Resuelve y conecta")
clock = pg.time.Clock()

#Se carga las imagenes como objetos
menu_img = pg.image.load(r"D:\Proyectos Python\Lenguaje Python UABC\Juego\menu.png").convert()
lvl_img = pg.image.load(r"D:\Proyectos Python\Lenguaje Python UABC\Juego\levels.png").convert()
crdts_img = pg.image.load(r"D:\Proyectos Python\Lenguaje Python UABC\Juego\credits.png").convert()
act_img = menu_img

#Se crea un rectangulo para la posicion del boton jugar
btn_play = pg.Rect(319, 400, 360, 109)
btn_cred = pg.Rect(350, 546, 299, 90)
btn_back = pg.Rect(25, 701, 210, 64)
btn_lvl1 = pg.Rect(385, 400, 227, 69)
btn_lvl2 = pg.Rect(385, 488, 227, 69)
btn_lvl3 = pg.Rect(385, 576, 227, 69)
btn_lvl4 = pg.Rect(385, 662, 227, 69)

# Ciclo de juego6
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:  #Si se hace clic izquierdo
                mouse_pos = pg.mouse.get_pos()
                #Verificar si se hizo clic en el area del algun boton en base de que imagen este activa
                #Verificaciones para cuando la imagen activa es el menu
                if act_img == menu_img and btn_play.collidepoint(mouse_pos):
                    act_img = lvl_img
                if act_img == menu_img and btn_cred.collidepoint(mouse_pos):
                    act_img = crdts_img
                #Verificaciones para cuando la imagen activa son los creditos
                if act_img == crdts_img and btn_back.collidepoint(mouse_pos):
                    act_img = menu_img
                #Verificaciones para cuando la imagen activa es el selector de niveles
                if act_img == lvl_img and btn_back.collidepoint(mouse_pos):
                    act_img = menu_img
                if act_img == lvl_img and btn_lvl1.collidepoint(mouse_pos):
                    running = lvl1()
                if act_img == lvl_img and btn_lvl2.collidepoint(mouse_pos):
                    running = lvl2()
                if act_img == lvl_img and btn_lvl3.collidepoint(mouse_pos):
                    running = lvl3()
                if act_img == lvl_img and btn_lvl4.collidepoint(mouse_pos):
                    running = lvl4()


    screen.blit(act_img, (0,0))
        
    clock.tick(60)               
    pg.display.update()
        
# Cierra el juego
pg.quit()