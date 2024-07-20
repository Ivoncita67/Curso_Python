import os
import subprocess

# Função para criar diretórios
def create_dirs():
    dirs = [
        "data/train/images", "data/train/labels",
        "data/val/images", "data/val/labels"
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)

# Função para criar o arquivo data.yaml
def create_data_yaml():
    data_yaml_content = """
    train: ../data/train/images
    val: ../data/val/images

    nc: 2  # Número de classes
    names: ['classe1', 'classe2']  # Nomes das classes
    """
    with open('data.yaml', 'w') as file:
        file.write(data_yaml_content)

# Função para instalar bibliotecas necessárias
def install_dependencies():
    subprocess.run(["pip", "install", "torch", "torchvision", "torchaudio"])
    subprocess.run(["pip", "install", "opencv-python-headless", "numpy", "pandas", "matplotlib"])
    subprocess.run(["pip", "install", "-r", "requirements.txt"])

# Função para clonar o repositório YOLOv5
def clone_yolov5_repo():
    subprocess.run(["git", "clone", "https://github.com/ultralytics/yolov5"])
    os.chdir('yolov5')

# Função para treinar o modelo
def train_model():
    subprocess.run(["python", "train.py", "--img", "640", "--batch", "16", "--epochs", "50", "--data", "../data.yaml", "--cfg", "models/yolov5s.yaml", "--weights", "yolov5s.pt"])

# Função para avaliar o modelo
def evaluate_model():
    subprocess.run(["python", "val.py", "--data", "../data.yaml", "--weights", "runs/train/exp/weights/best.pt"])

# Função para exportar o modelo
def export_model():
    subprocess.run(["python", "export.py", "--weights", "runs/train/exp/weights/best.pt", "--img", "640", "--batch", "1"])

# Função principal para executar todas as etapas
def main():
    # Etapa 1: Instalar bibliotecas necessárias
    install_dependencies()

    # Etapa 2: Clonar repositório YOLOv5
    clone_yolov5_repo()

    # Etapa 3: Criar diretórios de dados
    create_dirs()

    # Etapa 4: Criar arquivo data.yaml
    create_data_yaml()

    # Etapa 5: Treinar o modelo
    train_model()

    # Etapa 6: Avaliar o modelo
    evaluate_model()

    # Etapa 7: Exportar o modelo
    export_model()

# Executar função principal
if __name__ == "__main__":
    main()
