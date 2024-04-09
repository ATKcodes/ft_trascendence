# Usa l'immagine di base di Python
FROM python:3.9

RUN pip install --upgrade pip

# Imposta la directory di lavoro
WORKDIR /app

# Copia il file requirements.txt nella directory di lavoro
COPY requirements.txt /app/

# Installa le dipendenze
RUN pip install -r requirements.txt

# Copia il resto del codice nella directory di lavoro
COPY . /app

# Imposta le variabili d'ambiente per Django
ENV DJANGO_SETTINGS_MODULE=trascendence.settings

# Avvia il server Django
CMD ["python3", "trascendence/manage.py", "runserver", "0.0.0.0:9000"]