[README in English](README.md)

# RadicalPolymerDS

## 概要
このリポジトリは、量子化学計算によって得られたポリマーの伝搬反応に関するさまざまな特徴量を集めたデータセットを配布するために作成されました。ポリマーに関する化学・情報科学コミュニティに役立つことを目指しています。

## データセットの内容
データセットは csv 形式で提供されており、化学反応に関する多様な特徴量を含んでいます。([csv](RadicalPolymerDS/datasets/data/PropagationQuantumChem_2023-12-13.csv))
データセットに含まれる特徴量は以下の通りです。

|特徴量|説明|
| --- | --- |
| Radical | ラジカル分子に対応する SMILES |
| Monomer | モノマー分子の対応する SMILES |
| ... | ... |

収集対象分子は以下の通りです。


## 利用方法
このリポジトリには、csv ファイルの読み込みと処理を行うための Python モジュールも含まれています。Python 環境にて、このモジュールを利用することで、データセットを簡単に操作し分析を行うことができます。

### インストール方法
```sh
git clone https://github.com/hatanaka-lab/RadicalPolymerDS
```

### 使用例 1. SMILES 文字列を使って特徴量を取得する。
最も基本的な使い方は伝搬反応に関して集められた特徴量を `dataset.QCValuesFromSMILES()` 関数を使って取得する方法です。以下の例はラジカルの SMILES `smi_rad` とモノマーの SMILES `smi_mon` を使って特徴量を `pandas.DataFrame` の形で取得します。

```python
from RadicalPolymerDS import datasets

smi_rad = "C=CC(=O)OCCCCCCCCCCCC"
smi_mon = "C=CC(=O)O"

features = datasets.QCValuesFromSMILES(smi_rad, smi_mon)

print(features)
```
出力
```
      DE_decomposition_tail  ...  CCdist_TS
2078               0.042541  ...   2.268076

[1 rows x 26 columns]
```

データセットに未記載の SMILES を入力すると空のデータフレームが返ってきます。エテン分子 `"C=C"` を使って試してみます。
```python
features = datasets.QCValuesFromSMILES("C=C", smi_mon)

print(features)
```
出力
```
Empty DataFrame
Columns: [DE_decomposition_tail, DE_decomposition_head, DE_precursor, DE_TS, DE_product, DE_barrier, DE_reaction, DG_precursor, DG_TS, DG_product, DG_barrier, DG_reaction, E_Rad_SOMO, E_Rad_LUMO, E_Mon_HOMO, E_Mon_LUMO, DE_SHgap, DE_SLgap, VBur_R228_Mon, VBur_R350_Mon, VBur_R228_Rad, VBur_R350_Rad, Real_theta, Volume_MonteCarlo_Mon, Volume_MonteCarlo_Rad, CCdist_TS]
Index: []
```

欠損値を明示したい場合は `with_nan` (初期値は `False`) オプションを使って以下のようにします。
```python
features = datasets.QCValuesFromSMILES("C=C", smi_mon, with_nan=True)

print(features)
```
出力
```
      DE_decomposition_tail  ...  CCdist_TS
2500                    NaN  ...        NaN

[1 rows x 26 columns]
```

戻り値に入力した SMILES を含ませる場合には `with_smiles` (初期値は `False`) を使います。
```python
features = datasets.QCValuesFromSMILES("C=C", smi_mon, with_nan=True, with_smiles=True)

print(features)
```
出力
```
      Radical    Monomer  ...  CCdist_TS
2500      C=C  C=CC(=O)O  ...        NaN

[1 rows x 26 columns]
```

SMILES は `list` 型で入力することもできます。`list` を用いることで複数の特徴量を同時に取得できます。
```python
smi_list = [
    ["C=C(C)C(=O)OC", "C=C(C)C(=O)OC"],
    ["C=C(C)C(=O)OC", "C=CC(=O)O"],
    ["CO/C=C\C(=O)OC", "C=Cc1ccccc1"]
]

features = datasets.QCValuesFromSMILES(smi_list)
```
出力
```
     DE_decomposition_tail  ...  CCdist_TS
0                 0.038534  ...   2.254882
28                0.038534  ...   2.248237
152               0.045085  ...   2.409667

[3 rows x 26 columns]
```

