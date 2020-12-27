"""
The module with functions to operate and process with relations based on the martix representation.
Project repository: https://github.com/just1ce415/relations_project
"""

def read_relation(path):
    '''
    (str) -> list(list)
    Reads a relation (matrix) from the file stated as (path) and returns the list of lists                 
    (!!!of strings).
    Supported separators: ' ', ',', ' ,'. If there's inappropriate separator, the function
    will return None.
    '''
    with open(path, 'r', encoding='utf=8') as rel_f:
        relation_lst = []
        for line in rel_f:
            if line.find(' ,') != -1:
                relation_lst.append(line[:-1].split(' ,'))
            elif line.find(',') != -1:
                relation_lst.append(line[:-1].split(','))
            elif line.find(' ') != -1:
                relation_lst.append(line[:-1].split(' '))
            else:
                return None
        return relation_lst


def write_relation(relation, path='relation_out.txt'):
    '''
    (list(list), str) ->
    Writes relation (matrix) to the file with (path). The function create relation_out.txt in
    the project root directory by default. Separator: ' '.
    '''
    with open(path, 'w', encoding='utf-8') as rel_f:
        for row in relation:
            rel_f.write(' '.join(row) + '\n')


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
