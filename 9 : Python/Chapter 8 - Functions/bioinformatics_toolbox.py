import re
# import pprint as pp

fasta_path = '/Users/jade/Documents/MATLAB/SysMIC/9 : Python/Chapter 8 - Functions/gpcr.fasta'

def read_fasta(path):
    """
    Reads a FASTA file and returns a single, continuous string.
    :param path: Path to the FASTA file.
    :type path: str
    :return: String of the sequence.
    :rtype: str
    """
    with open(path, mode='r') as fasta_file:
        fasta_data = fasta_file.read()
        fasta_list = fasta_data.splitlines()
        seq_list   = fasta_list[1:] # sequence is everything beyond line 0 (aka the header)
        seq        = ''.join(seq_list) # Remove all whitespace
    return seq

def complimentary_dna(dna):
    """
    Convert a DNA sequence to cDNA.
    :param dna: DNA sequence
    :type dna: str
    :return: String of cDNA
    :rtype: str
    """
    dna2cdna = {
        'A': 'T',
        'C': 'G',
        'G': 'C',
        'T': 'A'
    }

    cdna = ''
    for nucleotide in dna:
        cdna += dna2cdna[nucleotide]
    return cdna

def transcribe(dna):
    """
    Convert a cDNA sequence to mRNA.
    :param dna: cDNA sequence
    :type dna: str
    :return: String of mRNA
    :rtype: str
    """
    dna2mrna = {
        'A': 'U',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }

    mrna = ''
    for nucleotide in dna:
        mrna += dna2mrna[nucleotide]
    return mrna

def translate(mrna, reading_frame=1):
    """
    Produce an amino acid (polypeptide) sequence from each of the 3 reading frames in an mRNA and return first frame by default. Optional reading_frame param to specify which reading frame is returned.
    :param mrna: mRNA sequence
    :type mrna: str
    :param reading_frame: The reading frame of interest. Default value: 1. Takes 1-3 where 1 is the first reading frame only, 2 returns 2nd reading frame only, and 3 returns third reading frame only. Any value outside this range returns empty string.
    :type reading_frame: int
    :return: String of protein sequence
    :rtype: str
    """

    codon2aa = {
        "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "CUU": "L",
        "CUC": "L", "CUA": "L", "CUG": "L", "AUU": "I", "AUC": "I",
        "AUA": "I", "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S",
        "AGC": "S", "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T", "GCU": "A",
        "GCC": "A", "GCA": "A", "GCG": "A", "UAU": "Y", "UAC": "Y",
        "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q", "AAU": "N",
        "AAC": "N", "AAA": "K", "AAG": "K", "GAU": "D", "GAC": "D",
        "GAA": "E", "GAG": "E", "UGU": "C", "UGC": "C", "UGG": "W",
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R",
        "AGG": "R", "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
        "AUG": "<Met>", "UAA": "<STOP>", "UAG": "<STOP>", "UGA": "<STOP>"
    }
    protein = ''
    for n in range(reading_frame-1, len(mrna)+1, 3):
        if mrna[n:n+3] in codon2aa:
            protein += codon2aa[mrna[n:n+3]]
    return protein

def translate_all_frames(mrna):
    """
    Produce all the reading frames in an mRNA.
    :param mrna: mRNA sequence
    :type mrna: str
    :return: Dictionary containing the translation of all three reading frames.
    :rtype: dict
    """
    frames = dict()
    for frame in range(1,4):
        frames['Frame %s' % (frame)] = translate(mrna, frame)
    return frames

def replace_met(seq):
    """
    Takes a protein sequence and replace all instances of ''<MET>' with 'M'.
    :param seq: Protein sequence from a single frame.
    :type frame: str
    :return: Modified string where '<MET>' has been replaced with 'M'.
    :rtype: str
    """
    replaced = re.sub('<Met>', 'M', seq)
    return replaced

def find_exons(frame):
    """
    Takes a protein sequence, indentifies exons, and places them in a list.
    :param frame: Protein sequence from a single frame.
    :type frame: str
    :return: A list of all exons.
    :rtype: list
    """
    results = re.findall(r'M(.*?)<STOP>', frame) # Find and extract all amino acids between M and <STOP>.
    filtered = ['M'+seq for seq in results if len (seq) > 1] # Filter out any proteins that are less than 2 amino acids long.
    return filtered

def extract_exons(frames):
    """
    Produce the exons in each reading frame.
    :param frames: A dictionary that is formatted in the same way as the output of the translate_all_frames function.
    :type frames: dict
    :return: A dictionary with the reading frames as keys, and list of dictionaries as values. Each dictionary in the list of dictionaries should contain 4 pieces of information: exon number, total number of exons in that reading frame, length of exon (excl. the <STOP> marker, and with <Met> replaced by M), and exon sequence (excl. the <STOP> marker, and with <Met> replaced by M).
    :rtype: dict
    """
    extracted_exons = dict()

    for frame in frames:

        replaced    = replace_met(frames[frame])
        exons       = find_exons(replaced)
        total_exons = len(exons)

        temp = []
        for i, exon in enumerate(exons):
            temp.append({
                    'exon number': i+1,
                    'total exons': total_exons,
                    'length'     : len(exon),
                    'sequence'   : exon

                    })

        extracted_exons[frame] = temp

    return extracted_exons

# seq  = read_fasta(fasta_path)
# cdna = complimentary_dna(seq)
# mrna = transcribe(cdna)
#
# frames = translate_all_frames(mrna)
# pp.pprint(extract_exons(frames))
