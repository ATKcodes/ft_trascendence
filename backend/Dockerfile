# Usa l'immagine di base di Python
FROM python:3.9

# Imposta la directory di lavoro
WORKDIR /app

# Copia il file requirements.txt nella directory di lavoro
COPY requirements.txt /app/

# Installa le dipendenze
RUN pip install -r requirements.txt

RUN -u postgres psql trascendence

RUN ALTER USER postgres with encrypted password 'your_password'

/etc/postgresql/*/main/pg_hba.conf (Devi aggiungere la riga host scritta sotto)
hostssl trascendence       postgres        192.168.122.1/24        scram-sha-256

RUN sudo systemctl restart postgresql.service

# Copia il resto del codice nella directory di lavoro
COPY . /app

# Imposta le variabili d'ambiente per Django
ENV DJANGO_SETTINGS_MODULE=trascendence.settings

# Avvia il server Django
CMD ["python3", "trascendence/manage.py", "runserver", "0.0.0.0:9000"]