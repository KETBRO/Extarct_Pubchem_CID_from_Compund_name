import pubchempy as pcp
import pandas as pd

# Read the list of CIDs from a CSV file
csv_file = "compound.csv"  
data = pd.read_csv(csv_file, header=None)
list_of_compounds = list(data[0])

for cid in list_of_compounds:
    try:
        pcp.download('SDF', f'{cid}.sdf', cid, 'CID', record_type='3d')
        print(f"Downloaded 3D structure for CID {cid}")
    except Exception as e:
        with open('not_downloaded.txt', 'a') as f:
            print(f"Error downloading 3D structure for CID {cid}: {str(e)}", file=f)
