
# Palindrome

**🎯 Schreibe eine Funktion, die überprüft, ob ein String ein Palindrom ist:**

    :::python3
    def is_palindrome(s):
        ...

## Tests

    :::python3
    assert is_palindrome('Abba')
    assert is_palindrome('Legovogel')
    assert is_palindrome('Retsinakanister')
    assert is_palindrome('Vitaler Nebel mit Sinn ist im Leben relativ')
    assert not is_palindrome('abc')
    assert not is_palindrome('Lego Ego')

## Hinweise

* entferne alle Leerzeichen
* ignoriere Satzzeichen
* ignoriere Groß-/Kleinschreibung
* Wikipedia führt eine [Liste deutschsprachiger Palindrome](https://de.wikipedia.org/wiki/Liste_deutscher_Palindrome).
