FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    gfortran \
    libblas-dev \
    liblapack-dev \
    && apt-get clean

# On crée un répertoire pour notre application
WORKDIR /app

# On copie le fichier requirements.txt dans le répertoire de travail
COPY requirements.txt /app

# On installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# On copie le reste des fichiers dans le répertoire de travail
COPY . /app

# On expose le port 8000
EXPOSE 8000

# Commande pour lancer l'application fastapi
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]