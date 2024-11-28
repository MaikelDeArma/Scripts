import os

#creando una carpeta
#nueva_carpeta = "Carpeta Nueva"
#os.mkdir(nueva_carpeta)

#creandola en una rura

#creando cantidad carpertas en una ubicacion
for marcador in range(1,4):
    dirCarpeta = "//home//maikelcnry//Escritorio//Automatizaion Python//Carpeta Nueva"
    nombre_carperta = "Nueva subcarpeta #" + str(marcador)
    rutaCompleta = os.path.join(dirCarpeta,nombre_carperta)
    os.mkdir(rutaCompleta)