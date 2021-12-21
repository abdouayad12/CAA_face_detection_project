from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
import cv2
from PIL import Image, ImageTk
import imutils
import os
import detect_faces as df
import numpy as np
def close_camera():
    global cap
    cv2.destroyAllWindows()
    cap.release()


def change_to_camera_frame():
   camera_frame.pack( fill = "both",expand="yes")
   global cap
   cap = cv2.VideoCapture(0)
   detect_faces()
   #visualisation()
   FrameContainer.forget()


def change_to_upload_frame():

   FrameContainer.forget()
   camera_frame.forget()

def change_to_main_window():
    global ret
    if ret:
        close_camera()
    camera_frame.forget()

    FrameContainer.pack(expand="yes")



def popup():
    messagebox.showinfo("Nombre d'absents","Le nombre d'absents est: 5!")


def detect_faces():
        global ret
        global cap
        ret,frame = cap.read()
        if ret == True:
            #Appel de l'algorithme de détection de visage
            frame = df.face_detection_algo(frame)

            #Affichage des résultats de détection
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = imutils.resize(frame, width=720)
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)
            lblVideo.configure(image=img)
            lblVideo.image = img
            lblVideo.after(10, detect_faces)

        #Condition d'arrêt (fermeture de la caméra)
        else:
            lblVideo.image = ""
            cap.release()




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
              command = change_to_camera_frame
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
              command = change_to_upload_frame
              )
boutonImportFile.pack(side = BOTTOM,
                      fill="both",
                      pady = 5)




#====================================Camera Frame=============================
#Le frame de lancement de la caméra
camera_frame = Frame(mainWidget,

                             bg = '#021b34',
                             bd = 2,
                             )

# bouton de retour à la fenetre de départ
returnbtn=Button(camera_frame,
              text="retour en arrière",
              bg = '#021b34',
              font=("Courier", 12, "italic"),
              padx = 2,
              pady = 5,
              relief = GROOVE,
              height = 2,
              cursor = 'exchange',
              command = change_to_main_window,
              bd = 0,

              )
returnbtn.pack(anchor = NE,
               padx = 2,
               pady = 5)

buttonsContainerFrame = LabelFrame(camera_frame,

                             bg = '#021b34',
                             bd = 2,
                             fg = '#FFFFFF',
                             )
buttonsContainerFrame.pack( side = RIGHT)

#Titre -> choix du nombre d'étudiants total
labelStudentNB = Label(buttonsContainerFrame,
                       text="choix du nombre total d'étudiants",
                       pady = 5,
                       bg = '#021b34',
                       fg = '#FFFFFF',
                       font=("Courier", 12, "italic"),
                       )
labelStudentNB.pack(side = TOP,
                    padx = 2,
                    pady = 10)


#Choix du nombre d'étudiants total
studentsNB = IntVar()
studentsNB.set("saisissez le nombre d'étudiants de la promo!")
entree = Entry(buttonsContainerFrame,
               )
entree.pack( pady = 10)

# bouton pour lancer l'algorithme de détection du nombre d'absents
launchDetection=Button(buttonsContainerFrame,
              text="Lancer la détection",
              bg = '#021b34',
              font=("Courier", 12, "italic"),
              padx = 2,
              pady = 5,
              relief = GROOVE,
              height = 2,
              cursor = 'exchange',
              command = popup,
              ).pack(side = BOTTOM, pady = 10)


lblVideo = Label(camera_frame)
lblVideo.pack(side = LEFT, padx = 30)



#====================================Import File Frame========================



#Initialisation du frame principal "mainWidget"
change_to_main_window()

mainWidget.mainloop()