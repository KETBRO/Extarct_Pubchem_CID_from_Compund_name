import pandas as pd
import pubchempy as pcp


def get_properties(cid):
    try:
        compound = pcp.Compound.from_cid(cid)
        props = {
            'H-bond acceptor': compound.h_bond_acceptor_count,
            'H-bond donor': compound.h_bond_donor_count,
            'MW': compound.molecular_weight,
            'logP': compound.xlogp,
            'TPSA': compound.tpsa,
            'Total charge': compound.charge,
            'Rotatable bonds': compound.rotatable_bond_count,
            'Isomeric smiles': compound.isomeric_smiles,
            'IUPAC name': compound.iupac_name,
            'Canonical smiles': compound.canonical_smiles,
            'Molecular formula': compound.molecular_formula,
            'InChI': compound.inchi,
            'InChIKey': compound.inchikey,
            'Exact mass': compound.exact_mass,
            'Monoisotopic mass': compound.monoisotopic_mass,
            'Heavy atom count': compound.heavy_atom_count,
            'Complexity': compound.complexity,
            'Covalently bonded unit count': compound.covalent_unit_count,
            'Hydrogen bond donor count': compound.h_bond_donor_count,
            'Hydrogen bond acceptor count': compound.h_bond_acceptor_count,
            'Number of rotatable bonds': compound.rotatable_bond_count,
        }
        return props
    except pcp.PubChemHTTPError:
        return None


excel_file = 'pubchem_cids.xlsx'
df = pd.read_excel(excel_file)

properties_list = []
for cid in df['CID']:
    props = get_properties(cid)
    if props:
        properties_list.append(props)
    else:
        properties_list.append({prop: None for prop in props.keys()})

properties_df = pd.DataFrame(properties_list)


result_df = pd.concat([df, properties_df], axis=1)


output_file = 'output.xlsx'  
result_df.to_excel(output_file, index=False)
