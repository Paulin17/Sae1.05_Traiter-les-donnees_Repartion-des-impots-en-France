import opening
import traitement_impot_revenue
import traitements_recette_impot

if __name__ == '__main__':

    def department_ok(dept):
        return dept in opening.departement("csv/dept_nb_foyer.csv").keys()

    def annee_ok(annee):
        return int(annee) in range(2014,2022)
    
    print("\n                ╔════════════════════════════════════════════════════════╗")
    print("                ║ Programme réalisé par Nathan MICHELON et Paulin DOYON  ║")
    print("                ╚════════════════════════════════════════════════════════╝")
    print("                                       Bienvenue\n")
    print("Vous pouvez consulter des statistiques sur les recettes des impôts en France de 2010 à 2021")
    menu='ok!'
    while menu!="q":
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Les fonctionnalités disponibles sont réparties selon deux catégories:")
        print("                          ---------------")
        print(" 1 - Les recettes fiscales de 2010 à 2021,")
        print(" 2 - Les Recettes de l'impôt sur le revenu de 2014 à 2021.")
        print(" q - Quitter")
        print("                          ---------------")
        menu=input("Faites votre choix: 1 ou 2 ? ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        if menu=="1":
            saisie=""
            while saisie!="q":
                print("\n Vous allez consulter les données concernant les recettes fiscales perçus par l'état français.")
                print(" _____________________________________________________________________________________________")
                print("                         Les données utilisées vont de 2010 à 2022.")
                print(" _____________________________________________________________________________________________")
                print("Les fonctionnalités disponible sont :")
                print(" 1 - Consulter tout les types d'impôt et leurs valeurs pour une année")
                print(" 2 - Consulter l'évolution d'un type d'impôt sur un intervalle d'année")
                print(" 3 - Consulter toutes les évolution d'un type d'impôt pour chaque année")
                print(" 4 - Consulter la plus grande évolution d'un type d'impôt")
                print(" 5 - Consulter le classement de la plus grande évolution d'un impôt pour chaque intervalle d'année")
                print(" 6 - Consulter la répartition en pourcentage de chaque types d'impôt pour une année")
                print(" q - Quitter")
                saisie = int(input("Veuillez entrer le numéro de la fonctionnalité : "))
                print("")
                if saisie == 1:
                    print("Vous avez choisi de consulter les types d'impôt et leurs valeurs pour une année. ")
                    saisie1 = int(input("Veuillez entrer une année entre 2010 et 2022 compris : "))
                    if saisie1 >= 2010 and saisie1 <= 2022:
                        print(traitements_recette_impot.recette_fiscale_année(saisie1))
                    else:
                        print("L'année n'est pas comprises dans les données.")
                elif saisie == 2:
                    print("Vous avez choisi de consulter l'évolution d'un type d'impot sur un intervalle de deux années. ")
                    année1 = int(input("Veuillez saisir une première année : "))
                    année2 = int(input("Veuillez saisir une deuxième année : "))
                    type_impot = input(
                        "Veuillez saisir un type d'impôt parmi : impôt_revenu, impôt_locaux, impôt_sociétés, autres_impôts, taxes_énergétiques, tva et taxes_indirectes : ")
                    if année1 >= 2010 and année1 <= 2022 and année2 >= 2010 and année2 <= 2022:
                        print(traitements_recette_impot.évolution_type(année1, année2, type_impot))
                    else:
                        print("Une des deux années n'est pas dans les données.")
                elif saisie == 3:
                    print("Vous avez choisi de consulter toutes les évolution d'un type d'impôt pour chaque année. ")
                    type_impôt = input("Veuillez saisir un type d'impôt parmi : impôt_revenu, impôt_locaux, impôt_sociétés, autres_impôts, taxes_énergétiques, tva et taxes_indirectes : ")
                    print(traitements_recette_impot.liste_évolution(type_impôt))
                elif saisie == 4:
                    print("Vous avez choisi de consulter la plus grande l'évolution d'un type d'impôt. ")
                    type_impôt = input("Veuillez saisir un type d'impôt parmi : impôt_revenu, impôt_locaux, impôt_sociétés, autres_impôts, taxes_énergétiques, tva et taxes_indirectes : ")
                    print(traitements_recette_impot.plus_grosse_année_dévo_type(type_impôt))
                elif saisie == 5:
                    print("Vous avez choisi de consulter le classement de la plus grande évolution d'un impôt d'une année à l'autre. ")
                    print(traitements_recette_impot.classement_plus_grande_augmentation_par_année())
                elif saisie == 6:
                    print("Vous avez choisi de consulter la répartition en pourcentage de chaque types d'impôt pour une année . ")
                    année = int(input("Veuillez entrer une année entre 2010 et 2022 compris : "))
                    print(traitements_recette_impot.calcul_repartition_pourcentage_année(année))
                elif saisie != (1, 2, 3, 4, 5, 6):
                    print("Aucun numéro valide n'a été saisie")
            menu="quit"
        elif menu=="2":
            while menu!="q":
                print("                   Les Recettes de l'impôt sur le revenu de 2014 à 2021        ")
                print("                                     ---------------                           ")
                print("Les fonctionnalités disponibles sont :")
                print(" 1 - Consulter l’impôt moyen sur une année ou un département.")
                print(" 2 - Consulter l’impôt médian sur une année ou un département.")
                print(" 3 - Classement des départements les plus chers pour une personne sur une année")
                print(" 4 - Classement des département les plus chers pour un foyer fiscal sur une année")
                print(" 5 - Classement des départments ayant la plus grande évolution")
                print(" q - Menu précédent")
                print("                                     ---------------")
                menu = input("Faites votre choix: ")
                print("                                     ---------------")
                match menu:
                    case"1":
                        print("Veuillez saisir une année ou un numéro de département :")
                        print("Année: 2014 à 2021 et dépt de 1 à 95, 971 à 976, 2A, 2B")
                        menu=input("-->")
                        if department_ok(menu):
                            print("Les contribuables du département {0:s} payent en moyenne {1:.2f} millions € d'impôt sur le revenu chaque année.".format(menu,traitement_impot_revenue.moyenne_dept_sur_periode(menu)))
                        elif annee_ok(menu):
                            print("En {0:4d} les contribuables d'un département payent en moyenne {1:.2f} millions € d'impôt sur le revenu.".format(int(menu),traitement_impot_revenue.moyenne_annuel_national(int(menu))))
                        else:
                            print("Erreur de saisie")
                        input("Appuyez sur entrée pour continuer\n")
                    case "2":
                        print("Veuillez saisir une année ou un numéro de département :")
                        print("Année: 2014 à 2021 et département de 1 à 95, 971 à 976, 2A, 2B")
                        menu = input("-->")
                        if department_ok(menu):
                            print("Le montant de l'impôt sur le revenu médian payé par les contribuables du département {0:s} est de {1:.2f} millions €".format(menu,traitement_impot_revenue.mediane_dept_sur_periode(menu)))
                        elif annee_ok(menu):
                            print("Le montant de l'impôt médian en {0:s} est {1:.2f} millions € par département".format(menu,traitement_impot_revenue.medianne_annuel_national(int(menu))))
                        else:
                            print("Erreur de saisie")
                        input("Appuyez sur entrée pour continuer\n")
                    case "3":
                        print("Veuillez choisir une année :")
                        print("      *2014 à 2021*")
                        menu=int(input('-->'))
                        if not(annee_ok(menu)):
                            print("                           !!! L'année saisie est incorrecte !!!\n")
                        else:
                            print("En {0:4d} les trois départements qui sont le moins/plus cher pour une personne seule sont".format(menu))
                            var=traitement_impot_revenue.classement(traitement_impot_revenue.rapport_population(menu))
                            print('1 - {0:3s} avec {1:.2f} €/personne              99 - {2:3s} avec {3:.2f} €/personne'.format(var[0][0],var[0][1],var[98][0],var[98][1]))
                            print('2 - {0:3s} avec {1:.2f} €/personne             100 - {2:3s} avec {3:.2f} €/personne'.format(var[1][0],var[1][1],var[99][0],var[99][1]))
                            print('3 - {0:3s} avec {1:.2f} €/personne             101 - {2:3s} avec {3:.2f} €/personne'.format(var[2][0],var[2][1],var[100][0],var[100][1]))
                            input("Appuyez sur entrée pour continuer\n")
                    case "4":
                        print("Veuillez choisir une année :")
                        menu = int(input('-->'))
                        if not(annee_ok(menu)):
                            print("           !!! L'année saisie est incorrecte !!!\n")
                        else:
                            print("En {0:4d} les trois départements qui sont le moins/plus cher pour un foyer fiscal".format(menu))
                            var = traitement_impot_revenue.classement(traitement_impot_revenue.rapport_foyer_fiscaux(menu))
                            print('1 - {0:3s} avec {1:.2f} €/foyer                 99 - {2:3s} avec {3:.2f} €/foyer'.format(var[0][0],var[0][1],var[98][0],var[98][1]))
                            print('2 - {0:3s} avec {1:.2f} €/foyer                100 - {2:3s} avec {3:.2f} €/foyer'.format(var[1][0],var[1][1],var[99][0],var[99][1]))
                            print('3 - {0:3s} avec {1:.2f} €/foyer                101 - {2:3s} avec {3:.2f} €/foyer'.format(var[2][0],var[2][1],var[100][0],var[100][1]))
                            input("Appuyez sur entrée pour continuer\n")
                    case "5":
                        print("Veuillez choisir une année de début")
                        print("      *2014 à 2020*")
                        annee1 = int(input('-->'))
                        print("Veuillez choisir une année de fin")
                        print("      *2015 à 2021*")
                        annee2 = int(input('-->'))
                        if annee1>2020 or annee1<2014 or annee2>2021 or annee2<2015 or annee2<=annee1:
                            print("      !!! Ereur de saisie sur les années !!!\n")
                            type='raté'
                        else:
                            print("Veuillez choisir pour quelle catégorie :")
                            print(' 1 - Population\n 2 - Foyer fiscal\n 3 - Brut')
                            type=input('-->')
                            if type=='1' or type=='2':
                                if type=='1':
                                    mot="/personne"
                                    var = traitement_impot_revenue.classement(traitement_impot_revenue.taux_accroissement_rapport('population', annee1, annee2))
                                else:
                                    mot="/foyer fiscal"
                                    var = traitement_impot_revenue.classement(traitement_impot_revenue.taux_accroissement_rapport('foyer', annee1, annee2))

                                print("\nDe {0:4d} à {1:4d} les trois départements qui ont le moins/plus augmenté sont:".format(annee1,annee2))
                                print('1 - {0:3s} avec {1:.2f} %{4:s}              99 - {2:3s} avec {3:.2f} %{4:s}'.format(var[0][0], var[0][1], var[98][0], var[98][1],mot))
                                print('2 - {0:3s} avec {1:.2f} %{4:s}             100 - {2:3s} avec {3:.2f} %{4:s}'.format(var[1][0], var[1][1], var[99][0], var[99][1],mot))
                                print('3 - {0:3s} avec {1:.2f} %{4:s}             101 - {2:3s} avec {3:.2f} %{4:s}'.format(var[2][0], var[2][1], var[100][0], var[100][1],mot))
                                input("Appuyez sur entrée pour continuer\n")
                            elif type=='3':
                                var=traitement_impot_revenue.classement(
                                    traitement_impot_revenue.accroissement_tous_departementS(annee1, annee2))
                                mot=" brut "
                                print("\nDe {0:4d} à {1:4d} les trois départements qui ont le moins/plus augmenté sont:".format(annee1, annee2))
                                print('1 - {0:3s} avec {1:.2f} %{4:s}              99 - {2:3s} avec {3:.2f} %{4:s}'.format(var[0][0], var[0][1], var[98][0], var[98][1], mot))
                                print('2 - {0:3s} avec {1:.2f} %{4:s}             100 - {2:3s} avec {3:.2f} %{4:s}'.format(var[1][0], var[1][1], var[99][0], var[99][1], mot))
                                print('3 - {0:3s} avec {1:.2f} %{4:s}             101 - {2:3s} avec {3:.2f} %{4:s}'.format(var[2][0], var[2][1], var[100][0], var[100][1], mot))
                                input("Appuyez sur entrée pour continuer\n")
                            else:
                                print("           !!! Le type saisi est incorrect !!!\n")
            menu="quit"
        elif menu!="q":
            print("                                 !!! Erreur de saisie !!!\n")