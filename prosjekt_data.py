# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 12:59:22 2020

@author: Erike

Dette prosjektet skal gjøre noe med en bro
"""
lengde_bro = 36
bredde_bro = 4.9

n_målinger = 5


liste_erik_lengde = [46.8,46.9,46.1,47.2,46.4]
liste_sander_lengde = [48.1,46,44.9,45.7,46.9]
liste_ask_lengde = [39.1,40,39.5,38.8,40.2]
liste_aleks_lengde = [41.1,41.2,40.8,40.8,41.2]
liste_bjørn_lengde = [39.1,39.5,38.8,39.7,40.5]
liste_oskar_lengde = [44.8,43.5,42.8,45.2,43.5,46]
liste_lengde=[liste_erik_lengde,liste_sander_lengde,liste_ask_lengde,liste_aleks_lengde,liste_bjørn_lengde,liste_oskar_lengde]

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

for n in liste_bredde:
    line_sum = (sum(n))/n_målinger
    i= liste_bredde.index(n)
    liste_bredde[i]=line_sum
    

"""
Her viser antal steg vi brukte på 5 meter.
Alle målte hvor mange steg på samme avstanden 5 ganger
"""
steglengde_erik = [7,6.9,6.9,6.9,6.9]
steglengde_sander = [7,7,7,7,7]
steglengde_ask = [5.4,5.4,5.4,5.4,5.4]
steglengde_aleks = [7,6.5,6,6,6]
steglengde_bjørn = [5.8,5.8,5.8,5.6,5,6]
steglengde_oskar = [6,6.5,6.2,6.2,5.8]
liste_steglengde = [steglengde_erik,steglengde_sander,steglengde_ask,steglengde_aleks,steglengde_bjørn,steglengde_oskar]

for n in liste_steglengde:
    line_sum = (sum(n))/n_målinger
    i= liste_steglengde.index(n)
    liste_steglengde[i]=line_sum
