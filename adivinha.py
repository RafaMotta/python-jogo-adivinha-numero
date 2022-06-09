import random
import math

menor = int(input("Digite o menor número: "))
maior = int(input("Digite o maior número: "))

x = random.randint(menor, maior)
print("Você tem apenas ", round(math.log(maior-menor+1, 2)), "chances de acertar!")

count = 0

while count < math.log(maior - menor + 1, 2):
    count += 1

    guess = int(input("Escolha um número: "))

    if(x == guess):
        print("Parabéns, você acertou na ", count, "° tentativa")
        break
    elif(x > guess):
        print("Valor é muito baixo!")
    elif(x < guess):
        print("Valor é muito alto!")

if(count >= math.log(maior - menor + 1, 2)):
    print("O número é ", x)
    print("Mais sorte da próxima vez!")

    
