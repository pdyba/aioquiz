#!/usr/bin/env python3.5
# encoding: utf-8


class EmailData:
    recipients = '...'
    subject = '...'
    text = "..."
    per_user = False

    @classmethod
    def to_dict(cls):
        return {
            'subject': cls.subject,
            'text': cls.text,
            'email_type': cls.__name__,
            'recipients': cls.recipients,
            'per_user': cls.per_user
        }


class Accepted(EmailData):
    per_user = True
    recipients = 'accepted'
    subject = 'Zostałaś przyjęta/przyjęty na warsztaty PyLove.org'
    text = '''Cześć {name}!
    Z przyjemnością informujemy, że Twoje zgłoszenie na warsztat weekendowy PyLove.org w Poznaniu zostało zaakceptowane.
    Przypominamy, że wydarzenie odbędzie się w dniach 23-24 września 2017 r. (sobota-niedziela).

    Przypominamy, że bardzo ważnym warunkiem uczestnictwa jest przyniesienie własnego sprawnego laptopa z ładowarką oraz wcześniej zainstalowanym środowiskiem (Python 3.6.2 oraz PyCharm).
    Instalację wspierają nasi mentorzy na wydarzeniu Facebookowym.
    Oczekujemy od Ciebie potwierdzenia, że weźmiesz udział w warsztatach. Musisz kliknąć w link poniżej lub skopiować go i wkleić w pasek przeglądarki (link jest jednorazowego użycia).

    UWAGA, TEJ OPERACJI NIE MOŻNA COFNĄĆ!
    {link_yes}

    Jeżeli jednak nie możesz dotrzeć, kliknij proszę lub skopiuj link poniżej:

    UWAGA, TEJ OPERACJI NIE MOŻNA COFNĄĆ!
    {link_no}


    Masz 72 godziny na potwierdzenie swojego uczestnictwa w warsztacie. W przypadku braku odpowiedzi - na Twoje miejsce przydzielimy osobę z listy rezerwowej.
    Jeżeli wiesz, że nie możesz skorzystać z warsztatu, również prosimy o informację zwrotną.

    Zapraszamy do obserwowania naszego profilu Facebooku:
    https://www.facebook.com/PyLoveOrg

    Pozdrawiamy,
    PyLove.org Team'''


class Rejected(EmailData):
    per_user = True
    recipients = 'rejected'
    subject = 'Jesteś na liście rezerwowej - warsztaty PyLove.org'
    text = '''Cześć {name}!
    Ponownie dziękujemy za rejestrację na warsztat weekendowy PyLove.org w Poznaniu w dniach 23-24 września.
    Niestety, z uwagi na dużą ilość zgłoszeń Twoja aplikacja trafiła na listę rezerwową. Nie możemy w tej chwili zapewnić Ci miejsca na zajęciach.
    Jak tylko zwolni się miejsce, niezwłocznie Cię o tym poinformujemy.
    Otrzymasz maila w tej sprawie 17 września.

    Zapraszamy do obserwowania naszego profilu Facebooku:
    https://www.facebook.com/PyLoveOrg

    Pozdrawiamy,
    PyLove.org Team'''


class Reminder(EmailData):
    per_user = True
    recipients = 'accepted_noans'
    subject = 'Potwierdź swój udział w warsztatach PyLove.org'
    text = '''Cześć {name}!
    Czy pamiętacie o pilnej konieczności potwierdzenia swojego udziału w warsztacie weekendowym PyLove.org w Poznaniu, 23-24 września?
    Jeżeli jeszcze tego nie zrobiliście - czekamy.
    Aby potwierdzić swój udział, kliknij w link poniżej lub skopiuj go i wklej w pasek przeglądarki (link jest jednorazowego użycia).

    UWAGA, TEJ OPERACJI NIE MOŻNA COFNĄĆ!
    {link_yes}

    Jeżeli jednak nie możesz dotrzeć, kliknij proszę lub skopiuj link poniżej:

    UWAGA, TEJ OPERACJI NIE MOŻNA COFNĄĆ!
    {link_no}

    Przypominamy, że bardzo ważnym warunkiem uczestnictwa jest przyniesienie własnego sprawnego laptopa z ładowarką oraz wcześniej zainstalowanym środowiskiem (Python 3.6.2 i wybrany edytor tekstu).
    Instalację wspierają nasi mentorzy na wydarzeniu Facebookowym.

    Masz 72 godziny od poprzedniego maila na potwierdzenie swojego uczestnictwa w warsztacie.
    W przypadku braku odpowiedzi - na Twoje miejsce przydzielimy osobę z listy rezerwowej. Jeżeli wiesz, że nie możesz skorzystać z warsztatu, również prosimy o informację zwrotną.


    Zapraszamy do obserwowania naszego profilu Facebooku:
    https://www.facebook.com/PyLoveOrg

    Pozdrawiamy,
    PyLove.org Team'''


class TooLate(EmailData):
    per_user = True
    recipients = 'accepted_noans'
    subject = 'Dziękujemy za zainteresowanie warsztatami PyLove.org'
    text = '''Cześć {name}!
    Przykro nam, że nie zobaczymy się na warsztacie weekendowym PyLove.org 23-24 września!
    Nie wpłynęło do nas Twoje potwierdzenie udziału, ale wierzymy, że mimo to Twoje zainteresowanie programowaniem przerodzi się wkrótce w pasję.

    Zapraszamy do obserwowania naszego profilu Facebooku:
    https://www.facebook.com/PyLoveOrg

    Jeszcze raz dziękujemy za zainteresowanie i rejestrację!

    Pozdrawiamy,
    PyLove.org Team'''


class SecondChance(EmailData):
    per_user = True
    recipients = 'accepted_noans'
    subject = 'Zostałaś przyjęta/przyjęty na warsztaty PyLove.org'
    text = '''Cześć {name}!
    Miło nam zawiadomić, że zwolniły się miejsca na liście uczestników warsztatu weekendowego PyLove.org, na który aplikowałaś/aplikowałeś!
    Na pewno nadal masz ochotę na wzięcie udziału w tym fajnym wydarzeniu.
    Zapraszamy zatem!

    Aby potwierdzić swój udział, kliknij w link poniżej lub skopiuj go i wklej w pasek przeglądarki (link jest jednorazowego użycia).

    UWAGA, TEJ OPERACJI NIE MOŻNA COFNĄĆ!
    {link_yes}

    Jeżeli jednak nie możesz dotrzeć, kliknij proszę lub skopiuj link poniżej:

    UWAGA, TEJ OPERACJI NIE MOŻNA COFNĄĆ!
    {link_no}

    Przypominamy, że bardzo ważnym warunkiem uczestnictwa jest przyniesienie własnego sprawnego laptopa z ładowarką oraz wcześniej zainstalowanym środowiskiem (Python 3.6.2 i wybrany edytor tekstu).
    Instalację wspierają nasi mentorzy na wydarzeniu Facebookowym.

    Masz 24 godziny na potwierdzenie swojego uczestnictwa w warsztacie. W przypadku braku odpowiedzi - na Twoje miejsce przydzielimy inną osobę z listy rezerwowej.
    Jeśli wiesz, że nie możesz skorzystać z warsztatu, również prosimy o informację zwrotną.


    Zapraszamy do obserwowania naszego profilu Facebooku:
    https://www.facebook.com/PyLoveOrg

    Pozdrawiamy,
    PyLove.org Team'''


class Custom(EmailData):
    subject = 'PyLove: '
    text = """Cześć!

    W razie pytań, pisz do nas na Facebooku:
    https://www.facebook.com/PyLoveOrg

    Do zobaczenia za tydzień!
    PyLove.org Team
    """
    recipients = "all"


class WorkshopInfo(EmailData):
    recipients = 'confirmed'
    subject = 'Najważniejsze informacje przed warsztatem PyLove.org'
    text = '''Cześć!

    Bardzo się cieszymy, że będziesz z nami na PyLove.org! Widzimy się już w najbliższą sobotę! Poniżej znajdziesz wszystkie najważniejsze informacje - zapoznaj się z nimi przed warsztatami.

    Miejsce warsztatów: Międzynarodowe Targi Poznańskie, Pawilon 14, wejście B

    Mapkę z zaznaczonym miejscem warsztatów znajdziesz na: https://pylove.org/#/agenda

    Skrócony plan warsztatów:

        23.09.2017 SOBOTA
        8:15 Otwarcie bramek w MTP Wejście Wschodnie (ul. Roosevelta)
        8:15 – 8:45 Rejestracja uczestników w Pawilonie 14, wejście B
        9:00 – 18:00 Warsztaty
        19:00 – 22:00 Afterparty w Tandem Pub (ul. Gwarna 9)

        24.09.2017 NIEDZIELA
        8:30 Otwarcie bramek - MTP Wejście Wschodnie (ul. Roosevelta)
        9:00-18:00 Warsztaty

    Pełną agendę warsztatów znajdziesz na: https://pylove.org/#/agenda

    WAŻNE!

    PIERWSZEGO DNIA PRZYJDŹ PRĘDZEJ – potrzebujemy czasu, by wręczyć Ci pakiet rejestracyjny, odłożyć Twoje przekąski na szwedzki stół, podłączyć Twój komputer do zasilania i sprawdzić czy wszystko jest OK :)

    ZAINSTALUJ PYTHONA I PYCHARM IDE - Uprzednia instalacja Pythona i PyCharm IDE zapewni gładki start i szybsze przejście do głównych treści warsztatu. Instrukcje instalacji znajdziesz tu: https://pylove.org/#/agenda

    PAMIĘTAJ, BY PRZYNIEŚĆ PRZEDŁUŻACZ ORAZ ZADEKLAROWANE PRZEKĄSKI - my zapewnimy do picia wodę, kawę oraz herbatę. Ty deklarowałaś/deklarowałeś, że przyniesiesz: {what_can_you_bring}

    NIE ZAPOMNIJ IDENTYFIKATORA – wręczymy Ci go podczas rejestracji. Wyjście podczas trwania warsztatów z terenów MTP oraz ponowne wejście na podstawie otrzymanego identyfikatora na hasło PyLove.org. Identyfikator zabierz też na afterparty - upoważni Cię on do 20% zniżki w Tandem Pub!

    JESTEŚ NA KÓŁKACH? Jeśli chcesz przyjechać własnym samochodem i zaparkować go na terenie MTP to całodzienny pobyt kosztuje 20 zł, dostępność miejsc parkingowych można uzyskać na bramkach przy wjeździe od ul. Śniadeckich.

    POTRZEBUJESZ POMOCY? Jeśli jesteś osobą z ograniczeniami ruchowymi (lub po prostu potrzebujesz pomocy), to napisz do Weroniki (Weronikapylove.org) –  ona postara się, by wszystko było dla Ciebie gotowe, ponieważ obiekt jest dostosowany do osób na z ograniczeniami ruchowymi.

    W razie pytań, pisz do nas na Facebooku:
    https://www.facebook.com/PyLoveOrg

    Do zobaczenia!
    PyLove.org Team
    '''


class UserFeedback(EmailData):
    recipients = 'confirmed'
    subject = 'Feedback dla PyLove.org'
    text = '''Cześć!

Warsztaty PyLove.org dobiegły końca... Bardzo chcielibyśmy dostać Twój feedback, żeby wiedzieć co ulepszyć przy okazji następnej edycji!

Wejdź proszę tutaj: https://goo.gl/forms/XbtGgW8MEnZ8TaPT2 i wypełnij tę bardzo krótką ankietę - zrób to tak szybko, jak tylko możesz, byś miała/miał jeszcze świeże wspomnienia z warsztatów :)

Z góry bardzo dziękujemy!
PyLove.org Team
    '''


class PyLoveMeetings(EmailData):
    recipients = 'confirmed'
    subject = 'Ruszamy z kontynuacją PyLove.org!'
    text = """Hej!
Zapraszamy wszystkie osoby, które brały udział w warsztacie weekendowym oraz pozostałe, które chcą dołączyć do uczestnictwa w spotkaniach będących kontynuacją warsztatów PyLove.org

Pierwsze spotkanie PyLove z grupą "continued" odbędzie się 17.10 w Collegium Da Vinci przy ulicy Kutrzeby 10 w Poznaniu.

Na pierwszych zajęciach czeka Was przede wszystkim powtóreczka materiału przerobionego podczas warsztatów PyLove.org.

CO JEST POTRZEBNE?
Znajomość i umiejętność zastosowania w praktyce:
- def, for, while, if, elif, else, print, return, import
- umiejętność posługiwania się: stringami, listami, słownikami, tuplami
- umiejętność samodzielnego kodowania niezbyt skomplikowanych zadań
- zainstalowany Python 3.4+ (3.5 lub 3.6 (https://www.python.org/downloads/)
- PyCharm
- NAŁADOWANY laptop - prąd i garść przedłużaczy mamy, ale gniazd dla każdego oczywiście nie starczy
- dowolny sposób prezentacji swojego imienia, aby mentor nie musiał stosowac zwrotu "ej, ty..." - logistycznie: pamiętaj, że mentor stoi nie od frontu, ale za Twoimi plecami, twarzą ku Twojemu ekranowi. Będą dostępne nalepki PyLove.org :)

WAŻNA INFROMACJA! Mamy tylko 200 miejsc na sali, a rejestracja jest obowiązkowa ze względu na przepisy BHP.
    """


class Feedback(EmailData):
    recipients = 'confirmed'
    subject = "Ankieta i parę przydatnych linków"
    text = """Cześć!

    Parę przydatnych linków:
    - ankieta do oceny zajęć (coś czujemy, że będziecie dla nas mieli parę wskazówek ;p): https://goo.gl/forms/1fF5WXQjNe13CpKV2
    - ściąga i zadania z zajęć: https://pylove.org/#/lesson/0021
    - program warsztatów do końca roku: https://pylove.org/#/program
    - regulamin warsztatow: https://pylove.org/#/rules
    - dla tych co czują, że trzeba utrwalić podstawy: https://www.codecademy.com/learn/learn-python

    Super było Was zobaczyć!
    Do zobaczenia za tydzień!
    PyLove.org Team
    """


class PyLoveChange(EmailData):
    recipients = 'all'
    subject = "PyLove"
    text = """Drogie Adeptki, drodzy Adepci Pythona!

    Przed Wami, Uczestnikami, i nami, Organizatorami, niewielkie zmiany :) Ci, którzy pojawili się na dzisiejszych zajęciach wiedzą już, że ze względów organizacyjnych i komunikacyjnych Organizatorzy warsztatów #continued dedykowanych grupie “zaawansowanej” postanowili odłączyć się od ruchu PyLadies Poznań i kontynuować zajęcia pod nową marką wspieraną przez PyPolska - jedną z największych polskich społeczności skupionej wokół języka Python oraz organizatora konferencji PyConPL.

    Dziś narodziła się grupa PyLove, która pragnie zaszczepić bakcyla programowania w Pythonie we wszystkich - niezależnie od wieku, płci czy pochodzenia.

    Co to zmienia dla Ciebie? Absolutnie nic! Warsztaty nadal będą odbywać się we wtorki o godzinie 18:30 na terenie Collegium da Vinci w Poznaniu. Harmonogram zajęć nie ulega zmianie :)

    Nowa nazwa, to jednak nowe kanały komunikacji. Teraz znajdziecie nas:
    strona: https://pylove.org
    fanpage na FB: https://fb.me/PyLoveOrg
    grupa na FB (tzw. “grupa wsparcia”, gdzie możecie umieszczać swoje zapytania): https://www.facebook.com/groups/1510308165721555/

    Dodatkowy komunikat: w aplikacji pojawiła się możliwość usunięcia konta (w zakładce edycja)

    W razie pytań, piszcie na kontakt@pylove.org !

    Do zobaczenia na kolejnych zajęciach - tym razem już pod flagą PyLove!
    """


class RulesChange(EmailData):
    recipients = 'all'
    subject = "PyLove zmiany w regulaminie"
    text = """Hej,
    W związku ze zmianami, które zaszły we wtorek, nastąpiły kosmetyczne zmiany w regulaminie:

    Punkt 1. został zmodyfikowany z:
    Organizatorem warsztatu jest wolontariacka społeczność PyLadies reprezentowana przez: Zuzannę Kunik oraz Piotra Dyba, który funkcjonuje jako osobowość prawna pod nazwą PHOTOJOURNALIST.PL Agencja Fotograficzna Piotr Dyba, zwaną dalej Organizatorem, we współpracy z Collegium Da Vinci zwanym dalej CDV.
    na:
    Organizatorem warsztatu jest wolontariacka społeczność PyLove reprezentowana przez: Zuzannę Kunik oraz Piotra Dyba, który funkcjonuje jako osobowość prawna pod nazwą PHOTOJOURNALIST.PL Agencja Fotograficzna Piotr Dyba, zwaną dalej Organizatorem, we współpracy z Collegium Da Vinci zwanym dalej CDV oraz we współpracy z stowarzyszeniem PyPolska.

    Punkt 2. z:
    Strona Internetowa Organizatora to pyladiesstart.pl
    na:
    Strona Internetowa Organizatora to pylove.org

    Punkt 5. z:
    Liczba miejsc jest ograniczona do maksymalnie 200 osób. W wypadku większej liczby chętnych pierwszeństwo mają osoby, które brały w dwudniowym warsztacie PyLadies.start(), pozostałe osoby zostaną wybrane wg uznania Organizatora.
    na:
    Liczba miejsc jest ograniczona do maksymalnie 200 osób.

    W punkcie 16. słowo "warsztatach" zostało zamienione na "spotkaniach".

    Osobom, którym nie odpowiadają zmiany w regulaminie - w aplikacji w zakładce "edycja konta" znajduje się się możliwość usunięcia konta.

    Do zobaczenia na kolejnych zajęciach!

    Zespół PyLove
    """


class TestEmail(EmailData):
    recipients = 'admin'
    subject = "PyLove test email"
    text = """To jest e-mail testowy"""


ALL_EMAILS = [
    Custom.to_dict(),
    Accepted.to_dict(),
    Rejected.to_dict(),
    Reminder.to_dict(),
    TooLate.to_dict(),
    SecondChance.to_dict(),
    WorkshopInfo.to_dict(),
    UserFeedback.to_dict(),
    PyLoveMeetings.to_dict(),
    Feedback.to_dict(),
    PyLoveChange.to_dict(),
    RulesChange.to_dict(),
    TestEmail.to_dict(),
]
