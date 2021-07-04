
import numpy as np

def powerset(m):
    """
    Generates the power set of `fullset`.

    Parameters
    ----------
    m : int
    The number of elements in the universal set `X`.

    Returns
    -------
    powerset : numpy array
    An boolean array with size :math:`m \\times 2^m` that define whether an
    element of `X` (on columns) belongs to the element (on rows) of the power
    set.

    """
    powerset = [np.zeros((m,))]
    for i in range(m):
        for j in range(len(powerset)):
            x = np.copy(powerset[j])
            x[i] = 1
            powerset.append(x)
    return np.stack(powerset)

def _sample_mass_values(n):
    """
    Sample `n` random numbers that sum to 1.
    """
    w = -np.log(np.random.rand(n))
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
    idxs = np.random.choice(np.arange(1, m), n, replace=False)
    for i, idx in enumerate(idxs):
        mass[idx] = w[i]
    return mass

def mass2belief(mass):
    """
    Compute the beliefe value from a mass value.
    """
    raise NotImplementedError

def mass2plausibility(mass):
    """
    Compute the plausibility value from a mass value.
    """
    raise NotImplementedError

def generate_dataset(powerset, mass):
    """
    Generate a list of dictionaries ready to be transformed into a Pandas
    DataFrame for visualization.
    A probability mass value is assigned to `known_mass_elements` elements of
    the power set and all the values of the mass sum to 1.

    Parameters
    ----------
    powerset : list
    A list of lists representing a powerset.

    mass : numpy array
    The number of elements which mass is known.

    Returns
    -------
    data : list
    A list of dicts containing the powerset elements and the relative values
    of mass, believe, and plausibility.

    """
    raise NotImplementedError

if __name__ == "__main__":
    pass
