import importlib 
def dot_detection(mod_c, mod_coor):

    for dot in mod_coor.dot_coords:
        relative_x, relative_y = mod_c.x - dot[0], mod_c.y - dot[1]
        hypotenuse = (relative_x**2+relative_y**2)**(1/2)
        if hypotenuse < mod_c.r:
            print(1)
        elif hypotenuse > mod_c.r:
            print(2)
        else:
            print(0)
        
if __name__ == '__main__': 
    circle_file = input('Введите фаил значений окружности: ')
    coordinates_file  = input('Введите фаил значений координат: ')
    mod_c = __import__(circle_file)
    mod_coor = __import__(coordinates_file)
    dot_detection(mod_c, mod_coor)
