
print('Welches Tier im Märchen heißt Isegrim?')

antworten = ['der Bär', 'der Wolf', 'der Fuchs', 'der Storch']

i = 1
for text in antworten:
    print(str(i) + ". " + text)
    i += 1

eingabe = input("\nGib Deine Antwort ein: ")
if eingabe == '2':
    print('Richtig!')
else:
    print('Leider falsch.')
