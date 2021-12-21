from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
import cv2
from PIL import Image, ImageTk
import imutils
import os
import detect_faces as df
import numpy as np



#Configuration de la fenêtre principale
mainWidget = Tk()
mainWidget.title("Comptage du nombre d'absents")
mainWidget.geometry("1080x720")
mainWidget.configure(background = '#021b34')

screen_width = mainWidget.winfo_screenwidth()
screen_height = mainWidget.winfo_screenheight()

ret = None
img = None
 
#Frame contenant le frame du choix du fichier source/ lancement de la cam
FrameContainer = LabelFrame(mainWidget,
                             text="Accéder à la caméra/ Importez une image ou une vidéo source! ",
                             bg = '#021b34',
                             bd = 2,
                             fg = '#FFFFFF',
                             font=("Courier", 14, "italic")
                             )
FrameContainer.pack(expand = 'yes')

#Le frame du choix du fichier source/ lancement de la cam
detectionMethod = Frame(FrameContainer,
                             pady=50,
                             bg = '#021b34',
                             bd = 2,
                             )
detectionMethod.pack( expand="yes")
 
# bouton d'accès à la caméra
boutonCam=Button(detectionMethod, 
              text="Accéder à la caméra",
              bg = '#021b34',
              font=("Courier", 14, "italic"),
              padx = 2,
              pady = 5,
              relief = GROOVE,
              height = 2,
              cursor = 'sizing',

              )
boutonCam.pack(side = TOP,
               fill="both",
               pady = 5)

# bouton d'importation d'un fichier
boutonImportFile=Button(detectionMethod, 
              text="Importer une image/ vidéo source",
              bg = '#021b34',
              font=("Courier", 14, "italic"),
              padx = 2,
              pady = 5,
              relief = GROOVE,
              height = 2,
              cursor = 'plus',

              )
boutonImportFile.pack(side = BOTTOM,
                      fill="both",
                      pady = 5)


mainWidget.mainloop()