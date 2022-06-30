import doctest
from math import pow, pi


class Circulo(object):
    
    @staticmethod
    def valid_radio(radio):
        """
        Checks if a radius is valid for a circle
        """
        if radio <= 0:
            raise CirculoException('Debe ingresar un radio mayor a 0 para un Círculo')

    def __init__(self, radio):
        self.set_radio(radio)

    def __str__(self):
        return 'Círculo. Radio: ' + str(self._radio)
    
    def __mul__(self, other):
        try:
            temp_radio = self._radio * other
            Circulo.valid_radio(temp_radio)
            return Circulo(temp_radio)
        except CirculoException as ce:
            print(ce.message)
        except Exception as e:
            print(e.message)

    def set_radio(self, radio):
        try:
            Circulo.valid_radio(radio)
            self._radio = radio
        except Exception as e:
            print(e.message)
    
    def get_area(self):
        return pi * pow(self._radio, 2)

    def get_perimetro(self):
        return 2 * pi * self._radio


class CirculoException(Exception):
    pass
