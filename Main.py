phenotype = [['<MP>', '<Sex>', '<Sex>', '<Sex>', '<Sex>', ['<MP>', '<Sex>', ['<MP>', '<Sex>', '<MP>', '<Sex>', '<MP>', '<Sex>', '<MP>', '<Sex>', ['<MP>', '<Sex>']]]], ['('], ['<Expr>'], [')']]

def no_terminal_identifier(phenotype):
    no_terminal_count = 0
    for i in range(len(phenotype)):
        if len(phenotype[i]) == 1:
            if phenotype[i][0][0] == '<' and phenotype[i][0][-1] == '>':
                no_terminal_count += 1
        elif len(phenotype[i]) > 1:
            for ii in range(len(phenotype[i])):
                if len(phenotype[i][ii]) > 1:
                    no_terminal_count += no_terminal_identifier([phenotype[i][ii]])
                if phenotype[i][ii][0] == '<' and phenotype[i][ii][-1] == '>':
                    no_terminal_count += 1
    return no_terminal_count

print(no_terminal_identifier(phenotype))