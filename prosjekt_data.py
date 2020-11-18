# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 12:59:22 2020

@author: Erike

Dette prosjektet skal gjøre noe med en bro
"""
import math
### Input: Liste med målinger
### Output: Standarddavvik
def avviksutregner(maalinger):

    gjennomsnitt = 0
    for maling in maalinger:
        gjennomsnitt += maling
        #print(gjennomsnitt)

    gjennomsnitt /= len(maalinger)
    #print("Gjennomsnittet er: " + str(gjennomsnitt))

    diff = []
    for maling in maalinger:
        diff.append(gjennomsnitt - maling)
    #print("Differansene fra gjennomsnittet er:" + str(diff))

    diff_srqd = []
    for dif in diff:
        diff_srqd.append(dif**2)
    #print("Roten av alle differansene er: " + str(diff_srqd))

    varianse = 0
    for dif in diff_srqd:
        varianse += dif

    varianse /= len(diff_srqd)
    #print("Variansen er: " + str(varianse))

    stdavvik = math.sqrt(varianse)
    #print("Standarddavviket er: " + str(standarddavvik))

    return stdavvik

def areal_regning(li_lengde,u_l,li_bredde,u_b,li_steg,u_s,n):
    """
    Formelen for arealet blir lengde*bredde
    formel for usikkerheten for lengde og for bredde vil begge være:
        (skritt, omgjort til meter)*(antall skritt på avstanden)
        altså s*(l,b)
    usikkerhet bredde = u_b
    usikkerhet lengde = u_l
    usikkerhet steg = u_s
    Vi må finne ut kombinert standardusikkerhet, vi gjør dette gjennom en formel du kan finne i oppg 4: b og c
    
    """
    #Begynner med usikkerhet for lengde omgjort til meter
    #Da bruker vi formelen for kombinert usikkerhet for lengde og skritt
    ko_u_l= math.sqrt(((li_lengde[n])**2)*((u_l[n])**2)+((li_steg[n])**2)*((u_s[n])**2))
    print("lengde i skritt: ", li_lengde[n])
    print("kombinert u lengde: ",ko_u_l)
    
    #Her finner vi lengden i meter som vi skal bruke for aralet?
    x = li_lengde[n]*li_steg[n] #Her må vi ta med den kombinerte usikkerheten ko_u_l
    print("Lengde i meter: ",x)

    #Begynner med usikkerhet for bredde omgjort til meter
    #Da bruker vi formelen for kombinert usikkerhet for bredde og skritt
    ko_u_b= math.sqrt(((li_bredde[n])**2)*((u_b[n])**2)+((li_steg[n])**2)*((u_s[n])**2))
    print("Bredde i skritt: ",li_bredde[n])
    print("Kombinert u bredde",ko_u_b)

    #Her finner vi lengden i meter som vi skal bruke for aralet?
    y = li_bredde[n]*li_steg[n] #Her må vi ta med den kombinerte usikkerheten ko_u_b
    print("Lengde i meter: ",y)
    
    areal_list=[]
    ko_standardusikkerhet = math.sqrt(((x)**2)*((ko_u_l)**2)+((y)**2)*((ko_u_b)**2))
    areal_list.append(ko_standardusikkerhet)
    #print(ko_standardusikkerhet)
    print("""
          
          """)
    return areal_list



lengde_bro = 36
bredde_bro = 8.9

n_målinger = 5

list_standardavvik_lengde=[]
list_standardavvik_bredde=[]
list_standardavvik_steg=[]


liste_erik_lengde = [46.8,46.9,46.1,47.2,46.4]
liste_sander_lengde = [48.1,46,44.9,45.7,46.9]
liste_ask_lengde = [39.1,40,39.5,38.8,40.2]
liste_aleks_lengde = [41.1,41.2,40.8,40.8,41.2]
liste_bjørn_lengde = [39.1,39.5,38.8,39.7,40.5]
liste_oskar_lengde = [44.8,43.5,42.8,45.2,43.5,46]
liste_lengde=[liste_erik_lengde,liste_sander_lengde,liste_ask_lengde,liste_aleks_lengde,liste_bjørn_lengde,liste_oskar_lengde]

for i in liste_lengde:
    list_standardavvik_lengde.append(avviksutregner(i))

for n in liste_lengde:
    line_sum = (sum(n))/n_målinger
    i= liste_lengde.index(n)
    liste_lengde[i]=line_sum
    

    
        
"""
Listene med 5 antall målinger, hvor vi testet antall steg over 
"""
liste_erik_bredde = [10.9,11.2,11.2,11.2,11.2]
liste_sander_bredde = [11.7,11.5,11.9,11.5,12]
liste_ask_bredde = [10,9.4,9.3,9.4,9.5]
liste_aleks_bredde = [10.6,10.5,10,10.5,10.2]
liste_bjørn_bredde = [10.9,10.3,10.8,10.8,10.8]
liste_oskar_bredde = [11.4,11.3,11.3,11.4,11.2]
liste_bredde=[liste_erik_bredde,liste_sander_bredde,liste_ask_bredde,liste_aleks_bredde,liste_bjørn_bredde,liste_oskar_bredde]

for i in liste_bredde:
    list_standardavvik_bredde.append(avviksutregner(i))

for n in liste_bredde:
    line_sum = (sum(n))/n_målinger
    i= liste_bredde.index(n)
    liste_bredde[i]=line_sum
    

"""
Her viser antal steg vi brukte på 5 meter.
Alle målte hvor mange steg på samme avstanden 5 ganger
"""
steglengde_erik = [7.0,6.9,6.9,6.9,6.9]
steglengde_sander = [7.0,7,7,7,7]
steglengde_ask = [5.4,5.4,5.4,5.4,5.4]
steglengde_aleks = [7,6.5,6,6,6]
steglengde_bjørn = [5.8,5.8,5.8,5.6,5]
steglengde_oskar = [6,6.5,6.2,6.2,5.8]
liste_steglengde = [steglengde_erik,steglengde_sander,steglengde_ask,steglengde_aleks,steglengde_bjørn,steglengde_oskar]

for i in liste_steglengde:
    list_standardavvik_steg.append(avviksutregner(i))

for n in liste_steglengde: #Loopen vil gjøre om dataen til antall meter pr gjennomsnitlig steg
    line_sum = ((sum(n))/n_målinger)/5
    meter=(1/line_sum)
    i= liste_steglengde.index(n)
    liste_steglengde[i]=meter


a=liste_lengde
b=list_standardavvik_lengde
c=liste_bredde
d=list_standardavvik_bredde
e=liste_steglengde
f=list_standardavvik_steg
areal = []
    
for i in range(0,6):
    areal =areal_regning(a,b,c,d,e,f,i)


#print(areal)
    
    

