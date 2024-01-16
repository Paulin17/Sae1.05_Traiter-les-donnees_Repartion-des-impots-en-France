import opening

def recette_fiscale_année(année):
    '''
    Prend une année en entrée
    retourne le type d'impot et sa valeur de cette année là
    '''

    année = int(année)
    resultats= {}
    données = opening.recette_fiscale("csv/recettes_fiscales_brutes.csv")

    for type_impot, valeurs_par_année in données.items():
        if année in valeurs_par_année:
            resultats[type_impot] = valeurs_par_année[année]
        else:
            resultats[type_impot] = 0

    return(resultats)

def somme_année(resultats):
    '''
    prend un dictionnaire
    retourne la somme de l'année donnée
    '''
    total = sum(valeur for cle, valeur in resultats.items() if cle != 'total') #provisoire

    return(total)

def évolution_type(année1, année2, type_impot):
    '''
    prend deux années et le type d'impot
    retourne l'évolution du type en %
    '''
    année1 = recette_fiscale_année(année1)
    année2= recette_fiscale_année(année2)

    if type_impot in année1 and type_impot in année2:
        évo = (année2[type_impot] / année1[type_impot] - 1) * 100
        return évo
    else:
        return None

def liste_évolution(type_impot):
    '''
    prend un type
    retourne une liste l'évolution d'un tupe d'impot pour chaque année
    '''
    évolutions = []

    for année in range(2010, 2022):
        évo_type = évolution_type(année, année + 1, type_impot)
        évolutions.append(évo_type)

    return évolutions

def plus_grosse_année_dévo_type(type_impot):
    '''
    prend le type d'impot
    retourne l'évolution de la plus grande avec son année
    '''
    évolutions = liste_évolution(type_impot)

    liste_évolutions = [[annee, evolution] for annee, evolution in zip(range(2010, 2022), évolutions)]

    liste_évolutions_triee = sorted(liste_évolutions, key=lambda x: x[1], reverse=True)

    année_max_évolution, max_évolution = liste_évolutions_triee[0]

    return(année_max_évolution, max_évolution)

def classement_plus_grande_augmentation_par_année():
    '''
    fonction pour faire le classement de l'impôt qui a le plus augmenté par intervalle d'année
    '''
    années = list(range(2010, 2022))
    types_impots = ["impôt_revenu", "impôts_locaux", "impôt_sociétés", "autres_impôts", "taxe_énergétiques", "tva",
                    "taxes_indirectes"]

    # Créer dictionnaire pour stocker les évolutions par type d'impôt et par année
    évolutions_par_type_et_année = {type_impot: [] for type_impot in types_impots}

    # Calculer les évolutions pour chaque type d'impôt / les stocker dans dictionnaire
    for type_impot in types_impots:
        évolutions = liste_évolution(type_impot)
        évolutions_par_type_et_année[type_impot] = évolutions

    # Créer dictionnaire pour stocker l'augmentation maximale par année
    augmentation_max_par_année = {}

    # Parcours chaque année
    for année in années:
        # Trouver type d'impôt avec augmentation maximale pour cette année
        type_impot_max_augmentation = max(évolutions_par_type_et_année.keys(),
                                          key=lambda x: évolutions_par_type_et_année[x][année - 2010])

        # Stocker type impôt et augmentation maximale pour cette année
        augmentation_max_par_année[année] = (
        type_impot_max_augmentation, évolutions_par_type_et_année[type_impot_max_augmentation][année - 2010])

    # Afficher classement avec intervalle de une année
    print("Classement de l'impôt qui augmente le plus par année :")
    for année in années[:-1]:
        année_suivante = année + 1
        type_impot, augmentation_max = augmentation_max_par_année[année]
        print(f"{année}-{année_suivante}: {type_impot} avec une augmentation de {augmentation_max}%.")

def calcul_repartition_pourcentage_année(année):
    '''
    Calcule la répartition en pourcentage des types d'impôts pour une année spécifique.

    Args:
    - année (int): L'année pour laquelle calculer la répartition.

    Returns:
    - dict: Dictionnaire contenant la répartition en pourcentage des types d'impôts pour l'année donnée.
    '''
    resultats = recette_fiscale_année(année)

    if not resultats:
        print(f"Aucune donnée disponible pour l'année {année}.")
        return None

    total_année = somme_année(resultats)

    repartition_pourcentage = {}
    for type_impot, valeur in resultats.items():
        pourcentage = (valeur / total_année) * 100
        repartition_pourcentage[type_impot] = pourcentage

    # Supprimer l'entrée 'total' si elle existe
    repartition_pourcentage.pop('total', None)

    return repartition_pourcentage