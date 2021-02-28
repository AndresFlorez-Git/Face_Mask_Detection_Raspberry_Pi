import picamera
from picamera.array import PiRGBArray
from tensorflow.keras.models import load_model
from Function_util import detect_and_predict_mask, plot_box
import numpy as np
import time
import cv2
import os

print('Cargando redes neuronales...')

# Se carga el modelo de detección de rostros
modelPath = r"Modelo_deteccion_rostros/model.prototxt"
weightsPath = r"Modelo_deteccion_rostros/weights.caffemodel"
face_detection_Net = cv2.dnn.readNet(modelPath, weightsPath)

# Se carga el modelo de detección de máscaras
maskNet = load_model("mask_detector.model")

# Se inicializa el video
print("Iniciando Video...")

# Configuración de la cámara de Raspberry pi
camera = picamera.PiCamera()
camera.resolution = (256,256)
camera.framerate = 30
raw_Capture = PiRGBArray(camera, size=(256,256))
time.sleep(0.01)


for image in camera.capture_continuous(raw_Capture, format='bgr', use_video_port=True):
    frame = image.array
    
    # Usando los modelos de detección de rostro concatenado al modelo de detección de máscara.
    # Se obtiene la ubicación sobre la imagen del rostro y la probabilidad de que se este o no
    # usando máscara.
    (Ubicacion, Probabilidades) = detect_and_predict_mask(frame, face_detection_Net, maskNet)
    
    # Se pinta sobre la imagen la ubicacion y la probabilidad de deteccion de máscara
    # en tiempo real
    frame = plot_box(frame, Ubicacion, Probabilidades)
    
    # Se visualiza la imagen captada por la cámara
    cv2.imshow('Frame',frame)
    key = cv2.waitKey(1) & 0xFF
    raw_Capture.truncate(0)
    
    if key == ord("q"):
        break

