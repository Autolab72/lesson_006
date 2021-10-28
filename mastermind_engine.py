from random import randint

def get_hidden_number():
    hidden_numbers = []
    while len(hidden_numbers) < 4:
        if len(hidden_numbers) == 0:
            random_number = randint(1, 9)
        else:
            random_number = randint(0, 9)
        if random_number not in hidden_numbers:
            hidden_numbers.append(random_number)
    return hidden_numbers


def check_number(hidden_numbers, user_numbers):
    """Проверяем сколько "Быков" и "Коров" """
    counter_bulls = 0
    counter_cow = 0
    for i in range(hidden_numbers):
        if hidden_numbers[i] == user_numbers[i]:
            counter_bulls += 1
            continue
        elif hidden_numbers[i] in user_numbers:
            counter_cow += 1
            continue
    output = {
        "cows": counter_cow,
        "bulls": counter_bulls,
    }
    return output
