
waren = {
    'Laptop': (2, 600),
    'Silberbesteck': (2, 400),
    'Stereoanlage': (3, 300),
    'Juwelen': (2, 1100),
    'Vase': (5, 700),
    'Kamera': (2, 500),
    'Gemälde': (4, 900),
    'Bargeld': (1, 800)
}

beste = {0: []}

for g in range(1, 9):
    # packe Rucksack der Grösse g
    for w in waren:
        groesse, wert = waren[w]
        # wert noch ignoriert
        ...
