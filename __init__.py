
# pre-requisite:
# pip install -r requirements.txt
# python __init__.py

# Workflow:
# reads data from MonkeyPox_in.fasta
# modifies as asked -> extraxted subset sequence is reverse, modified and then replaced with the original
# write data to MonkeyPox_out.fasta



import random
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from config import Configs
from file_operations import read_fasta_file, write_fasta_file
from string_operations import get_subset, reverse
    

sequences = read_fasta_file()
print(f"{len(sequences)} seq_record is gathered from the input file.\n")

random_indices = random.sample(range(0, len(sequences)), 3)
print(f"random seq_record indices to be processed are {random_indices}\n\n")

modified_sequences = []
with open(Configs.BED_FILE, "w") as wfile:
    wfile.writelines("ID" + "\t" + str(Configs.CHROMO_START_INDEX) + "\t" + str(Configs.CHROMO_LENGTH_COUNT) + "\t" + "SEQUENCE" + "\t" + "REVERSED" + "\t" "MODIFIED" + "\n")

    for index in range(len(sequences)):
        seq_record = sequences[index]

        if index in random_indices:

            sequence_subset = get_subset(seq_record.seq)
            print("--> subset_string extracted is ", sequence_subset)

            sequence_reversed = reverse(sequence_subset)
            print("--> reversed_string of subset is ", sequence_reversed)


            random_gene_index = random.randrange(0, len(sequence_reversed))
            random_gene = sequence_reversed[random_gene_index]

            genes = Configs.GENES
            if random_gene in genes:
                genes.remove(random_gene)
            
            modified_gene = random.choice(genes)
            print(f"--> random gene modifiication done at index {random_gene_index} which changed {random_gene} to {modified_gene}")
            modified_sequence_subset = str(sequence_reversed[:random_gene_index-1] + modified_gene + sequence_reversed[random_gene_index+1:])
            modified_sequence = modified_sequence_subset + seq_record.seq[len(sequence_subset)+1:]

            seq_record = SeqRecord(seq=Seq(modified_sequence), id=seq_record.id)
            print("New seq_record created with modified sequence --->")
            print(seq_record, "\n\n")
        
            wfile.writelines(str(seq_record.id) + "\t" + str(Configs.CHROMO_START_INDEX) + "\t" + str(Configs.CHROMO_LENGTH_COUNT) + "\t" + str(seq_record.seq) + sequence_reversed + "\t" + seq_record + "\n")

        modified_sequences.append(seq_record)
    wfile.close()

write_fasta_file(modified_sequences)
print("-----modified data added to file-----------")

