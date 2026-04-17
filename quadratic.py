# Replace the "ANSWER HERE" for your answer
import math
def roots(a, b, c):
    delta = b**2 - 4*a*c

    if delta > 0:
        r1 = (-b + math.sqrt(delta)) / (2*a)
        r2 = (-b - math.sqrt(delta)) / (2*a)
        return f"({r1}, {r2})"
    elif delta == 0:
        r = -b / (2*a)
        return f"({r})"
    else:
        return "( )"


def value_y(a, b, c, x):
    return a*x**2 + b*x + c


def to_string(a, b, c):
    partes = []

    # término cuadrático
    if a != 0:
        partes.append(f"{a} * X^2")

    # término lineal
    if b != 0:
        partes.append(f"{b} * X")

    # término independiente
    if c != 0 or (a == 0 and b == 0):
        partes.append(f"{c}")

    return "f(x) = " + " + ".join(partes)


def derivation(a, b, c):
    partes = []

    # derivada de ax^2 → 2ax
    if a != 0:
        partes.append(f"{2*a} * X")

    # derivada de bx → b
    if b != 0:
        partes.append(f"{b}")

    # si todo es 0
    if not partes:
        return "f'(x) = 0"

    return "f'(x) = " + " + ".join(partes)