import matplotlib.pyplot as plt

memoria= []

#Aquecimento:
    #x^7 - 3.7x^4 + 5x^3 - 88 = [(1,7),(-3.7,4),(5,3),(-88,0)]
    #2x^2 + 17 = [(2,2),(17,0)]
    #7x^4 + 6x^3 - x^2 + 43 = [(7,4),(6,3),(-1,2),(43,0)]
    #x^4 = [(1,4)]
    #x^2 = [(1,2)]
    #x^3 = [(1,3)]

#Define uma função que dado um polinómio calcula a sua derivada
def calcDerivada(p):
    res = []
    for i in p:
        derivada = (int(i[0])*int(i[1]),int(i[1])-1)
        if derivada[1] >= 0:    
            res.append(derivada)
    return res

#Define uma função que recebe dois polinomios p1 e p2 e calcula um novo polinomio corresponde à soma de p1 e p2 
def calcSoma(p1,p2):
    res = []
    
    maximo = max(len(p1),len(p2))

    while len(p1) < maximo:    
        p1.append((0,0))

    while len(p2) < maximo:    
        p2.append((0,0))
                                                    
    i = 0
    while i < maximo:
        if p1[i][1] == p2[i][1]:
            soma = (p1[i][0]+p2[i][0],p1[i][1])
            res.append(soma)
        else:
            if p1[i] != (0,0):
                semsoma = p1[i]
                res.append(semsoma)
            if p2[i] != (0,0):
                semsoma = p2[i]    
                res.append(semsoma)
        i += 1
    return res


#Define uma função que recebe um polinomio e o desenha num gráfico
def desenhar(p):
    pass # Nao consegui mexer com o matplot

def lerFicheiro():
    file = open("polinomios.txt","r")
    res = []
    for line in file:
        line = line.strip()
        registo = line.split("|")
        polinomio = []
        for j in registo:
            interior = j.split(";")
            coeficiente = int(interior[0])
            grau = int(interior[1]) 
            fim = (coeficiente,grau)
            polinomio.append(fim)

        res.append([polinomio])
    file.close()
    return res


def listarPolinomios(memoria):
    i = 0
    while i < len(memoria):
       print(f"\n{i+1} | {memoria[i]}")
       i+=1

def listarPolinomiosGrau(memoria):
    i = 0
    while i < len(memoria):
        j = 0
        graus = []
        while j < len(memoria[i]):
            graus.append(memoria[i][j][1])
            j+=1
        maximo = max(graus)
        print(f"\n{i+1} | {memoria[i]} | Grau: {maximo}")
        i+=1

def listarDerivadas(memoria):
    i = 0
    while i < len(memoria):
       print(f"\n{i+1} | {memoria[i]} | Derivada: {calcDerivada(memoria[i])}")
       i+=1

def maiorGrau(memoria):
    grausmaximos =[]
    i = 0
    while i < len(memoria):
        j = 0
        graus = []
        while j < len(memoria[i]):
            graus.append(memoria[i][j][1])
            j+=1
        maximo = max(graus)
        grausmaximos.append(maximo)
        i+=1
    maior = max(grausmaximos)
    i=0
    while i < len(memoria):
        j=0
        while j< len(memoria[i]):   
            if memoria[i][j][1] == maior:
                polinomiomaior = memoria[i]
                indice = i+1
            j+=1
        i+=1
    
    print(f"\nPolinómio de maior grau: {indice} | {polinomiomaior} | Grau: {maior}")

def criaPolin():
    resPol =[]
    g = int(input("Introduza o grau do polinomio: "))
    while g >= 0 : 
        coeficiente = int(input("Introduza o coeficiente: "))
        if coeficiente != 0:
            termo = (coeficiente,g)
            resPol.append(termo)
        g -= 1
    return resPol

def calcPolinomio(p, x):
    res = 0
    for j in p:
        coeficiente = int(j[0])
        grau = int(j[1])
        res += coeficiente * x ** grau
    return res

def guardarPolinomios(memoria):
    file = open("polinomios.txt","a")
    for i in memoria:
        for p in i:
                coe = p[0]
                grau = p[1]
                file.write(str(coe) +";"+str(grau) + "\n")
    file.close() #REVER ESTE

def main():
    escolha = int(input("\n----------Bem vindo ao menu----------\n[1]Criar um polinómio\n[2]Ler os polinómios de um ficheiro\n[3]Listar polinómios em tabela\n[4]Calcular um polinómio num ponto\n[5]Listar polinómios com grau\n[6]Polinómio de maior grau\n[7]Calcular derivada do polinómio\n[8]Somar polinómios\n[9]Gerar gráfico para polinómio\n[10]Gravar no ficheiro os polinómios na memoria\n[11]Sair "))
    while escolha != 11:
        if escolha == 1:
            novopol = (criaPolin()) 
            memoria.append(novopol)
        if escolha == 2:
            print(lerFicheiro())
            memoria=lerFicheiro()
        if escolha == 3:
            listarPolinomios(memoria)
        if escolha == 4:
            print(calcPolinomio(memoria[int(input("Qual o número do polinomio para calcular? "))-1],int(input("Qual o valor? "))))
        if escolha == 5:
            listarPolinomiosGrau(memoria)
        if escolha == 6: 
            maiorGrau(memoria)
        if escolha == 7:
            listarDerivadas(memoria) 
        if escolha == 8:
            print(calcSoma(memoria[int(input("Qual o número do primeiro polinómio? "))-1],memoria[int(input("Qual o número do primeiro polinómio? "))-1])) #erro
        if escolha == 9:
            desenhar(memoria[int(input("Qual o número do polinómio que pretende visualizar graficamente? "))-1])
        if escolha == 10:
            guardarPolinomios(memoria)
        escolha = int(input("\n----------Bem vindo ao menu----------\n[1]Criar um polinómio\n[2]Ler os polinómios de um ficheiro\n[3]Listar polinómios em tabela\n[4]Calcular um polinómio num ponto\n[5]Listar polinómios com grau\n[6]Polinómio de maior grau\n[7]Calcular derivada do polinómio\n[8]Somar polinómios\n[9]Gerar gráfico para polinómio\n[10]Gravar no ficheiro os polinómios na memoria\n[11]Sair "))
    print("Saiu da aplicação. ")

main()