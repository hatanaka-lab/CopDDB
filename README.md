[README in Japanese](./README_jp.md)

# CopDDB

## Overview
This repository has been created to distribute a dataset that collects various descriptors related to the propagation of polymers, obtained from quantum chemical calculations. It is intended to be useful to the polymer chemistry and computer science communities.

## Contents of CopDDB
The dataset is provided in [csv](./copddb/datasets/data/PropagationQuantumChem_2023-12-13.csv) format and contains a variety of descriptors for chemical reactions. The descriptors include in the dataset are as follows.

|Descriptor name|Description|
| --- | --- |
| Radical | SMILES for a radical (M<sub>1</sub>*) |
| Monomer | SMILES for a monomer (M<sub>2</sub>) |
| DE_tail | Reaction energy for the addition of a model initiator radical (Me*) to M<sub>1</sub> at the tail position |
| DE_head | Reaction energy for the addition of a model initiator radical (Me*) to M<sub>1</sub> at the head position, which affords M<sub>1</sub>* |
| DE_precursor | Relative energy of the precurser from the dissociation limit (M<sub>1</sub>* and M<sub>2</sub>) |
| DE_TS | Relative energy of the TS of C-C bond formation from the dissociation limit (M<sub>1</sub>* and M<sub>2</sub>) |
| DE_product | Relative energy of the product from the dissociation limit (M<sub>1</sub>* and M<sub>2</sub>) |
| DE_barrier |  Activation barrier for the C-C bond formation (<I>i.e.</I>, the energy difference between the precursor and the TS) |
| DE_reaction | Reaction energy for the C-C bond formation (<I>i.e.</I>, the energy difference between the precursor and the product) |
| E_Rad_SOMO | SOMO energy of M<sub>1</sub>* |
| E_Rad_LUMO | LUMO energy of M<sub>1</sub>* |
| E_Mon_HOMO | HOMO energy of M<sub>2</sub> |
| E_Mon_LUMO | LUMO energy of M<sub>2</sub> |
| DE_SHgap | Energy difference between SOMO of M<sub>1</sub>* and HOMO of M<sub>2</sub> |
| DE_SLgap | Energy difference between SOMO of M<sub>1</sub>* and LUMO of M<sub>2</sub> |
| VBur_R228_Rad | %<I>V</I><sub>Bur</sub> within 2.28 Å of the reactive carbon atom of M<sub>1</sub>* |
| VBur_R350_Rad | %<I>V</I><sub>Bur</sub> within 3.50 Å of the reactive carbon atom of M<sub>1</sub>* |
| VBur_R228_Mon | %<I>V</I><sub>Bur</sub> within 2.28 Å of the reactive carbon atom of M<sub>2</sub> |
| VBur_R350_Mon | %<I>V</I><sub>Bur</sub> within 3.50 Å of the reactive carbon atom of M<sub>2</sub> |
| Volume_Rad | Volume of M<sub>1</sub>* |
| Volume_Mon | Volume of M<sub>2</sub> |
| CCdist_TS | Reactive C-C bond distance at the TS structure |
| Sum_MW | Sum of molecular weight of M<sub>1</sub>* and M<sub>2</sub> |
| logP_Rad | Partition coefficient log<I>P</I> of M<sub>1</sub>* |
| logP_Mon | Partition coefficient log<I>P</I> of M<sub>2</sub> |

List of monomers.
| Monomer | CAS RN | Name | Abbreviation |
| --- | --- | --- | --- |
| ![MMA](./copddb/images/monomer_0.svg) | 80-62-6 | Methyl methacrylate | MMA |
| ![GMA](./copddb/images/monomer_1.svg) | 106-91-2 | Glycidyl methacrylate | GMA |
| ![St](./copddb/images/monomer_2.svg) | 100-42-5 | Styrene | St |
| ![St](./copddb/images/monomer_3.svg) | 5739-81-1 | Methyl (*Z*)-3-methoxyacrylate |
| ![monomer 4](./copddb/images/monomer_4.svg)  | 79-41-4 | Methacrylic acid |
| ![monomer 5](./copddb/images/monomer_5.svg) | 97-63-2 | Ethyl methacrylate |
| ![monomer 6](./copddb/images/monomer_6.svg) | 97-88-1 | Butyl methacrylate |
| ![monomer 7](./copddb/images/monomer_7.svg) | 97-86-9 | Isobutyl methacrylate |
| ![monomer 8](./copddb/images/monomer_8.svg) | 585-07-9 | *tert*-Butyl methacrylate
| ![monomer 9](./copddb/images/monomer_9.svg) | 37674-57-0 | (3-Ethyloxetan-3-yl)methyl methacrylate | 
| ![monomer 10](./copddb/images/monomer_10.svg) | 688-84-6 | 2-Ethylhexyl methacrylate |
| ![monomer 11](./copddb/images/monomer_11.svg) | 142-90-5 | Dodecyl methacrylate |
| ![monomer 12](./copddb/images/monomer_12.svg) | 32360-05-7 | Stearyl methacrylate |
| ![monomer 13](./copddb/images/monomer_13.svg) | 101-43-9 | Cyclohexyl methacrylate |
| ![monomer 14](./copddb/images/monomer_14.svg) | 2495-37-6 | Benzyl methacrylate |
| ![monomer 15](./copddb/images/monomer_15.svg) | 868-77-9 | 2-Hydroxyethyl methacrylate |
| ![monomer 16](./copddb/images/monomer_16.svg) | 923-26-2 | 2-Hydroxypropyl methacrylate |
| ![monomer 17](./copddb/images/monomer_17.svg) | 115372-36-6 | 3-Hydroxy-1-methacryloyloxyadamantane |
| ![monomer 18](./copddb/images/monomer_18.svg) | 115522-15-1 | 3,5-Dihydroxy-1-adamantyl methacrylate |
| ![monomer 19](./copddb/images/monomer_19.svg) | 2867-47-2 | 2-(Dimethylamino)ethyl methacrylate |
| ![monomer 20](./copddb/images/monomer_20.svg) | 105-16-8 | (2-Diethylamino)ethyl methacrylate |
| ![monomer 21](./copddb/images/monomer_21.svg) | 34759-34-7 | Dicyclopentanyl methacrylate |
| ![monomer 22](./copddb/images/monomer_22.svg) | 68586-19-6 | Dicyclopentenyloxyethyl methacrylate |
| ![monomer 23](./copddb/images/monomer_23.svg) | 2455-24-5 | Tetrahydrofurfuryl methacrylate |
| ![monomer 24](./copddb/images/monomer_24.svg) | 41988-14-1 | (3-Ethyloxetan-3-yl)methyl acrylate |
| ![monomer 25](./copddb/images/monomer_25.svg) | 2628-16-2 | 4-Acetoxystyrene |
| ![monomer 26](./copddb/images/monomer_26.svg) | 79-06-1 | Acrylamide |
| ![monomer 27](./copddb/images/monomer_27.svg) | 15214-89-8 | (1,1-Dimethyl-2-sulfoethyl)acrylamide |
| ![monomer 28](./copddb/images/monomer_28.svg) | 79-10-7 | Acrylic acid |
| ![monomer 29](./copddb/images/monomer_29.svg) | 96-33-3 | Methyl acrylate |
| ![monomer 30](./copddb/images/monomer_30.svg) | 93841-48-6 | Isooctadecyl acrylate |
| ![monomer 31](./copddb/images/monomer_31.svg) | 51952-49-9 | Isononyl acrylate |
| ![monomer 32](./copddb/images/monomer_32.svg) | 5888-33-5 | Isobornyl acrylate |
| ![monomer 33](./copddb/images/monomer_33.svg) | 106-63-8 | Isobutyl acrylate |
| ![monomer 34](./copddb/images/monomer_34.svg) | 2499-59-4 | *n*-Octyl acrylate |
| ![monomer 35](./copddb/images/monomer_35.svg) | 216581-76-9 | 3-Hydroxy-1-adamantyl acrylate |
| ![monomer 36](./copddb/images/monomer_36.svg) | 2478-10-6 | 4-Hydroxybutyl acrylate |
| ![monomer 37](./copddb/images/monomer_37.svg) | 86273-46-3 | Vinyl ethoxyethyl acrylate |
| ![monomer 38](./copddb/images/monomer_38.svg) | 1663-39-4 | *tert*-Butyl acrylate |
| ![monomer 39](./copddb/images/monomer_39.svg) | 65983-31-5 | Dicyclopentenyloxyethyl acrylate |
| ![monomer 40](./copddb/images/monomer_40.svg) | 3121-61-7 | 2-Methoxyethyl acrylate |
| ![monomer 41](./copddb/images/monomer_41.svg) | 2156-97-0 | Dodecyl acrylate |
| ![monomer 42](./copddb/images/monomer_42.svg) | 32002-24-7 | Ethyl 3,3-diethoxyacrylate |
| ![monomer 43](./copddb/images/monomer_43.svg) | 23117-36-4 | 1,4-Cyclohexanedimethanol monoacrylate |
| ![monomer 44](./copddb/images/monomer_44.svg) | 4813-57-4 | Stearyl acrylate |
| ![monomer 45](./copddb/images/monomer_45.svg) | 2399-48-6 | Tetrahydrofurfuryl acrylate |
| ![monomer 46](./copddb/images/monomer_46.svg) | 818-61-1 | 2-Hydroxyethyl acrylate |
| ![monomer 47](./copddb/images/monomer_47.svg) | 999-61-1 | 2-Hydroxypropyl acrylate |
| ![monomer 48](./copddb/images/monomer_48.svg) | 119692-59-0 | 4-(2,3-epoxypropoxy)butylacrylate |
| ![monomer 49](./copddb/images/monomer_49.svg) | 48145-04-6 | 2-Hydroxypropyl acrylate |

## Installation
### Dependencies
CopDDB includes Python modules for reading and processing csv files. In a Python environment, By utilizing these modules in a Python environment, you can easily manipulate and analyze the CopDDB. CopDDB uses the following external libraries.
- NumPy
- pandas
- RDKit

### User installation
```sh
git clone https://github.com/hatanaka-lab/CopDDB
```

### Before Retrieving Descriptors
To obtain the list of SMILES registered in CopDDB, use the `copddb.datasets.get_available_smiles()` function.
```python
>>> copddb.datasets.get_available_smiles()
['C=CC(=O)OC(C)(C)C', 'C=CC(=O)OCCCCCCCCCCCCCCCCCC', 'C=C(C)C(=O)OC12CC3CC(O)(CC(O)(C3)C1)C2', 'C=CC(=O)NC(C)(C)CS(=O)(=O)O', 'C=CC(=O)OC1C[C@@H]2CC[C@@]1(C)C2(C)C', 'C=C(C)C(=O)OC', 'C=CC(=O)OCC(C)O', 'C=C(C)C(=O)OC(C)(C)C', 'C=C(C)C(=O)OCC(C)C', 'C=C(C)C(=O)OCc1ccccc1', 'C=C(C)C(=O)O', 'C=C(C)C(=O)OCCCCCCCCCCCCCCCCCC', 'C=COCCOCCOC(=O)C=C', 'C=C(C)C(=O)OCCN(CC)CC', 'C=C(C)C(=O)OCC(CC)CCCC', 'C=C(C)C(=O)OCC(C)O', 'C=C(C)C(=O)OCCCC', 'C=CC(=O)OCCOC', 'C=CC(=O)OCC1(CC)COC1', 'C=CC(=O)OCCCCOCC1CO1', 'C=CC(=O)OCCOc1ccccc1', 'C=CC(=O)OCCCCCCC(C)C', 'C=Cc1ccc(OC(C)=O)cc1', 'C=CC(N)=O', 'C=C(C)C(=O)OC1CCCCC1', 'C=C(C)C(=O)OCCO', 'C=C(C)C(=O)O[C@@]12C[C@H]3C[C@@H](C1)C[C@](O)(C3)C2', 'C=CC(=O)OCCCCCCCCCCCC', 'C=C(C)C(=O)OCCCCCCCCCCCC', 'C=Cc1ccccc1', 'C=CC(=O)OCC1CCCO1', 'C=C(C)C(=O)OCC1(CC)COC1', 'C=C(C)C(=O)OC1CC2CC1C1CCCC21', 'C=C(C)C(=O)OCCOC1CC2CC1C1C=CCC21', 'C=CC(=O)OCC(C)C', 'C=C(C)C(=O)OCCN(C)C', 'C=C(C)C(=O)OCC', 'C=CC(=O)OCC1CCC(CO)CC1', 'C=C(C)C(=O)OCC1CO1', 'C=CC(=O)OCCOC1CC2CC1C1CC=CC21', 'C=CC(=O)O', 'C=CC(=O)OC', 'C=CC(=O)OCCO', 'CCOC(=O)C=C(OCC)OCC', 'C=CC(=O)OCCCCCCCCCCCCCCCC(C)C', 'C=CC(=O)OCCCCCCCC', 'C=C(C)C(=O)OCC1CCCO1', 'CO/C=C\\C(=O)OC', 'C=CC(=O)OCCCCO', 'C=CC(=O)O[C@@]12C[C@H]3C[C@@H](C1)C[C@](O)(C3)C2']
```

To obtain the names of descriptors registered in CopDDB, use the `copddb.datasets.get_available_descriptors()` function.
```python
>>> copddb.datasets.get_available_descriptors()
['Radical', 'Monomer', 'DE_decomposition_tail', 'DE_decomposition_head', 'DE_precursor', 'DE_TS', 'DE_product', 'DE_barrier', 'DE_reaction', 'E_Rad_SOMO', 'E_Rad_LUMO', 'E_Mon_HOMO', 'E_Mon_LUMO', 'DE_SHgap', 'DE_SLgap', 'VBur_R228_Mon', 'VBur_R350_Mon', 'VBur_R228_Rad', 'VBur_R350_Rad', 'Volume_MonteCarlo_Mon', 'Volume_MonteCarlo_Rad', 'CCdist_TS']
```

### Example 1: Obraining descriptors using SMILES strings.
The most basic usage is to retrieve descriptors collected for propagation reactions using the `copddb.datasets.descriptors_from_smiles()` function. The following example retrieves descriptors in the form of a `pandas.DataFrame` using the SMILES for a radical `smi_rad` and a monomer `smi_mon`.

```python
from copddb

smi_rad = "C=CC(=O)OCCCCCCCCCCCC"
smi_mon = "C=CC(=O)O"

descriptor = copddb.datasets.descriptors_from_smiles(smi_rad, smi_mon)
```
The output of the descriptor is as follows.
```
>>> descriptor
      DE_decomposition_tail  DE_decomposition_head  ...  Volume_MonteCarlo_Rad  CCdist_TS
2078               0.042541               0.058434  ...                227.414   2.268076

[1 rows x 20 columns]
```

If you input SMILES that are not listed in the CopDDB, an empty DataFrame will be returned. Let's try using the ethene molecule `"C=C"`
```python
descriptor = copddb.datasets.descriptors_from_smiles("C=C", smi_mon)
```
The output of descriptor is as follows.
```python
>>> descriptor
Empty DataFrame
Columns: [DE_decomposition_tail, DE_decomposition_head, DE_precursor, DE_TS, DE_product, DE_barrier, DE_reaction, E_Rad_SOMO, E_Rad_LUMO, E_Mon_HOMO, E_Mon_LUMO, DE_SHgap, DE_SLgap, VBur_R228_Mon, VBur_R350_Mon, VBur_R228_Rad, VBur_R350_Rad, Volume_MonteCarlo_Mon, Volume_MonteCarlo_Rad, CCdist_TS]
Index: []
```

If you want to explicitly include missing values, use the `with_nan` option (which is `False` by default) as follows.
```python
descriptor = copddb.datasets.descriptors_from_smiles("C=C", smi_mon, with_nan=True)
```
The output of descriptor is as follows.
```python
descriptor
      DE_decomposition_tail  DE_decomposition_head  ...  Volume_MonteCarlo_Rad  CCdist_TS
2500                    NaN                    NaN  ...                    NaN        NaN

[1 rows x 20 columns]
```

To include the input SMILES in the returned value, use the `with_smiles` option (which is `False` by default).
```python
descriptor = copddb.datasets.descriptors_from_smiles("C=C", smi_mon, with_nan=True, with_smiles=True)
```
The output of descriptor is as follows.
```python
>>> descriptor
     Radical    Monomer  ...  Volume_MonteCarlo_Rad  CCdist_TS
2500     C=C  C=CC(=O)O  ...                    NaN        NaN

[1 rows x 22 columns]
```

SMILES can also be input as a `list` type. By using a `list`, you can obtain multiple descriptors at the same time. For example, you can use it as follows.
```python
smi_list = [
    ["C=C(C)C(=O)OC", "C=C(C)C(=O)OC"],
    ["C=C(C)C(=O)OC", "C=CC(=O)O"],
    ["CO/C=C\C(=O)OC", "C=Cc1ccccc1"]
]

descriptors = copddb.datasets.descriptors_from_smiles(smi_list)
```
The output of descriptors is as follows.
```python
descriptors
     DE_decomposition_tail  DE_decomposition_head  ...  Volume_MonteCarlo_Rad  CCdist_TS
0                 0.038534               0.061518  ...               103.2494   2.254882
28                0.038534               0.061518  ...               103.2494   2.248237
152               0.045085               0.045173  ...               103.2451   2.409667

[3 rows x 20 columns]
```

### Example 2: Creating a Dataset from a List of SMILES and a List of Target Variables (Preprocessing)
In the second example, we use the `copddb.datasets.build_dataset_from_smiles_and_y()` function to create a dataset from SMILES strings and target variables, including both descriptors and target variables. The function is useful for removing missing values in descriptors. The resulting dataset is returned as a Bunch object.

```python 
smi_list = [
    ["C=C(C)C(=O)OC", "C=C(C)C(=O)OC"],
    ["C=C(C)C(=O)OC", "C=CC(=O)O"],
    ["CO/C=C\C(=O)OC", "C=Cc1ccccc1"],
    ["C=C", "C=C"] # SMILES that result in missing values
]

target = [1, 2, 3, 4] # Target variables

new_dataset = copddb.datasets.build_dataset_from_smiles_and_y(smi_list, target)
```
The `Bunch` object created contains descriptors `data` and target variables `target`. If you examine the contents of each, you will find the following.

The `Bunch` object created includes both descriptors, under `data`, and the target variable, labeled `target`. Examining the contents of each reveals the following.
```python
>>> new_dataset.keys()
dict_keys(['data', 'target'])

>>> new_dataset["data"]
     DE_decomposition_tail  DE_decomposition_head  ...  Volume_MonteCarlo_Rad  CCdist_TS
0                 0.038534               0.061518  ...               103.2494   2.254882
28                0.038534               0.061518  ...               103.2494   2.248237
152               0.045085               0.045173  ...               103.2451   2.409667

[3 rows x 20 columns]

>>> new_dataset["target"]
array([1, 2, 3])
```

Just like in Example 1, you have the option to explicitly handle missing values by using the `with_nan` parameter, which is set to `False` by default.
```python
>>> new_dataset = copddb.datasets.build_dataset_from_smiles_and_y(smi_list, target, with_nan=True)

>>> new_dataset["data"]
      DE_decomposition_tail  DE_decomposition_head  ...  Volume_MonteCarlo_Rad  CCdist_TS
0                  0.038534               0.061518  ...               103.2494   2.254882
28                 0.038534               0.061518  ...               103.2494   2.248237
152                0.045085               0.045173  ...               103.2451   2.409667
2501                    NaN                    NaN  ...                    NaN        NaN

[4 rows x 20 columns]

>>> new_dataset["target"]
array([1, 2, 3, 4])
```

### Example 3: Creating a Descriptor for Monomer Pairs (Preprocessing)
In this example, we will demonstrate how to create descriptors for a copolymer composed of two different monomers, $M_1$ and $M_2$, using the `copddb.datasets.build_pair_valiables_from_smiles_and_y()` function. This function generates a new set of descriptors by combining those related to Equations 1 and 2.

First, let's explore the rationale behind creating a new set of descriptors. The propagation reaction of the copolymer, formed from monomers $M_1$ and $M_2$, encompasses the four fundamental reactions outlined below.

$$
M_1^* + M_1 \xrightarrow{k_{11}} M_1^* ~~~~(1)
$$

$$
M_1^* + M_2 \xrightarrow{k_{12}} M_2^* ~~~~(2)
$$

$$
M_2^* + M_1 \xrightarrow{k_{21}} M_1^* ~~~~(3)
$$

$$
M_2^* + M_2 \xrightarrow{k_{22}} M_2^* ~~~~(4)
$$

Here, $M_1^*$ and $M_2^*$ represent the radicals of $M_1$ and $M_2$ respectively, and $k_{ij}$ denotes the reaction rate constants between $M_i^*$ and $M_j$. A single record in CopDDB contains information about one of the reactions from Equations 1 to 4. This implies that using a combination of the above equations to describe the reaction of a mixture of $M_1$ and $M_2$ is expected to provide a better explanation of the actual reaction.

In the `copddb.datasets.build_pair_variables_from_smiles_and_y()` function, new descriptors are created by appending the numbers of the molecules involved in the reaction to the end of descriptors within CopDDB.
For example, for Equations 1 and 2, the descriptor DE_TS becomes DE_TS_11 and DE_TS_12, respectively.
Descriptors derived from a single molecule, such as the radical $M_i*$ or monomer $M_i$, are appended with only one number for the molecule.
For instance, descriptors of molecular orbital energy like E_Rad_SOMO become E_Rad_SOMO_1.

Let's try using the same list of SMILES and target variables as in Example 2.
```python
smi_list = [
    ["C=C(C)C(=O)OC", "C=C(C)C(=O)OC"],
    ["C=C(C)C(=O)OC", "C=CC(=O)O"],
    ["CO/C=C\C(=O)OC", "C=Cc1ccccc1"],
    ["C=C", "C=C"] # SMILES that result in missing values
]

target = [1, 2, 3, 4] # Target variables

new_dataset = copddb.datasets.build_pair_variables_from_smiles_and_y(smi_list, target)
```
The contents of the new_dataset is as follows.
```python
>>> new_dataset["data"]
   DE_TS_11  DE_TS_12  ...  Volume_MonteCarlo_Rad_1  Volume_MonteCarlo_Rad_2
0 -0.005547 -0.005547  ...                 103.2494                 103.2494
1 -0.005547  0.008555  ...                 103.2494                  68.5728
2 -0.001421 -0.003731  ...                 103.2451                 108.9815

[3 rows x 40 columns]

>>> new_dataset["data"].keys()
Index(['DE_TS_11', 'DE_TS_12', 'DE_product_11', 'DE_product_12',
       'DE_barrier_11', 'DE_barrier_12', 'DE_reaction_11', 'DE_reaction_12',
       'DE_SHgap_11', 'DE_SHgap_12', 'DE_SLgap_11', 'DE_SLgap_12',
       'CCdist_TS_11', 'CCdist_TS_12', 'DE_decomposition_tail_1',
       'DE_decomposition_tail_2', 'DE_decomposition_head_1',
       'DE_decomposition_head_2', 'DE_precursor_1', 'DE_precursor_2',
       'E_Rad_SOMO_1', 'E_Rad_SOMO_2', 'E_Rad_LUMO_1', 'E_Rad_LUMO_2',
       'E_Mon_HOMO_1', 'E_Mon_HOMO_2', 'E_Mon_LUMO_1', 'E_Mon_LUMO_2',
       'VBur_R228_Mon_1', 'VBur_R228_Mon_2', 'VBur_R350_Mon_1',
       'VBur_R350_Mon_2', 'VBur_R228_Rad_1', 'VBur_R228_Rad_2',
       'VBur_R350_Rad_1', 'VBur_R350_Rad_2', 'Volume_MonteCarlo_Mon_1',
       'Volume_MonteCarlo_Mon_2', 'Volume_MonteCarlo_Rad_1',
       'Volume_MonteCarlo_Rad_2'],
      dtype='object')
```

Based on this idea, [ref1] rearranged the descriptors in CopDDB to create a set of descriptors and used them to build a predictive model for the copolymerization monomer reactivity ratio $r_1$.

[ref1]: https://www.rsc.org/journals-books-databases/about-journals/digital-discovery/
