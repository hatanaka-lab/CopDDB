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


def m1m2list_to_11_12(smiles=[], with_nan=False, with_smiles=False):
    """
    Generates and returns features from given pairs of monomer SMILES.

    Args:
        smiles (list)     : A list of pairs of monomer SMILES, where each pair
                            is specified as [["M1", "M2"], ...].
        with_nan (bool)   : Include  NaN in the output if True.
                            Defaults to False.
        with_smiles (bool): Include SMILES in the output if True.
                            Defaults to False.

    Returns:
        Bunch('data': pandas.DataFrame, 'smiles': smiles) 
    """
    # Names of descriptors
    desc_names = get_available_descriptors()
    # Get descriptor names derived from molecule (M* or M)
    f_mol = os.path.dirname(__file__)+"/data/moleculeProperties.txt"
    f_rad = os.path.dirname(__file__)+"/data/radicalProperties.txt"
    mol_desc_names = [key for key in _read_text_to_list(f_mol)
                      if key in desc_names]
    rad_desc_names = [key for key in _read_text_to_list(f_rad)
                      if key in desc_names]
    # (dict) to store information that will be output.
    preserve = {}
    if with_smiles:
        preserve.update({"Monomer 1": [], "Monomer 2": []})
    sufs = ["11", "12"]
    for name in desc_names:
        for suf in sufs:
            if name in rad_desc_names:
                preserve[f"{name}_{suf[0]}"] = []
            elif name in mol_desc_names:
                preserve[f"{name}_{suf[1]}"] = []
            else:
                preserve[f"{name}_{suf}"] = []
    # The part to add features.
    for m1, m2 in smiles:
        if with_smiles:
            preserve["Monomer 1"].append(m1)
            preserve["Monomer 2"].append(m2)
        for i_pair, smi_pair in enumerate([[m1, m1], [m1, m2]]):
            vals = descriptors_from_smiles(smi_pair, with_nan=True)
            for name in desc_names:
                i_col = vals.columns.get_loc(name)
                val = vals.iloc[0, i_col]
                if name in rad_desc_names:
                    if i_pair == 0: # M1* + M1
                        preserve[f"{name}_1"].append(val)
                elif name in mol_desc_names:
                    if i_pair == 0: # M1* + M1
                        preserve[f"{name}_1"].append(val)
                    else: # i_pair == 1, M1* + M2
                        preserve[f"{name}_2"].append(val)
                else:
                    preserve[f"{name}_{sufs[i_pair]}"].append(val)
    # Make pandas.DataFrame
    new_df = pd.DataFrame.from_dict(preserve)
    # with_nan option
    if with_nan:
        mask = np.full(new_df.shape[0], True)
    else:
        mask = ~new_df.isnull().any(axis=1)
    # Output
    return Bunch(
                 data=new_df[mask],
                 smiles=smiles,
                )


def m1list_and_m2_to_11_12_21(m1s=[], m2="",
                              with_nan=False,
                              with_smiles=False):
    """
    Generates and returns features from given M1 SMILES list and M2 SMILES.

    Args:
        m1s (list): The list of monomers of M1. ["A", "B", "C",... ].
        m2 (str): The monomer that must be included. "Monomer 2" (SMILES).

    Returns:
        Bunch('data': pandas.DataFrame, 'm1s': list, 'm2': str) 
    """
    # Names of descriptors
    desc_names = get_available_descriptors()
    # Get descriptor names derived from molecule (M* or M)
    f_mol = os.path.dirname(__file__)+"/data/moleculeProperties.txt"
    f_rad = os.path.dirname(__file__)+"/data/radicalProperties.txt"
    mol_desc_names = [key for key in _read_text_to_list(f_mol)
                      if key in desc_names]
    rad_desc_names = [key for key in _read_text_to_list(f_rad)
                      if key in desc_names]
    # (dict) to store information to be out.
    preserve = {}
    if with_smiles:
        preserve.update({"Monomer 1": [], "Monomer 2":[]})
    sufs = ["11", "12", "21"]
    for name in desc_names:
        for suf in sufs:
            if name in rad_desc_names:
                preserve[f"{name}_{suf[0]}"] = []
            elif name in mol_desc_names:
                preserve[f"{name}_{suf[1]}"] = []
            else:
                preserve[f"{name}_{suf}"] = []
    # The part to add features.
    for m1 in m1s:
        if with_smiles:
            preserve["Monomer 1"].append(m1)
            preserve["Monomer 2"].append(m2)
        for i_pair, smi_pair in enumerate([[m1, m1], [m1, m2], [m2, m1]]):
            vals = descriptors_from_smiles(smi_pair, with_nan=True)
            for name in desc_names:
                i_col = vals.columns.get_loc(name)
                val = vals.iloc[0, i_col]
                if name in rad_desc_names:
                    if i_pair == 0: # M1* + M1
                        preserve[f"{name}_1"].append(val)
                    elif i_pair == 2: # M2* + M1
                        preserve[f"{name}_2"].append(val)
                elif name in mol_desc_names:
                    if i_pair == 0: # M1* + M1
                        preserve[f"{name}_1"].append(val)
                    elif i_pair == 1: # M1* + M2
                        preserve[f"{name}_2"].append(val)
                else:
                    preserve[f"{name}_{sufs[i_pair]}"].append(val)
    # Make pandas.DataFrame
    new_df = pd.DataFrame.from_dict(preserve)
    # with_nan option
    if with_nan:
        mask = np.full(new_df.shape[0], True)
    else:
        mask = ~new_df.isnull().any(axis=1)
    # Out
    return Bunch(
                 data=new_df[mask],
                 m1s=m1s,
                 m2=m2,
                )


def build_11_12_variables_from_smiles_and_y(smiles=[], y=[],
                                            with_nan=False,
                                            with_smiles=False):
    """
    Generates and returns features from given pairs of monomer SMILES.          
                                                                                
    Args:                                                                       
        smiles (list)     : A list of pairs of monomer SMILES, where each pair  
                            is specified as [["M1", "M2"], ...].
        y (list)          : Target variables.
        with_nan (bool)   : Include  NaN in the output if True.
                            Defaults to False.
        with_smiles (bool): Include SMILES in the output if True.
                            Defaults to False.

    Returns:                                                                    
        Bunch('data': pandas.DataFrame, 'target': numpy.array)
    """
    if len(smiles) != len(y):
        print("The lengths of smiles and y must be the same.")
        print(f"len(smiles): {len(smiles)}\nlen(y)     : {len(y)}")
        return None

    dataset = m1m2list_to_11_12(smiles, with_nan=True, with_smiles=with_smiles)
    new_df = dataset.data

    mask = new_df.isnull().any(axis=1)
    if with_nan:
        mask = np.full(new_df.shape[0], True)
    else:
        mask = ~new_df.isnull().any(axis=1)
    # Out
    return Bunch(
                 data=new_df[mask],
                 target=np.array(y)[mask],
                )
