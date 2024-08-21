def function1(a):
   """
    This function takes a DNA sequence (string) `a` and returns a dictionary `b` where the keys are the unique 
    nucleotides (A, C, G, T) from the sequence `a`, and the values represent the frequency (count) of each nucleotide.

    Args:
    a (str): A string representing a DNA sequence composed of characters A, C, G, and T.

    Returns:
    b (dict): A dictionary containing the frequency of each nucleotide in the DNA sequence `a`.
    """

    b = dict()
    for c in a:
        if c not in b:
            b[c] = 1
        else:
            b[c] += 1
    return b

def function2(a):
    """
    This function takes a dictionary `a` (likely produced by `function1`) and prints out the relative
    frequencies of nucleotides in a DNA sequence. The relative frequency is calculated by dividing the 
    nucleotide's count by the total count of all nucleotides.

    Args:
    a (dict): A dictionary where keys are nucleotides (A, C, G, T) and values are their respective frequencies.
    """

    print('freqs')
    total = float(sum([a[b] for b in a.keys()]))
    for b in a.keys():
        print(b + ':' + str(a[b]/total))

function2(function1('ATCTGACGCGCGCCGC'))
