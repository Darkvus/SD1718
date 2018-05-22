import os
import dropbox
from dropbox.files import WriteMode
from PIL import Image
from matplotlib.pylab import *


def grafica(tagId, porcentajes):
    
    representacion(porcentajes,tagId)

def representacion(porcentajes, tagId):

    
    figure(1, figsize=(8,8))
    ax = axes([0, 0, 0.9, 0.9])
    labels = 'Victorias', 'Derrotas' #nomre de los datos
    #print(porcentajes[0])
    fracs = [porcentajes[0],porcentajes[1]] #datos a graficar
    pie(fracs,labels=labels, autopct='%10.0f%%', shadow=True)
    legend()
    title('StastsRoyale', bbox={'facecolor':'0.8', 'pad':5})

    savefig(tagId + ".jpg")
    #show() #mostrar grafico
    userdbx = dropbox.Dropbox('')
    #print(userdbx.users_get_current_account())
    print("Subiendo la Grafica")
    #userdbx.files_list_folder("", False)

    nombre = tagId+".jpg"
    with open(nombre, "rb") as f:
         userdbx.files_upload(f.read(), "/"+nombre, mute = True) #response =

    enlace = userdbx.files_get_temporary_link("/"+nombre)
    print('Grafica subida a: ', enlace)

    #Eliminación de la parte que guarda el enlace en un TXT
    

    

    
