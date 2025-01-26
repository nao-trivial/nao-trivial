# Exemplo de sequências de DNA
seq1 = 'TCTGCTTTAACTTAT'
seq2 = 'AGTGCGCTGACCTAC'

# Função para traduzir uma sequência de DNA em proteína
def translate(DNA):
    # Dicionário para mapear códons para aminoácidos
    dna_to_pro = {...}
    
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