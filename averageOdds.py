def averageOdds(numbers: list[int]) -> float:
    total = 0
    count = 0

    for n in numbers:
        if n % 2 != 0:
            total += n
            count += 1
    if count == 0:
        return -1
    
    return total / count

# entrada do usuario:


user_input = input("Digite os numeros da lista")
numbers =  list(map(int, user_input.split()))
result = averageOdds(numbers)
if result == -1:
    print("Não há números ímpares na lista.")
else:
    print(f"Média dos números impares: {result}")