while True:
    poeng = 0

    print("Velkommen til Erlingsprosjekteventyr!")
    navn = input("Hva heter du?")
    print(f"Hei {navn}, gjør deg klar til å løse konflikter.")
    
    print ("Konflikt 1")
    print ("Silje og Elias har havnet i en konflikt")
    print ("Silje mener løsningen Elias foreslår vil låse brukeropplevelsen og hindre innovasjon.")
    print ("Elias mener Siljes forslag er urealistisk, usikkert og for kostbart.")
    
    Valg=input ("Velger du løsning A eller løsning B?") 
    print ("A) Snakk med de i plenum")
    print ("B Ta samtalen individuelt")
    
    if Valg == "A":
        print ("Du snakker med de i plenum")
        print ("Konflikten løser seg, Silje blir ening med Elias.")
        poeng +=1
        
        
        
    elif Valg == "B":
        print ("Du snakker med de individuelt")
        print ("Konflikten eskalerer ikke, men de blir fortsatt ikke ening med hverandre.")
        
        
    print ("Konflikt 2")
    print ("Hamdi og Hallgeir har havnet i en konflikt")
    print ("Hamdi ønsker en kontrollert løsning gjennom kommunens eksisterende plattform.")
    print ("Hallgeir ønsker et mer åpent, dialogbasert system med rom for spontane innspill.")
        
    Valg=input ("Velger du løsning A eller Løsning B?")
    print ("A) Ta et felles møte for å avklare konflikten.")
    print ("B) Du avventer og håper at Hamdi og Hallgeir løser det selv.")
    
    if Valg == "A":
        print ("Du tar et felles møte for å avklare konflikten.")
        print ("Dere kommer sammen frem til en løsning og konflikten løses.")
        poeng +=1
        
    elif Valg == "B":
        print ("Du avventer og håper at hamdi og hallgeir løser det selv.")
        print ("De blir ikke enige om en løsning og prosjektet stopper litt opp.")
        
    if poeng == 2:
        print ("Gratulerer! Du er en konfliktløser. Nå leveres prosjektet i tide.")
        
    elif poeng == 1: 
        print ("Du løste den ene konflikten, den andre er fortsatt ikke løst, prosjektet blir forsinket.")
        
    else:
        print ("Det er full kaos og mange uløste konflikter, prosjektet blir ikke ferdig hvis det fortsetter slik.")
        
        
    Svar =input ("Vil du spille en gang til? (ja/nei)")
    
    if Svar == "nei":
        print ("Takk for at du spilte!")
        break 
