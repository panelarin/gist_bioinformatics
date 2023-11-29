# gist_bioinformatics
open source of codes used in my structural bioinformatics project


## Hydrogen Bond Calculator with PyMOL

This Python script is a Hydrogen Bond Calculator that utilizes the PyMOL library to analyze and compute hydrogen bond details between two PDB (Protein Data Bank) structures. Hydrogen bonds play a crucial role in the interaction and stability of biomolecules, and understanding their presence and strength is essential in the field of structural biology.

### How It Works

Initialization and Structure Loading: The script initializes PyMOL and loads two PDB structures, '6lni' and '1qlz,' provided by the user. These structures are essential for calculating hydrogen bonds.

Hydrogen Bond Cutoff Distance: You can specify the hydrogen bond cutoff distance (in Ångströms) as a parameter. This value determines how close atoms need to be to be considered part of a hydrogen bond.

Selection of Donors and Acceptors: The script selects hydrogen bond donors from 'chain A' of the '6lni' structure and all acceptors from the '1qlz' structure. These selections are critical for identifying potential hydrogen bond interactions.

Calculating Hydrogen Bond Distances: The script iterates over each donor and acceptor pair, calculates the distance between them, and checks if it falls within the specified cutoff distance. If a valid hydrogen bond is detected, the donor residue number, acceptor residue number, and the distance are recorded.

Saving Results: The calculated hydrogen bond details are saved to a CSV file named hbonds.csv, making it easy to analyze and visualize the results.
