# Exemplo de sequências de DNA
seq1 = 'TCTGCTTTAACTTAT'
seq2 = 'AGTGCGCTGACCTAC'

# Função para traduzir uma sequência de DNA em proteína
def translate(DNA):
    # Dicionário para mapear códons para aminoácidos
    dna_to_pro = {
     'ATG': 'M', 'GCG': 'A', 'TCA': 'S', 'GAA': 'E', 'GGG': 'G', 'GGT': 'G', 'AAA': 'K', 'GAG': 'E',
        'AAT': 'N', 'CTA': 'L', 'CAT': 'H', 'TCG': 'S', 'TAG': 'STOP', 'GTG': 'V', 'TAT': 'Y', 'CCT': 'P',
        'ACT': 'T', 'TCC': 'S', 'CAG': 'Q', 'CCA': 'P', 'TAA': 'STOP', 'AGA': 'R', 'ACG': 'T', 'CAA': 'Q',
        'TGT': 'C', 'GCT': 'A', 'TTC': 'F', 'AGT': 'S', 'ATA': 'I', 'TTA': 'L', 'CCG': 'P', 'ATC': 'I',
        'TTT': 'F', 'CGT': 'R', 'TGA': 'STOP', 'GTA': 'V', 'TCT': 'S', 'CAC': 'H', 'GTT': 'V', 'GAT': 'D',
        'CGA': 'R', 'GGA': 'G', 'GTC': 'V', 'GGC': 'G', 'TGC': 'C', 'CTG': 'L', 'CTC': 'L', 'CGC': 'R',
        'CGG': 'R', 'AAC': 'N', 'GCC': 'A', 'ATT': 'I', 'AGG': 'R', 'GAC': 'D', 'ACC': 'T', 'AGC': 'S',
        'TAC': 'Y', 'ACA': 'T', 'AAG': 'K', 'GCA': 'A', 'TTG': 'L', 'CCC': 'P', 'CTT': 'L', 'TGG': 'W'
    
}
    
    protein = []
    start = 0

    # Percorre a sequência de DNA e traduz cada códon
    while start + 2 < len(DNA):
        codon = DNA[start:start + 3]
        # Verifica se o códon é válido
        if codon in dna_to_pro:
            protein.append(dna_to_pro[codon])
        else:
            protein.append('?')  # Marca códons inválidos como '?'
        start += 3
    
    return ''.join(protein)

# Imprime as sequências traduzidas
print("Seq1: ", seq1, "-> Proteína: ", translate(seq1))
print("Seq2: ", seq2, "-> Proteína: ", translate(seq2))