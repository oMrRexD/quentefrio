from os import system, name
from random import randint

def game():
    clear()
    print('''*******************************
             Bem-vindo(a) ao jogo Quente e Frio!
                              Created by: Victor Mateus
                              *******************************''')
    print('''
Por favor, escolha sua dificuldade:

Easy (30 tentativas)
Normal (15 tentativas)
Hard (10 tentativas)
Very Hard (5 tentativas)
''')
    difficulty = ["easy", "normal", "hard", "very hard"]
    choise = input("Input:").lower()
    if checkDif(difficulty, choise):
        return choise
    else:
        while choise.lower() not in difficulty:
            print("Dificuldade inválida! Digite novamente.")
            choise = input("input:").lower()
            checkDif(difficulty, choise)
            if checkDif(difficulty, choise):
                return choise

def checkDif(difficulty, choise):
    if choise.lower() in difficulty:
        return True

def start(dif):
    print("Dificuldade escolhida!")
    trying = getTrying(dif)
    randomNumber = randint(1, 100)
    match(trying, randomNumber)

def getTrying(dif):
    if dif == "easy":
        return 30
    if dif == "normal":
        return 15
    if dif == "hard":
        return 10
    if dif == "very hard":
        return 5

def match(trying, randomNumber):
    clear()
    print("Beleza, foi sorteado um número aleatório de 1 a 100, agora tente adivinhar o número!")
    attempt = trying
    while attempt != 0:
        if attempt < 10:
            print("* Restam apenas", attempt, "tentativas restantes!")
        result = getPlayerNumber()
        if result == randomNumber:
            print("*********VOCÊ GANHOU!!!*********")
            print("O numero escolhido era:", randomNumber)
            print("\nVocê teve que chutar", trying - attempt + 1, "vezes para achar o número correto, parabéns!\n")
            break
        if result != None:
            print(hotorcold(result, randomNumber))
            attempt = attempt - 1
        if attempt == 0:
            clear()
            print("*********GAME OVER*********")
            print("\nO numero escolhido era:", randomNumber, "\n")
            break
    again()

def getPlayerNumber():
    try:
         number = int(input(":"))
    except:
         print('Digite um número!')
         number = None
    return number

def hotorcold(result, randomNumber):
    calc = result - randomNumber
    if numberCondition(calc, 90, 60):
        return "Tá frio demais (muito longe)"
    if numberCondition(calc, 60, 40):
        return "Tá frio (longe)"
    if numberCondition(calc, 40, 20):
        return "Tá morno (próximo)"
    if numberCondition(calc, 20, 10):
        return "Tá bem morno (bem próximo)"
    if numberCondition(calc, 10, 5):
        return "Tá ficando quente (perto)"
    if numberCondition(calc, 5, 1):
        return "Tá pelandoo (muito perto)"
    if numberCondition(calc, 1, 0):
        return "Tá pegando fogo bixo soccoro (COLADO)"

def numberCondition(var, conditionOne, conditionTwo):
    return var >= conditionOne or var >= -float('inf') and var <= -conditionTwo

def again():
    print('''============================
Você deseja jogar novamente?

Digite Y para sim
Digite N para não
============================''')
    userInput = input("input:").lower()
    while userInput != "y" and userInput != "n":
        print("Digite um argumento correto!")
        userInput = input("input:").lower()
    if userInput == "y":
        start(game())
    if userInput == "n":
        exit()

def clear():
    system('cls' if name=='nt' else 'clear')

start(game())