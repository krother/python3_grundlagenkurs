
# Verschlüsselung

Implementiere einen einfachen Verschlüsselungsalgorithmus.

### Schritt 1: Nachricht im Klartext

Speichere die zu verschlüsselnde Nachricht als String:

    s = "STRENG_GEHEIME_NACHRICHT"

### Schritt 2: Als Tabelle darstellen

Brich den String in mehrere gleich lange Zeilen um:

    STRENG
    _GEHEI
    ME_NAC
    HRICHT

### Schritt 3: Schlüssel anwenden

Verwende einen Schlüssel, der die Spalten in eine neue Reihenfolge umsortiert. Mit dem Schlüssel `215403` erhälst Du:

    RTGNSE
    EGIE_H
    _ECAMN
    IRTHHC

### Schritt 4: Spalten aufschreiben

Füge die Spalten nacheinander zu einem neuen String zusammen. Dies ist die fertig chiffrierte Nachricht:

    RE_ITGERGICTNEAHS_MHEHNC

### Schritt 5: Dechiffrieren

Verwende den Schlüssel, um den gesamten Prozeß umzukehren und die Nachricht wieder in Klartext zu überführen.

#### Achtung:

Natürlich ist diese Art von Chiffrieralgorithmus eher leicht zu knacken. Den Code von jemand anderem ist natürlich auch eine gute (etwas schwierigere) Übung.
