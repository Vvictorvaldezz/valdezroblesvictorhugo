def DDAL(x1, y1, x2, y2, color1, color2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    steps = 0
    
    if (dx) > (dy):
        steps = (dx)
    else:
        steps = (dy)
          
    xInc = float(dx / steps)
    yInc = float(dy / steps)

    xInc = round(xInc,1)
    yInc = round(yInc,1)

    for i in range(0, int(steps + 1)):
        plt.plot(round(x1),round(y1), color2)
        x1 += xInc
        y1 += yInc

        resultado.set("Resultado:"+str(x1))
        resultado.set(str(y1))
        #print(x1)
        #print(y1)
    plt.show()

   