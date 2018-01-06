1.9 Aplikacje internetowe - powtórka
====================================

POST - Redirect - GET
---------------------

Poniżej znajduje się kod prostej aplikacji służącej do tworzenia listy zadań.
Zawiera jedną stronę, która umożliwia dodanie nowego zadania i wyświetla już listę zadań już utworzonych.

### Szablon (templates/zadania.html)

    :::html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Lista zadań</title>
    </head>
    <body>
        <h1>Lista zadań</h1>
        {% if zadania %}
            <ul>
                {% for zadanie in zadania %}
                    <li>{{ zadanie }}</li>
                {% endfor %}
            </ul>
        {% else %}
            Brak zadań
        {% endif %}
    
        <br><br>
        <form method="post">
            Nowe zadanie
            <input type="text" name="zadanie">
            <button type="submit">Dodaj</button>
        </form>
    </body>
    </html>

### Backend

    :::python
    from flask import Flask, request, render_template
    
    app = Flask(__name__)
    
    zadania = []
    
    @app.route("/zadania", methods=['GET', 'POST'])
    def lista_zespolow():
        if request.method == 'POST':
            zadania.append(request.form['zadanie'])
    
        return render_template('zadania.html', zadania=zadania)
    
    app.run(debug=True)

Powyższa aplikacja ma pewnien problem - jeśi użytkownik doda nowe zadanie, a następnie odświeży stronę,
zobaczy komunikat z pytaniem typu "Czy na pewno chcesz ponownie przesłać formularz?".
Jeśli użytkownik odpowie "Tak", przeglądarka wykona ponownie zapytanie POST w wyniku którego otrzymała od serwera listę zadań,
co spowoduje dodanie jeszcze raz tego samego zadania. Aby tego uniknąć należy zastosować tzw. wzorzec projektowy
"POST - Redirect - GET", a więc w odpowiedzi na zapytanie POST zwrócić przekierowanie na ten sam adres.
Wtedy przeglądarka po przesłaniu formularza zapytaniem POST wykona zapytanie GET, w wyniku którego dostanie listę zadań.
Wówczas użytkownik będzie mógł odświeżać stronę bez ryzyka ponownego wykonania tej samej operacji na danych po stronie serwera.

### Poprawiony backend

    :::python
    from flask import Flask, request, render_template, redirect
    
    app = Flask(__name__)
    
    zadania = []
    
    @app.route('/zadania', methods=['GET', 'POST'])
    def lista_zespolow():
        if request.method == 'POST':
            zadania.append(request.form['zadanie'])
            return redirect('/zadania')
    
        return render_template('zadania.html', zadania=zadania)
    
    app.run(debug=True)
