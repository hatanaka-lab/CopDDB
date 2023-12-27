import csv
from glob import glob
import os
import numpy as np
import pandas as pd
import textwrap


from ..utils import Bunch, canonical_smiles


# A DataFrame object that hold data obtained from
# quantum chemical calculations.
_QCValues = ""


def buildVariablesFromSMILESandY(smiles=[], y=[],
                                 with_nan=False,
                                 with_smiles=False):
    """

    Expranation

    Args:
        smiles (list):
        y (list):

    Returns:
        Bunch('data': DataFrame, "target": array)
    """
    if len(smiles) != len(y):
        print("The lengths of smiles and y must be the same.")
        print(f"len(smiles): {len(smiles)}\nlen(y)     : {len(y)}")
        return None

    data = QCValuesFromSMILES(smiles, with_nan=True, with_smiles=with_smiles)
    label = data.isnull().any(axis=1)

    if with_nan:
        return Bunch(
                   data=data,
                   target=np.array(y)
               )
    else:
        return Bunch(
                   data=data[~label],
                   target=np.array(y)[~label]
               )


def getAvailableFeatures(csv_file=""):
    """ Return keys in the feature dataset.

    Expranation

    Returns:
        list
    """

    global _QCValues

    if type(_QCValues) == str:
        _load_QCValues(csv_file)
    return list(_QCValues["data"].keys())


def getAvailableSMILES(csv_file=""):
    """ Returns a list of SMILES registered in the feature dataset.

    Expranation

    Returns:
        list
    """

    global _QCValues

    if type(_QCValues) == str:
        _load_QCValues(csv_file)
    data = _QCValues["data"]

    return list(set(data["Radical"]) | set(data["Monomer"]))


def _load_QCValues(csv_file=""):
    """ Functions for reading data on propagation reactions.

    Explanation

    Args:
        csv_file (str): csv file.

    Returns:
        None
    """

    global _QCValues

    if not csv_file:
        files = glob(os.path.dirname(__file__)+"/data/PropagationQuantumC*csv")
        files.sort()
        csv_file = os.path.basename(files[-1])
    csv_path = f"{os.path.dirname(__file__)}/data/{csv_file}"

    if os.path.exists(csv_path):
        data = pd.read_csv(csv_path)
 
        # Canonicalize SMILES.
        cansmi_list = []
        for targ in ["Radical", "Monomer"]:
            for i in data.index:
                inpsmi = data[targ][i]
                if inpsmi in cansmi_list:
                    continue
                cansmi = canonical_smiles(inpsmi)
                # 変換に失敗した場合
                if not cansmi:
                    print(f"{inpsmi} cannot be converted into ", end="")
                    print("canonical SMILES.")
                    cansmi = np.NaN
                data.loc[data["Radical"] == inpsmi, "Radical"] = cansmi
                data.loc[data["Monomer"] == inpsmi, "Monomer"] = cansmi
                # Canonical SMILES をリストに記録する
                cansmi_list.append(cansmi)
 
        _QCValues = Bunch(
                        data=data,
                        initDataCount=data.index,
                        csv_file=csv_file
                         )
    else:
        print(f"{csv_file} does not exist in {os.path.dirname(__file__)}.")
        files = glob(os.path.dirname(__file__)+"/data/PropagationQuantumC*csv")
        print("The following files are available instead")
        for file in files:
            print(os.path.basename(file))


def QCValuesFromSMILES(*smi, csv_file="", with_nan=False, with_smiles=False):
    """ Return a pandas DataFrame containing the data corresponding to the
        input SMILES.

    Args:
        smi (str or list): 

    Returns:
        pandas.DataFrame

    Examples:
        ...

    """

    global _QCValues

    if type(_QCValues) == str:
        _load_QCValues(csv_file)
    data = _QCValues["data"]

    smi_arr = np.array(smi)
    if (len(smi_arr.shape) == 1 and smi_arr.shape[0] < 2) or \
       (len(smi_arr.shape) == 2 and smi_arr.shape[1] < 2):
        print(textwrap.dedent("""
          Two or more SMILES are required. Try the following

             >>> dataset.QCValuesFromSMILES("SMILES1", "SMILES2")

        """))

    elif len(smi_arr.shape) == 1:
        cansmi_rad = canonical_smiles(smi_arr[0])
        cansmi_mon = canonical_smiles(smi_arr[1])
        label = data["Radical"] == cansmi_rad
        label &= data["Monomer"] == cansmi_mon
        # データが無い場合
        if not label.any():
            # 新しい空の行を追加する
            new_data = pd.DataFrame({"Radical": [cansmi_rad],
                                     "Monomer": [cansmi_mon]},
                                     index=[label.size])
            _QCValues["data"] = pd.concat([data, new_data], sort=False)
            if with_nan:
                preserve = _QCValues["data"].tail(1)
            else:
                preserve = data[label]
        # NaN を含んでも良い場合
        elif with_nan:
            preserve = data[label]
        else:
            # NaN を含んではいけないが、対象に NaN が無い場合
            test = data[label].values[0, 2:].sum()
            if test == test:
                preserve = data[label]
            # それ以外
            else:
                preserve = pd.DataFrame(columns=data.columns)

    elif len(smi_arr.shape) == 2:
        preserve = QCValuesFromSMILES(smi_arr[0, 0], smi_arr[0, 1],
                                      with_nan=with_nan,
                                      with_smiles=True)

    elif len(smi_arr.shape) == 3:
        preserve = pd.DataFrame(columns=data.columns)
        for rad, mon in smi_arr[0]:
            new_data = QCValuesFromSMILES(rad, mon,
                                          with_nan=with_nan,
                                          with_smiles=True)
            preserve = pd.concat([preserve, new_data])
    else: # No case should come here.
        preserve = pd.DataFrame(columns=data.columns)

    if with_smiles:
        return preserve
    else:
        return preserve.drop(["Radical", "Monomer"], axis=1)
