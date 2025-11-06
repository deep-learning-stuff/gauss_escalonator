# test_esglaonar.py
import numpy as np
from gaus import esglaonar  # cambia 'tu_modulo' por el nombre real del archivo .py


def test_matriz_identidad():
    A = np.eye(3, dtype=np.float64)
    res = esglaonar(A.copy())
    assert np.allclose(res, np.eye(3)), f"Esperado identidad, obtenido:\n{res}"


def test_matriz_diagonal_simple():
    A = np.array([[2.0, 0.0], [0.0, 3.0]])
    res = esglaonar(A.copy())
    esperado = np.array([[1.0, 0.0], [0.0, 1.0]])
    assert np.allclose(res, esperado), f"Resultado incorrecto:\n{res}"


def test_pivote_cero_intercambio():
    A = np.array([[0.0, 2.0], [1.0, 3.0]])
    res = esglaonar(A.copy())
    esperado = np.array([[1.0, 3.0], [0.0, 1.0]])
    assert np.allclose(res, esperado), f"No intercambió filas correctamente:\n{res}"


def test_fila_proporcional():
    A = np.array([[1.0, 2.0], [2.0, 4.0]])
    res = esglaonar(A.copy())
    # Segunda fila debería quedar en ceros
    assert np.allclose(res[1], [0.0, 0.0]), f"Fila proporcional no anulada:\n{res}"


def test_matriz_rectangular():
    A = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    res = esglaonar(A.copy())
    # Comprobamos que está en forma escalonada (ceros debajo del pivote)
    assert res[1, 0] == 0, f"No está escalonada:\n{res}"
    # El pivote de la primera fila debe ser 1
    assert res[0, 0] == 1


def test_caso_sin_pivotes_validos():
    A = np.zeros((3, 3), dtype=np.float64)
    res = esglaonar(A.copy())
    assert np.allclose(res, np.zeros_like(A)), f"Esperado todo ceros, obtenido:\n{res}"
