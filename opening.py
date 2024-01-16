import csv

def population(fichier_population):
    '''Cette fonction sert à ouvrir les fichiers .csv contenant la répartition démographique pour chacun des départements.
Elle prend en paramètre un seul argument, qui est le nom du fichier à ouvrir.
Et renvoie un dictionnaire avec comme clé le  numéro de département et en valeur le nombre de résidents.'''

    resultat={}

    with open(fichier_population,'r') as fil:
        donnes=csv.reader(fil, delimiter=';') #On utilise la bibliothèque csv pour ouvrir le fichier avec le délimiteur ;
        next(donnes)    #On saute la première ligne qui est une légende.
        for ligne in donnes:
            clef=ligne[0]
            valeur=0
            for col in range (2,18):    #On somme les colonnes 2 à 17, car la population est répartie par tranche d'âge et ce n'est pas ce qui nous intéresse ici.
                valeur+=int(ligne[col])
            resultat[clef]=valeur
    return resultat

def recette_fiscale(fichier_recette):
    '''Cette fonction sert à ouvrir le fichier .csv contenant les recette d'imposition brut
    Elle prend en parametre le fichier a ouvrir.
    En sortie se programme renvoie un dictionnaire, contenant en clé le nom de l'impot revenue et en en valeur un dictionaire avec qui a en clé l'anné et en valeur le montant.'''

    resultat = dict()

    with open(fichier_recette, 'r') as f:
        données = csv.reader(f, delimiter=';')#On utilise la bibliothèque csv pour ouvrir le fichier avec le délimiteur ;
        next(données)
        for ligne in données:
            clef = ligne[0]
            valeur = {} #Création du deuxieme dictionaire
            for col in range (1,14):
                valeur[2009+col]=int(ligne[col]) #on ajoute un element corespondant a chaque anné(la clé) et le montant(valeur)
            resultat[clef] = valeur
    return resultat

def departement(fichier_dept):
    '''Cette fonction prend en entré le nom de fichier à ouvrir,
    en locurence les fichier contenant le nb de foyer fiscaux et montant des impot sur le revenue pour chaque départements
    En sortie la fonction renvoie une dictionaire, contenant en clé le numéro de dept et en valeur un autre dictionaire,
    Pour ce second, en clé l'anné et la valeur dpt du fichier ouvert, ou bien le montant ou le nb de foyer fiscaux.'''

    resultat = dict()

    with open(fichier_dept, 'r') as f:
        données = csv.reader(f, delimiter=';') #On utilise la bibliothèque csv pour ouvrir le fichier avec le délimiteur ;
        next(données) #on skip la premier ligne qui est une légendes
        for ligne in données:
            clef = ligne[0]
            valeur = {} #Création du deuxieme dictionaire
            for col in range (2,10): #les colones 2 a 9 sont celle on les donné sont.
                valeur[2012+col]=int(ligne[col]) #on ajoute un element corespondant a chaque anné(la clé) et le montant ou le nb de foyer fiscaux (valeur)
            resultat[clef] = valeur
    return resultat

#print(population("csv/pop_2014.csv"))
#print(recette_fiscale("csv/recettes_fiscales_brutes.csv"))
#print(departement("csv/dept_montant_impot.csv"))
#print(opening.departement("csv/dept_nb_foyer.csv"))