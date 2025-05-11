import pubchempy as pcp
import pandas as pd

data = pd.read_csv("compound_2001_3000.csv", header=None)
list_of_compounds = list(data[0])

results = []

for compound_name in list_of_compounds:
    compounds = pcp.get_compounds(compound_name, 'name')
    if compounds:
        for compound in compounds:
            result_dict = {
                "Compound Name": compound_name,
                "CID": compound.cid,
                "Canonical SMILES": compound.canonical_smiles,
                "Isomeric SMILES": compound.isomeric_smiles
            }
            results.append(result_dict)
    else:
        result_dict = {
            "Compound Name": compound_name,
            "CID": None,
            "Canonical SMILES": None,
            "Isomeric SMILES": None
        }
        results.append(result_dict)
        print(compound_name)
results_df = pd.DataFrame(results)
results_df.to_excel("compound_info_2001_3000.xlsx", index=False)
