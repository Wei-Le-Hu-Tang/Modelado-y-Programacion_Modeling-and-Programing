import numpy as np
from PIL import Image
import os

class fractal:
    def __init__(self, txt):
        '''
        Constructor:
        Se inicializan los atributos y después se usan los SETTERS para asignarles el valor procesado,
        tomando así en consideración las excepciones y errores de formato desde la construcción del objeto
        '''
        parametros = self.__procesador(txt)

        self._width = int
        self._height = int
        self._iterations = int
        self._threshold = float
        self._min = complex
        self._max = complex
        self._polynomial = list
        self._nombre = str
        self._color = np.array([])

        self.width = parametros[0]
        self.height = parametros[1]
        self.iterations = parametros[2]
        self.threshold = parametros[3]
        self.min = parametros[4]
        self.max = parametros[5]
        self.polynomial = parametros[6]
        self.nombre = parametros[7]
        self.color = parametros[8]

        self._imagen = None
        self.__actualizar()

        self._actualizada = True
    
    def __procesador(self,txt):
        '''
        PARAM
        file.txt txt : archivo .txt con la lista de parámetros

        RETURN
        list param : lista de parámetros procesados del archivo de texto para asignarlos a los atributos
        '''
        param = self.__esValido(txt)

        #width
        param[0] = int(param[0][8:])
        #height
        param[1] = int(param[1][9:])
        #iterations
        param[2] = int(param[2][13:])
        #threshold
        param[3] = float(param[3][12:])
        #min
        param[4] = complex(param[4][6:][:-1]+'j')
        #max
        param[5] = complex(param[5][6:][:-1]+'j')

        #polynomial
        #se procesa a una lista de la forma: [coeficiente, exponente, coeficiente, exponente ...]
        poliTxt = param[6][13:]
        polinomio = []
        i=0
        while i<len(poliTxt):
            if poliTxt[i] == '(':
                coeficiente = ''
                i+=1
                while poliTxt[i] != ')':
                    coeficiente += poliTxt[i]
                    i+=1
                polinomio.append(complex(coeficiente[:-1]+'j'))
                i+=3
            else:
                exponente = ''
                while i<len(poliTxt) and poliTxt[i] != '+':
                    exponente += poliTxt[i]
                    i+=1
                polinomio.append(int(exponente))
                i+=1
        param[6] = polinomio

        #nombre
        param[7] = param[7][9:]
        #color
        param[8] = param[8][9:len(param[8])-1].split(',')
        param[8] = [int(param[8][i]) for i in range(3)]

        return param
    
    def __esValido(self, txt):
        '''
        Verifica que el archivo indicado sí sea un archivo de texto .txt existente y que cumpla con el formato de nombres de parámetros

        PARAM
        str txt : la dirección del archivo de texto con los parámetros

        RETURN
        list param : si pasa los filtros de validez, regresa el texto separado por lineas en una lista
        '''

        if txt[-4:] != '.txt':
            raise ValueError('No es un archivo de texto .txt')
        if not os.path.exists(txt):
            raise FileNotFoundError('Archivo no existente')
        
        param = open(txt, "r").read().split('\n')
        if len(param) != 9:
            raise Exception(f'Se esperaban 9 parámetros, {len(param)} fueron dados')
        if param[0][:8] != 'width : ':
            raise Exception('Formato de width inválido')
        if param[1][:9] != 'height : ':
            raise Exception('Formato de height inválido')
        if param[2][:13] != 'iterations : ':
            raise Exception('Formato de iterations inválido')
        if param[3][:12] != 'threshold : ':
            raise Exception('Formato de threshold inválido')
        if param[4][:6] != 'min : ':
            raise Exception('Formato de min inválido')
        if param[5][:6] != 'max : ':
            raise Exception('Formato de max inválido')
        if param[6][:13] != 'polynomial : ':
            raise Exception('Formato de polynomial inválido')
        if param[7][:9] != 'nombre : ':
            raise Exception('Formato de nombre inválido')
        if param[8][:9] != 'color : (':
            raise Exception('Formato de color inválido')
        
        return param
    
    #GETTERS

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height
    
    @property
    def iterations(self):
        return self._iterations

    @property
    def threshold(self):
        return self._threshold

    @property
    def min(self):
        return self._min

    @property
    def max(self):
        return self._max

    @property
    def polynomial(self):
        return self._polynomial

    @property
    def nombre(self):
        return self._nombre

    @property
    def color(self):
        return self._color
    
    @property
    def imagen(self):
        if not self._actualizada:
            self.__actualizar()
        return self._imagen
    
    #SETTERS

    @width.setter
    def width(self, value:int):
        if value <= 0:
            raise ValueError('El ancho debe ser un entero positivo')
        self._actualizada = False
        self._width = value
    
    @height.setter
    def height(self, value:int):
        if value <= 0:
            raise ValueError('El alto debe ser un entero positivo')
        self._actualizada = False
        self._height = value
    
    @iterations.setter
    def iterations(self, value:int):
        if value <= 0:
            raise ValueError('El número máximo de iteraciones debe ser un entero positivo')
        self._actualizada = False
        self._iterations = value
    
    @threshold.setter
    def threshold(self, value:float):
        if value <= 0:
            raise ValueError('El umbral de convergencia debe ser positivo')
        self._actualizada = False
        self._threshold = value
    
    @min.setter
    def min(self, value:complex):
        self._actualizada = False
        self._min = value
    
    @max.setter
    def max(self, value:complex):
        self._actualizada = False
        self._max = value
    
    @polynomial.setter
    def polynomial(self, value:list):
        if len(value)%2 != 0:
            raise ValueError('La lista de términos del polinomio debe ser de longitud par, con el orden sucesivo: coeficiente, exponente')
        self._actualizada = False
        self._polynomial = value
    
    @nombre.setter
    def nombre(self, value:str):
        if value[-4:]!='.png' and value[-4:]!='.jpg':
            raise ValueError('Formato inválido, la imagen debe ser guardada en PNG o JPG')
        self._nombre = value
    
    @color.setter
    def color(self, value):
        if len(value) != 3:
            raise ValueError('El color debe ser en formato RGB con una lista, arreglo o tupla de tamaño 3')
        if type(value[0]) != int or type(value[1]) != int or type(value[2]) != int:
            raise ValueError('Los parámetros del color deben ser enteros')
        if value[0] < 0 or value[0] > 255 or value[1] < 0 or value[1] > 255 or value[2] < 0 or value[2] > 255:
            raise ValueError('Los parámetros del color deben estar entre 0 y 255 incluyéndolos')
        self._actualizada = False
        self._color = np.array(value)

    #MÉTODOS

    def __pixelComplejo(self,x,y) -> complex:
        '''
        PARAM
        int x : índice horizontal del arreglo de pixeles
        int y : índice vertical del arreglo de pixeles

        RETURN
        complex : número complejo correspondiente al pixel (x,y)
        '''
        real = self.min.real + (x/self.width)*(self.max.real-self.min.real)
        imag = self.min.imag + (y/self.height)*(self.max.imag-self.min.imag)
        return complex(real,imag)
    
    def __evaluarPolinomio(self,z) -> complex:
        '''
        PARAM
        complex z : el número complejo a evaluar en el polinomio

        RETURN
        complex eval : el polinomio evaluado en z
        '''
        eval = 0
        for i in range(int(len(self.polynomial)/2)):
            #en la lista polynomial, los índices pares (0,2...) son coeficiente e impares (1,3...) exponentes
            eval += self.polynomial[2*i] * (z**self.polynomial[2*i+1])
        return eval

    def __colorFinal(self,z) -> np.array:
        '''
        PARAM
        complex z : número complejo a evaluar

        RETURN
        np.array : color correspondiente al número complejo en formato RGB
        '''
        if abs(z) > self.threshold:
            return self.color
    
        i = 0
        zi = z
        while i < self.iterations:
            i += 1
            zi = self.__evaluarPolinomio(zi)
            if abs(zi) > self.threshold:
                break
        if abs(zi) <= self.threshold:
            return np.array([0,0,0])
        else:
            return self.color + (i/self.iterations)*(np.array([255,255,255])-self.color)
    
    def __actualizar(self):
        '''
        Actualiza la imagen del fractal
        '''
        self._actualizada = True

        pixeles = [[self.__colorFinal(self.__pixelComplejo(i,j)) for i in range(self.width)] for j in range(self.height)]
        pixeles.reverse()

        arreglo = np.array(pixeles, dtype=np.uint8)

        self._imagen = Image.fromarray(arreglo)
    
    def mostrar(self):
        '''
        Muestra el fractal
        '''
        if not self._actualizada:
            self.__actualizar()

        self.imagen.show()

    def guardar(self,direccion = ''):
        '''
        Guarda el fractal en la dirección indicada, si no hay dirección, se guarda en la misma carpeta
        '''
        if not self._actualizada:
            self.__actualizar()

        if direccion == '':
            self.imagen.save(self.nombre)
        else:
            if os.path.exists(direccion):
                self.imagen.save(f'{direccion}/{self.nombre}')
            else:
                raise NotADirectoryError('Dirección inválida') 
