# 1.7 AWS - DynamoDB i boto3

## [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
NoSQLowa baza danych oferowana przez AWSa.

Kilka cech DynamoDB:
* pozwala na zagnieżdżenie danych (do 32 poziomów głębokości),
* nie trzeba definiować struktury poza kluczem,
* większość danych może mieć tylko 1 wartość (np. liczby, stringi),
* posiada GUI w AWSie, gdzie możemy dodawać/edytować/usuwać tabele i ich rekordy.

### Rodzaje danych
* **scalar** - reprezentujące 1 wartość (number, string, boolean, binary, null)
* **document** - bardziej złożona struktura z zagnieżdżonymi danymi (JSON)
* **set** - wiele wartości typu scalar

### Partition key i Sort key

Przy tworzeniu tabeli mamy dwie możliwości:
* tabela z partition key (wartości klucza muszą być unikalne),
* tabela z partition key i sort key.

W przypadku tabeli z partition key i sort key nie musimy mieć unikalnego partition key'a, jeśli sort key będzie unikalny.

Sort key jak nazwa mówi, sortuje nam kolejność rekordów w tabeli.

### Secondary Indexes

Indeksy umożliwiają nam odpytywać tabelę za pomocą alternatywnego klucza (jednego z pól w rekordzie).

Pozwala to nam na zmniejszenie łącznej ilości zapytań.

Rodzaje:
* Global secondary index - (i partition key i sort key mogą być inne)
* Local secondary index - (ma taki sam partition key ale inny sort key)

### Nazewnictwo

Domyślnie do konwencji nazw wykorzystywany jest camelCase. Możemy używać też nazw z podkreślnikiem.

Wspierane znaki w nazwach:
* `a-z`
* `A-Z`
* `0-9`
* `_`
* `-`
* `.`

**DynamoDB posiada też [zarezerwowane nazwy](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html) (wszystkie dużymi literami), których nie możemy używać.**

### Tryby odczytu/zapisu

#### On-Demand mode
Tryb pay-per-request - automatycznie skaluje nam potrzeby bazy danych na odczyt i zapis. Płacimy tylko za, to co wykorzystaliśmy.

Dobry wybór, jeśli oczekujemy nagłych peaków w zapytaniach do bazy i chcemy rozliczać się w łatwy sposób.

#### Provisioned Mode (domyślnie 5 jednostek na odczyt i 5 na zapis)
Z góry zdefiniowana ilość jednostek dla odczytu i zapisu. Zalecane kiedy jesteśmy w stanie przewidzieć obciążenie bazy i nie zdarzają się duże peaki w zapytaniach do bazy.

### Komendy
#### Tworzenie tabeli za pomocą AWS CLI
```
aws dynamodb create-table \
    --table-name Szkolenie \
    --attribute-definitions \
        AttributeName=Pracownik,AttributeType=S \
    --key-schema AttributeName=Pracownik,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1
```

#### Dodanie rekordu za pomocą AWS CLI
```
aws dynamodb put-item \
    --table-name Szkolenie \
    --item '{ \
        "Pracownik": {"S": "Jan Nowak"}, \
        "Stanowisko": {"S": "DevOps"}, \
        "Staz": {"N": 2} }' \
    --return-consumed-capacity TOTAL
```


## [Boto3](https://github.com/pyenv)
To biblioteka Pythonowa, która służy do komunikacji się z API AWSa. Za jej pomocą możemy używać zasobów AWSa (np. S3, EC2, DynamoDB, itd.)

W tej lekcji pokazane zostaną jedne z najpopularniejszych zastosowań. Sama biblioteka daje dostęp praktycznie do wszystkich zasobów AWSa.

### Uwierzytelnienie
Boto3 domyślnie korzysta z tych samych danych co AWS CLI (`~/.aws/credentials`).

Region można podać w konfiguracji lub w kodzie w trakcie tworzenia obiektu klienta:
```python
ssm_client = boto3.client('ssm', region_name="eu-west-1")
```

#### Kolejność sprawdzania danych dostępowych przez boto3
1. Dane przekazane jako parametry do metody boto.client()
2. Dane przekazane jako parametry przy tworzeniu obiektu Session
3. Zmienne środowiskowe
4. Plik używany przez AWS CLI (`~/.aws/credentials`)
5. Plik konfiguracyjny AWS (`~/.aws/config`)
6. Assume Role provider 
7. Plik konfiguracyjny Boto2 (`/etc/boto.cfg` i `~/.boto`)
8. Metadane instancji Amazon EC2, która ma skonfigurowaną rolę IAM.

### DynamoDB

#### Tworzenie tabeli

```python
import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName='Szkolenie',
    KeySchema=[
        {
            'AttributeName': 'Pracownik',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Pracownik',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
)

# Czekaj, aż tabela zostanie utworzona
table.meta.client.get_waiter('table_exists').wait(TableName='Szkolenie')

# Zwróci ilość rekordów w tabeli
print(table.item_count)
```

#### Tworzenie rekordu

```python
table.put_item(
   Item={
        'Pracownik': 'Jan Nowak',
        'Staz': 2,
    }
)
```

#### Wyciąganie rekordu

```python
response = table.get_item(
    Key={
        'Pracownik': 'Jan Nowak',
    }
)
item = response['Item']
print(item)
```

#### Aktualizowanie rekordu

```python
table.update_item(
    Key={
        'Pracownik': 'Jan Nowak',
    },
    UpdateExpression='SET staz = :val1',
    ExpressionAttributeValues={
        ':val1': 3
    }
)
```

#### [DynamORM](https://github.com/NerdWalletOSS/dynamorm)
Biblioteka pozwalająca na komunikację z DynamoDB poprzez ORM (Object & relation mapping).
Dodaje warstwę abstrakcji przy pracy z bazą. Ponad to możemy wykorzystać biblioteki [Marshmallow](https://marshmallow.readthedocs.io/en/latest/) i [Schematics](https://schematics.readthedocs.io/en/latest/) do walidacji danych.

### S3

#### Tworzenie bucketa

```python
s3_client = boto3.client('s3')
s3_client.create_bucket(Bucket="nazwa_bucketa")
```
lub w w konkretnym regionie:
```python
s3_client = boto3.client('s3', region_name="eu-west-1")
location = {'LocationConstraint': "eu-west-1"}
s3_client.create_bucket(Bucket="nazwa_bucketa",
                        CreateBucketConfiguration=location)
```

#### Wgrywanie pliku

```python
s3_client = boto3.client('s3')
response = s3_client.upload_file("nazwa_pliku", "bucket", "nazwa_obiektu_w_s3")
```
lub
```python
s3 = boto3.client('s3')
with open("nazwa_pliku", "rb") as f:
    s3.upload_fileobj(f, "bucket", "nazwa_obiektu_w_s3")
```

#### Pobieranie pliku

```python

s3 = boto3.client('s3')
s3.download_file("bucket", "nazwa_obiektu_w_s3", "nazwa_pliku")
```
lub
```python
s3 = boto3.client('s3')
with open('nazwa_pliku', 'wb') as f:
    s3.download_fileobj('bucket', 'nazwa_obiektu_w_s3', f)
```
#### Usuwanie pliku
```python
s3 = boto3.client('s3')
s3.delete_object("bucket", "nazwa_obiektu_w_s3")
```

### EC2

#### Wyciąganie informacji o instancjach

```python
import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)
```

#### Uruchamianie instancji

```python
response = ec2.start_instances(InstanceIds=["instance_id"], DryRun=False)
print(response)
```

#### Wyłączanie instancji

```python
response = ec2.stop_instances(InstanceIds=["instance_id"], DryRun=False)
print(response)
```

#### Reboot instancji

```python
response = ec2.reboot_instances(InstanceIds=["instance_id"], DryRun=False)
print(response)
```

### Parameter Store
Pozwala przechowywać sekrety i dane konfiguracyjne aplikacji. Dzięki ukośnikom możemy tworzyć zagnieżdżenia danych.

Wspierane typy:
* String
* StringList (lista oddzielana przecinkami)
* SecureString (szyfrowany string kluczem KMS)

#### Dodawanie parametrów

```python
client = boto3.client("ssm")
client.put_parameter(Name="/moj_parametr", Value="hello world", Type="string")
```

#### Pobieranie parametrów

```python
response = client.get_parameter(
    Name='/moj_parametr',
    WithDecryption=True
)
```

#### Usuwanie parametrów

```python
response = client.delete_parameter(
    Name='/moj_parameter'
)
```

#### [SSM Parameter Store](https://github.com/christippett/ssm-parameter-store) wrapper

Wrapper, który pozwala na wyciąganie danych z Parameter Store'a w formie słownika. Pod spodem używa boto3.

```python
parameters = store.get_parameters_with_hierarchy('/dev/')

assert parameters == {
    'app': {
        'secret': 'dev_secret',
    },
    'db': {
        'postgres_username': 'dev_username',
        'postgres_password': 'dev_password',
    },
}
```