
# Import packages

import os
import subprocess
import sys

FOLDERS = [
    "data/raw.nosync",         # Unveränderte Originaldaten
    "data/_archive",   # Archivierte Daten
    "scripts",        # Jupyter Notebooks and other scripts
    "scripts/models",           # Abgespeicherte Modelle
    "scripts/figures",             # Exportierte Grafiken und Visualisierungen
    "scripts/_archive"  ,        # Archivierte Notebooks
    "presentations"            # Wiederverwendbarer Python-Code (Skripte, Module)
]

def create_folders():
    for folder in FOLDERS:
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, ".gitkeep"), "w") as f:
            pass

def create_venv():
    venv_dir = "venv"
    try:
        subprocess.run([sys.executable, "-m", "venv", venv_dir], check=True)
    except subprocess.CalledProcessError as e:
        print(f"! Fehler beim Erstellen des venv: {e}")
        sys.exit(1)

def create_requirements():
    requirements_content = """\
pandas
numpy
matplotlib
seaborn
scikit-learn
jupyterlab
ipykernel
kagglehub[pandas-datasets] 
google-cloud-bigquery[pandas]
"""
    with open("requirements.txt", "w", encoding="utf-8") as f:
        f.write(requirements_content)



def install_packages_from_requirements():    
    # Pfad zum pip-Executable innerhalb des venv bestimmen
    if os.name == "nt":  # Windows
        pip_path = os.path.join("venv", "Scripts", "pip")
    else:  # macOS / Linux
        pip_path = os.path.join("venv", "bin", "pip")
        
    try:
        # Upgrade pip zuerst
        subprocess.run([pip_path, "install", "--upgrade", "pip"], check=True)
        # Installiere die Pakete aus der Datei
        subprocess.run([pip_path, "install", "-r", "requirements.txt"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Fehler bei der Paketinstallation: {e}")
        sys.exit(1)

def register_jupyter_kernel():    
    # Pfad zu Python innerhalb des venv bestimmen
    if os.name == "nt":
        python_path = os.path.join("venv", "Scripts", "python")
    else:
        python_path = os.path.join("venv", "bin", "python")
        
    # Projektname aus dem aktuellen Ordnernamen generieren
    project_name = os.path.basename(os.getcwd())
    
    try:
        # Registriert das venv in Jupyter unter dem Namen des Projektordners
        subprocess.run([
            python_path, "-m", "ipykernel", "install", 
            "--user", f"--name={project_name}", f"--display-name=Python ({project_name})"
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Kernel-Registrierung fehlgeschlagen: {e}")

if __name__ == "__main__":
    print("=== Starte automatischen Data Science Project Setup ===")
    create_folders()
    create_venv()
    install_packages_from_requirements()
    register_jupyter_kernel()
    
    # Startanleitung ausgeben
    if os.name == "nt":  # Windows
        print("👉 Starte JupyterLab mit: venv\\Scripts\\jupyter-lab")
    else:  # macOS / Linux
        print("👉 Starte JupyterLab mit: ./venv/bin/jupyter-lab")


