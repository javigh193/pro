"""
Dada una lista de valores numéricos enteros, obtenga el resultado de multiplicar
todos los valores en orden.
"""


def run(numbers: list) -> int:
    rmult = 1
    for number in numbers:
        rmult *= number
    return rmult


if __name__ == "__main__":
    run([1, 2, 3, 4])
