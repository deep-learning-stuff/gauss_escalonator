import numpy as np
import numpy.typing as npt
import yogi


def esglaonar(matrix: npt.NDArray[np.float64], f: int = 0, c: int = 0):

    # caso final del recursivo
    if f >= len(matrix) or c >= len(matrix[0]):
        return matrix

    # analizar si la primera posicion es pivote, en ese caso se buscan opciones en la fila de abajo para permutar
    if matrix[f][c] == 0:
        # buscar candidatos
        for pivot in range(f + 1, len(matrix)):
            if matrix[pivot][c] != 0:
                matrix[[f, pivot]] = matrix[[pivot, f]]
                break
        else:
            esglaonar(matrix, f, c + 1)

    # normalizar pivote
    if matrix[f, c] != 0:
        matrix[f] = matrix[f] * 1 / matrix[f, c]

    # anular todos lo numeros por debajop del pivote
    for n in range(f + 1, len(matrix)):
        matrix[n] = matrix[n] - matrix[f] * matrix[n, c]

    return esglaonar(matrix, f + 1, c + 1)


def main() -> None:
    # preparar script para introducir datos por el usuario
    print("Di numero de filas y columnas >>>>>")

    f = yogi.read(int)
    c = yogi.read(int)

    m = []

    for _ in range(f):
        m.append([yogi.read(int) for _ in range(c)])

    matrix = np.array(m, dtype=np.float64)

    print(matrix)

    print(esglaonar(matrix))


if __name__ == "__main__":
    main()
