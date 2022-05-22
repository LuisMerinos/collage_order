

from PIL import Image, ImageEnhance





import os
from os import mkdir
import shutil
ruta ='C:/Users/Admin/OneDrive/Escritorio/fotos/'


files= os.listdir(ruta)

data = ['721','722','726','770']


compuesto= []
for i in data: 
    dato= 'DSC00'+i+'.JPG'
    compuesto.append(dato)
    


for i in compuesto:
    print(i)




mover = []

list_files = [f for f in files if f[-4:] == '.JPG'] 



for list in list_files:
    for buscar in compuesto:
        if buscar == list:
            print('Econtrado: '+buscar)
            mover.append(buscar)



# Crea la carpeta "Nueva carpeta" en el directorio actual.

lista_carpeta = [f for f in files if f[-4:] != '.JPG'] 

guardar =ruta+str(len(lista_carpeta)+1)+'/'
mkdir(guardar)



arreglo = []
new = Image.new("RGBA", (2000,1000))

for m in mover:
    shutil.move(ruta+m, guardar)
    arreglo.append(Image.open(guardar+m))
  



#----------------------------------------------------
arreglo2=[]
for r in arreglo:
     arreglo2.append(r.resize((500,500)))

  
cont =0; 



for i in range(0,2000,500):
    for j in range(0,2000,500):
        if cont< len(arreglo2):
            new.paste(arreglo2[cont], (j,i))
        cont= cont +1
         
new.save(guardar+'collage.png')

new.show()