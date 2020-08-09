import mss


def change_pixelisation():
    """
    Fonction à appeler pour avoir la même pixelisation pour pynput et les
    cliques souris qu'avec les screenshots. Si quelqu'un voit comment faire
    plus élegamment je suis preneur
    """
    with mss.mss():
        pass
