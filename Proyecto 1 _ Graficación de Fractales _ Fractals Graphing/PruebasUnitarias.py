import unittest
import Fractales
from PIL import Image
import pytest

class PruebasUnitarias(unittest.TestCase):
    def test_Getters(self):
        fractal = Fractales.fractal('img/parametros.txt')
        
        self.assertEqual(fractal.width, 1024)
        self.assertEqual(fractal.height, 1024)
        self.assertEqual(fractal.iterations, 10)
        self.assertEqual(fractal.threshold, 2.0)
        self.assertEqual(fractal.min, -2-2j)
        self.assertEqual(fractal.max, 2+2j)
        self.assertEqual(fractal.polynomial, [1+0j,2,-1+0j,0])
        self.assertEqual(fractal.nombre, 'fractal.png')
        self.assertEqual(fractal.color[0], 255)
        self.assertEqual(fractal.color[1], 100)
        self.assertEqual(fractal.color[2], 50)

    def test_Setters(self):
        fractal = Fractales.fractal('img/parametros.txt')
        
        fractal.width = 512
        self.assertEqual(fractal.width, 512)
        fractal.height = 512
        self.assertEqual(fractal.height, 512)
        fractal.iterations = 25
        self.assertEqual(fractal.iterations, 25)
        fractal.threshold = 5
        self.assertEqual(fractal.threshold, 5.0)
        fractal.min = -1-1j
        self.assertEqual(fractal.min, -1-1j)
        fractal.max = 1+1j
        self.assertEqual(fractal.max, 1+1j)
        fractal.polynomial = [1+0j,3,1-1j,2,-1+0j,0]
        self.assertEqual(fractal.polynomial, [1+0j,3,1-1j,2,-1+0j,0])
        fractal.nombre = 'nombre alterno.png'
        self.assertEqual(fractal.nombre, 'nombre alterno.png')
        fractal.color = [0,0,0]
        self.assertEqual(fractal.color[0], 0)
        self.assertEqual(fractal.color[1], 0)
        self.assertEqual(fractal.color[2], 0)
    
    def test_SettersError(self):
        fractal = Fractales.fractal('img/parametros.txt')

        with pytest.raises(ValueError):
            fractal.width = -1
        with pytest.raises(ValueError):
            fractal.height = -1
        with pytest.raises(ValueError):
            fractal.iterations = -1
        with pytest.raises(ValueError):
            fractal.threshold = -1
        with pytest.raises(ValueError):
            fractal.polynomial = [1+0j,3,1-1j,2,-1+0j]
        with pytest.raises(ValueError):
            fractal.nombre = 'nombre alterno.txt'
        with pytest.raises(ValueError):
            fractal.color = (1,2)
        with pytest.raises(ValueError):
            fractal.color = (1,2,3.5)
        with pytest.raises(ValueError):
            fractal.color = (1,2,-3)
    
    def test_Fractales(self):
        fractal0 = Fractales.fractal('img/parametros.txt')
        self.assertEqual(fractal0.imagen.convert('RGB'), Image.open('img/fractal.png').convert('RGB'))
        
        fractal1 = Fractales.fractal('img/parametros copy.txt')
        self.assertEqual(fractal1.imagen.convert('RGB'), Image.open('img/fractal1.png').convert('RGB'))
        
        fractal2 = Fractales.fractal('img/parametros copy 2.txt')
        self.assertEqual(fractal2.imagen.convert('RGB'), Image.open('img/fractal2.png').convert('RGB'))

    def test_FractalesError(self):
        with pytest.raises(ValueError):
            Fractales.fractal('img/fractal.png')
        with pytest.raises(FileNotFoundError):
            Fractales.fractal('parametros.txt')
        with pytest.raises(Exception):
            Fractales.fractal('img/parametros invalido.txt')
        with pytest.raises(Exception):
            Fractales.fractal('img/parametros invalido 2.txt')

if __name__ == '__main__':
    unittest.main()