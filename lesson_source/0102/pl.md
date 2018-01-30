<meta charset="utf-8">
<link rel="stylesheet" href="../css/codehilite.css">
<link rel="stylesheet" href="../css/vendor/bootstrap.min.css">
<link rel="stylesheet" href="../css/vendor/bootstrap-theme.min.css">
<link href="../css/vendor/font-awesome.min.css" rel="stylesheet">
<link rel="stylesheet" href="../css/main.css">
<link rel="stylesheet" href="../css/vendor/sweetalert.css">
<style>
    img {max-width: 600px};
</style>

Odczyt i zapis kart RFID z wyświetlaczem
========================================

Piotr Dyba - 22781 - piotr@dyba.it
----------------------------------

#### Opis:

Projekt pozwala na zapisanie klucza lub ideyntyfikatora (ID) na karcie RFID z potwierdzeniem udanego zapisu
oraz odczytanie karty RFID
i wyświetlenie wartości na ekranie. Niestety Arduino nie posiada wsparcia dla funkcji kryptograficznych wykorzystywanych
w protokole https np. AES. Ze względu na swoją niską moc obliczeniową, integracja z zew. API RESTowym minęłaby się z celem.
Integrację z HTTPSem można by osiągnąć na płytakch typu ESP8266 lub bardziej zawansownych typu Rasppbery Pi.
W projetkcie został wykorzystany moduł RFID MFRC522, Arduino UNO oraz wyświetlacz LM1602 z magistralą I2C.
Na warstwie progrmistycznej zostały wykorzystane biblioteki zewnetrzne MFRC522 (do sterowania modułem RFID) oraz LiquidCrystal_I2C
(do sterowanie wiadomościami na ekranie).

#### Przygotwanie Ardunio:

Czytnik RFID (MIFARE) podłączamy następująco:

| Signal      |  A. UNO Pin  |
| ----------- | ------------ |
| RST/Reset   |  9           |
| SPI SS      |  10          |
| SPI MOSI    |  11          |
| SPI MISO    |  12          |
| SPI SCK     |  13          |



Wyświetlacz LM1602, oparty na układzie PCF8574 został podłączony poprzez magistralę I2C w nastepujący sposób:


| LCM1602     |   A. Uno Pin |
| ----------- | ------------ |
| VCC	      |   5 V        |
| GND	      |	  GND        |
| SDA    	  |	  A4         |
| SCL	      |	  A5         |

#### Projekt:


![image](./images/arduino.jpg)

#### Wykonanie:


![image](./images/arduino_foto.jpg)


#### Kody źródłowe

##### RFID Zapisywanie:


    :::cpp
    #include <SPI.h>
    #include <MFRC522.h>

    constexpr uint8_t RST_PIN = 9;     
    constexpr uint8_t SS_PIN = 8;  

    MFRC522 mfrc522(SS_PIN, RST_PIN); 

    MFRC522::MIFARE_Key key;

    void setup() {
        Serial.begin(9600); 
        while (!Serial);    
        SPI.begin();        
        mfrc522.PCD_Init(); 
        for (byte i = 0; i < 6; i++) {
            key.keyByte[i] = 0xFF;
        }
        Serial.println(F("Data will be written to the PICC, in sector #1"));
    }

    void loop() {
        if ( ! mfrc522.PICC_IsNewCardPresent())
            return;
        if ( ! mfrc522.PICC_ReadCardSerial())
            return;
        MFRC522::PICC_Type piccType = mfrc522.PICC_GetType(mfrc522.uid.sak);

        // Check for compatibility
        if (    piccType != MFRC522::PICC_TYPE_MIFARE_MINI
            &&  piccType != MFRC522::PICC_TYPE_MIFARE_1K
            &&  piccType != MFRC522::PICC_TYPE_MIFARE_4K) {
            Serial.println(F("This sample only works with MIFARE Classic cards."));
            return;
        }

        byte sector         = 1;
        byte blockAddr      = 4;
        byte dataBlock[]    = {
            'P', 0x02, 0x03, 0x04, //  1,  2,   3,  4,
            0x05, 0x06, 0x07, 0x08, //  5,  6,   7,  8,
            0x09, 0x0a, 0xff, 0x0b, //  9, 10, 255, 11,
            0x0c, 0x0d, 0x0e, 0x0f  // 12, 13, 14, 15
        };
        byte trailerBlock   = 7;
        MFRC522::StatusCode status;
        byte buffer[18];
        byte size = sizeof(buffer);

        status = (MFRC522::StatusCode) mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, trailerBlock, &key, &(mfrc522.uid));
        if (status != MFRC522::STATUS_OK) {
            Serial.print(F("PCD_Authenticate() failed: "));
            Serial.println(mfrc522.GetStatusCodeName(status));
            return;
        }
        mfrc522.PICC_DumpMifareClassicSectorToSerial(&(mfrc522.uid), &key, sector);

        // Read data from the block
        if (status != MFRC522::STATUS_OK) {
            Serial.print(F("MIFARE_Read() failed: "));
            Serial.println(mfrc522.GetStatusCodeName(status));
        }
        status = (MFRC522::StatusCode) mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_B, trailerBlock, &key, &(mfrc522.uid));
        if (status != MFRC522::STATUS_OK) {
            Serial.print(F("PCD_Authenticate() failed: "));
            Serial.println(mfrc522.GetStatusCodeName(status));
            return;
        }

        // Write data to the block
        status = (MFRC522::StatusCode) mfrc522.MIFARE_Write(blockAddr, dataBlock, 16);
        if (status != MFRC522::STATUS_OK) {
            Serial.print(F("MIFARE_Write() failed: "));
            Serial.println(mfrc522.GetStatusCodeName(status));
        }
        status = (MFRC522::StatusCode) mfrc522.MIFARE_Read(blockAddr, buffer, &size);
        if (status != MFRC522::STATUS_OK) {
            Serial.print(F("MIFARE_Read() failed: "));
            Serial.println(mfrc522.GetStatusCodeName(status));
        }
        Serial.print(F("Data in block ")); Serial.print(blockAddr); Serial.println(F(":"));
        dump_byte_array(buffer, 16); Serial.println();

        byte count = 0;
        for (byte i = 0; i < 16; i++) {
            // Compare buffer (= what we've read) with dataBlock (= what we've written)
            if (buffer[i] == dataBlock[i])
                count++;
        }
        if (count == 16) {
            Serial.println(F("Success :-)"));
        } else {
            Serial.println(F("Failure, no match :-("));
            Serial.println(F("  perhaps the write didn't work properly..."));
        }

        mfrc522.PICC_DumpMifareClassicSectorToSerial(&(mfrc522.uid), &key, sector);
        

        // Halt PICC
        mfrc522.PICC_HaltA();
        // Stop encryption on PCD
        mfrc522.PCD_StopCrypto1();
    }

    void dump_byte_array(byte *buffer, byte bufferSize) {
        for (byte i = 0; i < bufferSize; i++) {
            Serial.print(buffer[i] < 0x10 ? " 0" : " ");
            Serial.print(buffer[i], HEX);
        }
    }


#### RFID Odczyt i wyświetlanie:



    :::cpp
    #include <SPI.h>
    #include <MFRC522.h>
    #include <Wire.h>
    #include <LiquidCrystal_I2C.h>


    constexpr uint8_t RST_PIN = 9;
    constexpr uint8_t SS_PIN = 8;

    LiquidCrystal_I2C lcd(0x3F, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);


    MFRC522 mfrc522(SS_PIN, RST_PIN);

    MFRC522::MIFARE_Key key;


    void setup() {
        Serial.begin(9600);
        lcd.begin(16,2);
        while (!Serial);
        SPI.begin();
        mfrc522.PCD_Init();
        mfrc522.PCD_DumpVersionToSerial();
        for (byte i = 0; i < 6; i++) {
            key.keyByte[i] = 0xFF;
        }
        dump_byte_array(key.keyByte, MFRC522::MF_KEY_SIZE);
        lcd.print("Ready");
    }


    void loop() {
        // Look for new cards
        if ( ! mfrc522.PICC_IsNewCardPresent())
            return;
        // Select one of the cards
        if ( ! mfrc522.PICC_ReadCardSerial())
            return;
        Serial.print(F("Card UID:"));
        dump_byte_array(mfrc522.uid.uidByte, mfrc522.uid.size);
        Serial.println();
        Serial.print(F("PICC type: "));
        MFRC522::PICC_Type piccType = mfrc522.PICC_GetType(mfrc522.uid.sak);
        Serial.println(mfrc522.PICC_GetTypeName(piccType));

        // Check for compatibility
        if (    piccType != MFRC522::PICC_TYPE_MIFARE_MINI
            &&  piccType != MFRC522::PICC_TYPE_MIFARE_1K
            &&  piccType != MFRC522::PICC_TYPE_MIFARE_4K) {
            Serial.println(F("This sample only works with MIFARE Classic cards."));
            return;
        }

        byte sector         = 1;
        byte blockAddr      = 4;
        byte dataBlock[]    = {
            0x5d,
            0x16,
            0x39,
            0x3e,
            0xfa,
            0xb2,
            0x4a,
            0x2,
            0x32,
            0xbc,
            0x45,
            0xd4,
            0x57,
            0x4c,
            0x89,
            0xe2,
        };
        byte trailerBlock   = 7;
        MFRC522::StatusCode status;
        byte buffer[18];
        byte size = sizeof(buffer);

        status = (MFRC522::StatusCode) mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, trailerBlock, &key, &(mfrc522.uid));
        if (status != MFRC522::STATUS_OK) {
            Serial.print(F("PCD_Authenticate() failed: "));
            Serial.println(mfrc522.GetStatusCodeName(status));
            return;
        }

        status = (MFRC522::StatusCode) mfrc522.MIFARE_Read(blockAddr, buffer, &size);
        if (status != MFRC522::STATUS_OK) {
            Serial.print(F("MIFARE_Read() failed: "));
            Serial.println(mfrc522.GetStatusCodeName(status));
        }
        Serial.print(F("Data in block "));
        Serial.print(blockAddr);
        show_screen(buffer, 16);
        dump_byte_array(buffer, 16);
        Serial.println();

        // Halt PICC
        mfrc522.PICC_HaltA();
        mfrc522.PCD_StopCrypto1();
    }

    void dump_byte_array(byte *buffer, byte bufferSize) {
        for (byte i = 0; i < bufferSize; i++) {
            Serial.print(buffer[i] < 0x10 ? "0" : "");
            Serial.print(buffer[i], HEX);
        }
    }

    void show_screen(byte *buffer, byte bufferSize) {
        lcd.setCursor(0,0);
        for (byte i = 0; i < bufferSize; i++) {
            lcd.print(buffer[i], HEX);
        }
    }