"""
Programme interactif pour le TP2 (Partie 1)
IFT-1004 Été 2020

Auteur: François Gauthier-Drouin
"""

import tp2_reseau_identifiants

print('--- Chargement du réseau (identifiants) ---')
reseau = tp2_reseau_identifiants.ouvrir_et_lire_fichier_reseau()
nb_usagers = len(reseau)

matrice = tp2_reseau_identifiants.calculer_scores_similarite(reseau)

fin_du_programme = False
while not fin_du_programme:

    while True:
        try:
            id_usager = int(input("Entrer l'id de l'usager pour lequel vous voulez une recommandation (entre 0 et {}):"
                                  .format(nb_usagers-1)))
            break
        except ValueError:
            print("L'usager doit être un nombre entier entre 0 et 9 inclusivement")
            continue

    identifiant_valide = True

    # Traitement des cas où l'identifiant est hors de l'intervalle accepté
    if id_usager < 0 or id_usager > nb_usagers - 1:
        identifiant_valide = False
        print("Erreur: l'id de l'usager doit être un nombre entier entre 0 et {} inclusivement".format(nb_usagers - 1))
    # Recommandation si l'identifiant est valide
    if identifiant_valide:
        id_recommandation = tp2_reseau_identifiants.recommander(id_usager, reseau, matrice)
        print("Pour la personne {}, nous recommandons l'ami {}.".format(id_usager, id_recommandation))

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