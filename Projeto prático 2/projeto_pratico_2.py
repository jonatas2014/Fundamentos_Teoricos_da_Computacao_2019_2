def pilha_in(lista, symbol):
    lista.append(symbol)


def pilha_out(lista):
    lista.pop()


def pilha_is_empty(lista):
    return len(lista) == 0


def get_topo(pilha):
    return pilha[-1]


def eh_casada(string):
    pilha = []
    for char in string:
        # colocar cada caracter da string na pilha (empilhar) se for (,[ ou {
        if ((char == '(') or (char == '[') or (char == '{')):
            pilha_in(pilha, char)
        # desempilhar se for ),] ou }
        if ((char == ')') or (char == ']') or (char == '}')):
            # se for ),],} e a pilha estivar vaiza retorna FALSE
            if pilha_is_empty(pilha):
                return False
            pilha_out(pilha)

    return pilha_is_empty(pilha)


# Verifica se so ha um simbolo na string
def so_tem_um_simbolo(string):
    contraparte = ""
    simbolo = string[0]
    if simbolo == '(':
        contraparte = ')'
    elif simbolo == '[':
        contraparte = ']'
    elif simbolo == '{':
        contraparte = '}'
    i = 1
    while (i < len(string)):
        if (string[i] != simbolo) and (string[i] != contraparte):
            return False
        i += 1
    return True


# Apenas verifica se a string eh correta
def eh_correta(string):
    # Retirar espacos da string
    string_sem_espacos = []
    for char in string:
        if char != " ":
            string_sem_espacos.append(char)
    # Verifica se a string tinha apenas espacos em branco
    if len(string_sem_espacos) == 0:
        return True
    if so_tem_um_simbolo(string_sem_espacos):
        return True
    i = 0
    while (i < len(string_sem_espacos)):
        # nao precisa verificar ultima ou primeira posicao
        if (i > 0) and (i < (len(string_sem_espacos) - 1)):
            if string_sem_espacos[i] == '{':
                if string_sem_espacos[i - 1] != '{':
                    # se a fatia da string anterior a { nao for casada
                    # e nao for { garante q nao eh correta
                    if eh_casada(string_sem_espacos[:i:]) is False:
                        return False
            # se for } nao pode ter ) ou ] pela direita
            elif string_sem_espacos[i] == '}':
                if string_sem_espacos[i + 1] != '}':
                    if eh_casada(string_sem_espacos[i + 1::]) is False:
                        return False
            # se for [ nao pode ter somente parenteses abrindo pela esquerda
            elif string_sem_espacos[i] == '[':
                if (string_sem_espacos[i - 1] != '{' and
                        string_sem_espacos[i - 1] != '['):
                    if eh_casada(string_sem_espacos[:i:]) is False:
                        return False
            # se for ] nao pode ter ) pela direita
            elif string_sem_espacos[i] == ']':
                if (string_sem_espacos[i + 1] != '}' and
                        string_sem_espacos[i + 1] != ']'):
                    if eh_casada(string_sem_espacos[i + 1::]) is False:
                        return False

        i += 1
    return True


def corrige(string):
    mapeamento_numeros = {'{': 1, '[': 2, '(': 3, ')': 4, ']': 5, '}': 6,
                          " ": 7}
    chaves = list(mapeamento_numeros.keys())
    string_numeros = []
    string_corrigida = []
    for char in string:
        string_numeros.append(mapeamento_numeros[char])
    aux = 0
    i = 0
    while (i < len(string)):

        if i >= 1 and string_numeros[i] == 1:
            j = i - 1
            while ((string_numeros[j] == 2 or string_numeros[j] == 3 or
                   string_numeros[j] == 7) and (i >= 1)):
                aux = string_numeros[j]
                string_numeros[j] = string_numeros[i]
                string_numeros[i] = aux
                j -= 1
                i -= 1

        if i >= 1 and string_numeros[i] == 2:
            j = i - 1
            while ((string_numeros[j] == 3 or string_numeros[j] == 7) and
                   (i >= 1)):
                aux = string_numeros[j]
                string_numeros[j] = string_numeros[i]
                string_numeros[i] = aux
                j -= 1
                i -= 1

        if i >= 1 and string_numeros[i] == 4:
            j = i - 1
            while (string_numeros[j] == 5 or string_numeros[j] == 6 or
                   string_numeros[j] == 7):
                aux = string_numeros[j]
                string_numeros[j] = string_numeros[i]
                string_numeros[i] = aux
                j -= 1
                i -= 1

        if i >= 1 and string_numeros[i] == 5:
            j = i - 1
            while (string_numeros[j] == 6 or string_numeros[j] == 7):
                aux = string_numeros[j]
                string_numeros[j] = string_numeros[i]
                string_numeros[i] = aux
                j -= 1
                i -= 1
        i += 1

    for number in string_numeros:
        if number != 7:
            string_corrigida.append(chaves[number - 1])

    return ''.join(string_corrigida)


entrance = input()
# lista q vai armazenando no while as saidas para cada string
# a saber (nao eh casada, casada e correta ou casada e incorreta)
strings_results = []
strings_corrigidas = []

while (entrance != ""):

    if eh_casada(entrance):

        if eh_correta(entrance):
            strings_results.append("casada e correta")
        else:

            strings_corrigidas.append(corrige(entrance))
            strings_results.append("casada e incorreta")

    else:
        strings_results.append("nao casada")
    entrance = input()


# impressao do resultado: nao eh casada, casada e correta ou casada e incorreta
for results in strings_results:
    print(results)
# mostrar correcoes de entradas casadas e incorretas
for correcoes in strings_corrigidas:
    print(correcoes)
