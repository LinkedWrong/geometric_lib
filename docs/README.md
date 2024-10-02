# Geometric Library

## Описание

Эта библиотека предоставляет функции для вычисления площади и периметра различных геометрических фигур:

- Круг
- Прямоугольник
- Квадрат
- Треугольник

## Установка

Скопируйте файлы библиотеки в ваш проект.

## Использование

Импортируйте необходимые функции из соответствующих модулей:

```python
from geometric_lib.circle import area as circle_area, perimeter as circle_perimeter
from geometric_lib.rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from geometric_lib.square import area as square_area, perimeter as square_perimeter
from geometric_lib.triangle import area as triangle_area, perimeter as triangle_perimeter
```

## Примеры

```python
# Площадь круга с радиусом 5
circle_area_result = circle_area(5)

# Периметр прямоугольника со сторонами 4 и 6
rectangle_perimeter_result = rectangle_perimeter(4, 6)
```


## Круг

### `area(r)`

Вычисляет площадь круга.

**Аргументы:**

- `r`: Радиус круга.

**Возвращает:**

Площадь круга.

**Пример:**

```python
from geometric_lib.circle import area as circle_area
>>> circle_area(5)
78.53981633974483
```

## Прямоугольник

### `area(a, b)`

Вычисляет площадь прямоугольника.

**Аргументы:**

- `a`: Длина прямоугольника.
- `b`: Ширина прямоугольника.

**Возвращает:**

Площадь прямоугольника.

**Пример:**

```python
from geometric_lib.rectangle import area as rectangle_area
>>> rectangle_area(4, 6)
24
```

### `perimeter(a, b)`

Вычисляет периметр прямоугольника.

**Аргументы:**

- `a`: Длина прямоугольника.
- `b`: Ширина прямоугольника.

**Возвращает:**

Периметр прямоугольника.

**Пример:**

```python
from geometric_lib.rectangle import perimeter as rectangle_perimeter
>>> rectangle_perimeter(4, 6)
20
```

## Квадрат

### `area(a)`

Вычисляет площадь квадрата.

**Аргументы:**

- `a`: Длина стороны квадрата.

**Возвращает:**

Площадь квадрата.

**Пример:**

```python
from geometric_lib.square import area as square_area
>>> square_area(5)
25
```

### `perimeter(a)`

Вычисляет периметр квадрата.

**Аргументы:**

- `a`: Длина стороны квадрата.

**Возвращает:**

Периметр квадрата.

**Пример:**

```python
from geometric_lib.square import perimeter as square_perimeter
>>> square_perimeter(5)
20
```

## Треугольник

### `area(a, h)`

Вычисляет площадь треугольника.

**Аргументы:**

- `a`: Длина основания треугольника.
- `h`: Высота треугольника.

**Возвращает:**

Площадь треугольника.

**Пример:**

```python
from geometric_lib.triangle import area as triangle_area
>>> triangle_area(4, 6)
12.0
```

### `perimeter(a, b, c)`

Вычисляет периметр треугольника.

**Аргументы:**

- `a`: Длина первой стороны треугольника.
- `b`: Длина второй стороны треугольника.
- `c`: Длина третьей стороны треугольника.

**Возвращает:**

Периметр треугольника.

**Пример:**

```python
from geometric_lib.triangle import perimeter as triangle_perimeter
>>> triangle_perimeter(3, 4, 5)
12
```

## История изменений

* **97fad27 (HEAD -> main, origin/main, origin/HEAD)**: added doocstrings for files
* **d078c8d**: L-03: Docs added
* **8ba9aeb**: L-03: Circle and square added
