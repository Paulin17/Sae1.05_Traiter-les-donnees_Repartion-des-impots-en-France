import opening

##Ouverture des fichier utiliser

nb_foyer_par_dept=opening.departement("csv/dept_nb_foyer.csv")
montants_par_dept=opening.departement("csv/dept_montant_impot.csv")


##Fonction de renversement, plus de détatailles dans le docstring
def renversement(dictionaire):
    """prend en paramètre un des dictionnaires précédents et va renverser le rangement
    de dépt:{année:valeur,...} à année:{dépt:valeur,...}"""
    resultat={}
    for i in range (2014,2022): #Création du dictionaire de resultat vide
        resultat[i] = {}
    for departement,dict2 in dictionaire.items():#Pour chaque clé/valeur on recuper le deuxieme dictionaire
        for anne, montant in dict2.items():#On recuper l'anne et le montant dans le deuxieme dictionaire
            resultat[anne][departement]=montant #On range tout sa corectement dans le dictionaire de resultat.
    return resultat

##Programes de calculs de l'impot sur le revenue moyen et médian: 1&2 sur un département de 2014 a 2022 3&4 sur une anné a l'echelle nationale.

def moyenne_dept_sur_periode(dept):
    """Renvoie la valeur de l'impôt sur le revenu moyen de 2015 à 2022 dans le département en question"""
    somme=0 #on intialise une somme et un compteur à zero
    cpt=0

    departement=montants_par_dept[str(dept)] #On recupere un dictionaire contenant uniquement les donné du département

    for montant in departement.values():    #On parcours les valeur de celui si en les sommant
        somme+=montant
        cpt+=1
    return somme/cpt    #On renvoie un calcul de moyenne.

def mediane_dept_sur_periode(dept):
    """Prend en paramètre le numéro d'un département et renvoie l'impôt médian de 2015 à 2022"""

    departement=list(montants_par_dept[str(dept)].values())  # On crée un dictionaire contenant uniquement les donné du département et on recuper uniquement les valeurs de celui si sous forme d'une liste.
    departement.sort()  #On trie la liste

    longeur=len(departement)    #Comme on va en avoir besoin plusieur fois on pose une variable

    if longeur%2==1:#si la taille de la liste est impaire
        return departement[longeur//2]  #On renvoie l'element au milieut
    else:   #Sinon on prend la moyenne des deux éléments du milieux.
        return (departement[longeur//2]+departement[longeur//2-1])/2

def moyenne_annuel_national(anné):
    """
    Prend une année en entrée
    et renvoie la valeur de l'impôt sur le revenu moyen de cette année-là à l'échelle nationale
    """
    somme=0
    cpt=0
    dicto_renversé=renversement(montants_par_dept)[anné] #on renverse le dictionaire et on recuper l'anné qui nous interesse

    for montant in dicto_renversé.values():
        somme+=montant
        cpt+=1
    return somme/cpt


def medianne_annuel_national(anné):
    """Prend un année en entrée
    et renvoie la valeur de l'impôt sur le revenu médian de cette anneé-là à l'échelle nationale
    """
    dicto_renversé=list(renversement(montants_par_dept)[anné].values())    #on renverse le dictionaire et on recuper l'anné qui nous interesse pui on le transforme en liste
    dicto_renversé.sort()

    longeur=len(dicto_renversé)    #Comme on va en avoir besoin plusieur fois on pose une variable

    if longeur%2==1:#si la taille de la liste est impaire
        return dicto_renversé[longeur//2]  #On renvoie l'element au milieux

    else:   #Sinon on prend la moyenne des deux éléments du milieux.
        return (dicto_renversé[longeur//2]+dicto_renversé[longeur//2-1])/2

##Acroisement brut
def taux_accroissement_brut(anné_debut,anné_fin,dept):
    """Cette fonction prend en paramètre deux années
    et renvoie le taux d'évolution de l'impôt sur le revenu sur un département
    """
    dept=str(dept)
    montant_y1 = montants_par_dept[dept][anné_debut]    #On recuper le montant de chaque département sur l'anné ciblé
    montant_y2 = montants_par_dept[dept][anné_fin]
    return (montant_y2 / montant_y1 - 1) * 100  #On renvoie le rapport des deux


def accroissement_tous_departementS(anné_debut=2014,anné_fin=2021):
    """Prend en paramètre une année de début et de fin
    renvoie le taux d'accroissement pour chaque département sur une période donnée ou par défaut 2014 à 2021 soit la moyenne"""
    resultat={}
    for dept in montants_par_dept.keys():#On parcour tout les département
        resultat[dept]= taux_accroissement_brut(anné_debut, anné_fin,str(dept))  #Pour chacun d'eux on recupere le taux d'acroissemnt souhaité et on le met dans le dictionaire de résultat.
    return resultat

def get_all_accroissement_y_b_y():
    """Ne prend aucun paramètre,
    renvoie l'accroissement de tous les départements d'une année en une année"""
    resultat={}
    for année in range(2015,2022):#On parcour tout les anné qui on une précedente et on compare l'évolution
        resultat[année]=accroissement_tous_departementS(année - 1, année)
    return resultat

##Raport Population

def rapport_population(anné):
    """Prend en paramètre une année,
    et renvoie le montant d'impôt payé cette année-là par personne majeure sur tous les dépt."""
    resultat={}
    dict_population = opening.population("csv/pop_" + str(anné) + ".csv")
    for dept,population in dict_population.items():
        resultat[dept]=montants_par_dept[dept][anné]/population*1000000
    return resultat

def rapport_foyer_fiscaux(anné):
    """Prend en paramètre une année
    et renvoie le montant d'impôt payé cette année-là par foyer fiscal sur tous les dépt."""
    resultat={}
    for dept,foyer in nb_foyer_par_dept.items():
        resultat[dept]=montants_par_dept[dept][anné]/(foyer[anné]*1000)*1000000
    return resultat



##Acroisement des rapports
def taux_accroissement_rapport(type, anné_debut=2014, anné_fin=2021):
    """prend en paramètre deux années et un type(population ou foyer)
    renvoie le taux d'évolution de tous les départements entre les deux années et sur le type spécifié."""
    resultat={}
    if type =='population' :
        rapport_y1 = rapport_population(anné_debut)
        rapport_y2 = rapport_population(anné_fin)
        for dept in nb_foyer_par_dept.keys():
            resultat[dept]=(rapport_y2[dept]/rapport_y1[dept]-1)*100
        return resultat
    elif type =='foyer':
        rapport_y1 = rapport_foyer_fiscaux(anné_debut)
        rapport_y2 = rapport_foyer_fiscaux(anné_fin)
        for dept in nb_foyer_par_dept.keys():
            resultat[dept] = (rapport_y2[dept] / rapport_y1[dept] - 1) * 100
        return resultat
    else:
        return 'erreur de type'

def get_all_accroissement_rapport_y_b_y(type):
    """Ne prend aucun paramètre,
        renvoie l'accroissement de tous les rapports du type spécifié sur tous les départements d'une année en une année"""
    resultat = {}
    for année in range(2015, 2022):  # On parcour tout les anné qui on une précedente et on compare l'évolution
        resultat[année] = taux_accroissement_rapport(type,année - 1, année)
    return resultat

def classement(dict:dict):
    """Prend un dictionnaire de type {dept:valeur,...}
    et classe les départements dans l'ordre de valeurs croissantes"""
    resultat=[]
    cpt=0
    while cpt!=len(list(montants_par_dept.keys())):
        min=[list(dict.keys())[0],float(list(dict.values())[0])]
        for dept,montant in dict.items():
            if montant<min[1]:
                min=[dept,montant]
        dict.pop(min[0])
        cpt+=1
        resultat.append(min)
    return resultat