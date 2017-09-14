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
    recipients = {'accepted': True, 'organiser': True} #TODO: remove organiser after prod test
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
    recipients = {'accepted': False}
    subject = 'Zostałaś przyjęta/przyjęty na warsztaty PyLadies Start'
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
    subject = 'Zostałaś przyjęta/przyjęty na warsztaty PyLadies Start'
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
    recipients = {'accepted': True, 'confirmation': 'rej'}
    subject = 'Zostałaś przyjęta/przyjęty na warsztaty PyLadies Start'
    text = '''Cześć {name}!
    Przykro nam, że nie zobaczymy się na warsztacie weekendowym PyLadies.start() 23-24 września!
    Nie wpłynęło do nas Twoje potwierdzenie udziału, ale wierzymy, że mimo to Twoje zainteresowanie programowaniem przerodzi się wkrótce w pasję.

    Zapraszamy do obserwowania naszego wydarzenia na Facebooku:
    https://www.facebook.com/events/518360511838646

    Jeszcze raz dziękujemy za zainteresowanie i rejestrację!

    Pozdrawiamy,
    PyLadies Poznań Team'''


class EmailSeconChance(EmailData):
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


ALL_EMAILS = [
    EmailAccepted.to_dict(),
    EmailRejected.to_dict(),
    EmailReminder.to_dict(),
    EmailTooLate.to_dict(),
    EmailSeconChance.to_dict(),
    EmailCustom.to_dict(),
]
