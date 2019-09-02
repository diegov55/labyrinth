
def Encontrar():
    for i in range(y):#
        for j in range(x):
            if matriz[i][j] == 2:
                iniciox=i
                inicioy=j
    print "posicion [%s][%s]"%{iniciox,inicioy}
    return(iniciox,inicioy)
def Actualizar():
    for i in range(y):
        for j in range(x):
            if matriz[i][j] == 0:
                iniciox=i
                inicioy=j
                matriz[i][j]=4

    return(iniciox,inicioy)

def Nodos():
    for i in range(y):#
        for j in range(x):
            if matriz[i][j]==4 and matriz[i][j-1]==4 and matriz[i+1][j]==4:
                matriz[i][j]=5
            elif matriz[i][j]==4 and matriz[i+1][j]==4 and matriz[i][j-1]==4:
                matriz[i][j]=5
            elif matriz[i][j]==4 and matriz[i-1][j]==4 and matriz[i][j+1]==4:
                matriz[i][j]=5
            elif matriz[i][j]==4 and matriz[i-1][j]==4 and matriz[i][j-1]==4:
                matriz[i][j]=5
    for i in matriz:
        print i

if __name__ == '__main__':
    matriz=[]
    ar=open('/media/diegova56/USB_DIEGO/agentes/laberinto.txt','r')
    for item in ar.readlines():
        item=item.rstrip()
        aux=[int(ii) for ii in item.split(",")]
        matriz.append(aux)
    print matriz
    y=len(matriz)
    x=len(matriz[0])

    print "Numero de filas:",x#filas 6
    print "Numero de columnas:",y#columnas 10

    iniciox,inicioy=Encontrar()#pocision original del perdido=2
    print matriz[iniciox][inicioy]#matriz[x][y]
    inix=iniciox
    iniy=inicioy



    buscando=1
    while buscando==1:

        if matriz[inix-1][iniy]==3 or matriz[inix+1][iniy]==3 or matriz[inix][iniy-1]==3 or matriz[inix][iniy+1]==3:
            print "Se encontro la salida en %s%s" %([inix],[iniy])
            buscando=0

        elif matriz[inix-1][iniy]==0:#recorrido izquierda
            inix=inix-1
            matriz[inix][iniy]=4
        elif matriz[inix+1][iniy]==0:#recorrido derecha
            inix=inix+1
            matriz[inix][iniy]=4
        elif matriz[inix][iniy-1]==0:#recorrido arriba
            iniy=iniy-1
            matriz[inix][iniy]=4
        elif matriz[inix][iniy+1]==0:#Recorrido abajo
            iniy=iniy+1
            matriz[inix][iniy]=4
        elif matriz[inix-1][iniy]!=0 or [inix+1][iniy]!=0 or matriz[inix][iniy-1]!=0 or matriz[inix][iniy+1]!=0:
            iniciox,inicioy=Actualizar()
            inix=iniciox
            iniy=inicioy
        else:
            print "no se encontro la salida"
            buscando=0

    for i in matriz:
        print i
    print"*****************************************************"
    Nodos()
