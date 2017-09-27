class EmailData:
    recipients = '...'
    subject = '...'
    text = "..."

    @classmethod
    def to_dict(cls):
        return {
            'subject': cls.subject,
            'text': cls.text,
            'email_type': cls.__name__,
            'recipients': cls.recipients
        }


class EmailAccepted(EmailData):
    recipients = {'accepted': True, 'organiser': False, 'mentor': False}
    subject = 'Zostałaś przyjęta/przyjęty na warsztaty PyLadies Start'
    text = '''Cześć {name}!
    Z przyjemnością informujemy, że Twoje zgłoszenie na warsztat weekendowy PyLadies.start() w Poznaniu zostało zaakceptowane.
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

    Zapraszamy do obserwowania naszego wydarzenia na Facebooku:
    https://www.facebook.com/events/518360511838646

    Pozdrawiamy,
    PyLadies Poznań Team'''


class EmailRejected(EmailData):
    recipients = {'accepted': False, 'mentor': False}
    subject = 'Jesteś na liście rezerwowej - warsztaty PyLadies Start'
    text = '''Cześć {name}!
    Ponownie dziękujemy za rejestrację na warsztat weekendowy PyLadies.start() w Poznaniu w dniach 23-24 września.
    Niestety, z uwagi na dużą ilość zgłoszeń Twoja aplikacja trafiła na listę rezerwową. Nie możemy w tej chwili zapewnić Ci miejsca na zajęciach.
    Jak tylko zwolni się miejsce, niezwłocznie Cię o tym poinformujemy.
    Otrzymasz maila w tej sprawie 17 września.

    Zapraszamy do obserwowania naszego wydarzenia na Facebooku:
    https://www.facebook.com/events/518360511838646

    Pozdrawiamy,
    PyLadies Poznań Team'''


class EmailReminder(EmailData):
    recipients = {'accepted': True, 'confirmation': 'noans'}
    subject = 'Potwierdź swój udział w warsztatach PyLadies Start'
    text = '''Cześć {name}!
    Czy pamiętacie o pilnej konieczności potwierdzenia swojego udziału w warsztacie weekendowym PyLadies.start() w Poznaniu, 23-24 września?
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


    Zapraszamy do obserwowania naszego wydarzenia na Facebooku:
    https://www.facebook.com/events/518360511838646

    Pozdrawiamy,
    PyLadies Poznań Team'''


class EmailTooLate(EmailData):
    recipients = {'accepted': True, 'confirmation': 'noans'}
    subject = 'Dziękujemy za zainteresowanie warsztatami PyLadies Start'
    text = '''Cześć {name}!
    Przykro nam, że nie zobaczymy się na warsztacie weekendowym PyLadies.start() 23-24 września!
    Nie wpłynęło do nas Twoje potwierdzenie udziału, ale wierzymy, że mimo to Twoje zainteresowanie programowaniem przerodzi się wkrótce w pasję.

    Zapraszamy do obserwowania naszego wydarzenia na Facebooku:
    https://www.facebook.com/events/518360511838646

    Jeszcze raz dziękujemy za zainteresowanie i rejestrację!

    Pozdrawiamy,
    PyLadies Poznań Team'''


class EmailSecondChance(EmailData):
    recipients = {'accepted': True, 'confirmation': 'noans'}
    subject = 'Zostałaś przyjęta/przyjęty na warsztaty PyLadies Start'
    text = '''Cześć {name}!
    Miło nam zawiadomić, że zwolniły się miejsca na liście uczestników warsztatu weekendowego PyLadies.start(), na który aplikowałaś/aplikowałeś!
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


    Zapraszamy do obserwowania naszego wydarzenia na Facebooku:
    https://www.facebook.com/events/518360511838646

    Pozdrawiamy,
    PyLadies Poznań Team'''


class EmailCustom(EmailData):
    subject = ''
    text = ""
    recipients = {}

class EmailWorkshopInfo(EmailData):
    recipients = {'accepted': True, 'confirmation': 'ack'}
    subject = 'Najważniejsze informacje przed warsztatem PyLadies Start'
    text = ''' Cześć, {name}!

    Bardzo się cieszymy, że będziesz z nami na PyLadies.start()! Widzimy się już w najbliższą sobotę! Poniżej znajdziesz wszystkie najważniejsze informacje - zapoznaj się z nimi przed warsztatami.

    Miejsce warsztatów: Międzynarodowe Targi Poznańskie, Pawilon 14, wejście B

    Mapkę z zaznaczonym miejscem warsztatów znajdziesz na: https://pyladiesstart.pl/#/agenda

    Skrócony plan warsztatów:

        23.09.2017 SOBOTA
        8:15 Otwarcie bramek w MTP Wejście Wschodnie (ul. Roosevelta)
        8:15 – 8:45 Rejestracja uczestników w Pawilonie 14, wejście B
        9:00 – 18:00 Warsztaty
        19:00 – 22:00 Afterparty w Tandem Pub (ul. Gwarna 9)

        24.09.2017 NIEDZIELA
        8:30 Otwarcie bramek - MTP Wejście Wschodnie (ul. Roosevelta)
        9:00-18:00 Warsztaty

    Pełną agendę warsztatów znajdziesz na: https://pyladiesstart.pl/#/agenda

    WAŻNE!

    PIERWSZEGO DNIA PRZYJDŹ PRĘDZEJ – potrzebujemy czasu, by wręczyć Ci pakiet rejestracyjny, odłożyć Twoje przekąski na szwedzki stół, podłączyć Twój komputer do zasilania i sprawdzić czy wszystko jest OK :)
    
    ZAINSTALUJ PYTHONA I PYCHARM IDE - Uprzednia instalacja Pythona i PyCharm IDE zapewni gładki start i szybsze przejście do głównych treści warsztatu. Instrukcje instalacji znajdziesz tu: https://pyladiesstart.pl/#/agenda
    
    PAMIĘTAJ, BY PRZYNIEŚĆ PRZEDŁUŻACZ ORAZ ZADEKLAROWANE PRZEKĄSKI - my zapewnimy do picia wodę, kawę oraz herbatę. Ty deklarowałaś/deklarowałeś, że przyniesiesz: {what_can_you_bring}

    NIE ZAPOMNIJ IDENTYFIKATORA – wręczymy Ci go podczas rejestracji. Wyjście podczas trwania warsztatów z terenów MTP oraz ponowne wejście na podstawie otrzymanego identyfikatora na hasło PYLADIES. Identyfikator zabierz też na afterparty - upoważni Cię on do 20% zniżki w Tandem Pub!

    JESTEŚ NA KÓŁKACH? Jeśli chcesz przyjechać własnym samochodem i zaparkować go na terenie MTP to całodzienny pobyt kosztuje 20 zł, dostępność miejsc parkingowych można uzyskać na bramkach przy wjeździe od ul. Śniadeckich.

    POTRZEBUJESZ POMOCY? Jeśli jesteś osobą z ograniczeniami ruchowymi (lub po prostu potrzebujesz pomocy), to napisz do Weroniki (Weronika@pyladiesstart.pl) –  ona postara się, by wszystko było dla Ciebie gotowe, ponieważ obiekt jest dostosowany do osób na z ograniczeniami ruchowymi.

    W razie pytań, pisz do nas na Facebooku:
    https://www.facebook.com/events/518360511838646

    Do zobaczenia!
    PyLadies Poznań Team
    '''


class EmailUserFeedback(EmailData):
    recipients = {'accepted': True, 'confirmation': 'ack', 'mentor': False, 'organiser': False}
    subject = 'Feedback dla PyLadies Start'
    text = ''' Cześć, {name}!

Warsztaty PyLadies.start() dobiegły końca... Bardzo chcielibyśmy dostać Twój feedback, żeby wiedzieć co ulepszyć przy okazji następnej edycji!

Wejdź proszę tutaj: https://goo.gl/forms/XbtGgW8MEnZ8TaPT2 i wypełnij tę bardzo krótką ankietę - zrób to tak szybko, jak tylko możesz, byś miała/miał jeszcze świeże wspomnienia z warsztatów :)

Z góry bardzo dziękujemy!
PyLadies Poznań Team    
    '''

class EmailKCF(EmailData):
    recipients = {'accepted': True, 'confirmation': 'ack', 'mentor': False, 'organiser': False}
    subject = 'Zniżka na warsztaty w Kids Code Fun'
    text = ''' Drodzy uczestnicy Pyladies.start()
    
Dziękujemy Wam bardzo za udział w warsztatach.

Nasz brązowy partner Kids Code Fun ma dla Was wszystkich 10% zniżkę na warsztaty programowania dla dzieci w wieku 5-7 lat (ScratchJr) i 8-12 lat (Scratch) startujące już 30 września. W celu uzyskania zniżki prosimy przy zapisach (na stronie kidscodefun.com) podać pyladies przy imieniu dziecka. Więcej informacji na stronie Kids Code Fun lub pod mailem poznan@kidscodefun.com. Serdecznie zapraszamy!

Pozdrawiamy
Zespół Pyladies.start()   
    '''

ALL_EMAILS = [
    EmailAccepted.to_dict(),
    EmailRejected.to_dict(),
    EmailReminder.to_dict(),
    EmailTooLate.to_dict(),
    EmailSecondChance.to_dict(),
    EmailCustom.to_dict(),
    EmailWorkshopInfo.to_dict(),
    EmailUserFeedback.to_dict(),
    EmailKCF.to_dict(),
]
