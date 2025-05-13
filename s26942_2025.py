# Purpose of the program:
# This script generates a random DNA sequence in FASTA format.
# It collects user input for sequence length, sequence ID, description, and name.
# It randomly inserts the user’s name into the sequence without affecting statistics.
# It calculates base percentages and CG/AT ratio.
# The sequence is saved to a FASTA file named with the sequence ID.

# Context:
# This task is part of a bioinformatics exercise to understand sequence generation,
# file formatting in FASTA, and basic statistics in DNA sequence analysis.

import random

# Function to generate a random DNA sequence
def generate_dna_sequence(length):
    nucleotides = ['A', 'C', 'G', 'T']
    return ''.join(random.choices(nucleotides, k=length))

# Function to insert a name at a random position without affecting sequence stats
def insert_name_into_sequence(sequence, name):
    insert_pos = random.randint(0, len(sequence))
    return sequence[:insert_pos] + name + sequence[insert_pos:]

# Function to calculate statistics of the DNA sequence (excluding name)
def calculate_stats(sequence, name):
    clean_seq = sequence.replace(name, '')
    total = len(clean_seq)
    stats = {
        'A': (clean_seq.count('A') / total) * 100,
        'C': (clean_seq.count('C') / total) * 100,
        'G': (clean_seq.count('G') / total) * 100,
        'T': (clean_seq.count('T') / total) * 100,
    }
    cg_ratio = ((clean_seq.count('C') + clean_seq.count('G')) / total) * 100
    return stats, cg_ratio

# -------------------------------
# MAIN INTERACTION WITH THE USER
# -------------------------------

# Get inputs from the user
length = int(input("Enter the sequence length: "))
seq_id = input("Enter the sequence ID: ")
description = input("Provide a description of the sequence: ")
name = input("Enter your name: ")

# Generate and modify sequence
original_seq = generate_dna_sequence(length)
final_seq = insert_name_into_sequence(original_seq, name)

# Save to FASTA file
file_name = f"{seq_id}.fasta"
with open(file_name, 'w') as fasta_file:
    fasta_file.write(f">{seq_id} {description}\n")
    fasta_file.write(final_seq + "\n")

# Calculate statistics
stats, cg_ratio = calculate_stats(final_seq, name)

# Print results
print(f"\nThe sequence was saved to the file {file_name}")
print("Sequence statistics:")
for base in ['A', 'C', 'G', 'T']:
    print(f"{base}: {stats[base]:.1f}%")
print(f"%CG: {cg_ratio:.1f}%")

# ----------------------------------------------------------
# IMPROVEMENTS MADE OVER ORIGINAL LLM VERSION:
# ----------------------------------------------------------

# ORIGINAL:
# sequence = ''.join(random.choices('ACGT', k=length))
# MODIFIED (to improve readability and allow flexibility):
# Used a separate list ['A', 'C', 'G', 'T'] → nucleotides = ['A', 'C', 'G', 'T']

# ORIGINAL:
# fasta_file.write(f">{seq_id} {description}\n{sequence}")
# MODIFIED (for better formatting and clarity):
# fasta_file.write(...) split into header + sequence on separate lines

# ORIGINAL:
# stats = {base: sequence.count(base) / len(sequence) for base in 'ACGT'}
# MODIFIED (to exclude name and show % properly):
# clean_seq = sequence.replace(name, '')
# and percentage calculations made more explicit

# EXTRA IMPROVEMENT:
# Defined reusable functions (generate_dna_sequence, insert_name_into_sequence, calculate_stats)
# to follow good coding practices and improve readability/testability.

# The code is ready to run in any IDE (VS Code, Thonny, etc.)
