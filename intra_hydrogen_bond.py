import pymol
import csv
from pymol import cmd

# Initialize PyMOL
pymol.finish_launching()

# Load the structures
print("Loading structures...")
cmd.load('/dir/6lni.pdb', '6lni')
cmd.load('/dir/1qlz.pdb', '1qlz')

# Define hydrogen bond cutoff distance
hbond_cutoff_distance = 3.5  # Ångströms

# Create a list to store hydrogen bond details
hbond_details = []

# Select hydrogen bond donors from chain A of 6lni and all acceptors from 1qlz
cmd.select("6lni_chainA_donors", "chain A and 6lni and donor")
cmd.select("1qlz_acceptors", "1qlz and acceptor")

# Check if selections are valid
if cmd.count_atoms("6lni_chainA_donors") == 0 or cmd.count_atoms("1qlz_acceptors") == 0:
    print("Error: One of the selections is empty.")
else:
    # Iterate over each donor and acceptor pair and calculate distances
    donor_list = cmd.index("6lni_chainA_donors")
    acceptor_list = cmd.index("1qlz_acceptors")

    for donor in donor_list:
        for acceptor in acceptor_list:
            distance = cmd.get_distance(donor, acceptor)
            if distance <= hbond_cutoff_distance:
                donor_resi = donor[1]  # Extract donor residue number
                acceptor_resi = acceptor[1]  # Extract acceptor residue number
                hbond_details.append([str(donor_resi), str(acceptor_resi), str(distance)])

# Define the path to save the CSV file
csv_file_path = '/dir/hbonds.csv'

# Save the hydrogen bond details to a CSV file
with open(csv_file_path, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    # Write the header row
    writer.writerow(["Donor Residue", "Acceptor Residue", "Distance (Å)"])
    # Write the hydrogen bond details
    writer.writerows(hbond_details)

# Print a message indicating successful completion
print("Hydrogen bond details saved to:", csv_file_path)
