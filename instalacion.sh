#!/bin/bash

echo "El instalador descargará e instalará las siguientes dependencias:"
# Array de dependencias
dependencies=("git" "pip" "python3-tkinter" "opencv-python" "python3-matplotlib" "python3-facenet-pytorch")
echo "Dependencias:"
# Recorrer el array de dependencias
for dependency in "${dependencies[@]}"; do
    echo "$dependency"
done
echo "La instalación puede demorar!"
read -p "¿Deseas ejecutar la instalacion? (si/no): " answer

# Verificar la respuesta del usuario
if [ "$answer" = "si" ]; then
    
    sudo apt update
    # Comando a ejecutar si la respuesta es "si"
    sudo apt install -y git python3-pip python3-tk
    pip install opencv-python matplotlib facenet-pytorch
    git clone https://github.com/bleussa-utn/srf.git
    echo "Instalacion Exitosa"
    read -p "¿Deseas iniciar el programa? (si/no): " run

    # Verificar la respuesta del usuario
    if [ "$run" = "si" ]; then
        python3 srf/Main.py
      
    else
        echo "Asistente de instalador finalizado"
    fi
else
    echo "Instalación Cancelada"
fi


