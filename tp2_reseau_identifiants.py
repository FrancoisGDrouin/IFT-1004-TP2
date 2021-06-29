"""
Module tp2_reseau_identifiants: : Recherche dans un réseau d'amis à partir d'identifiants (nombre unique)
IFT-1004 Été 2020

Auteur: François Gauthier-Drouin
"""
import tp2_utils


def ouvrir_et_lire_fichier_reseau():
    """
    Demande à l'utilisateur un nom de fichier contenant un réseau d'amis et charge le réseau en mémoire.
    PRÉCONDITION: On considère que le fichier du réseau respecte le format écrit dans l'énoncé du TP

    Returns:
        reseau (list): le réseau extrait du fichier (une liste de listes d'index d'usgers).

    """

    descripteur_fichier = tp2_utils.ouvrir_fichier()

    # La première ligne du fichier contient le nombre total d'usagers
    nb_usagers = int(descripteur_fichier.readline())
    print("Le réseau contient {} usagers".format(nb_usagers))

    # Création d'un réseau vide (c-a-d une liste de listes vides)
    reseau = []
    for i in range(nb_usagers):
        reseau.append([])

    # Chaque ligne du fichier (sauf la première) contient un couple "d'amis"
    for ligne in descripteur_fichier.readlines():
        couple_usagers = ligne.split(' ')
        id_usager_1 = int(couple_usagers[0])
        id_usager_2 = int(couple_usagers[1])
        reseau[id_usager_1].append(id_usager_2)
        reseau[id_usager_2].append(id_usager_1)

    # Fermeture du fichier
    descripteur_fichier.close()
    print("Lecture du fichier terminé.")

    return reseau


def trouver_nombre_elements_communs_entre_listes(liste1, liste2):
    """
    Permet de trouver le nombre d'éléments communs entre 2 listes.

    Returns:
        nombre_elements_communs (int) : nombre d'éléments communs entre les deux listes.

    """
    # Initialisation de la liste elements_communs vide et de la variable nombre_elements_communs à 0.
    elements_communs = []
    nombre_elements_communs = 0
    # Ajout des éléments se retrouvant dans liste1 et liste2 dans la nouvelle liste elements_communs.
    for element in liste1:
        if element in liste2:
            elements_communs.append(element)
            nombre_elements_communs = len(elements_communs)
    return nombre_elements_communs


def calculer_scores_similarite(reseau):
    """
    Crée une matrice de taille du nombre de listes dans réseaux (qui égale «n») et en modifie les valeurs
    de 0 initiales pour retourner le nombre d'amis en commun entre un usager et le reste des usagers du réseau.
    Args:
        reseau (list) : liste d'amis d'un usager donné

    Returns:
        matrice_similarite (list) : matrice contenant les scores de similarite pour chaque paire d'usagers dans
        le réseau

    """
    # Initialiser matrice_similarite en tant que liste de dimension (nombre de listes dans «reseau» x
    # nombre de listes dans «reseau»).
    # Il y a autant d'éléments dans chaque liste que de listes dans la liste «reseau».
    # La valeur de chaque élément est initialement de 0.
    matrice_similarite = tp2_utils.initialiser_matrice_carre(len(reseau))
    # Itération sur tous les usagers dans la liste «reseau»
    for id_usager in range(len(reseau)):
        # Itération sur tous les usagers dans la liste «reseau» pour un usager donné
        for id_autres_usagers in range(len(reseau)):
            # Comparaison d'un usager avec lui-même
            if id_usager == id_autres_usagers:
                # Assignation d'une valeur pour chaque élément d'une liste comparant un usager à lui-même.
                # La valeur correspond au nombre d'usagers dans la liste réseau pour l'usager sur lequel on itère
                matrice_similarite[id_usager][id_autres_usagers] = len(reseau[id_usager])
            # Comparaison d'un usager avec un usager différent de la liste «reseau»
            else:
                # Assignation d'une valeur pour chaque élément (correspondant à tous les usagers sauf
                # l'usager sur lequel on itère) d'une liste correspondant à un usager.
                # La valeur correspond au nombre d'usagers en commun dans les listes sur lesquelles on itère.
                matrice_similarite[id_usager][id_autres_usagers] = \
                    trouver_nombre_elements_communs_entre_listes(
                        reseau[id_usager],
                        reseau[id_autres_usagers])
    # La matrice de similarités remplie de valeurs est stockée en mémoire.
    return matrice_similarite


def recommander(id_usager, reseau, matrice_similarite):
    """
    Effectue la recommandation de l'id_usager ayant le plus grand nombre d'amis en commun avec l'id_usager demandé
    tout en validant qu'on ne recommande un usager_id à lui-même ou à un de ses amis actuels.
    Args:
        id_usager (int) : nombre représentant un usager

        reseau (list) : liste d'amis d'usager donné

        matrice_similarite (list) : liste contenant le nombre d'amis en commun entre deux usagers

    Returns:
        matrice_similarite_avec_contraintes.index(max(matrice_similarite_avec_contraintes)) (int) :
        usager_id recommandé pour devenir le prochain ami de l'usager_id qui nous intéresse.

   """
    # Création d'une variable représentant le réseau de l'usager sur lequel on itère
    reseau_usager_actuel = reseau[id_usager]
    # Cette matrice vient assigner la valeur 0 à tous les amis de l'usager actuel ainsi que l'usager lui-même.
    # Les contraintes auxquelles on réfère sont de ne pas recommander un usager à lui-même...
    matrice_similarite_avec_contraintes = matrice_similarite[id_usager]
    matrice_similarite_avec_contraintes[id_usager] = 0
    # ... ou à l'un de ses amis.
    for id_amis in reseau_usager_actuel:
        matrice_similarite_avec_contraintes[id_amis] = 0
    # Traitement du cas limite où un usager n'a aucun ami ou est déjà ami avec tous les usagers du réseau
    if max(matrice_similarite_avec_contraintes) == 0:
        print("Aucune recommandation ne peut être faite pour cet usager.")
    # Si une recommandation peut être émise, on retourne l'index comportant le plus grand nombre d'amis en commun
    # avec l'usager étudié.
    recommandation_usager_id = matrice_similarite_avec_contraintes.index(max(matrice_similarite_avec_contraintes))
    return recommandation_usager_id


# Tests unitaires (les docstrings ne sont pas exigés pour les fonctions de tests unitaires)

def test_trouver_nombre_elements_communs_entre_listes():
    assert trouver_nombre_elements_communs_entre_listes([1, 2, 3],[3, 4, 5]) == 1
    assert trouver_nombre_elements_communs_entre_listes([-1, -2, -3], [-3, -4, -5]) == 1
    assert trouver_nombre_elements_communs_entre_listes([1, 2, 3], [-3, -4, -5]) == 0
    assert trouver_nombre_elements_communs_entre_listes([0, 0, 0], [0, 0, 0]) == 3
    assert trouver_nombre_elements_communs_entre_listes([-2, 0, 2], [0, 4, 2]) == 2

def test_scores_similarite():
    assert calculer_scores_similarite([[1, 2], [0], [0]]) == [[2, 0, 0], [0, 1, 1], [0, 1, 1]]
    assert calculer_scores_similarite([[2], [2], [0, 1]]) == [[1, 1, 0], [1, 1, 0], [0, 0, 2]]
    assert calculer_scores_similarite([[1, 2], [0, 2], [0, 1]]) == [[2, 1, 1], [1, 2, 1], [1, 1, 2]]
    assert calculer_scores_similarite([[1, 2], [0, 2], [0, 1]]) == [[2, 1, 1], [1, 2, 1], [1, 1, 2]]
    assert len(calculer_scores_similarite([[1], [0]])) == 2

if __name__ == "__main__":
    test_trouver_nombre_elements_communs_entre_listes()
    test_scores_similarite()
    print('Test unitaires passés avec succès!')