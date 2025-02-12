ft_transcendence

Benvenuto nel progetto Transcendence! Questo progetto rappresenta un sito web per un torneo dei classici giochi **Pong** e **Tris**. L'obiettivo è sviluppare un'esperienza utente coinvolgente, con funzionalità avanzate come il multiplayer in tempo reale, la gestione degli utenti, la sicurezza e molto altro.

## 📜 **Panoramica del Progetto**

Il progetto è diviso in due parti principali:
1. **Parte Obbligatoria**: Abbiamo creato un sito web che permetta agli utenti di giocare a Pong in tempo reale, con un'interfaccia utente intuitiva e funzionalità di base come la registrazione degli utenti e la gestione dei tornei.
2. **Moduli Opzionali**: Una volta completata la parte obbligatoria, potevamo scegliere tra diversi moduli per migliorare il progetto, come l'integrazione di un backend con framework avanzati, l'aggiunta di un avversario AI, e molto altro.

## 📸 **Screenshot del Sito**
Di seguito sono riportati alcuni screenshot delle principali funzionalità del sito:

## 📸 **Screenshot del Sito**
Di seguito sono riportati alcuni screenshot delle principali funzionalità del sito:

### Homepage: 
![Homepage](screenshots/main-page.png)
La pagina principale, con un menu a tendina per gestire gli amici e muoversi agilmente nel sito

### Pagina di Accesso:
![Login](screenshots/pong.png)
Una semplice interfaccia per l'autenticazione degli utenti esistenti.

### Pagina di Registrazione:
![Register](screenshots/register.png)
Un modulo di registrazione intuitivo che permette ai nuovi utenti di creare un account.

### Partita in Corso: 
![4 Player Game](screenshots/game-vs-Ia.png)
Una schermata di gioco in tempo reale di Pong, con i punteggi aggiornati in tempo reale, e nella modalita 4 giocatori.

## 🛠️ **Tecnologie e Requisiti**

- **Frontend**: Vanilla JavaScript.
- **Backend**: Django.
- **Database**: PostgreSQL.
- **Containerizzazione**: Docker per eseguire il progetto in un ambiente autonomo.
- **Sicurezza**: Implementazione di HTTPS, protezione contro SQL injection/XSS, e hashing delle password.

## 🎮 **Funzionalità Principali**

- **Gioco in Tempo Reale**: Gli utenti possono giocare a Pong contro altri giocatori in tempo reale, con la possibilità di organizzare tornei.
- **Matchmaking**: Un sistema di matchmaking automatico per organizzare le partite tra i giocatori.
- **Gestione Utenti**: Registrazione, autenticazione e profili utente con statistiche di gioco.
- **Sicurezza**: Implementazione di best practice per la sicurezza, come l'uso di HTTPS, hashing delle password e protezione contro attacchi comuni.

## 🚀 **Moduli Opzionali**

Per raggiungere il 100% del progetto, è necessario implementare almeno **7 moduli principali**. Ecco alcuni esempi di moduli disponibili:
- **Web**: Utilizzo del framework Django per il backend.
- **User Management**: Gestione avanzata degli utenti con autenticazione OAuth 2.0.
- **Gameplay**: Aggiunta di funzionalità come multiplayer con più di 2 giocatori.
- **AI-Algo**: Introduzione di un avversario AI con comportamenti realistici.

## 📂 **Come Avviare il progetto**

1. Clona il repository:
   ```bash
   git clone https://github.com/dmax96/ft_transcendence.git
   ```
2. Esegui il progetto con il MakeFile:
   ```bash
   Make Up
   ```
3. Collegati al sito con la seguente porta:
    ```bash
    https://localhost:8443
   ```
Per cancellare tutte le dockerizzazioni puoi usare Make Down
