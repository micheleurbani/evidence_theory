
import pandas as pd
from evidence_theory_simulation import core


def generate_datasets(N, m, n):
    """
    Returns `N` pandas DataFrame each containing a simulated use-case of
    evidence theory.

    Paramters
    ---------
    N : int
    The number of datasets to be generated.
    m : int
    The number of elements in the universal set `X`.
    n : int
    The number of focal points of the powerset :math:`P_X`.

    Returns
    -------
    data : list
    A list of `pandas.DataFrame`.
    """
    data = []
    for i in range(N):
        data.append(
            core.generate_dataset(
                core.powerset(m),
                core.sample_mass(n, 2**m)
            )
        )
    return data


def experiment(N, m, n, entropy_measures):
    """
    Returns `N` samples of the entropy measures in `entropy_measures`.
    """
    ds = generate_datasets(N, m, n)
    results = []
    for d in ds:
        data = {}
        for measure in entropy_measures:
            data[measure.__name__] = measure(d)
        results.append(data)
    return pd.DataFrame(results)
