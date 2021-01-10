
from PIL import Image
from IPython.display import display
import os


pfad = 'bilder/'

bilder = ['rainbow.jpg', 'flower.jpg', 'pebbles.jpg']
beschriftung =  [
        'bunte Ölschlieren von Daniel Olah',
        'weiße Blume von Annie Spratt',
        'Kieselsteine von John Salzarulo'
        ]

i = 0
for dateiname in bilder:
    bild = Image.open(pfad + dateiname)
    display(bild)
    i = i + 1
    titel = f"Bild Nr. {i}: {beschriftung[i-1]}"
    print(titel)
    if i < len(bilder):
        input('drücke <Enter> für das nächste Bild')
