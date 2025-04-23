import Fractales

if __name__ == '__main__':
    parametros = input('Introduzca la dirección del archivo de texto:\n')
    fractal = Fractales.fractal(parametros)
    fractal.mostrar()
    direccion = input('Introduzca la dirección de la carpeta donde se guardará la imagen, en caso de que sea en esta misma carpeta, sólo pulse ENTER:\n')
    fractal.guardar(direccion)