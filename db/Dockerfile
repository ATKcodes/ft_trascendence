# Utilizza l'immagine ufficiale di Postgres
FROM postgres:13

# Imposta le variabili d'ambiente per il nome del database e l'utente
ENV POSTGRES_DB=mydatabase
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword

# Espone la porta 5432 per permettere le connessioni al database
EXPOSE 5432

# Imposta il comando di default per l'esecuzione del container
CMD ["postgres"]