"""
`RadicalPolymerDS.utils` module includes various utilities.
"""


import os


from rdkit import Chem as _Chem


from ._bunch import Bunch


def canonical_smiles(smiles):
    """ Function to obtain canonical SMILES.

    Args:
        smiles (str): SMILES

    Returns:
        str: Canonical SMILES
    """
    try:
        mol = _Chem.MolFromSmiles(str(smiles))
        can = _Chem.MolToSmiles(mol)
        return can
    except:
        return ""


def _read_text_to_list(file):
    """ Function that returns a list of words separated by lines in the text.

    Args:
        file (str): File name.

    Returns:
        list: ["str0", "str1", ...]
    """
    if os.path.exists(file):
        with open(file, 'rt') as fin:
            lines = fin.read().split("\n")
        return [l for l in lines if l]
    else:
        return []
