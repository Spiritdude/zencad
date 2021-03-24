# Анализ кривых

-------------------------
## Теоретическая сводка.
Общепризнанным методом задания кривых в системах вычислительной геометрии является параметрический метод.

Согласно ему кривая задана непрерывным отображением скалярного множества _[U\_min, U\_max]_ на пространство заданной мерности.
_P = F(U) : P ∈ R^N, U ∈ R^1[U\_min, U\_max]_, где _F_ - функтор отображения, а _N_ - мерность пространства.

На практике это означает, что любая точка _P_ на кривой имеет соответствующее ей значение скалярного параметра _U_. Следует понимать, что в общем случае функция связывающая параметр _U_ в точке _P_ и длину кривой из точки начала _O_ до точки _P_ не линейна. Поэтому вычисления над кривой в терминах длин требуют применения специального математического аппарата (реализованного в виде методов настоящей библиотеки).

-----------------
## Классы кривых.
В ZenCad существуют следующие классы реализующие методы анализа кривых:

* Edge (порождается инструментами segment, interpolate, bezier, bspline и т.д.)
* Curve3 (NotReleased)
* Curve2 (NotReleased)

---
## Крайние точки и диапазон конечной кривой.
Определение концевых точек конечных кривых.

Метод _endpoints_ возвращает объекты крайних точек. 
Параметры этих точек могут быть запрошены методом _range_.

```python 
curve.endpoints() -> point3, point3
curve.range() -> float, float
```

```python
crv = circle(r=5, wire=True, angle=deg(270))
s,f = crv.endpoints()
disp([crv, s, f])
```
![](../images/generic/endpoints0.png)

-----------------
## curve.length()
Вернуть длину кривой между параметрами _U\_min_ и _U\_max_.

--------------
## curve.d0(u)
Вернуть точку, соответствующую параметру _u_.

---------------
## curve.d1(u)
Вернуть точку и вектор первой производной, соответствующие параметру _u_.

------------------------
## curve.linoff(u, dist)
Вернуть параметр точки, смещенной на длину _dist_ относительно точки задаваемой параметром _u_.

------------------------------
## curve.linoff_point(u, dist)
Вернуть точку, смещенную на длину dist относительно точки задаваемой параметром _u_.  
alternate: `curve.d0(curve.linoff(u,dist))`

-------------------------------------------
## Равнораспределённые точки кривой.
Вернуть массив точек, равномерно распределённых на кривой. Параметр _npnts_ - задаёт количество точек.
Параметры umin, umax задают диапазон на множестве параметров в котором будет проведена процедура распределения.

```python3
curve.uniform(npnts, umin=U_min, umax=U_max) -> list(float) # Список параметров
curve.uniform_points(npnts, umin=U_min, umax=U_max) -> list(point3) # Список точек.
```  

```python
crv = circle(r=5, wire=True, angle=deg(270))

params = crv.uniform(8, math.pi/4, math.pi)
print(params) # [0.7853981633974483, 1.121997376282069, 1.4585965891666897, 1.7951958020513104, 2.131795014935931, 2.4683942278205517, 2.8049934407051724, 3.141592653589793]

pnts = crv.uniform_points(8, math.pi/4, math.pi)
disp(pnts + [crv])
```

![](../images/generic/uniform_points0.png)