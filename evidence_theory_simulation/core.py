
def powerset(fullset):
    """
    Generates the power set of `fullset`.

    Parameters
    ----------
        fullset : list
        The set of which the powerset is returned.

    Returns
    -------
        powerset : list
        The powerset is a list of lists.

    """
    listsub = list(fullset)
    subsets = []
    for i in range(2**len(listsub)):
        subset = []
        for k in range(len(listsub)):
            if i & 1 << k:
                subset.append(listsub[k])
        subsets.append(subset)
    return subsets

def mass2belief(mass_value):
    pass

def mass2plausibility(mass_value):
    pass

def generate_dataset(powerset, known_mass_elements):
    """
    Generate a list of dictionaries ready to be transformed into a Pandas
    DataFrame for visualization.
    A probability mass value is assigned to `known_mass_elements` elements of
    the power set and all the values of the mass sum to 1.

    Parameters
    ----------
        powerset : list
        A list of lists representing a powerset.

        known_mass_elements : int
        The number of elements which mass is known.

    Returns
    -------
        data : list
        A list of dicts containing the powerset elements and the relative
        values of mass, believe, and plausibility.

    """
    pass

if __name__ == "__main__":
    pass
