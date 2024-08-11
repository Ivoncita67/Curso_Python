import serial
import time
import speech_recognition as sr

# Configuração da porta serial
arduino = serial.Serial('COM3', 9600)  # Certifique-se de que a porta está correta
time.sleep(2)  # Tempo para estabilizar a conexão

# Inicializa o reconhecimento de voz
recognizer = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Diga um comando...")
        audio = recognizer.listen(source)

        try:
            comando = recognizer.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {comando}")

            if "ligar luz" in comando.lower():
                arduino.write(b'L')
                print("Luz ligada")
            elif "desligar luz" in comando.lower():
                arduino.write(b'D')
                print("Luz desligada")

        except sr.UnknownValueError:
            print("Não entendi o que você disse.")
        except sr.RequestError:
            print("Erro ao tentar se comunicar com o serviço de reconhecimento de voz.")

# Fechar a conexão
arduino.close()
