import copy


def get_transitive_closure(relation):
    '''
    (list(list)) ->list(list)
    Takes a relation (matrix) and using Warshall's Algorithm return it's
    transitive closure as list of lists.
    >>> get_transitive_closure([[0 ,0 ,0 ,1], [1, 0, 1, 0], \
        [1 ,0 ,0 ,1], [0, 0, 1, 0]])
    [[1, 0, 1, 1], [1, 0, 1, 1], [1, 0, 1, 1], [1, 0, 1, 1]]
    >>> get_transitive_closure([[1, 0, 0], [0, 1, 1], [1, 0, 1]])
    [[1, 0, 0], [1, 1, 1], [1, 0, 1]]
    >>> get_transitive_closure([[1, 0, 0, 0], [0, 1, 0, 0], \
        [0, 0, 1, 0], [0, 0, 0, 1]])
    [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    >>> get_transitive_closure([[1, 0, 0, 0], [0, 1, 1, 0], \
        [0, 1, 1, 0], [0, 0, 0, 1]])
    [[1, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]
    '''
    # k index states for W(k) matrix
    for k in range(len(relation)):
        for i in range(len(relation)):
            for j in range(len(relation)):
                # W(k)[i][j] = W(k-1)[i][j] or (W(k-1)[i][k] and W(k-1)[k][j])
                relation[i][j] = relation[i][j] | \
                    (relation[i][k] & relation[k][j])
    return relation


def is_transitive(relation):
    '''
    (list(list)) -> bool
    Takes a relation (matrix) and checks whether it is transitive. 
    Accordingly to result returns True ot False. 
    >>> is_transitive([[0 ,0 ,0 ,1], [1, 0, 1, 0], \
        [1 ,0 ,0 ,1], [0, 0, 1, 0]])
    False
    >>> is_transitive([[1, 0, 0], [0, 1, 1], [1, 0, 1]])
    False
    >>> is_transitive([[1, 0, 0, 0], [0, 1, 0, 0], \
        [0, 0, 1, 0], [0, 0, 0, 1]])
    True
    >>> is_transitive([[1, 0, 0, 0], [0, 1, 1, 0], \
        [0, 1, 1, 0], [0, 0, 0, 1]])
    True
    '''
    input_relation = copy.deepcopy(relation)
    final_relation = get_transitive_closure(input_relation)
    if relation == final_relation:
        return True
    else:
        return False

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())