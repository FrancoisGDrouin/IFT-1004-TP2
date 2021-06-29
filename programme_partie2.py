"""
Programme intéractif pour le TP2 (Partie 2)
IFT-1004 Été 2020

Auteur: François Gauthier-Drouin
"""

import tp2_reseau_identifiants
import tp2_reseau_noms


print('--- Chargement du réseau (identifiants) ---')
reseau = tp2_reseau_identifiants.ouvrir_et_lire_fichier_reseau()
nb_usagers = len(reseau)

print('--- Chargement des noms ---')
liste_noms = tp2_reseau_noms.ouvrir_et_lire_fichier_noms()

if nb_usagers != len(liste_noms):
    print("ERREUR: Le nombre d'usager est différents dans les deux fichiers.")
    fin_du_programme = True
else:
    matrice = tp2_reseau_identifiants.calculer_scores_similarite(reseau)
    dict_usagers = tp2_reseau_noms.creer_dictionnaire_usagers(liste_noms)
    fin_du_programme = False

while not fin_du_programme:

    nom_usager = input("Entrer le nom de l'usager pour lequel vous voulez une recommandation: " )
    nom_usager = nom_usager.strip() # Enlève les espaces superflus au début et à la fin de la chaîne de caractères

    nom_valide = True

    # Validation de la présence du nom dans notre réseau
    nom_valide = tp2_reseau_noms.nom_existe(nom_usager, liste_noms)
    # Traitement du cas où le nom de l'usager ne fait pas partie du fichier
    if nom_usager not in liste_noms:
        nom_valide = False
        print("Erreur: l'usager {} n'existe pas.".format(nom_usager))
    # Recommandation si l'identifiant est valide
    if nom_valide:
        nom_recommandation = \
            tp2_reseau_noms.recommander(nom_usager, reseau, matrice, liste_noms, dict_usagers)
        print("Pour {}, nous recommandons l'ami(e) {}".format(nom_usager, nom_recommandation))

        # Demander à l'utilisateur s'il veut une autre recommandation
    while True:

        nouvelle_recommandation = str(input("Voulez-vous une autre recommandation (oui/non)?"))
        # Traitement de la réponse obtenue : le programme est terminé si l'utilisateur répond «non».
        if nouvelle_recommandation.upper() in ["OUI","NON"]:
            if nouvelle_recommandation.upper() == "NON":
                fin_du_programme = True
            break
        else:
            print("Vous devez entrer oui ou non.")
