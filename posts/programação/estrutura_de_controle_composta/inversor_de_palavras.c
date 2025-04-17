#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char nome[100];
    char letras[] = "abcdefghijklmnopqrstuvwxyz";
    char nomes[100][100];
    char descripto[100];

    fgets(nome, sizeof(nome), stdin);
    nome[strcspn(nome, "\n")] = '\0';

    int count = 0;
    char *token = strtok(nome, " ");  // Corrigido: adicionado espaço como delimitador
    while (token != NULL) {
        int index = 0;
        for (int i = 0; i < strlen(token); i++) {
            char c = tolower(token[i]);
            if (strchr(letras, c)) {
                descripto[index++] = c;
            }
        }
        descripto[index] = '\0';

        int len = strlen(descripto);
        for (int i = 0; i < len; i++) {  // Corrigido: inverter a string corretamente
            nomes[count][i] = descripto[len - 1 - i];
        }
        nomes[count][len] = '\0';
        
        token = strtok(NULL, " ");
        count++;
    }

    for (int i = count - 1; i >= 0; i--) {  // Corrigido: sintaxe do loop
        printf("%s ", nomes[i]);  // Adicionado espaço entre as palavras
    }
    printf("\n");

    return 0;
}
