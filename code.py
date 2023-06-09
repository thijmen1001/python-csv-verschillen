#Deze functie importeert de CSV-module die wordt gebruikt om CSV-bestanden te lezen en te schrijven.
import csv


#Deze code is om een bestand te openen en lokaal op te slaan en een list te creëren van CSV het bestand
klantenoud = []
header = None
fileName = 'Klanten-oud.csv'
with open(fileName, mode= 'r',newline='') as klantenFile:
    file = csv.reader(klantenFile, delimiter=';')
    header = next(file)
    #Leest elke rij van het CSV-bestand dat is geopend met 'with open(fileName, mode= 'r',newline='') as klantenFile:' 
    #En voegt de inhoud van die rij toe aan de lijst 'klantenoud'.
    for line in file:
        klantenoud.append(line)


#Deze code is om een bestand te openen en lokaal op te slaan en een list te creëren van CSV het bestand        
klantennieuw = []
header = None
fileName = 'Klanten-nieuw.csv'
with open(fileName, mode= 'r',newline='') as klantenFile:
    file = csv.reader(klantenFile, delimiter=';')
    header = next(file)
    #Leest elke rij van het CSV-bestand dat is geopend met 'with open(fileName, mode= 'r',newline='') as klantenFile:' 
    #En voegt de inhoud van die rij toe aan de lijst 'klantennieuw'.
    for line in file:
        klantennieuw.append(line)
        


#Deze code vergelijkt elke klant in de lijst 'klantennieuw' met elke klant in de lijst 'klantenoud'. 
#Als een klant uit de nieuwe lijst niet in de oude lijst voorkomt, wordt de voornaam, tussenvoegsel en achternaam van die klant afgedrukt. 
#Dit geeft een lijst van nieuwe klanten.
#nieuw[0] = voornaam    nieuw[1] = tussenvoegsel     nieuw[2] = achternaam
for nieuw in klantennieuw:
    if nieuw not in klantenoud:
        print(nieuw[0], nieuw[1], nieuw[2])

'''
output = 

Rick  Albersen
Alexander  Freijser
Jack  Hoogmoed
Michael van Lieffering
Arno  Overkleeft
'''
