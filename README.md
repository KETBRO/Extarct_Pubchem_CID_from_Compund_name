# Extarct_Pubchem_CID_from_Compund_name
import pubchempy as pcp
import pandas as pd

# Load the list of compound names from a CSV file
data = pd.read_csv("ADR_only_drug_2004.csv", header=None)
list_of_compounds = list(data[0])

# Initialize a list to store results
results = []

# Iterate over each compound name
for compound_name in list_of_compounds:
    compounds = pcp.get_compounds(compound_name, 'name')
    if compounds:
        # If a CID is found, add it to the results
        results.append({
            "Compound Name": compound_name,
            "CID": compounds[0].cid
        })
    else:
        # If no CID is found, add a None entry
        results.append({
            "Compound Name": compound_name,
            "CID": None
        })
        print(f"CID not found for: {compound_name}")

# Convert results to a DataFrame and save to an Excel file
results_df = pd.DataFrame(results)
results_df.to_excel("name_CID.xlsx", index=False)

print("Processing complete. Output saved to 'name_CID.xlsx'.")
