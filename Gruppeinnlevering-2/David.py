while True:


    print("Du er Erling, prosjektleder for et digitalt prosjekt i kommunen.")
    print("Prosjektet dit har en tidfrist men din gruppe har havnet i konflikt.")
    print("Det er din job å ta gode valg slik at prosjektet blir levert i tide")
    input("Trykk enter for å fortsette...")
    poeng = 0
    print("Silje og Elias har havnet i en konflikt!")
    print("Silje mener løsningen Elias foreslår vil låse brukeropplevelsen og hindre innovasjon.")
    print("Elias mener Silje sin løsning vil være for komplisert og vanskelig å implementere.")
    print("1. Snakk med de i plenum")
    print("2. Snakk med de privat")

    valg=input("Hva velger du (1 eller 2)?")



    if valg == "1":
        poeng +=1
        print(" Du snakker med de i plenum")
        print(" De kommer overens og Silje blir enig med Elias")

    elif valg == "2":
        print(" Du snakker med de privat")
        print(" De kommer ikke overens og Silje blir uenig med Elias")


    print("En ny konflitk har oppstått mellom Hamdi og Hallgeir!")
    print("Hamdi ønsker å bruke kommunens eksisterende plattform.")
    print("Ønsker et mer åpent system der brukerne kan komme med innspill.")
    print("1. Vil du snakke med de i plenum")
    print("2. La de løse konflikten på egenhånd")

    valg=input("Hva velger du (1 eller 2)?")

    if valg == "1":
        poeng +=1
        print(" Du snakker med de i plenum")
        print(" De kommer overens og Hamdi blir enig med Hallgeir")
    elif valg == "2":
        print("Du lar de ordne det på egenhånd")
        print(" De kommer ikke overens og Hamdi blir uenig med Hallgeir")

    if poeng == 2:
        print("Gratulerer! Du har håndtert konfliktene på en god måte og prosjektet blir levert i tide!")

    elif poeng == 1:
        print("Du har håndtert en konflikt på en god måte, men den andre konflikten ble ikke løst. Prosjektet blir levert med forsinkelse.")
        
    else:
        print("Du har ikke håndtert konfliktene på en god måte. Prosjektet blir ikke levert i tide.")

    svar=input("Vil du spille igjen? (ja/nei)")

    if svar == "nei":
        print("Takk for at du spilte!")
        break
    