import pubchempy as pcp
import pandas as pd
import csv
# Load the list of compound names from a CSV file
data = pd.read_csv("compound_3001_4000.csv", header=None)
list_of_compounds = list(data[0])

# Create an empty list to store the results
results = []
for compound_name in list_of_compounds:
    try:
        compounds = pcp.get_compounds(compound_name, 'name')
        
        # Check if any compounds were found for the given name
        if compounds:
            for compound in compounds:
                properties = compound.to_dict(properties=['molecular_weight', 'xlogp', 'exact_mass', 'h_bond_donor_count', 'h_bond_acceptor_count'])
                result_dict = {
                    "Compound Name": compound_name,
                    "CID": compound.cid,
                    "Canonical SMILES": compound.canonical_smiles,
                    "Isomeric SMILES": compound.isomeric_smiles,
                    "Molecular Weight": properties['molecular_weight'],
                    "XLogP": properties['xlogp'],
                    "Exact Mass": properties['exact_mass'],
                    "H-Bond Donor Count": properties['h_bond_donor_count'],
                    "H-Bond Acceptor Count": properties['h_bond_acceptor_count']
                }
                results.append(result_dict)
        else:
            # If no compounds were found, store a placeholder result
            result_dict = {
                "Compound Name": compound_name,
                "CID": None,
                "Canonical SMILES": None,
                "Isomeric SMILES": None,
                "Molecular Weight": None,
                "XLogP": None,
                "Exact Mass": None,
                "H-Bond Donor Count": None,
                "H-Bond Acceptor Count": None
            }
            results.append(result_dict)
        
        # Save the accumulated data to an Excel file after each successful request
        results_df = pd.DataFrame(results)
        results_df.to_excel("compound_3001_4000.xlsx", index=False)
        
    except pcp.PubChemPyError as e:
        print(f"An error occurred for {compound_name}: {e}")
