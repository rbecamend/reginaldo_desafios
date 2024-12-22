# Lista de caracteres para bases até 62 (0-9, A-Z, a-z)
lista = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
        'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 
        'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
        'y', 'z']

# Função para converter um número de qualquer base para a base 10
def converter_decimal(numero_entrada, base):
    numero_entrada = list(numero_entrada)
    resultado = 0  # Variável para acumular o valor final
    tamanho = len(numero_entrada)
    # Verificar se o número é negativo
    if numero_entrada[0] == '-':
        return "???"  

    for i in range(tamanho):
        aux = numero_entrada[i]
        
        # Verificar o valor do caractere na base correspondente
        if aux in lista:
            numero = lista.index(aux)
        else:
            return "???"  
        
        # Verificar se o número é válido para a base
        if numero >= base:
            return "???" 
        
        expoente = (tamanho - 1) - i  
        resultado += numero * (base ** expoente)
    
    return resultado

# Função para converter de base 10 para qualquer base
def converter_base(base_saida, numero_convertido_base10):
    if numero_convertido_base10 == 0:
        return '0'  # Se o número for zero, a conversão é '0'
    
    resultado = ''
    while numero_convertido_base10 > 0:
        numero = numero_convertido_base10 % base_saida  # Resto da divisão para determinar o dígito
        # Usar a lista completa para representar o número convertido
        resultado = lista[numero] + resultado
        numero_convertido_base10 //= base_saida  # Divisão inteira para processar o próximo dígito
    return resultado

# Função principal para processar as entradas a partir de um arquivo
def entrada(arquivo_nome):
    
    with open(arquivo_nome, 'r') as file:
        linhas = file.readlines()  # Lê todas as linhas do arquivo

    for linha in linhas:
        linha = linha.strip()  # Remove espaços extras e quebras de linha

        # Ignorar linhas vazias
        if not linha:
            continue

        try:
            base_entrada, base_saida, numero_entrada = linha.split()
            base_entrada = int(base_entrada)
            base_saida = int(base_saida)

            # Verificar se as bases estão entre 2 e 62
            if base_entrada < 2 or base_entrada > 62 or base_saida < 2 or base_saida > 62:
                print("???")
                continue
            if base_entrada == 62 and len(numero_entrada) > 30:
                print("???")
                continue 
            # Verificar se o número é negativo
            if numero_entrada[0] == '-':
                print("???")
                continue
            
            # Verificar se o número contém caracteres inválidos para a base de entrada
            numero_convertido_base10 = converter_decimal(numero_entrada, base_entrada)
            if numero_convertido_base10 == "???":
                print("???")
                continue

            # Converter para a base de saída
            numero_convertido_base_saida = converter_base(base_saida, numero_convertido_base10)
            print(numero_convertido_base_saida)

        except ValueError:
            print("???")

entrada('baseconv.txt')
