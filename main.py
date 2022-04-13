from circle import Circle

if __name__ == '__main__':

    circle1=Circle(radius = 5)        
    circle2=Circle(radius = 3)    
    circle3=Circle(radius = 6)        
    circle4=Circle(radius = 4)   

    circle1.print()
    circle2.print()
    print( (circle1 + circle2).print() )

    circle_list = []
    circle_list.append(circle1)
    circle_list.append(circle2)
    circle_list.append(circle3)
    circle_list.append(circle4)
    for circle in circle_list:
        circle.print()
    circle_list.sort()
    for circle in circle_list:
        circle.print()