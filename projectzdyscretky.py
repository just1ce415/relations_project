from typing import List

need = [[0,1,0,0,0],\
        [1,1,1,0,1],\
        [1,1,1,0,0],\
        [0,0,0,1,1],\
        [0,0,0,0,0]]

def symetric_closure(lst: List[list]) -> List[list]:
    """
    Receives the list of lists with bool matrix and
    returns its symetric closure.
    >>> symetric_closure([[0, 0, 0], [0, 1, 0], \
[0, 0, 0]])
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    """
    for index in range(len(lst)):
        lst[index][index] = 1
    return lst

def reflective_closure(lst: List[list]) -> List[list]:
    """
    Receives the list of lists with matrix and returns
    the list with this matrix's reflexive closure.
    >>> reflective_closure([[0, 1, 0, 0, 0], [1, 1, 1, 0, 1], \
[1, 1, 1, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 0, 0]])
    [[0, 1, 1, 0, 0], [1, 1, 1, 0, 1], [1, 1, 1, 0, 0], \
[0, 0, 0, 1, 1], [0, 1, 0, 1, 0]]
    """
    for row in range(len(lst)):
        for column in range(len(lst)):
            if lst[row][column] == 1:
                lst[column][row] = 1
    return lst


def class_equivalence(lst: List[list]) -> List[list]:
    """
    Receives a matrix in list of lists and returns all
    its equivalence classes in list of lists.
    >>> class_equivalence([[1, 1, 1, 0, 0], [1, 1, 1, 0, 1], \
[1, 1, 1, 0, 0], [0, 0, 0, 1, 1], [0, 1, 0, 1, 1]])
    [[0, 1, 2], [1, 4], [3, 4]]
    """
    matrix_dict = {key: set() for key in range(len(lst))}
    length = len(lst)

    [matrix_dict[row].add(column)
        for row in range(length)
        for column in range(length) if lst[row][column]==1]

    result = []
    [result.append(key1.intersection(key2))
        for key2 in matrix_dict.values()
        for key1 in matrix_dict.values() if key2 != key1
        and key1.intersection(key2) != set()
        and key1.intersection(key2) not in result]

    key =  0
    while key < len(result):
        [result.remove(result[key])
        for item in result
        if result[key] != item
        if result[key].issubset(item)]
        key += 1

    result = [list(item) for item in result]
    return result

if __name__=='__main__':
    from doctest import testmod
    testmod()