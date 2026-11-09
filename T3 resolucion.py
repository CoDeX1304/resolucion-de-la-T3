import math
import random


def pedir_numero(mensaje, entero=False):
    while True:
        texto = input(mensaje).strip()
        try:
            valor = int(texto) if entero else float(texto)
        except ValueError:
            print("  Entrada no válida. Ingrese un número.")
            continue
        if valor <= 0:
            print("  El valor debe ser mayor que 0.")
            continue
        return valor


def area_referencia(a, b, c, d, pasos=200_000):
    if c >= a:
        return 0.0
    dx = (a - c) / pasos
    suma = 0.0
    for i in range(pasos):
        x = c + (i + 0.5) * dx
        y_elipse = b * math.sqrt(max(0.0, 1 - x**2 / a**2))
        y_hiper = d * math.sqrt(max(0.0, x**2 / c**2 - 1))
        suma += 2 * min(y_elipse, y_hiper) * dx
    return 2 * suma


def main():
    print("=== Montecarlo: elipse ∩ hipérbola ===")
    print("Elipse:    x^2/a^2 + y^2/b^2 <= 1")
    print("Hipérbola: x^2/c^2 - y^2/d^2 >= 1\n")

    a = pedir_numero("Ingrese a (elipse): ")
    b = pedir_numero("Ingrese b (elipse): ")
    c = pedir_numero("Ingrese c (hipérbola): ")
    d = pedir_numero("Ingrese d (hipérbola): ")
    n = pedir_numero("Cantidad de puntos aleatorios: ", entero=True)

    en_elipse = 0
    en_interseccion = 0

    for _ in range(n):
        x = random.uniform(-a, a)
        y = random.uniform(-b, b)

        dentro_elipse = (x**2) / (a**2) + (y**2) / (b**2) <= 1
        if dentro_elipse:
            en_elipse += 1
            dentro_hiperbola = (x**2) / (c**2) - (y**2) / (d**2) >= 1
            if dentro_hiperbola:
                en_interseccion += 1

    area_elipse = math.pi * a * b

    print("\n=== RESULTADOS ===")
    print(f"Puntos generados:                      {n}")
    print(f"Puntos dentro de la elipse:            {en_elipse}")
    print(f"Puntos en la intersección con la hipérbola: {en_interseccion}")
    print(f"Área de la elipse (π·a·b):             {area_elipse:.4f}")

    if en_elipse == 0:
        print("Ningún punto cayó en la elipse: no se puede estimar el área.")
        return

    area_aprox = (en_interseccion / en_elipse) * area_elipse
    print(f"Área aproximada de la intersección:    {area_aprox:.4f}")

    ref = area_referencia(a, b, c, d)
    error = abs(area_aprox - ref)
    print(f"\n(Referencia numérica del área:         {ref:.4f})")
    print(f"(Error absoluto de la estimación:      {error:.4f})")


if __name__ == "__main__":
    main()