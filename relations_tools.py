"""
The module with functions to operate and process with relations based on the martix representation.
Project repository: https://github.com/just1ce415/relations_project
"""

def read_relation(path):
    '''
    (str) -> list(list)
    Reads a relation (matrix) from the file stated as (path) and returns the list of lists.
    Supported separators: ' ', ',', ' ,'.
    '''
    pass


def write_relation(path='relation.txt', relation):
    '''
    (str, list(list)) ->
    Writes relation (matrix) to the file with (path). The function create relation.txt in
    the project root directory by default. Separator: ' '.
    '''
    pass


def get_reflexive_closure(relation):
    '''
    (list(list)) -> list(list)
    '''
    pass


def get_symmetric_closure(relation):
    '''
    (list(list)) -> list(list)
    '''
    pass


def get_transitive_closure(relation):
    '''
    (list(list)) ->l ist(list)
    '''
    pass


def is_transitive(relation):
    '''
    (list(list)) -> bool
    '''
    pass


def get_equivalence_classes(relation):
    '''
    (list(list)) -> list(list)
    '''
    pass


def get_number_transitive_relations(n):
    '''
    (int) -> int
    '''
    pass


if __name__ = '__main__':
    import doctest
    print(doctest.testmod())
