from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
import cv2
from PIL import Image, ImageTk
import imutils
import os
import detect_faces as df
import numpy as np


#Fermeture de la camera
def close_camera():
    global cap
    cv2.destroyAllWindows()
    cap.release()

#Fontion qui permet de changer au Frame Camera_frame
def change_to_camera_frame():
    camera_frame.pack( fill = "both",expand="yes")
    global cap
    cap = cv2.VideoCapture(0)
    detect_faces()
    FrameContainer.forget()
    upload_frame.forget()

#Fontion qui permet de changer au Frame Upload_image
def change_to_upload_frame():
    upload_frame.pack( fill = "both",expand="yes")
    FrameContainer.forget()
    camera_frame.forget()

#Fontion qui permet de changer au Frame principal
def change_to_main_window():
    global nbEtudiantsPresents
    nbEtudiantsPresents = 0
    global ret
    if ret:
        close_camera()
    close_image()
    camera_frame.forget()
    upload_frame.forget()
    FrameContainer.pack(expand="yes")


#Message box pour afficher le nombre d'absents
def popup_camera():
    booleen = False
    if(entree.get()==''):
        messagebox.showinfo("Erreur!","Veuillez insérer un nombre valide !")
        booleen = True

    if not booleen:
        messagebox.showinfo("Nombre d'absents","Le nombre d'absents est: {}!".format(nb_absents(entree)))

    #Réinitialisation du champ de saisie
    entree.delete(0,"end")


#Message box pour afficher le nombre d'absents
def popup_upload():
    booleen = False
    if(entree2.get()==''):
        messagebox.showinfo("Erreur!","Veuillez insérer un nombre valide !")
        booleen = True

    if not booleen:
        messagebox.showinfo("Nombre d'absents","Le nombre d'absents est: {}!".format(nb_absents(entree2)))

    #Réinitialisation du champ de saisie
    entree2.delete(0,"end")

# fonctions relatives a l'interface graphique (celle d'importation d'une image pour la detection de visage )
def import_file():
    global img
    global nbEtudiantsPresents
    filepath = askopenfilename(initialdir = os.getcwd(),title="Ouvrir une image",filetypes=[('JPG file','*.jpg'),('PNG file','*.png'),('All files','*.*')])
    img = Image.open(filepath)
    lar, long = img.size
    if (lar > 720):
        if(long > 480):
            img = img.resize((720,480), Image.ANTIALIAS)
        else:
            img = img.resize((720,long), Image.ANTIALIAS)
    elif(long > 480):
        img = img.resize((lar,480), Image.ANTIALIAS)

    #Conversion de l'image en an Array
    img = np.array(img)
    #Appel de l'algorithme de détection de visage
    img,nbEtudiantsPresents = df.face_detection_algo(img)

    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image = img)
    lbl.image = img

#Fermeture de l'image importée
def close_image():
    lbl.configure(image = "")

#Lancement de la détection des visages
def detect_faces():
    global ret
    global cap
    global nbEtudiantsPresents
    ret,frame = cap.read()
    if ret == True:
        #Appel de l'algorithme de détection de visage
        frame,maxFaces = df.face_detection_algo(frame)

        if(maxFaces > nbEtudiantsPresents):
            nbEtudiantsPresents = maxFaces
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


#Calcul du nombre d'étudiants absents
def nb_absents(e):
    global nbEtudiantsPresents
    global nbEtudiantsTotal
    nbEtudiantsTotal = 0
    nbEtudiantsTotal = int(e.get())
    return (nbEtudiantsTotal - nbEtudiantsPresents)


#Restreindre le type du texte passé en entrée du champs de saisie aux nombres seulement
def callback(P):
    if str.isdigit(P) or P == "":
        return True
    else:
        return False


#Configuration de la fenêtre principale
mainWidget = Tk()
mainWidget.title("Comptage du nombre d'absents")
mainWidget.geometry("1080x720")

#Ajout de la barre de menu
menubar = Menu(mainWidget)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Nouveau", command=change_to_main_window)
menu1.add_separator()
menu1.add_command(label="Quitter", command=mainWidget.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

mainWidget.configure(background = '#021b34', menu = menubar)

#Récupération de la taille de la fenêtre(width and height)
screen_width = mainWidget.winfo_screenwidth()
screen_height = mainWidget.winfo_screenheight()

ret = None
img = None

#Initialisation du nombre d'étudiants de la section et du nombre d'étudiants présents
nbEtudiantsPresents = 0
nbEtudiantsTotal = 0
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

#Configuration du champ de saisie
vcmd = (camera_frame.register(callback))

entree = Entry(buttonsContainerFrame, validate='all', validatecommand=(vcmd, '%P'))
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
                       command = popup_camera,
                       ).pack(side = BOTTOM, pady = 10)


lblVideo = Label(camera_frame)
lblVideo.pack(side = LEFT, padx = 30)

#====================================Import File Frame========================

#Le frame pour importer une image/ une vidéo
upload_frame = Frame(mainWidget,

                     bg = '#021b34',
                     bd = 2,

                     )

# bouton de retour à la fenetre de départ
returnbtn2=Button(upload_frame,
                  text="retour en arrière",
                  bg = '#021b34',
                  font=("Courier", 12, "italic"),
                  relief = GROOVE,
                  height = 2,
                  padx = 2,
                  pady = 5,
                  cursor = 'exchange',
                  command = change_to_main_window,
                  bd = 0,

                  )
returnbtn2.pack(anchor = NE,
                padx = 2,
                pady = 5)

#Frame contenant le bouton de détection et le champ de saisie
frm = LabelFrame(upload_frame,
                 bg = '#021b34',
                 bd = 2,
                 fg = '#FFFFFF',
                 )
frm.pack( side = RIGHT,
          padx = 2)

# bouton d'importation d'un fichier
boutonImport=Button(frm,
                    text="Importer une image/ vidéo source",
                    bg = '#021b34',
                    font=("Courier", 12, "italic"),
                    relief = GROOVE,
                    height = 2,
                    padx = 2,
                    pady = 5,
                    cursor = 'plus',
                    command = import_file,
                    bd = 0,
                    )
boutonImport.pack(side = TOP, pady = 50)

#Titre -> choix du nombre d'étudiants total
labelStudentNB2 = Label(frm,
                        text="choix du nombre total d'étudiants",
                        pady = 5,
                        bg = '#021b34',
                        fg = '#FFFFFF',
                        font=("Courier", 12, "italic"),
                        )
labelStudentNB2.pack(side = TOP, pady = 10)


#Choix du nombre d'étudiants total
studentsNB2 = IntVar()
studentsNB2.set("saisissez le nombre d'étudiants de la promo!")

#Configuration du champ de saisie
vcmd2 = (upload_frame.register(callback))

entree2 = Entry(frm, validate='all', validatecommand=(vcmd2, '%P'))
entree2.pack( pady = 10)

# bouton pour lancer l'algorithme de détection du nombre d'absents
launchDetection=Button(frm,
                       text="Lancer la détection",
                       bg = '#021b34',
                       font=("Courier", 12, "italic"),
                       relief = GROOVE,
                       height = 2,
                       padx = 2,
                       pady = 5,
                       cursor = 'exchange',
                       command = popup_upload,
                       bd = 0,
                       ).pack(side = BOTTOM, padx = 30, pady = 10)

#Label qui va contenir l'image importée
lbl = Label(upload_frame,
            bg = '#021b34',
            )
lbl.pack(side = LEFT, padx = 10)

#Initialisation du frame principal "mainWidget"
change_to_main_window()

mainWidget.mainloop()
