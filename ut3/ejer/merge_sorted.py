"""
Como datos de entrada dispone de dos listas con valores numéricos que ya vienen ordenadas.
Obtenga una lista de salida con la mezcla de las dos listas de entrada de forma ordenada.

NOTAS:
- No se puede utilizar la función sorted().
- No hay que realizar ninguna validación en los datos de entrada.
- Las listas de entrada pueden tener elementos repetidos.
- Las listas de entrada pueden tener distinto tamaño.
- Las listas de entrada pueden tener elementos comunes. Elimine los duplicados en la lista
de salida.
"""


def run(values1: list, values2: list) -> list:
    buffer = values1 + values2
    merged = []
    for value in buffer:
        if value not in merged:
            merged.append(value)
    buffer = []
    for i in range(len(merged)):
        min_index = merged.index(min(merged))
        buffer.append(merged[min_index])
        del merged[min_index]
        # merged.remove(min(merged))
    merged = buffer
    return merged


if __name__ == "__main__":
    run([1, 2, 3, 4], [1, 1, 2, 3, 4, 5])
