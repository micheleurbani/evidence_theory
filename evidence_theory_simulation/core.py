
import numpy as np

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

def _sample_mass_values(n):
    """
    Sample `n` random numbers that sum to 1.
    """
    w = np.random.rand(n)
    w = w / np.sum(w)
    return w

def sample_mass(n, m):
    """
    Sample a mass array with `n` non-zero elements that sum to one.

    Parameters
    ----------
    n : int
    The number of non-zero elements.

    m : int
    The length of the array.

    Returns
    -------
    mass : numpy array
    A numpy array with length `m` and `n` non-zero elements.

    """
    w = _sample_mass_values(n)
    mass = np.zeros((m,))
    idxs = np.random.choice(np.arange(m), n, replace=False)
    for i, idx in enumerate(idxs):
        mass[idx] = w[i]
    return mass

def mass2belief(mass_value):
    raise NotImplemented

def mass2plausibility(mass_value):
    raise NotImplemented

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
