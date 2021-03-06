import matplotlib.pyplot as plt
    
def Bresenham(x1, y1, x2, y2, color1):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    p = 2*dy - dx

    x = x1
    y = y1
    
    for i in range(x, x2):
        plt.plot(round(x),round(y), color1)
        x = x + 1
        if p <0:
            p = p + 2 * dy
        else:
            p = p + (2*dy) -(2*dx)
            y = y + 1
        
        print(x)
        print(y)
    plt.show()

def main():
    x1 = int(input("Ingresa  X1: "))
    y1 = int(input("Ingresa  Y1: "))
    x2 = int(input("Ingresa  X2: "))
    y2 = int(input("Ingresa  Y2: "))
    color1 = "r."
    
    
    Bresenham(x1, y1, x2, y2, color1)


if __name__ == '__main__':
    main()