from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from config import Configs


def read_fasta_file():
    sequences = []
    with open(Configs.READ_FILE, "r") as rfile:
        for seq_record in SeqIO.parse(rfile, "fasta"):
            sequences.append(seq_record)
        rfile.close()
    return sequences


def write_fasta_file(seq_records):
    with open(Configs.WRITE_FILE, "w") as wfile:
        SeqIO.write(seq_records, wfile, "fasta")
        wfile.close()
    return
