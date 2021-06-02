
# Römische Zahlen

**🎯 Schreibe eine Funktion `roman2arabic()`, die eine römische in eine arabische Zahl umwandelt.**

## Tests

Der folgende Code hilft beim Prüfen der Ergebnisse:

```python
def test_roman(self):
    assert roman2arabic("I") == 1
    assert roman2arabic("XI") == 11
    assert roman2arabic("IX") == 9
    assert roman2arabic("CLI") == 151
    assert roman2arabic("XCIII") == 93
    assert roman2arabic("CCXCIV") == 294
    assert roman2arabic("MCM") == 1900
    assert roman2arabic("MI") == 1001
```

## Hinweise

* Du mußt nur Zahlen von 1-5000 berücksichtigen
* Welche Datenstruktur eignet sich zum Nachschlagen der Zahlenwerte der römischen Ziffern?

## Zusatzaufgabe

* schreibe eine Funktion, die arabische Zahlen in römische umwandelt
