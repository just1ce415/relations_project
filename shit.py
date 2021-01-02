def is_transitive(matrix):
    '''
    (list(list)) -> bool
    Check if matrix (relation) is transitive.

    >>> is_transitive([[1, 0, 1], [1, 1, 0], [0, 0, 1]])
    False
    >>> is_transitive([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 1, 0]])
    True
    '''
    relation = transform_into_relation(matrix)
    second_elements = [b for (a, b) in relation]
    for (a, b) in relation:
        for c in second_elements:
            if (b, c) in relation and (a,c) not in relation:
                return False
    return True


def transform_into_relation(matrix):
    '''
    (list(list)) -> (list(tuple))
    Transform matrix into relation.

    >>> transform_into_relation([[1, 0, 1], [1, 1, 0], [0, 0, 1]])
    [(0, 0), (0, 2), (1, 0), (1, 1), (2, 2)]
    >>> transform_into_relation([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 1, 0]])
    [(2, 1), (3, 1), (3, 2), (4, 1), (4, 2), (4, 3)]
    '''
    result = []
    length = len(matrix)
    for i in range(length):
        for j in range(length):
            if matrix[i][j] == 1:
                lst = [i, j]
                result.append(tuple(lst))
    return result


def transform_into_matrix(relation):
    '''
    (list(tuple)) -> (list(list))
    Transform relation into matrix.

    >>> transform_into_matrix([(2, 1), (3, 1), (3, 2), (4, 1), (4, 2), (4, 3)])
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 1, 0]]
    >>> transform_into_matrix([(0, 0), (0, 2), (1, 0), (1, 1), (2, 2)])
    [[1, 0, 1], [1, 1, 0], [0, 0, 1]]
    '''
    result = []
    length = max(max(relation)) + 1
    for i in range(length):
        temporary = []
        for j in range(length):
            if (i, j) in relation:
                temporary.append(1)
            else:
                temporary.append(0)
        result.append(temporary)
    return result

