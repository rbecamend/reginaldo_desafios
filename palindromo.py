#Pede ao usuário dois parâmetros de entrada
comeco = int(input("Começo: "))
final = int(input("Final: "))

#Verifica se os parâmetros são válidos
if comeco >= final:
    print("Erro! Tente novamente!")
#Caso os parâmetros sejam válidos ele começa a buscar os palíndromos 
else:
    #Cria uma lista para armazenar os palíndromos
    palindromos = [] 

    #Inicia o laço para buscar os palíndromos
    for i in range(comeco,final+1,1):
        #Transforma a variável inteira em uma variável string para ser mais facil manipular
        string = str(i)
        #Verifica se a string é um palíndromo
        if string[::-1] == string:
            #Se for um palíndromo ele adiciona a lista
            palindromos.append(string)
    #Exibe os palíndromos encontrados
    for i in palindromos:
        print(i)