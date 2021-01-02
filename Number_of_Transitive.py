def is_transitive(relation):
    return True

def number_of_transitive(number_of_elements):
    """
    int -> int

    WARNING!!!
    DO NOT USE THIS VERSION OF FUNCTION FOR NUMBERS HIGHER THAN 5
    IT MAY LEAD TO CALCULATIONS THAT WILL CONTINUE FOR MORE THAN
    2000 MINUTES

    Also, this version of function is not working right, because it must
    use function which checks if the relation is transitive.
    Now it returns just amount of relations that may be built on the set
    that has amount_of_elements elements

    Counts a number of transitive relations on set {A x A}
    where A has [number_of_elements] elements

    >>> number_of_transitive(0)
    1
    >>> number_of_transitive(1)
    2
    >>> number_of_transitive(2)
    13
    >>> number_of_transitive(3)
    171
    >>> number_of_transitive(4)
    3,994
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
        if is_transitive(relation):
            amount_of_transitive_relations += 1

    return amount_of_transitive_relations

print(number_of_transitive(5))