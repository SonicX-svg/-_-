from circle1 import x, y, r
from coordinates2 import dot_coords

def dot_detection():
    for dot in dot_coords:
        relative_x, relative_y = x - dot[0], y - dot[1]
        hypotenuse = (relative_x**2+relative_y**2)**(1/2)
        if hypotenuse < r:
            print(1)
        elif hypotenuse > r:
            print(2)
        else:
            print(0)
        
dot_detection()
