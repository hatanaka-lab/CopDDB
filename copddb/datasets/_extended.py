import numpy as np
import os
import pandas as pd


from ._base import (
        get_available_descriptors,
        descriptors_from_smiles,
    )
from ..utils import (
        Bunch,
        canonical_smiles,
        _read_text_to_list
    )


def build_pair_variables_from_smiles_and_y(smiles=[], y=[],
                                           with_nan=False,
                                           with_smiles=False):
    """

    Expranation

    Args:
        smiles (list): [["A", "B"], ["C", "D"], ...]
        y (list): [v1, v2, v3, ...]

    Returns:
        Bunch('data': DataFrame, 'target': array)

    """
    if len(smiles) != len(y):
        print("The lengths of smiles and y must be the same.")
        print(f"len(smiles): {len(smiles)}\nlen(y)     : {len(y)}")
        return None

    descriptors = get_available_descriptors()
    # Get descriptor names derived from molecule (M* or M).
    f = os.path.dirname(__file__)+"/data/moleculeProperties.txt"
    mol_descriptors = [key for key in _read_text_to_list(f)
                       if key in descriptors]
    # Set descriptor names derived from reaction (M* and M).
    rea_descriptors = [key for key in descriptors if not key in mol_descriptors
                       if not key in ["Radical", "Monomer"]]

    # Set new descriptor names
    preserve = {"Monomer 1": [], "Monomer 2": []}
    rea_suffixes = ["_11", "_12"]
    preserve.update({k+suf: [] for k in rea_descriptors
                     for suf in rea_suffixes})
    mol_suffixes = ["_1", "_2"]
    preserve.update({k+suf: [] for k in mol_descriptors
                     for suf in mol_suffixes})

    # Reaction_11 : M1* + M1 -> M1*
    # Reaction_12 : M1* + M2 -> M2*
    # Reaction_22 : M2* + M2 -> M2*
    # Set data
    cansmi_dict = {}
    for smi1, smi2 in smiles:
        data_11 = descriptors_from_smiles(smi1, smi1, with_nan=True)
        data_12 = descriptors_from_smiles(smi1, smi2, with_nan=True)
        data_22 = descriptors_from_smiles(smi2, smi2, with_nan=True)
        # Add new descriptors (molecule)
        for data, suf in zip([data_11, data_22], mol_suffixes):
            for des in mol_descriptors:
                key = des + suf
                val = data[des].values[0]
                preserve[key].append(val)
        # Add new descriptors (reaction)
        for data, suf in zip([data_11, data_12], rea_suffixes):
            for des in rea_descriptors:
                key = des + suf
                val = data[des].values[0]
                preserve[key].append(val)
        # Add SMILES
        for smi, key in zip([smi1, smi2], ["Monomer 1", "Monomer 2"]):
            if smi in cansmi_dict:
                preserve[key].append(cansmi_dict[smi])
            else:
                cansmi = canonical_smiles(smi)
                cansmi_dict[smi] = cansmi
                preserve[key].append(cansmi)

    new_df = pd.DataFrame.from_dict(preserve)

    if with_smiles:
        pass
    else:
        new_df = new_df.drop(["Monomer 1", "Monomer 2"], axis=1)

    if with_nan:
        return Bunch(
                   data=new_df,
                   target=np.array(y)
               )
    else:
        label = new_df.isnull().any(axis=1)
        return Bunch(
                   data=new_df[~label],
                   target=np.array(y)[~label]
               )
