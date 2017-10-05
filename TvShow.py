serie = json.loads(r)
print (serie)

nom_serie = serie["name"] # Pour récupérer le nom de la série
print (nom_serie)

resume = serie["overview"] # Pour récupérer le résumé d'une série
print (resume)

nb_saison = serie["number_of_seasons"] # Pour récupérer le nombre de saisons dans la série
print(nb_saison)

en_production = serie["in_production"] # savoir si la série est toujours en production
if en_production:
    print("En cours")
else:
    print("Plus en cours")