#! /usr/bin/python
# coding: utf-8

from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Descriptors
from rdkit.Chem import Lipinski
from rdkit.Chem import rdFreeSASA
from rdkit.Chem.Scaffolds import MurckoScaffold
from rdkit.Chem import Draw

from rdkit import DataStructs
from rdkit.Chem import rdMolDescriptors
from rdkit.Chem.Draw import rdMolDraw2D
from rdkit import rdBase
from rdkit.Chem.Draw import SimilarityMaps



smiles='S1CSSC1'
m = Chem.MolFromSmiles(smiles)
#qed
qed_m = Descriptors.qed(m)
#logp
logp_m = Descriptors.MolLogP(m)
#molwt
molwt_m = Descriptors.MolWt(m)
#hba--氢键受体数
hba_m = Lipinski.NumHAcceptors(m)
#hbd--氢键供体数
hbd_m = Lipinski.NumHDonors(m)
#SASA--计算
homl = Chem.AddHs(m)
AllChem.EmbedMolecule(homl)
radii_m = rdFreeSASA.classifyAtoms(homl)
sas_m = rdFreeSASA.CalcSASA(homl, radii_m)
#tpsa
tpsa_m = Descriptors.TPSA(m)
#NumRotBonds
numrotbonds_m = Lipinski.NumRotatableBonds(m)
#scaffold_smiles
scaffold_smiles_m = Chem.MolToSmiles(m)
#####
a = MurckoScaffold.GetScaffoldForMol(m)
GetScaffoldForMol_m = Chem.MolToSmiles(a)
#m_core = [m, a]
#GridImage =Draw.MolsToGridImage(m_core, subImgSize=(250, 250))

#a = Chem.SmilesMolSupplierFromText('S1CSSC1')
#AllChem.ComputeGasteigerCharges(m)
#charge_atm0 = float(m.GetAtomWithIdx(0).GetProp('_GasteigerCharge'))

print('the qed of m is', qed_m)
print('the logP of m is', logp_m)  # the logP of m is 1.3848
print('the molwt of m is', molwt_m)
print('the hba of m is', hba_m)
print('the hbd of m is', hbd_m)
print('the sas of m is', sas_m)
print('the TPSA of m is', tpsa_m)  # the TPSA of m is 37.3
print('the numrotbonds of m is', numrotbonds_m)
print('the scaffold_smiles of m is', scaffold_smiles_m)
print('the GetScaffoldForMol of m is', GetScaffoldForMol_m)
#GridImage.show()

# the gasteigerCharge of the first atom - 0.04769375004654255
#print('the gasteigerCharge of the first atom', charge_atm0)