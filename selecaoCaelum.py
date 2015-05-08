auxiliar = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5,
             "f" : 6, "g" : 7, "h" : 8, "i" : 9,"j" : 10,
             "k" : 11, "l" : 12, "m" : 13, "n" : 14, "o" : 15,
             "p" : 16, "q" : 17, "r" : 18, "s" : 19, "t" : 20,
             "u" : 21, "v" : 22, "w" : 23, "x" : 24, "y" : 25,
             "z" : 26, "A" : 27, "B" : 28, "C" : 29, "D" : 30,
             "E" : 31, "F" : 32, "G" : 33, "H" : 34, "I" : 35,
             "J" : 36, "K" : 37, "L" : 38, "M" : 39, "N" : 40,
             "O" : 41, "P" : 42, "Q" : 43, "R" : 44, "S" : 45,
             "T" : 46, "U" : 47, "V" : 48, "W" : 49, "X" : 50,
             "Y" : 51, "Z" : 52, "\n" : 0}

def converterParaNumero(palavra):

    soma = 0

    for char in palavra:       
        soma += auxiliar[char]
        
        
    return soma
    




def ehPrimo(soma):

    divide = 0

    for cont in range(1,soma):
        if(soma%cont) == 0:
            divide+=1

    if (divide > 2):
        resultado = "Não é uma palavra prima"
    else:
        resultado = "É uma palavra prima"

    return resultado




def main():

    cont = 0
    palavras = []

    nomeDoArquivo = "conjuntoDePalavras.txt"
    arquivo = open(nomeDoArquivo,'r')
    print("Descobrindo se a palavra é prima ou não \n")

    palavras = arquivo.readlines()
      
   
    for palavra in palavras:
        
        soma = converterParaNumero(palavra)
        resultado = ehPrimo(soma)
        print (palavra +" "+ resultado + "\n")

    arquivo.close()


main()

