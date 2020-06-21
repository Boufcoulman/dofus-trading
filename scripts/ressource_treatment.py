def ressource_treatment(position):
    """
    Fonction à appeler quand une ressource est cliquée pour enregistrer
    ses données dans la base.
    En argument la position dans l'hdv : 1 tout en haut, 14 tout en bas.
    La fonction n'est exploitable que de 1 à 11 inclus.
    """

    # Ajouter un dictionnaire de tuple (cf test.py) avec le numéro de la ressource et les dimensions de rectangle de capture à donner à la fonction screen_rectangle
    # En fait la dim c'est toujours la même, ce qui change c'est juste l'ordonnée de départ donc no need un dictionnaire, juste une petite formule
    # A priori +46 en ordonnée pour passer d'une ressource à la suivante
    #
    # nom ressource :       (665, 215, 235, 25)
    # prix moyen :          (1070, 215, 100, 25)
    # premier champ lot :   (830, 261, 70, 25)
    # premier prix lot :    (940, 261, 80, 25)
    # deuxieme champ lot :  (830, 307, 70, 25)
    # deuxieme prix lot :   (940, 307, 80, 25)
    # troisieme champ lot : (830, 353, 70, 25)
    # troisieme prix lot :  (940, 353, 80, 25)

    # On capture les différentes portions intéressantes de l'ecran
