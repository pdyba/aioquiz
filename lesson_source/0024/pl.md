# 1.7 AWS - Lambda

## [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)

AWS-owa platforma do tworzenia aplikacji typu serverless.

Zalety serverless:

- Brak konieczności zarządzania serwerami, aktualizowania ich itp.
- Bardzo łatwe skalowanie
- Opłata tylko za wykorzystane zasoby
- Łatwość developmentu i deploymentu

Lambda może zostać uruchomiona na wiele różnych sposobów:

- Kliknięcie "Test" w konsoli AWS
- Wykonanie operacji Invoke przez API AWS (np. przez AWS CLI albo kod innej aplikacji)
- Zapytanie do API Gateway
- Eventy z kolejki SQS
- Upload pliku do S3
- Zmiany w DynamoDB
- ... i wiele innych

Języki programowania dostępne w Lambdzie:

- Python
- Node.js
- Java
- C#
- Go
- Ruby
- można utworzyć własny runtime

### Lambda handler

Punktem wejścia do każdej lambdy jest jedna funkcja, tzw. handler. Przykładowy handler w Pythonie:

```python
def handler(event, context):
    return do_something(event["value"])
```

Handler przyjmuje dwa argumenty:

- `event` - dane o zdarzeniu, które wywołało funkcję. Czasami sami go definiujemy (np. jeśli
  wykonujemy operację Invoke przez API), czasami AWS robi to dla nas (np. odpalenie przez API GW).
  Najczęściej jest to pythonowy dict.
- `context` - obiekt zawierający dodatkowe informacje typu nazwa lambdy lub request ID. W praktyce
  rzadko używany.

W konfiguracji Lambdy podajemy pełną ścieżkę do handlera - np. jeśli powyższa funkcja jest w pliku
`app.py`, to jako handler podajemy `app.handler`.

#### Dependencies

Jeśli nasza aplikacja posiada zależności (np. bibliotekę `requests`), trzeba je dostarczyć razem
z kodem w postaci paczki `zip`. Przykładowa procedura generowania paczki:

```shell
mkdir dist
pip install requests -t dist
cp app.py dist/
cd dist
zip -r ../dist.zip *
```

### Podstawowe opcje konfiguracyjne

- Rola IAM - definiuje, co jakie operacje w AWS mogą zostać wykonane przez Lambdę. Każda Lambda
  powinna mieć prawo pisania logów do CloudWatcha
- Timeout - domyślnie 3 sekundy, max 15 minut
- RAM - oprócz przydzielonej pamięci wpływa również na moc procesora. Zwiększenie RAMu może
  potencjalnie zmniejszyć kosz odpalenia Lambdy
- Zmienne środowiskowe

### Pricing

Koszt korzystania z Lambdy jest liczony jako suma dwóch składowych:

- opłata za ilość wywołań
- opłata za czas obliczeń (naliczanie milisekundowe), stawka zależy od przydzielonego RAMu

### Wady / ograniczenia Lambdy

- Cold start - pierwsze uruchomienie Lambdy jest znacząco wolniejsze (nawet kilka sekund
  w zależności od języka). Po pierwszym wywołaniu Lambda przez jakiś czas jest "gorąca", ale
  po pewnym czasie wraca do stanu "zimnego".
- Ograniczenia niektórych integracji (np. SQS - Lambda może przetworzyć max 10 eventów jednocześnie).
- Potencjalnie wyższe opłaty niż za np. kontenery / VM.

### Layery

Lambda posiada kilka innych ograniczeń:

- Limit na paczkę z kodem - 50 MB
- Brak możliwości instalowania paczek systemowych

Te problemy można rozwiązać korzystając z layerów - customowych fragmentów systemu plików, które
można dodać do Lambdy. W layerze mogą znaleźć się dowolne pliki, np. paczki pythonowe albo pliki
binarne.
