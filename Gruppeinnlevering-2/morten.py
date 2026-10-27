while True:
    poeng = 0

    print("Velkommen til Erlingsprosjekteventyr!")
    navn = input("Hva heter du?")
    print(f"Hei {navn}, gjør deg klar til å løse konflikter.")
    
    print ("Konflikt 1")
    print ("Silje og Elias har havnet i en konflikt")
    print ("Silje mener løsningen Elias foreslår vil låse brukeropplevelsen og hindre innovasjon.")
    print ("Elias mener Siljes forslag er urealistisk, usikkert og for kostbart.")
    
    print ("A) Snakk med de i plenum")
    print ("B) Ta samtalen individuelt")
    Valg=input ("Velger du løsning A eller løsning B?") 
    
    while Valg not in ["A", "B"]:
        print ("Dette er ikke mulig svar, svar med A eller B")
        Valg=input ("Skriv A eller B: ")
    
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
        
    print ("A) Ta et felles møte for å avklare konflikten.")
    print ("B) Du avventer og håper at Hamdi og Hallgeir løser det selv.")
    Valg=input ("Velger du løsning A eller Løsning B?")

    while Valg not in ["A", "B"]:
        print ("Dette er ikke mulig svar, svar med A eller B")
        Valg =input ("Skriv A eller B: ")
    
    if Valg == "A":
        print ("Du tar et felles møte for å avklare konflikten.")
        print ("Dere kommer sammen frem til en løsning og konflikten løses.")
        poeng +=1
        
    elif Valg == "B":
        print ("Du avventer og håper at hamdi og hallgeir løser det selv.")
        print ("De blir ikke enige om en løsning og prosjektet stopper litt opp.")
        
   
    print ("Konflikt 3")
    print ("Erling tenker at det er lurt å gjøre noe for å motivere gruppen. probelmet er at gruppen har lite tid igjen og det er viktig å få levert prosjektet i tide.")
    
    print ("A) Erling setter av litt tid til sosiale aktiviteter som bygger tillit og samhold.") 
    print ("B) Prioritere fremdrift av prosjektet.")
    Valg=input ("Velger du løsning A eller Løsning B?")

    while Valg not in ["A", "B"]:
        print ("Dette er ikke mulig svar, svar med A eller B")
        Valg =input ("Skriv A eller B: ")
    
    if Valg == "A":
        print ("Erling setter av litt tid til sosiale aktiviteter som bygger tillit og samhold.")
        print ("Prosjekter fortsetter bra.")
        poeng +=1
        
    elif Valg == "B":
        print ("Prioritere fremdrift av prosjektet.")
        print ("Folk er utbrent og nye konflikter fortsetter å oppstå.")
   
   
    if poeng == 3:
        print ("Gratulerer! Du er en konfliktløser. Nå leveres prosjektet i tide.")
        
    elif poeng == 2: 
        print ("Du løste den ene konflikten, den andre er fortsatt ikke løst, prosjektet blir forsinket.")
        
    else:
        print ("Det er full kaos og mange uløste konflikter, prosjektet blir ikke ferdig hvis det fortsetter slik.")
        
        
    Svar =input ("Vil du spille en gang til? (ja/nei)")
    
    if Svar == "nei":
        print ("Takk for at du spilte!")
        break 
