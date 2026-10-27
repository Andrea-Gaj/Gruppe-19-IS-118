while True:


    print("Du er Erling, prosjektleder for et digitalt prosjekt i kommunen.")
    print("Prosjektet ditt har en tidsfrist, men det har oppstått konflikter i gruppen.")
    print("Det er din oppgave å ta gode valg slik at prosjektet blir levert i tide.")
    input("Trykk enter for å fortsette...")
    poeng = 0

    # Konflikt 1: Silje og Elias

    print("Silje og Elias har havnet i en konflikt!")
    print("Silje mener løsningen Elias foreslår vil begrense brukeropplevelsen og hindre innovasjon")
    print("Elias mener Silje sin løsning vil være for komplisert og vanskelig å implementere.")
    print("1. Snakk med de i plenum")
    print("2. Snakk med de privat")

    valg = input("Hva velger du (1 eller 2)? ")
    while valg not in ["1", "2"]:
        print("Ikke lov, prøv enten 1 eller 2")
        valg = input("Skriv 1 eller 2: ")



    if valg == "1":
        poeng +=1
        print(" Du snakker med de i plenum")
        print(" De kommer til enighet, og Silje forstår hvorfor Elias sitt forslag fungerer bedre.")

    elif valg == "2":
        print(" Du snakker med de privat")
        print(" De kommer ikke til enighet fordi de ikke får diskutert problemet sammen.")

 # Konflikt 2: Hamdi og Hallgeir

    print("En ny konflitk har oppstått mellom Hamdi og Hallgeir!")
    print("Hamdi ønsker å bruke kommunens eksisterende plattform for å ha en kontrollert løsning.")
    print("Hallgeir ønsker et mer åpent system der innbyggerne kan komme med spontane innspill.")
    print("1. Ta initiativ til et felles møte for å løse konflikten")
    print("2. La de løse konflikten på egen hånd")

    valg = input("Hva velger du (1 eller 2)? ")
    while valg not in ["1", "2"]:
        print("Ikke lov, prøv enten 1 eller 2")
        valg = input("Skriv 1 eller 2: ")
    if valg == "1":
        poeng +=1
        print(" Du får de med på et felles møte hvor de kan diskutere og finne en løsning sammen")
        print(" De kommer overens og Hamdi blir enig med Hallgeir")
    elif valg == "2":
        print("Du lar de ordne det på egenhånd")
        print(" De klarer ikke å bli enige. Dette fører til forsinkelser i prosjektet")

        # Konflikt 3: Motivasjon i gruppen

    print("Erling tenker at det er lurt å gjøre noe for å motivere gruppen. probelmet er at gruppen har lite tid igjen og det er viktig å få levert prosjektet i tide.")
    print("1.Erling setter av litt tid til relasjonsbygging og sosiale aktiviteter som bygger tillit? ")
    print("2.Prioritere fremdrift av prosjektet")

    valg = input("Hva velger du (1 eller 2)? ")
    while valg not in ["1", "2"]:
        print("Ikke lov, prøv enten 1 eller 2")
        valg = input("Skriv 1 eller 2: ")
    if valg == "1":
        poeng +=1
        print("Å sette av litt til teambuilding gjorde at gruppen ble mer motivert og samarbeidet bedre.)")
        print("prosjektet fortsetter som planlagt")
    elif valg == "2":
        print("Gruppen blir utbrent av å jobbe så mye, og konfliktene fortsetter.")
        print("Samarbeide blir negativt påvirket. Dette fører til at prosjektet mister fremdrift")
    

 
       #Resultat


    if poeng == 3:
        print("Gratulerer! Du har håndtert konfliktene på en god måte og prosjektet blir levert i tide!")

    elif poeng == 2:
        print("Du har håndtert noen konflikter på en god måte, men en annen konflikt ble ikke løst. Prosjektet blir levert med forsinkelse.")
        
    else:
        print("Du har ikke håndtert konfliktene på en god måte. Gruppen sliter med samarbeidet, og prosjektet blir ikke ferdig.")

    svar=input("Vil du spille igjen? (ja/nei)")
    while svar not in ["ja", "nei"]:
        print("ikke vær lur, enten ja eller nei")
        svar = input("Vil du spille igjen? (ja/nei)")

    if svar == "nei":
        print("Takk for at du spilte!")
        break
    
    