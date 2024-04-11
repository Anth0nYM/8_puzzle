import numpy as np
import random
from copy import deepcopy
import os


def generate_random_state(seed=None):
    random.seed(seed)

    # Gerando numeros aleatorios
    numbers = list(range(10))
    random.shuffle(numbers)

    # Criando a matriz NumPy
    random_state = np.array(numbers[:9]).reshape(3, 3)

    return random_state

def generate_solved_state(type):
    if type == 1:
        state = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8]).reshape(3, 3)
        return state
    elif type == 2:
        state = np.array([1, 2, 3, 4, 5, 6, 7, 8, 0]).reshape(3, 3)
        return state

def generate_mock_state(type):
    if type == 1:
        state = np.array([1, 2, 5, 3, 0, 4, 6, 7, 8]).reshape(3, 3)
        return state
    elif type == 2:
        state = np.array([1, 2, 0, 3, 4, 5, 6, 7, 8]).reshape(3, 3)
        return state
    elif type == 3:
        state = np.array([3, 2, 0, 6, 1, 5, 7, 4, 8]).reshape(3, 3)
        return state

def generate_children(state):
    # Encontrando a posição do zero
    zero_position = np.where(state == 0)
    zero_position = zero_position[0][0], zero_position[1][0]

    children = []

    # esquerda, direita, cima, baixo
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    for move in moves:
        new_row = zero_position[0] + move[0]
        new_col = zero_position[1] + move[1]

        # Verificando se o movimento não ultrapassa os limites da matriz
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = deepcopy(state)
            new_zero_position = new_row, new_col
            swap_values(new_state, zero_position, new_zero_position)
            children.append(new_state)

    return children

# Funções auxiliares
def swap_values(state, pos1, pos2):
    state[pos1], state[pos2] = state[pos2], state[pos1]
def to_tuple(state):
    return tuple(map(tuple, state))
def save_path(path, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        for node in path:
            f.write(f"{node}\n")