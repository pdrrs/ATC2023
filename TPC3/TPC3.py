import random

def menu():
    menu_select = int(input("Hello!\nWhat mode would you like to play?\n[1]You try to guess\n[2]Computer tries to guess "))
    return menu_select

max = 0
def num_menu ():
    max = int(input("What number would you like to set has max? "))
    return max


def game_user_guess (max):
    nums = list(range(0,max+1))
    correct_num = random.choice(nums)
    guess = int(input("What number would you like to guess? "))
    numb_of_guesses = 1
    while guess != correct_num:
        if guess < correct_num:
            print("Your guess was lower then the answer!")
        elif guess > correct_num:
            print("Your guess was higher then the answer!")
        else:
            break
        guess = int(input("Try again! "))
        numb_of_guesses += 1
    print(str(correct_num) + " is the right answer! It took you " + str(numb_of_guesses) + " guesses!")

def game_PC_guess (max):
    nums = list(range(0,max+1))
    guess = random.choice(nums)
    numb_of_guesses = 1
    user_input = int(input("PC guessed: " + str(guess) + ", is your number: \n[1]Higher\n[2]Lower\n[3]This one! "))
    while user_input != 3:
        if user_input == 1:
            del nums[0:nums.index(guess)+1]
        elif user_input == 2:
            del nums[nums.index(guess):(len(nums))]
        guess = int(random.choice(nums))
        user_input = int(input("PC guessed: " + str(guess) + ", is your number: \n[1]Higher\n[2]Lower\n[3]Correct "))
        numb_of_guesses += 1
    print("The PC guesses your number in " + str(numb_of_guesses) + " tries!")

def main():
    choice = menu()
    if choice == 1:
        game_user_guess(num_menu())    
    elif choice == 2:
        game_PC_guess(num_menu())
    else:
        print("Insert a valid option!")

main()


"""Conclusão sobre o número de tentativas:
    O número de tentativas para o utilizador acertar no numero depende do metodo, 
    mas utilizando o metodo de começar pela valor medio e ir eliminando,sempre pela metade, para max = 100 foi em media 6 tentativas, 
    para max = 1000 o número de tentativas saltou para por volta de 10 tentativas. Para o computador adivinhar o numero,
    admito que nao implementei o melhor algoritmo possivel, uma vez que utiliza random, então não consigo muito bem dizer um número medio de tentativas para este,
    mas nos meus testes demorou sempre entre 10 e 15 tentativas"""