1.17 Systemy kolejkowe i bazy danych NOSQL
==========================================

System Kolejkowy - Message Queue
--------------------------------

Zwany też Kolejka komunikatów, jak nazwa wsakzuje służy do kolejkowania kolejnych zadań, operacji w sposób asynchroniczny co oznacza, że odbiorca (konsumer) i nadawca wiadomości (producent) nie muszą łączyć się z kolejką w tym samym czasie.
Używa kolejek do przesyłania wiadomości do przekazywania sterowania lub danych.
Może być również wykorzystwany wewnętrznie do komunikacji międzyprocesowej lub do międzywątkowej komunikacji.
Większość aplikacji czasu rzeczywistego takich jak czaty opiera się często na systemie kolejkowym. Systemy MQ często są też wykorzystywane do
processowania danych, tesktowych, graficznych itp. Ze względu na to iż ten process mógłbym zająć więcej niż użytkownik jest skłonny czekać na wynik.


Bazy danych Not Only SQL
------------------------