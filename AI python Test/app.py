from flask import Flask, render_template, request, redirect
import csv

# Crea il file CSV e aggiungi l'intestazione, se non esiste
def crea_csv():
    try:
        with open('inserimenti.csv', mode='r'):
            pass  # Il file esiste già
    except FileNotFoundError:
        with open('inserimenti.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['genere', 'anni', 'videogame'])  # Scrive l'intestazione

# Assicurati che il file CSV sia creato quando si avvia l'app
crea_csv()


app = Flask(__name__)

# Funzione per scrivere i dati nel CSV
def aggiungi_al_csv(genere, anni, videogame):
    with open('inserimenti.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([genere, anni, videogame])

# Route per la pagina principale
@app.route('/')
def index():
    return render_template('index.html')

# Route per gestire il form
@app.route('/invia', methods=['POST'])
def invia_dati():
    if request.method == 'POST':
        genere = request.form['genere']
        anni = request.form['anni']
        videogame = request.form['videogame']

        # Aggiungi i dati al CSV
        aggiungi_al_csv(genere, anni, videogame)

        # Dopo aver inserito, redirigi alla homepage
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
