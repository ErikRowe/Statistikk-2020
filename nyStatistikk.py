import math
import statistics

### Input: Liste med målinger
### Output: Standarddavvik
def avviksutregner(maalinger):

    gjennomsnitt = statistics.mean(maalinger)
    #print("Gjennomsnittet er: " + str(gjennomsnitt))

    diff = []
    for maling in maalinger:
        diff.append(gjennomsnitt - maling)
    # print("Differansene fra gjennomsnittet er:" + str(diff))

    diff_srqd = []
    for dif in diff:
        diff_srqd.append(dif ** 2)
    # print("Roten av alle differansene er: " + str(diff_srqd))

    varianse = 0
    for dif in diff_srqd:
        varianse += dif

    varianse /= len(diff_srqd)
    # print("Variansen er: " + str(varianse))

    stdavvik = math.sqrt(varianse)
    # print("Standarddavviket er: " + str(standarddavvik))

    return stdavvik

#Finner gjennomsnittlig antall steg brukt på å gå 5 meter og deler på 5 for å få gjennomsnittlig steglengde
steglengde_erik = 5/statistics.mean([7.0, 6.9, 6.9, 6.9, 6.9])
steglengde_sander = 5/statistics.mean([7.0, 7, 7, 7, 7])
steglengde_ask = 5/statistics.mean([5.4, 5.4, 5.4, 5.4, 5.4])
steglengde_aleks = 5/statistics.mean([7, 6.5, 6, 6, 6])
steglengde_bjorn = 5/statistics.mean([5.8, 5.8, 5.8, 5.6, 5])
steglengde_oskar = 5/statistics.mean([6, 6.5, 6.2, 6.2, 5.8])


#Lager en liste med hvert gruppemedlems gjennomsnittlig måling av lengden på broa i meter
lengdeListe = []
liste_erik_lengde = lengdeListe.append(statistics.mean([46.8, 46.9, 46.1, 47.2, 46.4])*steglengde_erik)
liste_sander_lengde = lengdeListe.append(statistics.mean([48.1, 46, 44.9, 45.7, 46.9])*steglengde_sander)
liste_ask_lengde = lengdeListe.append(statistics.mean([39.1, 40, 39.5, 38.8, 40.2])*steglengde_ask)
liste_aleks_lengde = lengdeListe.append(statistics.mean([41.1, 41.2, 40.8, 40.8, 41.2])*steglengde_aleks)
liste_bjorn_lengde = lengdeListe.append(statistics.mean([39.1, 39.5, 38.8, 39.7, 40.5])*steglengde_bjorn)
liste_oskar_lengde = lengdeListe.append(statistics.mean([44.8, 43.5, 42.8, 45.2, 43.5])*steglengde_oskar)
#print(lengdeListe)

#Lager in liste med hvert gruppemedlems gjennomsnittlig måling av bredden på broa i meter
breddeListe = []
liste_erik_bredde = breddeListe.append(statistics.mean([10.9, 11.2, 11.2, 11.2, 11.2])*steglengde_erik)
liste_sander_bredde = breddeListe.append(statistics.mean([11.7, 11.5, 11.9, 11.5, 12])*steglengde_sander)
liste_ask_bredde = breddeListe.append(statistics.mean([10, 9.4, 9.3, 9.4, 9.5])*steglengde_ask)
liste_aleks_bredde = breddeListe.append(statistics.mean([10.6, 10.5, 10, 10.5, 10.2])*steglengde_aleks)
liste_bjorn_bredde = breddeListe.append(statistics.mean([10.9, 10.3, 10.8, 10.8, 10.8])*steglengde_bjorn)
liste_oskar_bredde = breddeListe.append(statistics.mean([11.4, 11.3, 11.3, 11.4, 11.2])*steglengde_oskar)
#print(breddeListe)

#Finner standardavviket for både lengden og bredden.
#Dette blir da avviket mellom målingene til de forskjellige studentene
#ikke avviket mellom hver student sine egne målinger.
stdLengde = avviksutregner(lengdeListe)
stdBredde = avviksutregner(breddeListe)

#Den kombinerte usikkerheten sqrt(snittlenge^2*standarddavviket-til-bredden^2  +  snittbredden^2*standardavviket-til-lengden^2)
kombUsikkerhet = math.sqrt(statistics.mean(lengdeListe)**2 * stdBredde**2 + statistics.mean(breddeListe)**2 * stdLengde**2)
#print(kombUsikkerhet)


#print(statistics.mean(breddeListe))
areal = statistics.mean(lengdeListe) * statistics.mean(breddeListe)
#print(areal)

print("Arealet for broen er {}m^2 +- {}m^2".format(round(areal,1), round(kombUsikkerhet,1)))

#Antall folk som trengs for å halvere usikkerheten
n1 = 30
std = math.sqrt(n1)*kombUsikkerhet
n = ((std/(0.5*kombUsikkerhet))**2 - n1)/5
print("Det trengs " + str(round(n)) + " folk for å halvere usikkerheten.")










