#metodo.py

from enum import Enum


class Metodo(Enum):
    FIRST_FIT = 1
    NEXT_FIT = 2
    BEST_FIT = 3
    WORST_FIT = 4

    def get_name(metodo):
        if metodo == Metodo.FIRST_FIT:
            return "FIRST FIT"
        elif metodo == Metodo.NEXT_FIT:
            return "NEXT FIT"
        elif metodo == Metodo.BEST_FIT:
            return "BEST FIT"
        elif metodo == Metodo.WORST_FIT:
            return "WORST FIT"
