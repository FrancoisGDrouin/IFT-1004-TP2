"""
Module tp2_reseau_noms: Recherche dans un réseau d'amis à partir de noms
IFT-1004 Été 2020

Auteur: François Gauthier-Drouin
"""

import tp2_utils
import tp2_reseau_identifiants

def ouvrir_et_lire_fichier_noms():
    """
    Demande à l'utilisateur un nom de fichier contenant le répertoire de nom
    PRÉCONDITION: On considère que le fichier du réseau respecte le format écrit dans l'énoncé du TP.

    Returns:
        liste_noms (list): Une liste de noms (chaque nom est une chaîne de caractères).

    """
    descripteur_fichier = tp2_utils.ouvrir_fichier()

    # Initialisation d'une liste vide
    liste_noms = []
    # Ajout des noms dans la liste
    for ligne in descripteur_fichier:
        liste_noms.append(ligne.rstrip())

    # Fermeture du fichier
    descripteur_fichier.close()
    print("Lecture du fichier terminé.")

    return liste_noms


def nom_existe(nom_usager, liste_noms):
    """
    Valide la présence de la variable nom_usager dans la liste liste_noms

    Args:
        nom_usager (string): Nom d'un usager
        liste_noms (list): Une liste de noms (chaque nom est une chaîne de caractères).

    Returns:
        (bool) True si nom_usager est présent dans liste_noms, False autrement.

    """
    # Validation de la présence de nom_usager dans liste_noms
    if nom_usager in liste_noms:
        return True
    else:
        return False


def creer_dictionnaire_usagers(liste_noms):
    """
    Crée un dictionnaire liant un id_usager au nom correspondant. Sa forme est <nom, ID>.

    Args:
        liste_noms (list): liste de noms (chaque nom est une chaîne de caractères).

    Returns:
        dict_usagers (dictionary): dictionnaire <nom, ID> des renseignements des usagers.

    """
    # Création du dictionnaire vide
    dict_usagers = {}
    # Itération sur tous les noms présents dans la liste pour populer le dictionnaire
    for i in range(len(liste_noms)):
        dict_usagers[liste_noms[i]] = i
    return dict_usagers


def recommander(nom_usager, reseau, matrice_similarite, liste_noms, dict_usagers):
    """
    Effectue la recommandation du nom_usager ayant le plus grand nombre d'amis en commun avec le nom_usager demandé
    tout en validant qu'on ne recommande un nom_usager à lui-même ou à un de ses amis actuels.
    Args:
        nom_usager (string) : nom d'un usager

        reseau (list) : liste d'amis d'un usager donné

        matrice_similarite (list) : liste contenant le nombre d'amis en commun entre deux usagers

        liste_noms (list) : liste des noms des usagers

        dict_usagers (dictionary) : dictionnaire <nom, ID> des renseignements des usagers.

    Returns:
        liste_noms[tp2_reseau_identifiants.recommander(dict_usagers[nom_usager], reseau, matrice_similarite)] (list) :
        nom de l'usager recommandé pour devenir le prochain ami de l'usager qui nous intéresse.

    """
    # Recommandation du nom associé à l'id_usager retourné par
    # la fonction recommander du fichier tp2_reseau_identifiants
    return liste_noms[tp2_reseau_identifiants.recommander(dict_usagers[nom_usager], reseau, matrice_similarite)]


# Tests unitaires (les docstrings ne sont pas exigés pour les fonctions de tests unitaires)

def test_nom_existe():
    assert nom_existe("Gauthier", ["Gauthier","Tanguay","Morel"]) == True
    assert nom_existe("Lavoie", ["George","Tremblay","Lavoie"]) == True
    assert nom_existe("Fortin", ["Therrien","Cantin","Fortin"]) == True
    assert nom_existe("Gagne", ["Grenier","Gagne","Morel"]) == True
    assert nom_existe("Morin", ["Morin"]) == True


def test_creer_dictionnaire_usagers():
    assert creer_dictionnaire_usagers(["Gauthier", "Morel", "Jean"]) == {'Gauthier': 0, 'Morel': 1, 'Jean': 2}
    assert creer_dictionnaire_usagers(["Fortin", "Morel", "Jean"]) == {'Fortin': 0, 'Morel': 1, 'Jean': 2}
    assert creer_dictionnaire_usagers(["Blanchet", "Gravel", "Girard"]) == {'Blanchet': 0, 'Gravel': 1, 'Girard': 2}
    assert creer_dictionnaire_usagers(["Simon", "Antoine", "Parent"]) == {'Simon': 0, 'Antoine': 1, 'Parent': 2}
    assert creer_dictionnaire_usagers(["Veillette", "Déry", "Scott"]) == {'Veillette': 0, 'Déry': 1, 'Scott': 2}

if __name__ == "__main__":
    test_nom_existe()
    test_creer_dictionnaire_usagers()
    print('Test unitaires passés avec succès!')

