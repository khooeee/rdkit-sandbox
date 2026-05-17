from rdkit import Chem
from rdkit.Chem import Descriptors, Draw

mol = Chem.MolFromSmiles("CC(=O)Oc1ccccc1C(=O)O")  # aspirin

print("Canonical SMILES:", Chem.MolToSmiles(mol))
print("Molecular weight:", Descriptors.MolWt(mol))
print("LogP:", Descriptors.MolLogP(mol))
print("TPSA:", Descriptors.TPSA(mol))

img = Draw.MolToImage(mol)
img.save("aspirin.png")
