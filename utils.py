def kmer_permutations(alphabet, k_size):
    '''
    This function produces all possible permutations of letters/nucleotides for a given kmer size.

    alphabet: a list of the possible letters in your alphabet; e.g. for DNA this is ['A','C','G','T']

    k_size: an integer, the kmer size of your resulting permutations; e.g. 6

    The number of resulting permutations will be alphabet**k_size; e.g. for 10-mers of DNA nucleotides, there are 4^10 or 1048576 possible combinations of nucleotides.
    '''
    import itertools
    permutations = set()
    for combo in itertools.product(alphabet, repeat=k_size):
        permutations.add(''.join(combo))
    return permutations
