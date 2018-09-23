1.26 Web application security 101
=================================

Dodatkowe informacje
--------------------

Kod podatnej aplikacji można znaleźć pod: ![https://github.com/d0vine/pwnme-py](https://github.com/d0vine/pwnme-py)

Wprowadzenie
------------

Bezpieczeństwo aplikacji internetowych jest tematem, który od zarania dziejów - czyli powstania Internetu i koncepcji aplikacji internetowej ;-) - nie przestaje być aktualny. Można wręcz zaryzykować stwierdzenie, że zyskuje ono na znaczeniu - w dobie popularyzacji aplikacji mobilnych i przenoszenia infrastruktur do "chmury" cyberprzestępcy co raz częściej skupiają się na atakach właśnie na tym froncie. Porozmawiamy dziś trochę o tym, w jaki sposób takie ataki są dokonywan (zarówno od strony koncepcyjnej - począwszy od odpowiedniego sposobu myślenia - jak i technicznej), aby skupić się następnie na ochronie przed nimi.

Zaczynajmy!

Dlaczego powstają błędy bezpieczeństwa?
---------------------------------------

Najczęściej jest to spowodowane skupieniem na funkcjach aplikacji (ang. features) - na przykład w obliczu nadchodzącej wielkimi krokami publikacji produktu - lub pomyłkami programisty. Pomyłki te mogą oczywiście wynikać ze zmęczenia, przeoczenia lub nieznajomości tematu (biblioteki, frameworku); skupimy się dziś na tym ostatnim.

Złośliwi użytkownicy
--------------------

Zrozumienie, iż użytkownik może działać na niekorzyść aplikacji i/lub innych użytkowników jest fundamentalne dla programowania w "bezpieczny" sposób. W związku z tym, iż nie możemy ufać użytkownikom, wszystkie wysyłane przez nich dane - mogące stanowić "punkt wejścia" atakującego - powinny być w odpowiedni sposób weryfikowane i filtrowane.

Wygoda wrogiem bezpieczeństwa
-----------------------------

O ile będziemy dążyć do zwiększenia bezpieczeństwa naszych aplikacji, o tyle musimy pamiętać, iż nie należy robić tego za wszelką cenę. Próby zabezpieczenia aplikacji kosztem wygody użytkowników mogą zakończyć się ignorowaniem przez użytkowników zaleceń co do bezpiecznych praktyk, co z kolei spowoduje tylko i wyłącznie pogorszenie sytuacji.

Minimalizacja płaszczyzny ataku
-------------------------------

Powstrzymanie użytkownika przed wysłaniem złośliwych danych to nie wszystko. O ile znaczącą część "punktów wejścia" (tzw. *wektorów ataku*) możemy ochronić/powstrzymać sami, o tyle nadzwyczaj często korzystać będziemy z zewnętrznych bibliotek, narzędzi itd. W takim wypadku jedynym wyjściem jest minimalizacja zagrożenia - minimalizacja tzw. *płaszczyzny ataku*. Im mniej możliwości ataku (uzyskania dostępu, podwyższenia uprawnień, przejścia pomiędzy systemami itd.) tym bardziej zdeterminowany musi być atakujący aby wykorzystać luki znajdujące się w systemie.

Do minimalizacji płaszczyzny ataku możemy zastosować zarówno firewalle czy systemy kontroli dostępu (zarówno fizyczne jak i w oprogramowaniu [np. bazodanowym]) jak i odpowiednie konfiguracje systemu czy zewnętrznego oprogramowania.

Jak myśli atakujący aplikację?
------------------------------

Atakujących aplikacje możemy podzielić na dwie grupy: tych, którzy uruchamiają narzędzia "na ślepo" lub na bazie opisów innych (tzw. *script kiddies*) oraz tych, którzy rozumieją zasady którymi rządzą się atakowane aplikacje i systemy. Poza zrozumieniem tych zasad konieczne jest również wychodzenie poza utarte schematy - myślenie "a co, jeżeli..." jest kluczowe dla skutecznego testowania bezpieczeństwa.

OWASP TOP 10
------------

W obliczu zyskującej na popularności kwestii bezpieczeństwa aplikacji internetowych, w 2001 roku powstała organizacja OWASP - *The Open Web Application Security Project*. OWASP co roku definiuje 10 najpopularniejszych błędów wykrywanych w aplikacjach internetowych - tzw. *OWASP Top 10*.

Aktualnie owe podatności przedstawiają się w następujący sposób:

- A1:2017 - Injection 
- A2:2017 - Broken Authentication
- A3:2017 - Sensitive Data Exposure 
- A4:2017 - XML External Entities (XXE)
- A5:2017 - Broken Access Control
- A6:2017 - Security Misconfiguration
- A7:2017 - Cross-Site Scripting (XSS) 
- A8:2017 - Insecure Deserialization
- A9:2017 - Using Components with Known Vulnerabilities
- A10:2017 - Insufficient Logging & Monitoring

Jak się bronić?
---------------

Zdobycie dostępu do aplikacji jest z reguły kwestią czasu i determinacji atakującego - to co możemy zrobić, to spowolnić jego/jej działanie na opisane wcześniej sposoby. Możemy oczywiście odciąć maszynę od Internetu (#polecamy ;-) ), ale mija się to nieco z celem. Sposoby ochrony aplikacji przed zagrożeniami będziemy omawiać na przykładzie aplikacji stworzonej specjalnie pod te zajęcia.

Najczęstsze błędy bezpieczeństwa w aplikacjach Pythonowych
----------------------------------------------------------

O ile Python sam w sobie jest językiem stosunkowo bezpiecznym - nie uwzględniamy tutaj zewnętrznych bibliotek, które są chyba jedną z istotniejszych zalet tego języka - o tyle jest pewien zbiór funkcji/modułów, których należy unikać, ponieważ mogą one być potencjalnie niebezpieczne. Na komentarz *Funkcje, których chcemy unikać* należy oczywiście spojrzeć z przymrużeniem oka - możemy oczywiście ich używać, choć tylko i wyłącznie w uzasadnionych przypadkach.

### Deserializacja niezaufanych danych

Przez deserializację rozumiemy oczywiście załadowanie pewnej reprezentacji danych (np. tekstu/strumienia bajtów) do obiektu danego języka (w naszym wypadku obiektu pewnej klasy, słownika, tablicy itd.) - deserializację wykorzystywaliśmy gdy omawialiśmy format *JSON*. Deserializacja danych przez pickle/marshal (jest to alternatywna reprezentacja danych do omówionego już JSONa) może doprowadzić do wykonania kodu atakującego na serwerze ofiary. Jeśli tego rodzaju dane trzymamy po stronie klienta - na przykład w ciastkach - nie możemy również na nich polegać w kontekście kontroli dostępu, weryfikacji integralności itd.

Funkcje, których chcemy unikać: *pickle.dump(), pickle.dumps(), pickle.load(), pickle.loads(), marshal.\**, ...

### Wykonanie komendy użytkownika

O ile wydaje się to być naciągane, o tyle w pewnych zastosowaniach - na przykład w narzędziach administracyjnych routerów, czy aplikacjach wykonujących dodatkowe przetwarzanie w zewnętrznych aplikacjach - dane wysłane przez użytkownika wysyłane są wprost do systemu, na którym aplikacja działa. Jeśli nie zweryfikujemy tych danych, może dojść do wykonania dowolnego kodu - w tym złośliwego.

Funkcje, których należy unikać: *os.system(), subprocess.check_output(), ...*

### Konkatenacja niezaufanych danych

W przypadku zapytań SQL - lub, po raz kolejny, wykonywanych komend - konkatenacja danych wysłanych przez użytkownika może być brzemienna w skutkach. Przykładem takiego ataku może być wstrzyknięcie kodu SQL - *SQL Injection*.

Funkcje, których należy unikać: *brak* (zalecamy natomiast stosowanie ORMów lub wiązania zmiennych w SQL)

### eval() is evil

Próbując pozwolić użytkownikowi na nieco więcej wygody możemy ulec pokusie, by wysyłane dane wykonać w funkcji *eval*. Funkcja ta - poza wykonaniem *expressions* pokroju "1+2" czy "x+2" (gdzie *x* jest zmienną w scope funkcji *eval*), pozwala na wykonanie obiektów stworzonych poprzez *compile()*. Może pozwolić to na wykonanie dowolnej komendy systemowej, np.: *eval(compile('import subprocess; print(subprocess.check_output("ls"))', '', 'single'))* (co wylistuje zawartość katalogu z aplikacją).

O ile nie jest to częste, o tyle może to być pozostałością skryptu testowego w środowisku produkcyjnym (surprise, surprise ;P) - przypadki takie zdarzało się obserwować również w rozbudowanych aplikacjach znaczących klientów (ale ja o tym nie powiedziałem!).

Funkcje, których należy unikać: *eval(), exec()*

### Instalacja zewnętrznych paczek

O ile korzystanie z menedżerów paczek takich jak *pip* jest wygodne, o tyle wprowadza ono dodatkowe zagrożenie. Musimy pamiętać, że zewnętrzne paczki powinny zostać zweryfikowane pod kątem zawartego tam kodu - bądź co bądź to zarządzający paczką decyduje o tym, co się w niej znajdzie (np. złośliwy kod, który będzie wysyłał prywatne klucze SSH na zewnętrzny serwer [to jest akurat prawdziwy case]). Jeśli pomylimy się wpisując nazwę paczki - lub ktoś podmieni ją z premedytacją, działając na naszą niekorzyść - może dojść do instalacji paczki zawierającej złośliwy kod. Przykładem może być ![opisana tutaj sytuacja](https://www.bleepingcomputer.com/news/security/ten-malicious-libraries-found-on-pypi-python-package-index/).
