import csv
import os
import numpy as np
import pandas as pd
import textwrap


from ..utils import Bunch


_QCValues = "" #


def QCValuesFromSMILES(*smi, csv_file="", with_nan=False, with_smiles=False):
    """ Title

    text

    Args:
        smi (str):

    Returns:
        pandas.DataFrame

    Examples:
        ...

    """

    global _QCValues

    if not csv_file:
        csv_file = "PropagationQuantumChem_2023-12-13.csv"
    csv_path = f"{os.path.dirname(__file__)}/data/{csv_file}"

    if type(_QCValues) == str:
        if os.path.exists(csv_path):
            data = pd.read_csv(csv_path)
            _QCValues = Bunch(
                            data=data,
                            dataCount=data.index,
                            csv_file=csv_file
                             )
        else:
            return None
    else:
        data = _QCValues["data"]

    smi_arr = np.array(smi)
    if (len(smi_arr.shape) == 1 and smi_arr.shape[0] < 2) or \
       (len(smi_arr.shape) == 2 and smi_arr.shape[1] < 2):
        print(textwrap.dedent("""
          Two or more SMILES are required. Try the following

             >>> dataset.QCValuesFromSMILES("SMILES1", "SMILES2")

        """))

    elif len(smi_arr.shape) == 1:
        label = data["Radical"] == smi_arr[0]
        label &= data["Monomer"] == smi_arr[1]
        # データが無い場合
        if not label.any():
            # 新しい空の行を追加する
            i = label.size
            new_data = pd.DataFrame({"Radical": [smi_arr[0]],
                                     "Monomer": [smi_arr[1]]},
                                     index=[label.size])
            _QCValues["data"] = pd.concat([data, new_data])
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
        return QCValuesFromSMILES(smi_arr[0, 0], smi_arr[0, 1],
                                  with_nan=with_nan,
                                  with_smiles=True)

    elif len(smi_arr.shape) == 3:
        preserve = pd.DataFrame(columns=data.columns)
        for rad, mon in smi_arr[0]:
            new_data = QCValuesFromSMILES(rad, mon,
                                          with_nan=with_nan,
                                          with_smiles=True)
            preserve = pd.concat([preserve, new_data])
    else:
        preserve = pd.DataFrame(columns=data.columns)

    if with_smiles:
        return preserve
    else:
        return preserve.drop(["Radical", "Monomer"], axis=1)


def load_testset(*, N=10):
    data = list(range(N))
    target = list(range(N))
    return Bunch(
        data=data,
        target=target
    )


