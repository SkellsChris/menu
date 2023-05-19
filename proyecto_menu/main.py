import pandas
import random
import pandas as pd


def input_budget():
    budget = float(input("Quel est le budget ? : "))
    return budget

def input_doublon():
    doublon = input("Acceptez vous les doublons ? (oui/non) : ").lower()
    return doublon

#Critères
nbr_jours = int(input("Pour combien de jours souhaitez vous le menu ? : "))
budget = input_budget()
doublon = input_doublon()
cumul_prix = 0        #Pour cumuler les prix du menu généré aléatoirement

#Transformation du csv via Pandas
data = pandas.read_csv("plats.csv")
DF_plat_prix_croissant = data.sort_values(by=["Precio total"])
DF_plat_prix_croissant = DF_plat_prix_croissant["Precio total"]
DF_plat_prix_croissant.reset_index(drop=True, inplace=True)
plat_le_moins_cher = int(DF_plat_prix_croissant.iloc[0])
DF_plat_prix_cumules = DF_plat_prix_croissant.cumsum()
#Creation menu
menu = pandas.DataFrame()
menu_modifie_manuellement = pandas.DataFrame()
#While flag
fin_du_menu = 0
validated_menu = False
#Génération du menu

while fin_du_menu != nbr_jours and not data.empty and validated_menu != True:
    selection = random.choice(data["Plats"])                  #Sélection au hasard d'un plat (output ex : "Lasagna")
    ligne_complette = data[data["Plats"] == selection]        #Récupération de la ligne complète avec les ingrédients et le prix
    prix_ligne_complette = float(ligne_complette["Precio total"])       #Récupération du prix en float

    if doublon == "oui":
        if (cumul_prix + prix_ligne_complette) < budget:
            cumul_prix += prix_ligne_complette
            tab_temporaire = pandas.DataFrame(ligne_complette)    #Stockage de la ligne complete dans un tableau temporaire
            menu = pandas.concat([menu, tab_temporaire])          #Concatenation du tableau permanent menu avec le temporaire
            menu = menu.sort_values(by=["Precio total"])                  #Trie du DataFrame afin d'avoir le prix le plus cher a la fin
            fin_du_menu += 1
            menu.reset_index(drop=True, inplace=True)             #reindexation afin d'éviter de supprimer plusieurs éléments ayant le meme index
        elif (cumul_prix + prix_ligne_complette) > budget and budget >= (plat_le_moins_cher * nbr_jours ): #A MODIFFFFFFFFFF
            print(menu)
            if not menu.empty:
                menu = menu.drop(index=menu.index[-1],axis=0)         #Suppression de la derniere ligne (qui est donc la plus chere)
                cumul_prix = menu["Precio total"].sum()
                fin_du_menu -= 1
                menu.reset_index(drop=True, inplace=True)   #reindexation afin d'éviter de supprimer plusieurs éléments ayant le meme index
            else:
                selection = random.choice(data["Plats"])  # Sélection au hasard d'un plat (output ex : "Lasagna")
                ligne_complette = data[data["Plats"] == selection]  # Récupération de la ligne complète avec les ingrédients et le prix
                prix_ligne_complette = float(ligne_complette["Precio total"])  # Récupération du prix en float
        else:
            print(f"Le budget est insuffisant, veuillez en entrer un nouveau.")
            budget = input_budget()
    elif doublon == "non":
        if budget >= int(DF_plat_prix_cumules.iloc[nbr_jours-1]):
            if selection in menu.values:                                      #Vérifie si le plat séléctionné est une valeur déja présente dans le DataFrame
                selection = random.choice(data["Plats"])
            elif not selection in menu.values:                                #Vérifie s'il y a une colonne Prix
                if (cumul_prix + prix_ligne_complette) <= budget:
                    cumul_prix += prix_ligne_complette
                    tab_temporaire = pandas.DataFrame(ligne_complette)    #Stockage de la ligne complete dans un tableau temporaire
                    menu = pandas.concat([menu, tab_temporaire])          #Concatenation du tableau permanent menu avec le temporaire
                    menu = menu.sort_values(by=["Precio total"])                  #Trie du DataFrame afin d'avoir le prix le plus cher a la fin
                    fin_du_menu += 1
                    menu.reset_index(drop=True, inplace=True)             #reindexation afin d'éviter de supprimer plusieurs éléments ayant le meme index
                elif (cumul_prix + prix_ligne_complette) > budget and menu.empty:
                    selection = random.choice(data["Plats"])  # Sélection au hasard d'un plat (output ex : "Lasagna")
                    ligne_complette = data[data["Plats"] == selection]  # Récupération de la ligne complète avec les ingrédients et le prix
                    prix_ligne_complette = float(ligne_complette["Precio total"])  # Récupération du prix en float
                else:
                    print(menu)
                    menu = menu.drop(index=menu.index[-1],axis=0)         #Suppression de la derniere ligne (qui est donc la plus chere)
                    cumul_prix = menu["Precio total"].sum()
                    fin_du_menu -= 1
                    menu.reset_index(drop=True, inplace=True)             #reindexation afin d'éviter de supprimer plusieurs éléments ayant le meme index
            else:
                print("Réponse incorrecte, vous devez saisir oui ou non")
                doublon = input_doublon()
        else:
            print(f"Le budget est insuffisant, veuillez en entrer un nouveau.")
            budget = input_budget()
    else:
        print("Réponse incorrecte, vous devez saisir oui ou non")
        doublon = input_doublon()
#Le menu est créé dans sa totalité. Validation de celui-ci :
    if fin_du_menu == nbr_jours:
        print(menu)
        confirmation_menu = input("Voulez vous garder dans sa totalité le menu suivant oui ou non ? :").lower()
        if confirmation_menu == "non":
            index_a_supprimer = int(input("Quelles lignes souhaitez vous supprimer (indiquez le numéro d'index) :"))
            menu = menu.drop(index=menu.index[index_a_supprimer], axis=0)
            fin_du_menu -= 1
            menu.reset_index(drop=True, inplace=True)
        else:
            validated_menu = True



#TODO créer une option pour choisir le nombre de plat contenant de la viande, poisson etc
#TODO créer une option pour inclure un certain nombre de plats anti pso
#TODO faire le refactoring
#TODO possibilité de garder un ou plusieurs plat parmis la proposition de menu et de continuer a en generer d'autres en deduisant la somme du ou des plats gardés

menu_en_string = menu.to_string(index=False)
with open("Menu.txt","w") as file:
    file.write(menu_en_string)

print(f"dépense total {cumul_prix}")

INGREDIENTE = "Ingrediente "
QTDAD = "Qtdad "

#Création de la liste des ingrédients - création tableau
liste_ingrédients = []
liste_quantite = []

#Récupération des ingrédients pour chaque plat
for x in range(9):
    for y in range(nbr_jours):
        if menu[INGREDIENTE + str(x+1)].iloc[y]:
            liste_ingrédients.append(menu[INGREDIENTE + str(x+1)].iloc[y])
            liste_quantite.append(menu[QTDAD + str(x + 1)].iloc[y])

#Transformation de la liste en DataFrame
pd_liste_ingredient = pd.DataFrame(data=liste_ingrédients, columns=['Ingredientes'] )
pd_liste_ingredient['Cantidad'] = liste_quantite


#Élimination des NaN de la liste et stockage dans une nouvelle liste
liste_ingredients_sans_nan = pd_liste_ingredient.dropna()
liste_ingredients_sans_nan.reset_index(drop=True, inplace=True)

df_to_list = liste_ingredients_sans_nan.values.tolist()


list_group = liste_ingredients_sans_nan.groupby('Ingredientes').sum()

list_group.reset_index(inplace=True)
print(list_group)
liste_groupedBy = list_group.values.tolist()
print(liste_groupedBy)


liste_finale_sans_doublon_string = list_group.to_string(index=False)
with open("Lista.txt","w") as file:
    file.write(liste_finale_sans_doublon_string)

