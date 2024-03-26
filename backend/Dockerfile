# Usa l'immagine di base di Python
FROM python:3.9

# Imposta la directory di lavoro
WORKDIR /app

# Copia il file Pipfile e Pipfile.lock nella directory di lavoro
COPY Pipfile Pipfile.lock /app/

# Installa le dipendenze
RUN pip install pipenv
RUN pip install django
RUN pipenv install --system --deploy

# Copia il resto del codice nella directory di lavoro
COPY . /app

# Imposta le variabili d'ambiente per Django
ENV DJANGO_SETTINGS_MODULE=trascendence.settings

# Avvia il server Django
CMD ["python3", "trascendence/manage.py", "runserver", "0.0.0.0:9000"]