#!/usr/bin/env python3
"""Calculadora sencilla del área de un triángulo.

Uso:
 - Ejecutar sin argumentos y te pedirá la base y la altura.
 - O pasar base y altura como argumentos: `python Inteligencia-Artificial.py 3 4`
"""
import sys


def area_triangulo(base: float, altura: float) -> float:
	if base <= 0 or altura <= 0:
		raise ValueError("La base y la altura deben ser mayores que 0")
	return base * altura / 2.0


def pedir_float(prompt: str) -> float:
	while True:
		try:
			entrada = input(prompt).strip()
			valor = float(entrada.replace(",", "."))
			if valor <= 0:
				print("Introduce un número mayor que 0.")
				continue
			return valor
		except ValueError:
			print("Entrada no válida. Intenta de nuevo.")


def main():
	if len(sys.argv) >= 3:
		try:
			b = float(sys.argv[1].replace(",", "."))
			h = float(sys.argv[2].replace(",", "."))
			if b <= 0 or h <= 0:
				print("Los argumentos deben ser números mayores que 0.")
				return
		except ValueError:
			print("Argumentos no válidos. Usa números, por ejemplo: python Inteligencia-Artificial.py 3 4")
			return
	else:
		print("Calculadora de área de un triángulo")
		b = pedir_float("Base: ")
		h = pedir_float("Altura: ")

	area = area_triangulo(b, h)
	print(f"Área del triángulo = {area}")


if __name__ == "__main__":
	main()

