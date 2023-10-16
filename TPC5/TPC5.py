#cinema = sala e sala tem lugares,vendidos e filme


def listar (cinema):
    print("-------Filmes-------")
    for p in cinema:
        print("\n",p[2])

def disponivel (cinema,filme,lugar):
    for p in cinema:
        if p[2] == filme:
            for j in p[1]:
                if j == lugar:
                    return False
    return True

def inserirSala (cinema,sala):
    if len(cinema) == 0:
        cinema.append(sala)
    else:
        for s in cinema:
            if s != sala:
                cinema += sala
            else:
                print("A sala ja existe!")

    return cinema

def vendebilhete (cinema,filme,lugar):
    for p in cinema:
        if p[2] == filme:
            if lugar in p[1]:
                print("Não disponivel!")
            else:
                p[1].append(lugar)
    return cinema

def listardisponibilidades(cinema):
    for p in cinema:
        print(p[2] , ' - ' , p[0]-len(p[1]), ' lugares disponiveis.' )
    
cinema1 = []


def main():
    escolha =int(input(
                "Bem vindo ao gerenciador do cinema. O que gostaria de fazer?\n"
                "[1]Listar cinema\n"
                "[2]Verificar disponibilidade\n"
                "[3]Vender bilhete\n"
                "[4]Listar disponibilidade\n"
                "[5]Inserir nova sala\n"
                "[0]Sair\n"
                   ))
    
    while escolha != 0:
        if escolha == 1:
            cinema = input("Que cinema prentede listar? ")
            listar(cinema)
        if escolha == 2:
            cinema = input("Que cinema pretende verificar? ")
            filme = input("Que filme pretende verificar? ")
            lugar = input("Que lugar pretende verificar? ")
            disponivel(cinema,filme,lugar)
        if escolha == 3:
            cinema = input("Que cinema para a venda do bilhete? ")
            filme = input("Que filme para a venda do bilhete? ")
            lugar = input("Que lugar para a venda do bilhete? ")
            vendebilhete(cinema,filme,lugar)
        if escolha == 4:
            cinema = input("Que cinema deseja verificar a disponibilidade? ")
            listardisponibilidades(cinema)
        if escolha == 5:
            cinema = input("Que cinema deseja inserir? ")
            sala = input("Que sala deseja inserir? ")
            inserirSala(cinema,sala)
        
        escolha =int(input(
                "Bem vindo ao gerenciador do cinema. O que gostaria de fazer?\n"
                "[1]Listar cinema\n"
                "[2]Verificar disponibilidade\n"
                "[3]Vender bilhete\n"
                "[4]Listar disponibilidade\n"
                "[5]Inserir nova sala\n"
                "[0]Sair\n"
                   ))    
    print("Saiu do programa.")


main()
            











