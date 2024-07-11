import sys

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
    if len(sys.argv) != 3:
        print("Usage: python script.py <фаил окружность> <фаил точек> without .py")
        sys.exit(1)
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    mod_c = __import__(arg1)
    mod_coor = __import__(arg2)
    dot_detection(mod_c, mod_coor)
