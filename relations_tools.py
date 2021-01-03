"""
The module with functions to operate and process with relations based on the martix representation.
Project repository: https://github.com/just1ce415/relations_project
"""
import copy

def read_relation(path: str) -> list:
    '''
    (str) -> list(list)
    Reads a relation (matrix) from the file stated as (path) and returns the list of lists
    Supported separator: ',' (csv file).
    If the file has not .csv format, the function will return None.
    '''
    with open(path, 'r', encoding='utf=8') as rel_f:
        relation_lst = []
        for line in rel_f:
            if line.find(', ') != -1:
                sep = ', '
            elif line.find(' ') != -1:
                sep = ' '
            else:
                sep = ','

            if line == '':
                break
            # We always have csv file.
            row = line[:-1].split(sep)
            for i in range(len(row)):
                row[i] = int(row[i])
            relation_lst.append(row)
        return relation_lst


def write_relation(relation: list, path: str='relation_out.csv'):
    '''
    Writes relation (matrix) to the file with (path). The function create relation_out.csv in
    the project root directory by default.
    '''
    with open(path, 'w', encoding='utf-8') as rel_f:
        for row in relation:
            rel_f.write(str(row)[1:-1] + '\n')


def get_symmetric_closure(lst: list) -> list:
    """
    Receives the list of lists with matrix and returns
    the list with this matrix's reflexive closure.
    >>> get_symmetric_closure([[0, 1, 0, 0, 0], [1, 1, 1, 0, 1], \
[1, 1, 1, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 0, 0]])
    [[0, 1, 1, 0, 0], [1, 1, 1, 0, 1], [1, 1, 1, 0, 0], \
[0, 0, 0, 1, 1], [0, 1, 0, 1, 0]]
    """
    for row in range(len(lst)):
        for column in range(len(lst)):
            if lst[row][column] == 1:
                lst[column][row] = 1
    return lst


def get_reflexive_closure(lst: list) -> list:
    """
    Receives the list of lists with bool matrix and
    returns its symetric closure.
    >>> get_reflexive_closure([[0, 0, 0], [0, 1, 0], \
[0, 0, 0]])
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    """
    for index in range(len(lst)):
        lst[index][index] = 1
    return lst


def get_transitive_closure(relation: list) -> list:
    '''
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
                relation[i][j] = relation[i][j] | (relation[i][k] & relation[k][j])
    return relation


def is_transitive(matrix: list) -> bool:
    '''
    Check if matrix (relation) is transitive.
    >>> is_transitive([[1, 0, 1], [1, 1, 0], [0, 0, 1]])
    False
    >>> is_transitive([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], \
[0, 1, 1, 0, 0], [0, 1, 1, 1, 0]])
    True
    '''
    if len(matrix) == 0:
        return True
    trans_closure = copy.deepcopy(matrix)
    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                trans_closure[i][j] = trans_closure[i][j] | (trans_closure[i][k] & trans_closure[k][j])
                if matrix[i][j] != trans_closure[i][j]:
                    return False
    return True


def get_equivalence_class(lst: list) -> list:
    """
    Receives a matrix in list of lists and returns all
    its equivalence classes in list of lists.
    >>> get_equivalence_class([[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], \
[0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]])
    [[0], [1], [2], [3], [4]]
    """
    equivalence_dict = {key: set() for key in range(len(lst))}
    length = len(lst)

    [equivalence_dict[row].add(column)
        for row in range(length)
        for column in range(length) if lst[row][column] == 1]

    result = []
    [result.append(list(element)) for element in equivalence_dict.values()
    if list(element) not in result]
    return result


def is_transitive_1(relation):
    '''
    (list(list)) -> bool

    This function is used for function get_number_of_transitive_relations

    Check if relation is transitive.

    >>> is_transitive_1([(1, 2), (2, 3), (1, 3)])
    True
    >>> is_transitive_1([(1, 1), (2, 2), (1, 3)])
    False
    '''
    second_elements = [b for (a, b) in relation]
    for (a, b) in relation:
        for c in second_elements:
            if (b, c) in relation and (a,c) not in relation:
                return False
    return True

def get_number_of_transitive_relations(number_of_elements):
    """
    int -> int

    WARNING!!!
    DO NOT USE THIS VERSION OF FUNCTION FOR NUMBERS HIGHER THAN 5
    IT MAY LEAD TO CALCULATIONS THAT WILL CONTINUE FOR MORE THAN
    2000 MINUTES

    Counts a number of transitive relations on set {A x A}
    where A has [number_of_elements] elements

    >>> get_number_of_transitive_relations(0)
    1
    >>> get_number_of_transitive_relations(1)
    2
    >>> get_number_of_transitive_relations(2)
    13
    >>> get_number_of_transitive_relations(3)
    171
    >>> get_number_of_transitive_relations(4)
    3994
    """
    A = [x for x in range(number_of_elements)]
    main_relation = [(x, y) for y in A for x in A]
    # main_relation -- relation with all possible elements in set {A x A}
    binary_set = [0 for y in A for x in A]
    # binary_set -- will be used to generate differend relations from main_relation

    # Doing next cycle we will go trough all possible combinations of elements
    # in main_relation and count them if they are transitive
    amount_of_transitive_relations = 0
    while 0 in binary_set:

        # Creates blank that will be used for the current relation
        while 2 in binary_set:
            index_of_2 = binary_set.index(2)
            binary_set[index_of_2] = 0
            binary_set[index_of_2 + 1] += 1

        # Creates relation on the blank
        relation = []
        for index in range(len(binary_set)):
            if binary_set[index] == 1:
                relation.append(main_relation[index])
        
        # Prepares the blank for the next relation
        binary_set[0] += 1

        # Checks if the relation is transitive
        # If yes, then includes it in the amount of transitive relations
        if is_transitive_1(relation):
            amount_of_transitive_relations += 1

    return amount_of_transitive_relations + 1



if __name__ =='__main__':
    # Read
    relation = read_relation('rel_1500_0.9.csv')
    print('ended')

    ## Closures
    #reflexive = get_reflexive_closure(relation)
    #print('refl ended')
    #symmetric = get_symmetric_closure(relation)
    #print('symm ended')
    transitive = get_transitive_closure(relation)
    print('trans ended')

    ## Equivalance classes
    #eqiuv_classes = get_equivalence_class(relation)
    #print('eq_clss ended')

    # Is_transitive
    #trans = is_transitive(relation)
    #print('is_trans')

    #num = get_number_of_transitive_relations(5)
    #print('ended')

    # Write
    #write_relation(relation)
    #print('ended')
