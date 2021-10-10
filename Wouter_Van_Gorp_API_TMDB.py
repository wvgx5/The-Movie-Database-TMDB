#modules importeren
import datetime                 # gebruik van uur en maand
import requests                 # opvragen van gegevens
import urllib.parse             # om uit de url gegevens te halen
from tabulate import tabulate   # tabellen
from datetime import date       # dag en datums
import calendar                 # variable voor dag van de week

#start variabelen aanmaken en read access token invullen
titel = "" # variable voor titel
baseurl = "https://api.themoviedb.org/3/" # variable voor url
apiTok = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3OWVjMGRiZjYxODYxYTMxZTVkY2NlNTgyMjk2NTNmMiIsInN1YiI6IjYxNWQ0ODU0ZWIxNGZhMDA0M2UyMTg3NCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.9tBLmGPzHrnklKV7KJkMewpR9FmDb_2nFkPOSeXhzEo" # api v4 token
headers = {'Authorization': 'Bearer ' + apiTok}

#datum
today = date.today()
d1 = today.strftime("%d/%m/%Y")
#dag
curr_date = date.today()
#uur + maand
e = datetime.datetime.now()

# print calender gegevens
print("******************************************************************************* ")
print("tijd:  %s:%s:%s" % (e.hour, e.minute, e.second)) # print uur
print("datum:            ", d1) # print datum calender
print("dag van de week:  ", calendar.day_name[curr_date.weekday()]) # print datum dag
print("maand:           ", e.strftime('%B')) # print maand (engels)
print("*******************************************************************************")
# print sjabloon
print("                                       /\ ")
print("                                      /  \ ")
print("                                     / /\ \ ")
print("                                    / /  \ \ ")
print("                                   / /    \ \ ")
print("                                  / /      \ \ ")
print("                                 / /        \ \ ")
print("                                / /          \ \ ")
print("                               / /            \ \ ")
print("_ _____  _ _ _  ___ __________/ /              \ \_____________________________")
print("`|_   _|| |_| || __|___________/                \________________________  ,-'")
print("   | |`-|  _  || _|                                                  ,-',-'")
print("   |_|`-|_| |_||___|                                             _,-',-'")
print("  ____    `-.`-____        ____        ___      ___  ___  _____,-_,-'________")
print(" |    \      `/    |    ,-'    `-.    |   |    |   ||   ||        | /        |")
print(" |     \     /     |-.,'  __  __  `.  |   |    |   ||   ||    ____||    _____|")
print(" |      \   /      |-/   /  \/  \   \ |   |    |   ||   ||   |____ |   (____")
print(" |       \_/       ||    \      /    ||   |    |   ||   ||        ||        \ ")
print(" |   |\       /|   ||     |     ]    | \   \  /   / |   ||    ____| \____    |")
print(" |   | \     / |   |/\    |____|    /   \   \/   /  |   ||   |____  _____)   |")
print(" |   |  \   /  |   | / .  ,' | `. ,'   , \      /   |   ||        ||         |")
print(" |___|   \_/   |___|/   `-.____,-'  ,-',`-\____/    |___||________||________/")
print("                 / /             ,-',-' `-.`-.             \ \ ")
print("                / /           ,-',-'       `-.`-.           \ \ ")
print("               / /         ,-',-'             `-.`-.         \ \ ")
print("              / /       ,-',-'                   `-.`-.       \ \ ")
print("             / /     ,-',-'                         `-.`-.     \ \ ")
print("            / /   ,-',-'                               `-.`-.   \ \ ")
print("           / / ,-',-'                                     `-.`-. \ \ ")
print("          / /-',-'                                           `-.`-\ \ ")
print("         /_,-'`                                                 `'-._\ ")
#invullen van een naam
while True:
    name = input("\nwat is jou naam? ")
    if name.isalpha():
        break
    # controle dat het letters zijn
    print("alleen karakters A-Z.")
print("******************************************************************************* ")
print("        Welcome " + name + ", to the Movie database !            ")
print("******************************************************************************* \n")
# vragen naar de film of om te stoppen
while titel != "S":
    titel = input("Welke film wil je zoeken " + name +" ? druk S om te stoppen: ")
    if titel == "S":
        break
    # url wordt samengesteld aan de hand van de baseurl + de search functie met als parameter de titel van een film dat je zoekt.
    url = baseurl + "search/movie?" + urllib.parse.urlencode({"query":titel})
    json_data = requests.get(url,headers=headers).json()

    print(url)
    #lijst met resultaten wordt iedere keer opnieuw gemaakt
    resultaat = []
    #voor elk resultaat dat er is wordt dit toegevoegd aan de lijst resultaten
    for result in json_data["results"]:
        resultaat.append([result["popularity"], result["id"], result["title"], result["release_date"]])
    #met behulp van tabulate worden de resultaten afgeprint in een tabel.
    if resultaat == [] :
        print('geen films gevonden met deze naam')
    #afprinten van tabellen
    else:
        print(tabulate(resultaat, headers=["populariteit", "id", "titel", "release datum"]))