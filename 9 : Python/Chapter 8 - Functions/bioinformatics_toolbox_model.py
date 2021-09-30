"""
Bioinformatics Toolbox
======================

Tools for sequence manipulation; including:

- Sequence extraction from FASTA files
- Transcription
- Translation
- Exon extraction

"""

import re


TO_CDNA = {
    'A': 'T',
    'C': 'G',
    'G': 'C',
    'T': 'A'
}


TO_MRNA = {
    'A': 'U',
    'T': 'A',
    'G': 'C',
    'C': 'G'
}


TO_AMINO_ACID = {
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


def read_fasta(path):
    """
    Extracts the sequence from a FASTA file.

    :param path: Path to the FASTA file.
    :type path: str
    :return: Sequence, as one continuous piece of string.
    :rtype: str
    """
    with open(path, mode='r') as fasta_file:
        fasta_data = fasta_file.read()

    seq = fasta_data.splitlines()[1:]

    result = ''.join(seq)

    return result


def convert_sequence(seq, reference):
    """

    :param seq:
    :type seq: str
    :param reference:
    :type reference: dict
    :return:
    :rtype: str
    """
    result = str()
    key = str()

    for value in seq:
        key += value

        converted = reference.get(key, False)

        if converted:
            result += converted
            key = str()  # Reset the key

    return result


def complimentary_dna(dna):
    """
    Converts a DNA sequence to complementary DNA (cDNA).

    :param dna: DNA sequence.
    :type dna: str
    :return: Complimentary DNA (cDNA) sequence.
    :rtype: str


    Example
    -------

    >>> dna = 'ACTGGC'
    >>> cdna = complimentary_dna(dna)
    >>> print(cdna)
    TGACCG
    """

    result = convert_sequence(dna, TO_CDNA)

    return result


def transcribe(dna):
    """
    Transcribes a DNA sequence to an mRNA sequence.

    The process works in the same way as it does in a biological system;
    that is, it converts the sequence to its complimentary format using
    RNA nucleotides. For instance; A binds to U and T bind to A.

    :param dna: DNA sequence
    :type dna: str
    :return: mRNA sequence
    :rtype: str


    Example
    -------

    >>> dna = 'ACTGGC'
    >>> mrna = transcribe(dna)
    >>> print(mrna)
    UGACCG
    """

    result = convert_sequence(dna, TO_MRNA)

    return result


def translate(mrna, reading_frame=1):
    """
    Translates an mRNA sequence to a protein sequence by extracting codon triplets
    from the desired `reading_frame`.

    :param mrna: mRNA sequence
    :type mrna: str
    :param reading_frame: Desired reading frame. Must be 1, 2, or 3. [Default: 1]
    :type reading_frame: int
    :return: Translation of the mRNA sequence at the desired `reading_frame).
    :rtype: str


    Examples
    --------

    >>> mrna = 'CCGAUGUUGACUUAG'
    >>> peptide = translate(mrna)
    >>> print(peptide)
    P<Met>LT<STOP>

    >>> peptide = translate(mrna, 2)
    >>> print(peptide)
    RC<STOP>L

    Values below 0 or above 3 are invalid, and yield an empty output (blank line):

    >>> peptide = translate(mrna, reading_frame=5)
    >>> print(peptide)
    <BLANKLINE>
    """
    if reading_frame > 3 or reading_frame < 1:
        return str()

    frame_offset = 1
    starting_frame = reading_frame - frame_offset

    protein = convert_sequence(mrna[starting_frame:], TO_AMINO_ACID)

    return protein


def get_reading_frames(mrna):
    """
    Produces the translation for all of the reading frames in an mRNA sequence.

    :param mrna: mRNA sequence
    :type mrna: str
    :return: Dictionary of translations in the following format:

        {
            'frame 1': 'translation for frame 1',
            'frame 2': 'translation for frame 2',
            'frame 3': 'translation for frame 3'
        }

    :rtype: dict


    Example
    -------

    >>> mrna = 'CCGAUGUUGACUUAG'
    >>> frames = get_reading_frames(mrna)
    >>> print(frames)
    {'frame 1': 'P<Met>LT<STOP>', 'frame 2': 'RC<STOP>L', 'frame 3': 'DVDL'}
    """
    reading_frames = (1, 2, 3)
    result = dict()

    for frame in reading_frames:
        result[f"frame {frame}"] = translate(mrna, reading_frame=frame)

    return result


def find_exons(seq):
    """
    Extracts all of the possible exons from a polypeptide sequence.

    An exon is defined as any sequence with at least 2 residues, which is
    located between a Methionine (M) residue, and a `<STOP>` marker.

    :param seq: Polypeptide sequence.
    :type seq: str
    :return: List of exons (string values) extracted from the polypeptide sequence.
    :rtype: list


    Example
    -------

    >>> mrna = 'CCGAUGUUGACUUAGCUGAUGUUUUUGUUGAUCGUGUAGGGG'
    >>> peptide = translate(mrna)
    >>> print(peptide)
    P<Met>LT<STOP>L<Met>FLLIV<STOP>G

    >>> peptide = peptide.replace('<Met>', 'M')
    >>> exons = find_exons(peptide)
    >>> print(exons)
    ['MLT', 'MFLLIV']
    """
    pattern = re.compile(r'(M\w+?)<STOP>', re.IGNORECASE)
    found = pattern.findall(seq)

    return found


def get_sequence_exons(seq):
    """
    Extracts all of the possible exons from a polypeptide sequence.

    An exon is defined as any sequence with at least 2 residues, which is
    located between a Methionine (M) residue, and a `<STOP>` marker.

    :param seq: Polypeptide sequence.
    :type seq: str
    :return: List of dictionaries containing the exon number, total number of exons
             extracted from the sequence, length of the exon, and the exon sequence,
             in the following format:

        {
            'exon number': int (1 or more),
            'total exons': int (1 or more),
            'length': int (2 or more),
            'sequence: str
        }

    :rtype: list


    Example
    -------

    >>> mrna = 'CCGAUGUUGACUUAGCUGAUGUUUUUGUUGAUCGUGUAGGGG'
    >>> peptide = translate(mrna)
    >>> print(peptide)
    P<Met>LT<STOP>L<Met>FLLIV<STOP>G

    >>> exons = get_sequence_exons(peptide)
    >>> print(exons)
    [{'exon number': 1, 'total exons': 2, 'length': 3, 'sequence': 'MLT'}, \
{'exon number': 2, 'total exons': 2, 'length': 6, 'sequence': 'MFLLIV'}]
    """
    exons_list = find_exons(seq.replace('<Met>', 'M'))
    found_len = len(exons_list)

    result = list()

    for exon_number, exon in enumerate(exons_list, start=1):
        item = {
            'exon number': exon_number,
            'total exons': found_len,
            'length': len(exon),
            'sequence': exon,
        }

        result.append(item)

    return result


def extract_exons(reading_frames):
    """
    Extracts all of the possible exons from each reading frame.

    An exon is defined as any sequence with at least 2 residues, which is
    located between a Methionine (`M`) residue, and a `<STOP>` marker.

    :param reading_frames: Dictionary of reading frames in the following format:

        {
            'frame 1': 'translation for frame 1',
            'frame 2': 'translation for frame 2',
            'frame 3': 'translation for frame 3'
        }

    :type reading_frames: dict
    :return: Dictionary of exons in the following format:

        {
            'frame 1': [
                # Output of `get_sequence_exons` for frame 1.
            ],
            'frame 2': [
                # Output of `get_sequence_exons` for frame 2.
            ],
            'frame 3': [
                # Output of `get_sequence_exons` for frame 3.
            ],
        }

    :rtype: dict


    Example
    -------

    >>> mrna = 'CCGAUGUUGACUUAGCUGAUGUUUUUGUUGAUCGUGUAGGGG'

    First, we extract the reading frames:

    >>> frames = get_reading_frames(mrna)
    >>> print(frames)
    {'frame 1': 'P<Met>LT<STOP>L<Met>FLLIV<STOP>G', \
'frame 2': 'RC<STOP>LS<STOP>CFC<STOP>SCR', \
'frame 3': 'DVDLADVFVDRVG'}

    Now, we can use the reading frames dictionary to extract the exons:

    >>> exons = extract_exons(frames)
    >>> print(exons)
    {'frame 1': [{'exon number': 1, 'total exons': 2, 'length': 3, 'sequence': 'MLT'}, \
{'exon number': 2, 'total exons': 2, 'length': 6, 'sequence': 'MFLLIV'}], \
'frame 2': [], \
'frame 3': []}
    """
    result = dict()

    for frame_name, translation in reading_frames.items():
        result[frame_name] = get_sequence_exons(translation)

    return result
