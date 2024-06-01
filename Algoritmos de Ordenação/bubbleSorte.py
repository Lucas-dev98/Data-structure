def bubble_sort(lista):
    """
    Ordena uma lista de números usando o algoritmo Bubble Sort,
    imprimindo o estado da lista a cada passo.

    Args:
        lista (list): A lista de números a ser ordenada.

    Returns:
        list: A lista ordenada.
    """
    n = len(lista)
    passo = 1
    for j in range(n-1):
        for i in range(n-1-j):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
            print(f"Passo {passo}: {lista}")
            passo += 1
    return lista

def main():
    """
    Função principal para testar o algoritmo Bubble Sort.
    """
    lista = [23, 25, 27, 15, 32, 21, 32, 55, 99]
    print("Lista original:", lista)
    lista_ordenada = bubble_sort(lista)
    print("Lista ordenada:", lista_ordenada)

if __name__ == "__main__":
    main()