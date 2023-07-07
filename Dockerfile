# Utiliza una imagen de Python como base
FROM python:3.6

# Establece el directorio de trabajo en /app
WORKDIR /app

# actualiza pip
RUN python -m pip install --upgrade pip

# Instala las bibliotecas necesarias
RUN pip install transformers sentencepiece
RUN pip install torch==1.8.1+cu101 -f https://download.pytorch.org/whl/cu101/torch_stable.html

# Copia tu código fuente al contenedor
COPY Traslada5.py .

# Ejecuta tu código Python Inglres -> Español
CMD ["python", "Traslada5.py"]

# Ejecuta tu código Python Español -> Inglres
#CMD ["python", "Traslada4.py"]