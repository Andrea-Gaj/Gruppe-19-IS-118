#========================================================
# IS-118 - Gruppeoppgave 2: Interaktiv Historie
#========================================================

print("=================================================================================")
print("             VELKOMMEN TIL MEDBORGERPORTALEN: ERLINGS PROSJEKTEVENTYR!            ")
print("=================================================================================")

print()
print()

navn = input("Hva heter du? ")
print()
print(f"Hei {navn}, gjør deg klar til å hjelpe Prosjeklederen Erling med å løse konflikter.") 

print()

print("Erlings prosjekt har vart i seks uker og Teamet har havnet i 'storming-fasen'.")
print("I tverrfaglige team kolliderer ulike faglige perspektiver. Konflikter oppsto i teamet mellom ulike medlemmer")

print()

input("Trykk ENTER for å fortsette til neste beslutningspunkt...")


#-------------------------------------------------------------------------------------
# Beslutningspunkt 1: Konflikt mellom Silje og Elias. Sakskonflikt vs Personkonflikt.
#-------------------------------------------------------------------------------------

print()

print("Uenighet om teknologi og design har utviklet seg til en personlig konflikt mellom Silje (UX) og Elias (IT).")
print("hjelp Erling med beslutningsprosess for å løse konflikten.")

print()
print()

print("A) Ta individuelle samtaler.")
print("B) Ta det opp i plenum.")

print()
      
valg_1=input("hva ønsker du å gjøre? (svar med A eller B): ")

print()

while valg_1 not in ["A", "B"]:
    print("dette er ikke et mulig valg! Erling ser rart på deg i skam")
    valg_1 = input("Prøv igjen. Hva ønsker du å gjøre? (Svar med A eller B): ").strip().upper()
if valg_1 == "A":
    print("\n-> Individuelle samtaler demper temperatur")
    print("   Du ivaretar den psykologiske tryggheten.")
elif valg_1 == "B":
    print("\n-> Plenumsmøtet blir svært opphetet.")
    print("   åpen konfrontasjon kan øke sårbarheten, men det tvinger frem skjulte agendaer.")

print()

input("Trykk ENTER for å fortsette til neste beslutningspunkt...")

#-------------------------------------------------------------------------------------------------
# Beslutningspunkt 2: Konflikt mellom Hamdi og Hallgeir. Interne vs Eksterne interesser.
#-------------------------------------------------------------------------------------------------


print ()

print("Konfliktene tar ikke slutt, og med dem følger andre vanskelige avgjørelser for Erling.")
print()
print("Hamdi (kulturavdelingen) og Hallgeir (brukerrepresentant) er uenige")
print("De krangler om innbyggerdialogen: Kontrollert plattform (Hamdi) vs Åpent system (Hallgeir).")

print()
print()

print("A) Arranger et felles meklingsmøte for å finne et tverrfaglig kompromiss.")
print("B) Avvent situasjonen. La partene løse det selv for å fremme autonomi.")

print()

valg_2=input("hva ønsker du å gjøre? (svar med A eller B): ")

print()


while valg_2 not in ["A", "B"]:
    print("dette er ikke et mulig valg! Erling forlater rommet, sjokkert over trekket ditt. Du løper etter ham med øyne fulle av anger.")
    valg_2 = input("Prøv igjen. Hva ønsker du å gjøre? (Svar med A eller B): ").strip().upper()
if valg_2 == "A":
    print("\n-> Suksess! Dere integrerer begge perspektiver til en felles løsning.")
    print("   Dette viser god utnyttelse av tverrfaglig kompetanse.")
elif valg_2 == "B":
    print("\n-> Frustrasjonen ulmer videre. Uten strukturert ledelse.")
    print("   låser konflikten seg, og kommunikasjonen stopper opp.")

print()

input("Trykk ENTER for å fortsette til siste beslutningspunkt...")

# ---------------------------------------------------------------------
# BESLUTNINGSPUNKT 3: Bevare Motivasjon i Teamet (Mål vs Mennesker)
# ---------------------------------------------------------------------

print()

print("Det er tre uker til prototypen skal leveres. Teamet er slitent og stresset.")
print("Erling vet at hans neste valg kan avgjøre om teamet beveger seg videre mot “Norming”")

print()

print("A) Prioriter relasjoner: Sett av tid til teambuilding og sosialt samvær.")
print("B) Prioriter fremdrift: Ha strengt fokus på leveranser og harde tidsfrister.")

print()


valg_3=input("hva ønsker du å gjøre? (svar med A eller B): ")

print()


while valg_3 not in ["A", "B"]:
    print("dette er ikke et mulig valg! Erling stirrer ut i luften med tomme øyne og lurer på hva han har gjort galt for å fortjene denne samtalen.")
    valg_3 = input("Prøv igjen. Hva ønsker du å gjøre? (Svar med A eller B): ").strip().upper()
if valg_3 == "A":
    print("\n-> Tilliten gjenopprettes og motivasjonen øker")
    print("   men tidsplanen for prototypen blir ekstremt stram.")
elif valg_3 == "B":
    print("\n-> Oppgavefokuset sikrer fremdrift på kort sikt.")
    print("   men det emosjonelle klimaet forblir kjølig og sårbart.")


print()
print()


if valg_1 == "A" and valg_2 == "A" and valg_3 == "A":
    print("🏆 UTFALL 1: SUKSESS! VEIEN TIL NORMING! GRATULER MED RESULTAT")
elif valg_1 == "A" and valg_2 == "A" and valg_3 == "B":
    print("⚠️ UTFALL 2: DELRESULTAT, PROTOTYPEKLAR MEN SPENT ATMOSFÆRE I TEAMET.") 
else:
    print("❌ UTFALL 3: KRYSE, KONFLIKTEN ESKALERTE MED ALVORLIG FORSINKELSE I PROSJEKT")
    print("PRØV PÅ NYTT")