# Conversor de Sistemas Numéricos en Python :snake:

Primero, importamos los módulos necesarios para el funcionamiento del programa.
```python
from functools import reduce
from multipledispatch import dispatch
```
Cabe destacar que no usaremos estos módulos para hacer la conversión en sí sino, mas bien, para agregar funcionalidades útiles tales como `reduce` y sobrecarga de métodos.

Declaramos una variable de tipo `string` que almacenará los valores equivalentes de cada carácter.
```python
equivalences = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
```
La *base mínima* que podemos convertir es **2**.

La *base máxima* sería la longitud de la variable `equivalences` que, en este caso, es **36**.
```python
>>> len(equivalences)
36
```
<br>

## Convirtiendo de Decimal a cualquier Base

```python
def  dec_to_base(num: int, to_base: int) -> str:
```
Definimos la función `dec_to_base` que toma como parámetros, ambos de tipo entero:
- `num`, el número que queremos convertir
- `to_base`, la base a la que queremos convertir

Esta función retorna una representación textual del número en la base especificada .

Llamamos a la función `valid_base` (el cual definiremos más adelante) para validar si la base cumple con los parámetros.
```python
valid_base(to_base)
```

A continuación, definimos una variable `result` de tipo `list` que almacenara el resultado de la conversión.
```python
result = []
```
Haremos uso de un ciclo `while` para obtener cada uno de los elementos de nuestro resultado.
```python
while num > 0:
	calc = num % to_base
	result.append(equivalences[calc] or calc)
	num = int(num / to_base)
```
Dentro del ciclo `while`:
1. La variable `calc` almacena el resultado de la operación módulo, la cuál  retorna el residuo de la división de `num` y `to_base`.
	```python
	calc = num % to_base
	```

	Suponiendo que `num` sea igual a **25** y `to_base` sea igual a **4**:
	```python
	>>> num % to_base
	1
	```

2. Agregamos el resultado de la siguiente operación al final de la lista `result`:
	```python
	result.append(equivalences[calc] or calc)
	```

	- Si la lista `equivalences` contiene un elemento cuyo índice es el valor de `calc`, se devuelve dicho elemento, por ejemplo:
		```python
		>>> equivalences[0]
		0
		
		>>> equivalences[11]
		"A"
		```
		
	- Si no, se devuelve el valor de `calc`.

3. Asignamos a `num` el valor de la división de `num` entre `to_base`, sin la parte decimal.
	```python
	num = int(num / to_base)
	```


	Suponiendo que `num` sea igual a **26** y `to_base` sea igual a **4**:
	```python
	>>> num / to_base
	6.5
	
	>>> int(num / to_base)
	6 
	```

Finalmente, retornamos la lista en orden inverso y convertida a tipo `str`.
```python
return  "".join(result.__reversed__())
```
<br>

### Función `dec_to_base` completa
```python
def  dec_to_base(num: int, to_base: int) -> str:
	valid_base(to_base)
	result = []
	while num > 0:
		calc = num % to_base
		result.append(equivalences[calc] or calc)
		num = int(num / to_base)
	return  "".join(result.__reversed__())
```
<br>


## Convirtiendo de cualquier Base a Decimal

Definimos la función `base_to_dec` que toma como parámetros:
- `num`, la representación textual del número que queremos convertir
- `to_base`, la base del numero guardado en `num`

Esta función retorna el numero convertido a base 10.
```python
def base_to_dec(num: str, from_base: int) -> int:
```
Llamamos a la función `valid_base` (el cual definiremos más adelante) para validar si la base cumple con los parámetros.
```python
valid_base(from_base)
```
Declaramos la variable `string_list` de tipo `map` que recorre `num` y, por medio de una función<sup><a href="https://www.w3schools.com/python/python_lambda.asp">1</a></sup>, crea una nueva lista cuyos valores son los índices de cada elemento en `equivalences`.
```python
string_list = map(lambda  x: equivalences.find(x), num)
```

Esto tiene el efecto de *"traducir"* el carácter a su número correspondiente:
```python
num = "9C4"
string_list = [ 9, 12, 4 ]
```
Retornamos el resultado de un método<sup><a target="blank" href="https://docs.python.org/3/library/functools.html#functools.reduce">2</a></sup> `reduce` con los siguientes parámetros:
```python
return reduce(
...
)
```
-  Una función<sup><a href="https://www.w3schools.com/python/python_lambda.asp">1</a></sup>, repetida por cada elemento de `string_list`, que recibe dos parámetros:
	-  `acc`: variable acumulativa
	- `curr`: elemento actual
		<br>
	```python
	lambda  acc, curr: acc + curr[1] * from_base ** (len(num) - curr[0] - 1),
	```
	<br>
	
	Y ejecuta la siguiente operación
	
	<img src="https://latex.codecogs.com/gif.latex?\inline&space;\LARGE&space;\boldsymbol{a&plus;c_{1}&space;\cdot&space;b^{\(l-c_{0}-1\)}}" title="\large \boldsymbol{a+c_{1} \cdot b^{\(l-c_{0}-1\)}}" />
	<br>
	
	> **Dónde**:
	> a = acc<br>
	> c~0~ = curr[0]  = índice del elemento actual<br>
	> c~1~= curr[1] = valor del elemento actual<br>
	> b = valor de `from_base`<br>
	> l = len(num) = longitud de la variable `num`<br>
	
	...sumando todos los elementos.
	
	Por ejemplo:
	```python
	>>> reduce(lambda a,b: a+b,[1, 2, 3], 0)
	6
	```

-  Un método<sup><a target="blank" href="https://www.w3schools.com/python/ref_func_enumerate.asp">3</a></sup> que, para cada elemento, devuelve un objeto que contiene el índice, en el posición 0; el valor, en la posición 1; entre otras cosas.
	```python
	enumerate(string_list)
	```
- El estado inicial de la variable `acc` que, en este caso, seria **0**.
 
<br>

### Función`base_to_dec` completa
```python
def  base_to_dec(num: str, from_base: int) -> int:
	string_list = map(lambda  x: equivalences.find(x), num)
	return  reduce(
					lambda  acc, curr: acc + curr[1] * from_base ** (len(num) - curr[0] - 1),
					enumerate(string_list),
					0
				)
```
<br>

## Evitando errores

Definiremos una función corta que solo se encargará de confirmar, para cada base que le pasemos como parámetro `int`, si es *mayor o igual que* **2** o *menor o igual* a la longitud de la variable `equivalences`.
```python
def  valid_base(*bases: int):	
	for base in bases:
		if base < 2  or base > len(equivalences):
			raise  IndexError(f"Base must be higher or equal to 2 and lower or equal to {len(equivalences)}")
```
<br>

## Combinando todo

Definimos la función  `converter`, que hará uso de las funciones anteriores para convertir de decimal a cualquier base y, además, sera sobrecargada más adelante para permitir la conversión de cualquier base a cualquier base.

Recibe los parámetros:
- `num`: numero en base 10, de tipo  `int`, 
- `to_base`: la base a la que se quiere convertir

Devuelve una representación textual del número convertido a la base especificada.

```python
def  converter(num: int, to_base: int) -> str:
	return dec_to_base(num, to_base)
```

Una línea antes de la declaración de la función, agregamos el decorador...
 ```python
 @dispatch(int, int)
 ```
 ...con sus respectivos parámetros, para que la función correcta sea seleccionada en tiempo de ejecución.

### Función `converter` completa
```python
@dispatch(int, int)
def  converter(num: int, to_base: int) -> str:
	return dec_to_base(num, to_base)
```
<br>

## Sobrecargando la función `converter`

Finalmente, sobrecargamos la función  `converter`, para que nos permita convertir de cualquier base a cualquier base.

Recibe los parámetros:
- `num`:  representación textual del número que queremos convertir,
- `from_base`: la base del numero que queremos convertir
- `to_base`: la base a la que se quiere convertir

Devuelve una representación textual del número convertido a la base especificada.

```python
def  converter(num: str, from_base: int, to_base: int) -> str:
	return dec_to_base(base_to_dec(num, from_base), to_base)
```

De nuevo, una línea antes de la declaración de la función, agregamos el decorador...
 ```python
 @dispatch(str, int, int)
 ```
 ...con sus respectivos parámetros, para que la función correcta sea seleccionada en tiempo de ejecución.

### Función `converter` sobrecargada

```python
@dispatch(str, int, int)
def  converter(num: str, from_base: int, to_base: int) -> str:
	return dec_to_base(base_to_dec(num, from_base), to_base)
```

## Programa Completo
```python
from functools import reduce
from multipledispatch import dispatch

equivalences = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def dec_to_base(num: int, to_base: int) -> str:
    valid_base(to_base)
    result = []
    while num > 0:
        calc = num % to_base
        result.append(equivalences[calc] or calc)
        num = int(num / to_base)
    return "".join(result.__reversed__())


def base_to_dec(num: str, from_base: int) -> int:
    valid_base(from_base)
    string_list = map(lambda x: equivalences.find(x), num)
    return reduce(
                    lambda acc, curr: acc + curr[1] * from_base ** (len(num) - curr[0] - 1),
                    enumerate(string_list),
                    0
                )


def valid_base(*bases: int):
    for base in bases:
        if base < 2 or base > len(equivalences):
            raise IndexError(f"Base must be higher or equal to 2 and lower or equal to {len(equivalences)}")

@dispatch(int, int)
def converter(num: int, to_base: int) -> str:
    return dec_to_base(num, to_base)


@dispatch(str, int, int)
def converter(num: str, from_base: int, to_base: int) -> str:
    return dec_to_base(base_to_dec(num, from_base), to_base)
```
