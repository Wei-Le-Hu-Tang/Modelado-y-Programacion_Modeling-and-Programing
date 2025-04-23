# Proyecto 1: Graficación de fractales
**Autor:** Wei Le Hu Tang

**Profesor:** Francisco Alejandro Arganis Ramírez

**Materia:** Modelado y Programación

## 1. Introducción
En este proyecto, exploraremos la generación de fractales a partir de **polinomios complejos** utilizando **Programación Orientada a Objetos (POO)**.

Implementaremos un programa que:

- Procesará polinomios definidos en el plano complejo.
- Iterará sobre cada punto del plano para evaluar su convergencia o divergencia.
- Generará una imagen en formato PNG o JPG que represente el fractal resultante.

## 2. Objetivos
- Modelar un polinomio complejo y su evaluación iterativa.
- Implementar una arquitectura basada en POO para encapsular los elementos del programa.
- Leer un archivo de entrada con los parámetros necesarios para generar el fractal.
- Generar una imagen que represente el fractal resultante.

## 3. Formato del Archivo de Entrada
Es un archivo .txt que se verá de la siguiente forma, y con las especificaciones mostradas a continuación:

    width : 1024
    height : 1024
    iterations : 10
    threshold : 2
    min : -2-2i
    max : 2+2i
    polynomial : (1+0i)x^2+(-1+0i)x^0
    nombre : fractal.png
    color : (255,100,50)
    
### Nombres de parámetros
Los nombres de los parámetros (*widht, height,...*) deberán ser escritos exactamente como viene en el ejemplo, seguidos de ' : ' (un espacio, dos puntos y un espacio), a partir de donde se empieza a escribir el valor del parámetro

### Polynomial
El polinomio debe tener coeficientes complejos entre paréntesis y exponentes reales
- Si el coeficiente *c* es real, se escribe: "(c+0i)"
- Si el coeficiente *c* es imaginario, se escribe: "(0+ci)"
- El término constante debe ir acompañado de: "x^0"

### Color
El color es en formato RGB, debe ir entre paréntesis y tener los números separados por comas, sin espacios

Ejemplos de formatos inválidos:
- "(255, 100, 50)", tiene espacios después de las comas
- "255,100,50", no tiene paréntesis

## 4. Fractales.py
En este archivo se crea la clase **fractal** para poder manejarlos como objetos. Se trata de hacer lo más robusto y eficiente posible aunque este proyecto no lo requiera.

### Atributos
- *int* **width** : número de pixeles de ancho de la imagen.
- *int* **height** : número de pixeles de alto de la imagen.
- *int* **iterations** : número máximo de iteraciones.
- *float* **threshold** : umbral de convergencia.
- *complex* **min** : complejo *mínimo* (esquina inferior izquierda).
- *complex* **max** : complejo *máximo* (esquina superior derecha).
- *list* **polynomial** : polinomio procesado en una lista, donde las pocisiones impares (índices pares) son los coeficientes, y las pocisiones pares (índices impares) son los exponentes. Ejemplo: si el polinomio es $(1+2i)x^3+(4+5i)x^0$, entonces:

    polynomial = [1+2i, 3, 4+5i, 0]
    
- *str* **nombre** : nombre de la imagen generada para guardar, con la terminación ".png" o ".jpg".
- *array* **color** : arreglo con los parámetros del color en RGB.
- *Image* **imagen** : imagen generada del fractal. Se guarda como atributo con la intención de no tener que volver a generarla cada que se quiera mostrar o guardar. Este sólo tiene *getter* pero no *setter* público, porque es un atributo que no puede ser arbitrario como los parámetros.
- *bool* **actualizada** : indica si el atributo **imagen** está actualizado, pues una vez se crea el objeto **fractal**, los parámetros se pueden modificar con *setters*, pero sería costoso actualizar la imagen cada que se modifica un parámetro; entonces se deja que el usuario realice todos los cambios que quiera, e **imagen** sólo se actualiza cuando se manda a llamar el atributo, cuando se muestra o cuando se guarda el archivo. Este no cuenta con *getter* ni *setter* públicos, porque es un parámetro privado que sirve para llevar un control dentro del objeto.

### Métodos
#### Constructores
- **\_\_init\_\_(self,txt)** : constructor que utiliza primeramente métodos privados auxiliares para verificar la validez del archivo **txt** y procesarlo, inicializa las variables, y les asigna los valores procesados a través de los **setters**, porque éstos verifican formato y validez de los valores.

- **__esValido(self,txt)** : crea un primer filtro de validez del archivo de parámetros, verificando que sea un archivo .txt existente, con los 9 parámetros y que estos tengan el orden, los nombres y el espaciado correcto. Si se cumple todo, regresa en una lista las lineas del archivo de texto al procesador.

- **__procesador(self,txt)** : lee en cada linea lo que hay después de " : ", es decir el valor asignado al parámetro en el archivo de texto. Mete estos valores en una lista y son enviados al constructor.

#### Getters
Todos los atributos tienen **getter**, excepto **actualizada**, porque es una bandera booleana para control interno, por lo que se mantiene privada.

#### Setters
Sólo los atributos que son parámetros tienen **setter**, porque **imagen** es un resultado dependiente de los parámetros y no algo arbitrario; y **actualizada** es una bandera booleana para control interno, por lo que no se puede permitir que sea modificada por fuera.

#### Privados
- **__pixelComplejo(self, x, y)** : convierte el pixel $(x,y)$ en el complejo correspondiente.

- **__evaluarPolinomio(self, z)** : evalúa el polinomio dado por **polynomial** en el complejo **z**.

- **__colorFinal(self, z)** : itera sobre **z** y regresa el color que le corresponde en el fractal.

- **__actualizar(self)** : actualiza la imagen del fractal utilizando los otros tres métodos privados como auxiliares.

#### Públicos
En caso de que los parámetros hayan sufrido cambios, estos métodos actualizan la **imagen** antes de realizar su función principal
- **mostrar(self)** : muestra la **imagen** del fractal sin necesidad de guardarla

- **guardar(self, direccion = '')** : guarda la **imagen** del fractal en la dirección dada, en caso de no recibir alguna dirección, se guarda en la misma carpeta donde esté el archivo en ejecución.

## Ejecución de código
### PruebasUnitarias.py
Para correr las pruebas unitarias, basta con correr este archivo. Estas pruebas incluyen:
- Getters
- Setters
- Setters con valores inválidos
- Crear fractales con archivos válidos
- Crear fractales con archivos inválidos

Duración aproximada: 45 seg.

### Proyecto1.py
Al correr este código:
- Primero aparecerá un **input** donde se debe introducir la dirección del archivo de texto.
- Si éste es válido, se procesará y se mostrará el fractal en una imagen.
- Después aparecerá otro **input** donde se debe introducir la dirección de la carpeta donde se piensa guardar la imagen del fractal.
- Si es una dirección válida, esta se guarda y el programa termina

## Archivos de prueba
- *fractal.png* corresponde al creado por *parametros.txt*
- *fractal1.png* corresponde al creado por *parametros copy.txt*
- *fractal2.png* corresponde al creado por *parametros copy 2.txt*
- *parametros invalido.txt* es un archivo que no cumple con el formato correcto de los parámetros
- *parametros invalido 2.txt* es un archivo que cumple con el formato pero le falta un parámetro

## Notas adicionales
Es necesario tener instalados **unittest** y **pytest** para las pruebas unitarias, y **pillow** para el procesador de imágenes.