import pygame

MAXIMO=50 #NUMERO MAXIMO DE ITERACIONES PARA SABER SI CONVERGE
Amin, Amax, Bmin, Bmax = -1.05, 1.05, -1.05, 1.05 #COORDENADAS DE INICIO Y FIN
ancho, alto= 700, 700 #TAMAÑO DE LA VENTANA EN PIXELES

#INICIAMOS CREANDO LA VENTANA CON LAS DIMENCIONES ESPECIFICADAS
pygame.init()
screen = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("FRACTAL")

#ESCANEAMOS PIXEL POR PIXEL PARA SABER SI EL PUNTO CONVERGE O NO
for y in range(alto):
    for x in range(ancho):
        #INICIALIZAMOS EL PUNTO C (C_real, C_imaginario) DEFINIDO EN EL MARCO DE Amin, Amax, Bmin, Bmax
        cx = (x * (Amax - Amin) / ancho + Amin)
        cy = (y * (Bmin - Bmax) / alto + Bmax)
        xn=0
        yn=0
        n=0
        while (xn**2 + yn**2)<4 and n < MAXIMO: #INGRESAMOS LAS CONDICIONES PARA SABER SI EL PUNTO CONVERGE O NO
            #CALCULAMOS CON LA PARTE REAL E IMAGINARIA
            tmp_x = xn
            tmp_y = yn
            xn = (tmp_x**3)- 3*( tmp_x * tmp_y**2) - tmp_x + cx
            yn = 3 *(tmp_x **2 * tmp_y) - (tmp_y **3) - tmp_y + cy
            n = n + 1

        if n==MAXIMO:
            #SI N LLEGO HASTA EL FINAL ENTONCES DAMOS POR ENTENDIDO QUE PERTENESE AL CONJUNTO Y LO PINTAMOS DE NEGRO
            screen.set_at((x, y), (0, 0, 0))
        else:
            #SI N NO LLEGO HASTA EL FINAL ENTONCES LO PINTEMOS DE BLANCO
            #screen.set_at((x, y), (255, 255, 255))
            #TAMBIEN SE PUEDE PINTAR DE UN COLOR SEGUN EL VALOR DE N CON EL QUE SE QUEDO
            screen.set_at((x, y), ((6 * n) % 256, (1 * n) % 256, (20 * n) % 256))

    pygame.display.flip()#ACTIALIZAMOS LA VENTANA DE GRAFICOS

#CREAMOS ESTE BUCLE INFINITO PARA MANTENER LA VENTANA ABIERTA
loop = True
while loop:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: # PARA SALIR DEL BUCLE Y CERRAR EL PROGRAMA
      loop = False
pygame.quit()