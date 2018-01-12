1.10 Powtórka
=============

1. Próbujemy zrobić zadania w domu.
2. W czasie zajęć rozwiązujemy je wspólnie po kolei.

Informacje pomocnicze
---------------------

### Backend do zadania Cezar.com

    :::python
    from flask import Flask, request, render_template, redirect

    app = Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def cezar_handler():
        if request.method == 'POST':
            pass # tu dodaj obsluge "szyfrowania"
            
        return render_template('cezar.html')

    app.run(debug=True)

### Szablon do zadania Cezar.com

    :::html
    <!DOCTYPE HTML>
    <html lang="pl">
        <head>
            <meta charset="UTF-8">
            <title>Szyfr Cezara</title>
        </head>
        <body>
            <h1>Szyfr Cezara</h1>
            <form method="post">
                <table>
                    <tr>
                        <td><b>Tekst</b></td>
                        <td><textarea name="text"></textarea></td>
                    </tr>
                    <tr>
                        <td><b>Przesunięcie</b></td>
                        <td><input type="number" name="offset" value="0"/></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td align="right"><button type="submit">Szyfruj</button></td>
                    </tr>
                </table>
                <br/><br/>
                {% if encrypted_text %}
                <table>
                    <tr>
                        <td><b>Zaszyfrowane:</b></td>
                        <td><p>{{ encrypted_text }}</p></td>
                    </tr>
                </table>
                {% endif %}
            </form>
        </body>
    </html>
