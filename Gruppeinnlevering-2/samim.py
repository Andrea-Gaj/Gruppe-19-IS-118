# IS-118 GRUPPEOPPGAVE 2 - ERLINGS PROSJEKT 

print()
print("Du er Erling, prosjektleder for kommunens nye digitale medborgerportal.")
print("Det er tre uker til prosjektet skal leveres")
print("men konflikter skaper problemer i prosjektgruppen.")

input("\nTrykk ENTER for å starte spillet...")

poeng = 0


# 1. Konflikt mellom Silje og Elias

print("Silje og Elias er uenige om design og teknologi")
print("Uenigheten har utviklet seg til en personlig konflikt")

print("1. Snakk med dem individuelt.")
print("2. Ta konflikten opp i plenum.")

valg_1 = input("Hva velger du? (1 eller 2):")

while valg_1 not in ["1", "2"]:
    print("Ugyldig valg. Skriv 1 eller 2.")
    valg_1 = input("Hva velger du? (1 eller 2): ")

if valg_1 == "1":
    poeng += 1
    print("Du snakker med Silje og Elias hver for seg.")
    print("Begge får forklare sitt pespektiv, og temperaturen synker.")
else:
    print("DU tar konflikten opp i plenum.")
    print("Problemene blir synlige for helet teamet, men møtet blir mer anspent og krever god ledelse.")

input("\nTrykk ENTER for å fortsette...")

# 2. Konflikt mellom Hamdi og Hallgeir

print("Hamdi ønsker å bruke kommunens eksisterende platform")
print("Hallgeir ønsker et mer åpent system for innspill")

print("1. Arranger et felles møte for finne en løsning.")
print("2. La dem løse prøve å løse uenigheten selv.")

valg_2 = input("hva velger du (1 eller 2):")

while valg_2 not in ["1", "2"]:
    print("Ugyldig valg. Skriv 1 eller 2.")
    valg_2 = input("Hva velger du? (1 eller 2): ")

if valg_2 == "1":
    poeng += 1
    print("Du arrangerer et møte der begge blir hørt.")
    print("De finner en mulig løsning som tar hensyn til både kommunens behov og innbyggernes ønsker.")
else:
    print("Du lar dem løse uenigheten på egenhånd.")
    print("De får ansvar for å finne en løsning, konflikten kan fortsette å vokse.")


input("\nTrykk ENTER for å se fortsette...")

# . Motivasjon go fremdrift

print(" Teamet er slitent, og fristen for prosjektet nørmer seg")

print("1. Sett av tid til relasjonsbygging og samarbeid.")
print("2. Prioriter arbeidsoppgavene og tidsfristen.")

valg_3 = input("Hva velger du? (1 eller 2):")

while valg_3 not in ["1", "2"]:
    print("Ugyldig valg. Skriv 1 eller 2.")
    valg_3 = input("Hva velger du? (1 eller 2): ")

if valg_3 == "1":
    poeng += 1
    print("Teamet får tid til å styrke relasjonene.")
    print("Motivasjonen og tilliten øker, men tidsfristen nørmer seg.")
else:
    print("Teamet fokuserer på oppgavene og tidsfristen.")
    print("Arbeidet går raskere, men relasjonene og motivasjonen kan lide.")


# 4. Reultatene

print(" RESULTATENE!")

print(f" Du fikk {poeng} av 3 mulige poeng")

if poeng == 3:
    print ("TEAM LYKKES!")
    print("Konfliktene ble løst, tilliten styrkes og teamaet når målene")

elif poeng == 2:
    print("TEAMET HAR UTFORDRINGER")
    print("Noen utfordringer er løst, men samarbeidet er fortsatt sårbart og prosjektet kan bli forsinket.")
else:
    print("TEAMET MISLYKKES")
    print("Konfliktene ble ikke løst, tilliten svekkes og prosjektet blir forsinket.")




