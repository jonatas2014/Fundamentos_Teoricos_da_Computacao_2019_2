import re


def valida_local(galaxia):

    match = re.search(r"((?<!.)\bVia Lactea\b(?!.))|" +
                       r"((?<!.)\bAndromeda\b(?!.))|" +
                       r"((?<!.)\bTriangulo\b(?!.))|" +
                       r"((?<!.)\bRedemoinho\b(?!.))|" +
                       r"((?<!.)\bSombreiro\b(?!.))|" +
                       r"((?<!.)\bGirassol\b(?!.))|" +
                       r"((?<!.)\bGrande Nuvem de Magalhaes\b(?!.))|" +
                       r"((?<!.)\bPequena Nuvem de Magalhaes\b(?!.))|" + 
                       r"((?<!.)\bCompasso\b(?!.))|" +
                       r"((?<!.)\bAna de Fenix\b(?!.))|" +
                       r"((?<!.)\bMessier 87\b(?!.))|" +
                       r"((?<!.)\bMessier 32\b(?!.))|" +
                       r"((?<!.)\bLeo I\b(?!.))|" +
                       r"((?<!.)\bMessier 110\b(?!.))", galaxia, re.IGNORECASE)
    
    if match:
        return True
    else:
        return False

def valida_nave(nava_escolhida):

    match = re.search(r"((?<!.)\bNebula Class A\b(?!.))|" +
                       r"((?<!.)\bNebula Class B\b(?!.))|" +
                       r"((?<!.)\bIntrepid Class\b(?!.))|" +
                       r"((?<!.)\bNiagaria Class\b(?!.))|" +
                       r"((?<!.)\bWells Class\b(?!.))|" +
                       r"((?<!.)\bHoloship\b(?!.))|" +
                       r"((?<!.)\bRaven\b(?!.))|" +
                       r"((?<!.)\bPeregrine\b(?!.))|" + 
                       r"((?<!.)\bDanube Class\b(?!.))" , nava_escolhida)
    
    if match:
        return True
    else:
        return False

def valida_passageiro(id_usuario):

    match = re.search(r"(?<!.)\d{3}-\d{2}-\d{4}(?!.)", id_usuario)
    if match:

        nao_match_a_1 = re.search(r"000-\d{2}-\d{4}", id_usuario)
        nao_match_a_2 = re.search(r"\d{3}-00-\d{4}", id_usuario)
        nao_match_a_3 = re.search(r"\d{3}-\d{2}-0000", id_usuario)
        if nao_match_a_1 or nao_match_a_2 or nao_match_a_3:
            return False
        
        nao_match_b_1 = re.search(r"666-\d{2}-\d{4}", id_usuario)
        nao_match_b_2 = re.search(r"9\d{2}-\d{2}-\d{4}", id_usuario)
        if nao_match_b_1 or nao_match_b_2:
            return False
        
        nao_match_c_1 = re.search(r"111-11-1111", id_usuario)
        nao_match_c_2 = re.search(r"222-22-2222", id_usuario)
        nao_match_c_3 = re.search(r"333-33-3333", id_usuario)
        nao_match_c_4 = re.search(r"444-44-4444", id_usuario)
        nao_match_c_5 = re.search(r"555-55-5555", id_usuario)
        nao_match_c_7 = re.search(r"777-77-7777", id_usuario)
        nao_match_c_8 = re.search(r"888-88-8888", id_usuario)
        if (nao_match_c_1 or nao_match_c_2 or nao_match_c_3 or
            nao_match_c_4 or nao_match_c_5 or nao_match_c_7 or nao_match_c_8):
            return False

        nao_match_d_1 = re.search(r"078-85-1120", id_usuario)
        nao_match_d_2 = re.search(r"219-09-9999", id_usuario)
        if nao_match_d_1 or nao_match_d_2:
            return False

        return True
    else:
        return False

def valida_timestamp(user_timestamp):
    
    match = re.search(r"(?<!.)[0-3]\d/[0-1]\d/\d{4} [0-2]\d:[0-5]\d(?!.)", user_timestamp)

    if match:
        is_valid = re.search(r"([0-3]\d)/([0-1]\d)/(\d{4}) ([0-2]\d):([0-5]\d)", user_timestamp)
        # Dia maior que 31 e/ou mes maior que 12
        if (int(is_valid.group(1)) > 31 or
           int(is_valid.group(2)) > 12):
            return False
        
        # Fevereiro e ano bissexto
        if int(is_valid.group(2)) == 2:
            if int(is_valid.group(1)) > 29:
                return False
            bissexto = ((int(is_valid.group(3)) % 400 == 0) or
                       ((int(is_valid.group(3)) % 4 == 0) and
                        (int(is_valid.group(3)) % 100 != 0)))
            if ((bissexto is False) and
                int(is_valid.group(1)) > 28):
                return False
    
        # Meses que acabam no dia 30
        if int(is_valid.group(1)) == 31:
            meses_30 = [4, 6, 9, 11]
            if int(is_valid.group(2)) in meses_30:
                return False
                
        # Evitar dia 0, mes 0 e ano 0
        if (int(is_valid.group(1)) < 1 or
            int(is_valid.group(2)) < 1 or
            int(is_valid.group(3)) < 1):
            return False

        # HH maior do que 23
        if int(is_valid.group(4)) > 23:
            return False

        ## NN maior do que 59
        if int(is_valid.group(5)) > 59:
            return False
        
        return True
    else:
        return False

def valida_preco(price):

    match = re.search(r"(?<!.)(?:(?=ETH )|(?=BTC )|(?=LTC ))(\w{3})", price)
    
    if match:

        btc_match = re.search(r"BTC ([0]\.\d{3})(?!.)", price)
        if btc_match:
            valor = float(btc_match.group(1))
            if valor > 0 and valor < 1:
                return True, valor, "BTC"
        
        ltc_match = re.search(r"LTC (\d{2}\.\d{2})(?!.)", price)
        if ltc_match:
            valor = float(ltc_match.group(1))
            if valor > 0:
                return True, valor, "LTC"
        
        eth_match = re.search(r"ETH (\d{1,3})(?!.)", price)
        if eth_match:
            valor = int(eth_match.group(1))
            if valor > 0:
                return True, valor, "ETH"
               
        return False, 0, " "
           
    else:
        return False, 0, " "

def valida_codigo(codigo):

    match = re.search(r"(?=.*[A-Z].*[A-Z].*[A-Z])" +
                      r"(?=.*\d.*\d.*\d.*\d)" +
                      r"(?=.*[$@%(*].*[$@%(*])" +
                      r"(?=.*[a-z].*[a-z].*[a-z])" +
                      r"(?<!.)" +
                      r"(\S{12})" +
                      r"(?!.)", codigo)
    if match:
        return True
    else:
        return False

def valida_hash(hash):

    match = re.search(r"(?<!.)[\dabcdef]{32}(?!.)", hash)
    if match:
        return True
    else:
        return False

# Inicio do programa
validacao = True
total_btc = 0
total_eth = 0
total_ltc = 0
entrada = input()
while (entrada != 'END'):
    
    virgulas = re.findall(r',', entrada)
    if len(virgulas) == 7:
        dados = re.split(r',', entrada)
    
        # Valida origem
        validacao = valida_local(dados[0])

        # Valida destino
        if validacao is True:
            validacao = valida_local(dados[1])
        
        # Valida passageiro
        if validacao is True:
            validacao = valida_passageiro(dados[2])

        # Valida timestamp
        if validacao is True:
            validacao = valida_timestamp(dados[3])
            
        # Valida nave
        if validacao is True:
            validacao = valida_nave(dados[4])

        # Valida tarifa 
        if validacao is True:
            validacao = valida_preco(dados[5])[0]
        
        # Valida o codigo de seguranca
        if validacao is True:
            validacao = valida_codigo(dados[6])
        
        # Valida o Hash md5
        if validacao is True:
            validacao = valida_hash(dados[7])
            
        # Adicionar a tarifa
        if validacao is True:
            if valida_preco(dados[5])[2] == "BTC":
                total_btc += valida_preco(dados[5])[1]
            elif valida_preco(dados[5])[2] == "ETH":
                total_eth += valida_preco(dados[5])[1]
            else:
                total_ltc += valida_preco(dados[5])[1]
   
    else: 
        validacao = False
        
    print(validacao)
    entrada = input()

print("BTC %.2f"%total_btc)
print("ETH %.2f"%total_eth)
print("LTC %.2f"%total_ltc)