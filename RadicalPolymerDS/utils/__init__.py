"""
`RadicalPolymerDS.utils` module includes various utilities.
"""


from rdkit import Chem as _Chem


from ._bunch import Bunch


def canonical_smiles(smiles):
    """
    Function to obtain canonical SMILES.

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
