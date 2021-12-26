import cv2

def face_detection_algo(frame):
	nbEtudiantsAbsents = 0
	# Chemin du Classifier
	cascadeClassifierPath = 'haarcascade_frontalface_alt.xml'
	cascadeClassifier = cv2.CascadeClassifier(cascadeClassifierPath)
	# Conversion des images obtenues à niveaux de gris afin d'appliquer l'algorithme de détection
	grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#Détection des visages
	detectedFaces= cascadeClassifier.detectMultiScale(grayImage,  scaleFactor=1.1, minNeighbors=8, minSize=(20, 20))

	for(x,y, width, height) in detectedFaces:
		# Dessin d'un rectangle autour de(s) visage(s) détecté(s)
		cv2.rectangle(frame, (x, y), (x+width, y+height), (0,255,0), 3)

		#Comptage du nombre de visage détectés
		nbEtudiantsAbsents+=1

	return frame, nbEtudiantsAbsents


