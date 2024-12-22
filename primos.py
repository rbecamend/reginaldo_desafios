#Função para listar todos os números primos até um limite especificado
def listar_primos(limite):
    #Lista para armazenar os números primos encontrados
    primos = []

    #Itera sobre os números de 2 até o limite fornecido
    for num in range(2, limite + 1):
        eh_primo = True  #Assumimos que o número é primo inicialmente

        #Verifica divisibilidade por números até a raiz quadrada do número
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:  #Caso divisível não é primo
                eh_primo = False
                break

        #Adiciona à lista se o número for primo
        if eh_primo:
            primos.append(num)

    return primos  #Retorna a lista de números primos encontrados

#Executa a função para listar os números primos até 10000
primos = listar_primos(10000)
print(primos)  #Exibe a lista de números primos