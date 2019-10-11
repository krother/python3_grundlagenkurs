
# Verschlüsselung

**🎯 Implementiere einen einfachen Verschlüsselungsalgorithmus.**

## Schritt 1: Nachricht im Klartext

Speichere die zu verschlüsselnde Nachricht als String:

    s = "STRENG_GEHEIME_NACHRICHT"

## Schritt 2: Als Tabelle darstellen

Brich den String in mehrere gleich lange Zeilen mit einer vorgegebenen Länge um. Fülle Leerstellen am Ende auf:

    STRENG
    _GEHEI
    ME_NAC
    HRICHT

## Schritt 3: Schlüssel anwenden

Verwende einen Schlüssel, der die Spalten in eine neue Reihenfolge umsortiert. Mit dem Schlüssel `215403` erhälst Du:

    RTGNSE
    EGIE_H
    _ECAMN
    IRTHHC

## Schritt 4: Spalten aufschreiben

Füge die Spalten nacheinander zu einem neuen String zusammen. Dies ist die fertig chiffrierte Nachricht:

    RE_ITGERGICTNEAHS_MHEHNC

## Zusatzaufgaben:

* Lasse Dir den Text geben, den jemand anders verschlüsselt hat.
* Entschlüssele die Nachricht mit dem Schlüssel.
* Knacke den Code ohne Schlüssel!
