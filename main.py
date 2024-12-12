"""
Programme
"""

#### Imports et définition des variables globales
import sys
sys.setrecursionlimit(1100)


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de 
    caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici

    c = [s[0]]
    o = [1]
    k = 1

    while k < len(s):
        if s[k] == s[k-1]:
            o[-1] += 1
        else:
            c.append(s[k])
            o.append(1)
        k = k + 1

    return list(zip(c,o))


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici
    # cas de base

    if s == "":
        return []

    k = 0
    # recherche nombre de caractères identiques au premier
    while k < len(s) and s[k] == s[0]:
        k += 1

    return [(s[0], k)] + artcode_r(s[k:])



    # appel récursif



#### Fonction principale


def main():
    """
    Foncion Main
    """

    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
