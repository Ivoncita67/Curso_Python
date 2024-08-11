import cv2
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Carrega o classificador de face pré-treinado
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Captura de vídeo da webcam
cap = cv2.VideoCapture(0)

while True:
    # Captura frame por frame
    ret, frame = cap.read()
    
    # Converte para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detecção de faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    # Desenha um retângulo ao redor das faces detectadas
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Exibe o resultado
    cv2.imshow('Face Detection', frame)
    
    # Encerra a captura ao pressionar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a captura e fecha as janelas
cap.release()
cv2.destroyAllWindows()


# Definição do modelo
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid')  # Supondo reconhecimento binário
])

# Compilação do modelo
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Supondo que você já tenha o conjunto de dados pronto para treinamento
# X_train, y_train, X_test, y_test = ...  # Carregar seus dados aqui

# Treinamento
# model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Redimensiona a face detectada e faz a predição
for (x, y, w, h) in faces:
    face = frame[y:y+h, x:x+w]
    face = cv2.resize(face, (64, 64))
    face = face / 255.0  # Normalização
    face = face.reshape(1, 64, 64, 3)
    
    # Predição
    prediction = model.predict(face)
    
    if prediction > 0.5:
        label = 'Pessoa 1'
    else:
        label = 'Pessoa 2'
    
    cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('Face Recognition', frame)