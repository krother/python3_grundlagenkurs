
from PIL import Image
import os

im = Image.new(size=(1544, 644), mode='RGB')

positions = [(x, y) for x in range(5) for y in range(2)]
files = [fn for fn in os.listdir('.') if fn.endswith('.jpg')]

for (x,y), fn in zip(positions, files):
    sq = Image.open(fn)
    im.paste(sq, (x*300+44, y*300+44))

im.save('memory.png')
