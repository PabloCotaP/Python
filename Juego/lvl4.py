import pygame as pg

white = (255, 255, 255)
grey = (200, 200, 200)
black = (0, 0, 0)
cian = (51, 255, 218)
pink = (243, 127, 239)
orange = (255, 124, 0)
purple = (137, 100, 222)
salmon = (237, 126, 126)
green = (120, 232, 126)
blue = (120, 191, 232)
yellow = (241, 241, 119)


class Node:
    def __init__(self, x, y, unlock=False, color=grey, radius=25, start=False, value=1, end_value=0):
        self.x = x
        self.y = y
        self.color = color
        self.unlock = unlock
        self.radius = radius
        self.start = start
        self.value = value
        self.og_value = value
        self.end_value = end_value
        self.font = pg.font.Font(None, 24)
        
    def draw(self):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        if self.value > 1 or self.end_value == 1:
            text_surface = self.font.render(str(self.value), True, (0, 0, 0))  #Renderizar el valor como texto
            text_rect = text_surface.get_rect(center=(self.x, self.y))  #Obtener el rectángulo que contiene el texto
            screen.blit(text_surface, text_rect)  #Mostrar el texto en el centro del círculo

#Funcion que revisa si todos los nodos tienen su valor final
def check_nodes(nodes):
    for node in nodes:
        if node.end_value != 0 and node.end_value != node.value:
            return False  # Si al menos un nodo no tiene su valor final, retorna False
    return True  # Si todos los nodos tienen su valor final, retorna True
            
#Funcion para imprimir los valores finales de los circulos
def draw_end_value(nodes):
    y = 100
    for node in nodes:
        if node.end_value != 0:
            pg.draw.circle(screen, node.color, (100, y), 30)
            if node.end_value >= 1 and node.color != grey:
                text_surface = node.font.render(str(node.end_value), True, (0, 0, 0))  #Renderizar el valor como texto
                text_rect = text_surface.get_rect(center=(100, y))  #Obtener el rectángulo que contiene el texto
                screen.blit(text_surface, text_rect)  #Mostrar el texto en el centro del círculo
                y += 75
            
#Funcion que crea los nodos, le da sus atributos y diseña el nivel
def create_nodes(nodes):
    for node_y in range(100, 701, 100):
            for node_x in range(300, 901, 100):
                node_start = True if (node_x, node_y) in [(600, 100), (300, 700), (300, 300), (500, 400), 
                                                          (900, 500), (600, 700), (400, 500), (300, 200)] else False # Definir qué nodos son iniciales
                #Da valor y color a los nodos iniciales
                if node_x == 600 and node_y == 100:
                    node_color = cian
                    node_value = 9
                    node_end_value = 1
                elif node_x == 300 and node_y == 700:
                    node_color = pink
                    node_value = 27
                    node_end_value = 3
                elif node_x == 300 and node_y == 300:
                    node_color = orange
                    node_value = 32
                    node_end_value = 4
                elif node_x == 500 and node_y == 400:
                    node_color = purple
                    node_value = 64
                    node_end_value = 8
                elif node_x == 900 and node_y == 500:
                    node_color = salmon
                    node_value = 144
                    node_end_value = 12
                elif node_x == 600 and node_y == 700:
                    node_color = green
                    node_value = 55
                    node_end_value = 11
                elif node_x == 400 and node_y == 500:
                    node_color = blue
                    node_value = 198
                    node_end_value = 33
                elif node_x == 300 and node_y == 200:
                    node_color = yellow
                    node_value = 555
                    node_end_value = 37
                #Da valor a algunos nodos
                elif node_x == 300 and node_y == 100:
                    node_value = 3
                elif node_x == 400 and node_y == 400:
                    node_value = 9
                elif node_x == 700 and node_y == 300:
                    node_value = 8
                elif node_x == 900 and node_y == 400:
                    node_value = 4
                elif node_x == 900 and node_y == 700:
                    node_value = 4
                elif node_x == 600 and node_y == 600:
                    node_value = 5
                elif node_x == 800 and node_y == 500:
                    node_value = 3
                elif node_x == 800 and node_y == 200:
                    node_value = 5
                elif node_x == 500 and node_y == 100:
                    node_value = 3
                elif node_x == 800 and node_y == 300:
                    node_value = 2
                elif node_x == 700 and node_y == 600:
                    node_value = 3
                elif node_x == 500 and node_y == 700:
                    node_value = 2
                elif node_x == 900 and node_y == 100:
                    node_value = 3
                else:
                    node_value = 1
                if node_start == True:
                    new_node = Node(node_x, node_y, True, node_color, 50, node_start, node_value, node_end_value)
                else:
                    new_node = Node(node_x, node_y, value= node_value)
                new_node.draw()
                nodes.append(new_node)
        
    return nodes

def lvl4():
    # Ajuste básico
    pg.init()
    global screen 
    screen = pg.display.set_mode((1000, 800))
    pg.display.set_caption("Resuelve y conecta")
    clock = pg.time.Clock()
    lines = []
    nodes = []
    max_x_lim = 200
    other_node = None
    drawing = False
    lvl_img = pg.image.load(r"D:\Proyectos Python\Lenguaje Python UABC\Juego\lvl4.png").convert()
    win_img = pg.image.load(r"D:\Proyectos Python\Lenguaje Python UABC\Juego\win.png").convert()
    img_act = lvl_img
    btn_back = pg.Rect(41, 761, 162, 38)
    btn_rtrn = pg.Rect(361,467, 177, 64)
    
    # Dibujar los nodos
    nodes = []
    create_nodes(nodes)
    
    # Ciclo de juego
    while True:
        screen.blit(lvl_img, (0, 0))
        pg.draw.rect(surface=screen, color=black, rect=(200, 0, 800, 800))
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:  # Si se suelta el clic izquierdo
                    drawing = False
                    if other_node is not None:
                        end_pos = pg.mouse.get_pos()
                        for node in nodes:
                            distance = ((end_pos[0] - node.x) ** 2 + (end_pos[1] - node.y) ** 2) ** 0.5
                            if distance <= node.radius and node != other_node and node.color == grey:  # Verificar si se ha soltado en otro nodo
                                # Calcular la distancia entre el nodo actual y el nodo final
                                distance_to_final_node = ((node.x - other_node.x) ** 2 + (node.y - other_node.y) ** 2) ** 0.5
                                if distance_to_final_node <= 125:
                                    if not node.unlock:  # Verificar si el nodo está bloqueado
                                        other_node.unlock = False #Se bloque el nodo del que salio la linea
                                        node.color = other_node.color  #Cambiar el color del nodo al color del nodo original
                                        node.unlock = True  #Desbloquear el nodo soltado
                                        #Intercambiar el radio y valor final de ambos nodos
                                        other_node.radius, node.radius = node.radius, other_node.radius
                                        other_node.end_value, node.end_value = node.end_value, other_node.end_value
                                        #Multiplica los valores
                                        if other_node.value != 0:
                                            node.value = int(other_node.value / node.value)
                                        else:
                                            node.value = node.value
                                        other_node.value = 0 #Asigna 0 al nodo original
                                    lines.append(((other_node.x, other_node.y), (node.x, node.y), node.color))  # Agregar la línea a la lista
                                    other_node = None
                                    break
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:  #Si se hace clic izquierdo
                    mouse_pos = pg.mouse.get_pos()
                    if btn_back.collidepoint(mouse_pos) and img_act == lvl_img:
                        return True
                    for node in nodes:
                        distance = ((mouse_pos[0] - node.x) ** 2 + (mouse_pos[1] - node.y) ** 2) ** 0.5 #Se calcula el radio para saber si el mouse esta dentro de un nodo usando sqrt(x² + y²) = r
                        if distance <= node.radius and node.unlock:  #Verificar si el nodo está desbloqueado y no es un nodo inicial o final
                            other_node = node  #Establecer el nodo actual
                            drawing = True
                            break
                elif event.button == 3: #Si se hace click derecho
                    mouse_pos = pg.mouse.get_pos()
                    for node in nodes:
                        distance = ((mouse_pos[0] - node.x) ** 2 + (mouse_pos[1] - node.y) ** 2) ** 0.5
                        if distance <= node.radius and node.unlock and node.start == False:  
                            #Encontrar y eliminar las líneas conectadas al nodo
                            connected_lines = []
                            for line in lines:
                                if (line[0][0], line[0][1]) == (node.x, node.y) or (line[1][0], line[1][1]) == (node.x, node.y):
                                    connected_lines.append(line)
                            for line in connected_lines:
                                lines.remove(line)
                                other_end = line[1] if (line[0][0], line[0][1]) == (node.x, node.y) else line[0]
                                for other_node in nodes:
                                    if (other_node.x, other_node.y) == other_end and not other_node.unlock:
                                        other_node.color = node.color
                                        other_node.unlock = True
                                        #Intercambiar el radio y valor final de ambos nodos
                                        other_node.radius, node.radius = node.radius, other_node.radius
                                        other_node.end_value, node.end_value = node.end_value, other_node.end_value
                                        #Node es el que tendra el valor original
                                        #Other_node es el que pasara a tener el valor dividio
                                        if node.value !=0:
                                            other_node.value = node.value * node.og_value
                                        else:
                                            other_node.value = other_node.value
                                        node.value = node.og_value
                                        break
                            #Cambiar el color del nodo a gris y bloquearlo
                            node.color = grey
                            node.unlock = False
                            other_node = None  #Reinicia la variable para evitar errores
                            break

        if drawing and other_node is not None:
            current_pos = pg.mouse.get_pos()
            distance = ((current_pos[0] - other_node.x) ** 2 + (current_pos[1] - other_node.y) ** 2) ** 0.5 #Se calcula la distancia entre donde aparece la linea y la posicion del raton
            if current_pos[0] >= max_x_lim and distance <= 125:
                pg.draw.line(screen, other_node.color, (other_node.x, other_node.y), current_pos, 10)

        for line in lines:
            start_node = (line[0][0], line[0][1])
            end_node = (line[1][0], line[1][1])
            distance = ((end_node[0] - start_node[0]) ** 2 + (end_node[1] - start_node[1]) ** 2) ** 0.5
            
            if distance <= 125:
                pg.draw.line(screen, line[2], line[0], line[1], 10)  #Dibujar todas las líneas en gris
        
        for node in nodes:
            node.draw()
            if node.end_value !=0 and node.end_value == node.value:
                node.unlock = False #Si el nodo ya tiene el valor final se bloquea
        
        end_flag = check_nodes(nodes)
        if end_flag:
            screen.blit(win_img, [300, 200]) #Ponerlo en pantalla
            img_act = win_img
            if img_act == win_img and btn_rtrn.collidepoint(mouse_pos):
                return True
            
            
        clock.tick(60)               
        pg.display.update()
        
 
if __name__ == "__main__":
    lvl4()