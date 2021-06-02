
# Zahlenraten

**🎯 Schreibe ein einfaches Ratespiel.**

| Bereich | Thema |
|---------|-------|
| 💼 | Ein Ratespiel schreiben |
| 🔀 | Eine Event-Schleife entwerfen |
| 💡 | Das Modul `random` verwenden |
| 💡 | Schleifen mit `while` schreiben |
| 🔧 | Beispielausgabe als Programmierhilfe |
| 🐞 | Endlosschleifen erkennen |

 Der Spieler versucht eine Zahl zu erraten, die sich der Computer ausgedacht hat.

1. Das Programm *"erwürfelt"* eine Zahl zwischen 1 und 100.
2. Die Zahl wird **nicht** ausgegeben.
3. Der Spieler gibt eine Zahl ein.
4. Das Programm sagt, ob die geratene Zahl zu groß oder zu klein war.
5. Wiederhole ab `3.`, bis die richtige Zahl getroffen wurde.

----

### Beispielausgabe:

    Ich habe mir eine Zahl ausgedacht.
    Rate die Zahl.

    Bitte gib eine Zahl ein (1-100): 33
    Die Zahl ist zu gross.

    Bitte gib eine Zahl ein (1-100): 22
    Die Zahl ist zu gross.

    Bitte gib eine Zahl ein (1-100): 11
    Die Zahl ist zu klein.

    Bitte gib eine Zahl ein (1-100): 17
    Die Zahl ist zu gross.

    Bitte gib eine Zahl ein (1-100): 14
    Die Zahl ist zu gross.

    Bitte gib eine Zahl ein (1-100): 13
    Treffer!

----

### Hinweise

Du benötigst das Modul `random`:

```python
import random
```

Schlage in der Dokumentation des Moduls `random` nach, wie Du eine ganzzahlige Zufallszahl generieren kannst.
