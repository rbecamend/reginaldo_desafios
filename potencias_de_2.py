def pot(n):
    """Verifica se um número é potência de 2 e retorna o expoente correspondente."""
    if n <= 0:
        return False, None
    expoente = 0
    while n > 1:
        if n % 2 != 0:
            return False, None
        n //= 2
        expoente += 1
    return True, expoente

def process_file(filename):
    """Lê um arquivo com números e verifica se são potências de 2."""
    with open(filename, 'r') as file:
        lines = file.readlines()

    results = []
    for line in lines:
        try:
            number = int(line.strip())
            is_power, exponent = pot(number)
            if is_power:
                results.append(f"{number} true {exponent}")
            else:
                results.append(f"{number} false")
        except ValueError:
            results.append(f"{line.strip()} invalid input")

    return results
numbers = [
    1,        # Potência de 2: 2^0
    140,      # Não é potência de 2
    128,      # Potência de 2: 2^7
    137,      # Não é potência de 2
    65535,    # Não é potência de 2
    65536,    # Potência de 2: 2^16
    17179869184  # Potência de 2: 2^34
]
for number in numbers:
    is_power, exponent = pot(number)
    if is_power:
        print(f"{number} true {exponent}")
    else:
        print(f"{number} false")