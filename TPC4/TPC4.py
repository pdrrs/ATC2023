import random


def menu():
    choice = int()
    choice = int(input("(1)Criar Lista\n(2)Ler Lista\n(3)Soma\n(4)Média\n(5)Maior\n(6)Menor\n(7)estaOrdenada por ordem crescente\n(8)estaOrdenada por ordem descrescente\n(9)Procurar um elemento\n(0)Sair "))
    return choice

def criarLista(lista):
    lista.clear()
    n = random.randint(0,101)
    i = 0
    while i <= n:
        lista.append(random.randint(0,101))
        i += 1
    return lista

def lerLista(lista):
    lista.clear()
    while True:
        inp = input("Introduza um número: ").strip()
        if inp.upper() == "FIM":
            print(lista)
            return 
        try:
            inp = int (inp)
            lista.append(inp)
        except:
            print("Introduza um número válido! ")
        
def soma(lista):
    resultado = 0
    i = 0
    while i < len(lista):
        resultado += lista[i]
        i += 1

    return resultado

def media(lista):
    resultado = 0
    i = 0
    while i < len(lista):
        resultado += lista[i]
        i += 1
    resultado /= len(lista)

    return round(resultado,3)

def maior(lista):
    resultado = 0
    i = 0
    while i < len(lista):
        if lista[i] > resultado:
            resultado = lista[i]
        i += 1 
    return resultado

def menor(lista):
    i = 0
    resultado = lista[i]
    while i < len(lista):
        if lista[i] < resultado:
            resultado = lista[i]
        i += 1 
    return resultado

def estaOrdenadaCrecente(lista):
    if all(lista[i] <= lista[i+1] for i in range(len(lista)-1)) == True:
        print("Sim")
    else:
        print("Não")
    

def estaOrdenadaDecrescente(lista):
    if all(lista[i] >= lista[i+1] for i in range(len(lista)-1)) == True:
        print("Sim")
    else:
        print("Não")

def procurarElemento(lista,elemento):
    if lista.count(int(elemento)) > 0:
        return lista.index(int(elemento))
    else:
        return -1

def main():
    
    lista = []
    choice = menu()
    while True:
        if choice == 1:
            print(criarLista(lista))
            
        if choice == 2:
            lerLista(lista)

        if choice == 3:
            print(soma(lista))

        if choice == 4:
            print(media(lista))

        if choice == 5:
            print(maior(lista))

        if choice == 6:
            print(menor(lista))

        if choice == 7:
            estaOrdenadaCrecente(lista)

        if choice == 8:
            estaOrdenadaDecrescente(lista)

        if choice == 9:
            elemento = input("Que elemento deseja procurar? ")
            print(procurarElemento(lista,elemento))

        if choice == 0:
            print("Saiu do programa.")
            break

        choice = menu()

main()

