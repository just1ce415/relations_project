"""
This module is created to operate and process with
relations based on the martix representation
(every element[row][column] is presetented as:
1 - if element IS in relation
0 - if element IS NOT in relation)

Project repository:
https://github.com/just1ce415/relations_project
"""
import copy

def read_relation(path: str) -> list:
    '''
    (str) -> list(list)

    Reads a relation (matrix) from the file stated as [path]
    and returns the list of lists

    Supported separators: ","   ", "   " "(csv file).
    '''
    with open(path, 'r', encoding='utf=8') as relation_file:
        relation_list = []

        # Searching for separator in line
        for line in relation_file:
            if line.find(', ') != -1:
                separator = ', '
            elif line.find(' ') != -1:
                separator = ' '
            else:
                separator = ','

            # The last line of the file
            if line == '':
                break

            # Cutting off '\n' and turning into list (rows of matrix)
            row = line[:-1].split(separator)

            # Turning every element of matrix into integer number
            # and adding the row to the matrix
            for index in range(len(row)):
                row[index] = int(row[index])
            relation_list.append(row)

        return relation_list


def write_relation(relation: list, path: str='relation_out.csv'):
    '''
    list(list) -> file

    Writes relation (matrix) to the file with (path).
    The function creates relation_out.csv in
    the project root directory by default.
    '''
    with open(path, 'w', encoding='utf-8') as relation_file:

        # Writing every row into file with relation
        for row in relation:
            # Turning every element into string and joining it into file
            row = [str(element) for element in row]
            relation_file.write(','.join(row) + '\n')


def get_symmetric_closure(relation: list) -> list:
    """
    list(list) -> list(list)

    Receives the list of lists with matrix and
    returns the list with this matrix's symmetric closure.

    >>> get_symmetric_closure([[0, 1, 0, 0, 0], [1, 1, 1, 0, 1], \
[1, 1, 1, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 0, 0]])
    [[0, 1, 1, 0, 0], [1, 1, 1, 0, 1], [1, 1, 1, 0, 0], \
[0, 0, 0, 1, 1], [0, 1, 0, 1, 0]]
    >>> get_symmetric_closure([[0, 1, 0, 0], [1, 1, 1, 1], \
[0, 0, 1, 0], [0, 0, 1, 0]])
    [[0, 1, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 0]]
    """
    # Going through every element of matrix
    for row in range(len(relation)):
        for column in range(len(relation)):

            # If element (a, b) in relation, add (b, a)
            if relation[row][column] == 1:
                relation[column][row] = 1

    return relation


def get_reflexive_closure(relation: list) -> list:
    """
    list(list) -> list(list)

    Receives the list of lists with matrix and
    returns the list with this matrix's reflexive closure.

    >>> get_reflexive_closure([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    >>> get_reflexive_closure([[0, 1, 0, 0], [1, 1, 1, 1], \
[0, 0, 1, 0], [0, 0, 1, 0]])
    [[1, 1, 0, 0], [1, 1, 1, 1], [0, 0, 1, 0], [0, 0, 1, 1]]
    """
    for index in range(len(relation)):
        # Add element, that may be represented as (a, a)
        relation[index][index] = 1

    return relation


def get_transitive_closure(relation: list) -> list:
    '''
    list(list) -> list(list)

    Receives the list of lists with matrix and using Warshall's Algorithm
    transforms and returns the list with this matrix's transitive closure.

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


def is_transitive(relation: list) -> bool:
    '''
    list(list) -> bool

    Check if matrix with relation (list of lists) is transitive
    using Warshall's Algorithm.
    (If transitive closure of relation is equal to relation
    then it is itransitive)

    >>> is_transitive([[1, 0, 1], [1, 1, 0], [0, 0, 1]])
    False
    >>> is_transitive([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], \
[0, 1, 1, 0, 0], [0, 1, 1, 1, 0]])
    True
    >>> is_transitive([[1, 0, 1, 1], [1, 0, 1, 1], [1, 0, 1, 1], [1, 0, 1, 1]])
    True
    '''
    # If relation has no elements it is already transitive
    if len(relation) == 0:
        return True

    # t_closure -- transitive closure of the relation
    t_closure = copy.deepcopy(relation)
    # k index states for W(k) matrix
    for k in range(len(relation)):
        for i in range(len(relation)):
            for j in range(len(relation)):
                # W(k)[i][j] = W(k-1)[i][j] or (W(k-1)[i][k] and W(k-1)[k][j])
                t_closure[i][j] = t_closure[i][j] | (t_closure[i][k] & t_closure[k][j])

                # If only one element has a diference, it is already not transitive
                if relation[i][j] != t_closure[i][j]:
                    return False

    return True


def get_equivalence_classes(relation: list) -> list:
    """
    list(list) -> list(list)

    Receives the list of lists with matrix of relation of equivalence and
    returns all its equivalence classes as list of lists.

    >>> get_equivalence_classes([[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], \
[0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]])
    [[0], [1], [2], [3], [4]]
    >>> get_equivalence_classes([[1, 0, 1, 0], [0, 1, 0, 0], \
[1, 0, 1, 0], [0, 0, 0, 1]])
    [[0, 2], [1], [3]]
    """
    # Creating a blank for equivalence classes
    equivalence_dictionary = {key: set() for key in range(len(relation))}
    length = len(relation)

    # Adding an element to a needed equivalence class
    [equivalence_dictionary[row].add(column)
        for row in range(length)
        for column in range(length) if relation[row][column] == 1]

    # Creating final classes of equivalence
    result = []
    [result.append(list(element)) for element in equivalence_dictionary.values()
    if list(element) not in result]

    return result


def is_transitive_alternative(relation):
    '''
    (list(list)) -> bool

    This function is used for function get_number_of_transitive

    Checks if [relation] is transitive.

    >>> is_transitive_alternative([(1, 2), (2, 3), (1, 3)])
    True
    >>> is_transitive_alternative([(1, 1), (2, 2), (1, 3)])
    False
    '''
    second_elements = [b for (a, b) in relation]
    for (a, b) in relation:
        for c in second_elements:
            # if (a, b) in relation, (b, c) in relation
            # and (a, c) not in relation -> False 
            if (b, c) in relation and (a,c) not in relation:
                return False

    return True

def get_number_of_transitive(number_of_elements):
    """
    int -> int

    WARNING!!!
    DO NOT USE THIS FUNCTION FOR NUMBERS HIGHER THAN 5
    IT MAY LEAD TO CALCULATIONS THAT WILL CONTINUE FOR MORE THAN
    40 HOURS

    Counts a number of transitive relations on set {A x A}
    where A has [number_of_elements] elements

    >>> get_number_of_transitive(0)
    1
    >>> get_number_of_transitive(1)
    2
    >>> get_number_of_transitive(2)
    13
    >>> get_number_of_transitive(3)
    171
    >>> get_number_of_transitive(4)
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
        if is_transitive_alternative(relation):
            amount_of_transitive_relations += 1

    return amount_of_transitive_relations + 1



if __name__ =='__main__':
    #~~~Read~~~
    #relation = read_relation('rel_1500_0.45.csv')
    #print('read ended')

    #~~~Closures~~~
    #reflexive = get_reflexive_closure(relation)
    #print('refl ended')
    #symmetric = get_symmetric_closure(relation)
    #print('symm ended')
    #transitive = get_transitive_closure(relation)
    #print('trans ended')

    #~~~Equivalance classes~~~
    #eqiuv_classes = get_equivalence_classes(relation)
    #print('eq_clss ended')

    #~~~Is_transitive~~~
    #trans = is_transitive(relation)
    #print('is_trans')

    #~~~Number_of_transitive~~~
    #num = get_number_of_transitive(5)
    #print('num_of_tr ended')

    #~~~Write~~~
    #write_relation(relation)
    #print('write ended')
