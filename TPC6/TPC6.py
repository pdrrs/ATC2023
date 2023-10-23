#import os

def setpath():
    path = str(input(r"Qual é a diretoria do ficheiro? ")).strip("\"")
    return path
    

def ler (path):
    #seja o modela pessoa = ((gender),(age),(hypertension),(heart_disease),(smoking_history),(bmi),(HbA1c_level),(blood_glucose_level),(diabetes))
    conteudo = open("{fpath}".format(fpath=path),'r')
    next(conteudo)
    for pessoa in conteudo:
        pessoa = tuple(conteudo.readline().strip("\n").split(","))
        print(pessoa)
        
    conteudo.close()

def calcDistSex (path):
    homem = 0
    mulher = 0
    totaldoentes = 0
    conteudo = open("{fpath}".format(fpath = path),'r')
    next(conteudo)
    for pessoa in conteudo:
        pessoa = tuple(conteudo.readline().strip("\n").split(","))
        if pessoa[3] == "1" and pessoa[0]== "Male":
            homem += 1
            totaldoentes += 1
        elif pessoa[3] == "1" and pessoa[0]== "Female":
            mulher += 1
            totaldoentes +=1
    
    print("\n----------Distribuição de doentes por sexo----------")
    print(" Percentagem de homens com doença cardíaca: ","%.1f" % ((homem/totaldoentes)*100),"%\n","Percentagem de mulheres com doença cardíaca: ","%.1f" % ((mulher/totaldoentes)*100),"%\n")
    conteudo.close()

def calcDistIdade(path):
    idade0_10 = 0
    idade11_24 = 0
    idade25_29 = 0
    idade30_34 = 0
    idade35_39 = 0
    idade40_44 = 0
    idade45_49 = 0
    idade50_54 = 0
    idade55_59 = 0
    idade60_64 = 0
    idade65_69 = 0
    idade70_74 = 0
    idade75_79 = 0
    idade80_84 = 0
    totaldoentes = 0
    faixas_etarias = [idade0_10,idade11_24,idade25_29,idade30_34,idade35_39,idade40_44,idade45_49,idade50_54,idade55_59,idade60_64,idade65_69,idade70_74,idade75_79,idade80_84]
    
    conteudo = open("{fpath}".format(fpath=path),'r')
    next(conteudo)
    
    for pessoa in conteudo:
        a = 24
        b = 30
        pessoa = tuple(conteudo.readline().strip("\n").split(","))
        if float(pessoa[3]) == 1:
            totaldoentes += 1
            if float(pessoa[1]) < 11:
                faixas_etarias[0] += 1
            if float(pessoa[1]) > 10 and float(pessoa[1]) < 25:
                faixas_etarias[1] += 1
            for i in range(2,len(faixas_etarias)):
                if float(pessoa[1]) > a and float(pessoa[1]) < b:
                    faixas_etarias[i] += 1
                a+=5
                b+=5
    print("\n----------Distribuição por faixa etária----------\n")
    print("Faixa etaria [0-10]: {percentagem:.1f}%".format(percentagem = (faixas_etarias[0]/totaldoentes)*100))
    print("Faixa etaria [11-24]: {percentagem:.1f}%".format(percentagem = (faixas_etarias[1]/totaldoentes)*100))
    
    a = 25
    b = 29

    for i in range(2,len(faixas_etarias)):
        faixa = "[{c}-{d}]"
        totaldafaixa = faixas_etarias[i]
        texto = "Faixa etaria {faixaeta}: {percentagem:.1f}%"
        print(texto.format(faixaeta = faixa.format(c = a ,d = b) ,percentagem = (totaldafaixa/totaldoentes)*100))
        a += 5
        b+= 5

def calcDistGluc(path):
    totaldoentes = 0
    gluc_max = 0
    gluc_min = 0
    niveis_gluc = []
    
    conteudo = open("{fpath}".format(fpath=path),'r')
    next(conteudo)
    for pessoa in conteudo:
        pessoa = tuple(conteudo.readline().strip("\n").split(","))
        if float(pessoa[3]) == 1:
            totaldoentes += 1
            if gluc_min == 0:
                gluc_min = int(pessoa[7])
            if int(pessoa[7]) < gluc_min:
                gluc_min = int(pessoa[7]) 
                #niveis_gluc = de alguma forma inserir novos grupo apartir do inicio da lista(aumentar os minimos) 
            if int(pessoa[7]) > gluc_max:
                gluc_max = int(pessoa[7])
                #niveis_gluc = de alguma forma inserir novos grupos apartir do fim da lista(aumentar os maximos)
    grupos_gluc = int((gluc_max-gluc_min)/10)
    niveis_gluc = [0 for x in range(grupos_gluc+1)]
    
    conteudo.close()
    
    conteudo = open("{fpath}".format(fpath=path),'r')
    next(conteudo)
    
    for pessoa in conteudo:
        a=gluc_min
        b=gluc_min+10
        pessoa = tuple(conteudo.readline().strip("\n").split(","))
        if float(pessoa[3]) == 1:
            for i in range(0,len(niveis_gluc)):
                if float(pessoa[7]) >= a and float(pessoa[7]) < b:
                    niveis_gluc[i] += 1
                elif float(pessoa[7]) == 290:
                    niveis_gluc[i] += 1
                a += 10
                b += 10
    
    a=gluc_min
    b=a+10

    print("\n----------Distribuição por nível de glucose no sangue----------\n")
    for i in range(0,len(niveis_gluc)):
        if niveis_gluc[i] != 0:
            intervalo = "[{c}-{d}]"
            totaldointervalo = niveis_gluc[i]
            texto = "Nível de glucose {intervalotxt}: {percentagem:.1f}%"
            print(texto.format(intervalotxt = intervalo.format(c = a ,d = b) ,percentagem = (totaldointervalo/totaldoentes)*100))
        a += 10
        b+= 10    

    conteudo.close()



def tabelas(escolha,path):
    if escolha == 1:
        calcDistSex(path)
    elif escolha == 2:
        calcDistIdade(path)
    elif escolha == 3:
        calcDistGluc(path)
    elif escolha == 4:
        calcDistSex(path)
        calcDistIdade(path)
        calcDistGluc(path)
    
def main():
    path = setpath()
    escolha = int(input("\n----------Bem vindo, que distribuição pretende visualizar?----------\n[1]Distribuição por sexo\n[2]Distribuição por faixas etárias\n[3]Distribuição por intervalos de nível de glucose no sangue\n[4]Todas as anteriores\n[0]Sair\n "))
    while escolha != 0:
        if escolha == 1:
            tabelas(escolha,path)
        elif escolha == 2:
            tabelas(escolha,path)
        elif escolha == 3:
            tabelas(escolha,path)
        elif escolha == 4:
            tabelas(escolha,path)
        escolha = int(input("\n----------Que distribuição pretende visualizar?----------\n[1]Distribuição por sexo\n[2]Distribuição por faixas etárias\n[3]Distribuição por intervalos de nível de glucose no sangue\n[4]Todas as anteriores\n[0]Sair\n "))
    print("\n----------Saiu do programa----------\n")    
       
main()