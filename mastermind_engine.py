from random import randint

hidden_number = []
user_numbers = []
maximum_number_digits = 4

def get_hidden_number():
    while len(hidden_number) < maximum_number_digits:
        random_number = randint(1, 9)
        if random_number not in hidden_number:
            hidden_number.append(random_number)


def get_user_number():
    while len(user_numbers) < maximum_number_digits:
        user_digital = int(input("Введите число от 1 до 9: "))
        if user_digital > 10:
            print("Число больше 10, повторите попытку.")
            continue
        elif user_digital < 1:
            print("Число меньше 1, повторите попытку.")
            continue
        elif user_digital not in user_numbers:
            user_numbers.append(user_digital)
        else:
            print("Вы ввели два одинаковых числа, повторите снова")
            continue


def check_number():
    """Проверяем сколько "Быков" и "Коров" """
    counter_bulls = 0
    counter_cow = 0
    for i in hidden_number:
        if hidden_number[i] == user_numbers
    print("cow", counter_cow, 'bulls', counter_bulls)

get_hidden_number()
print(hidden_number)
get_user_number()
print(user_numbers)
# check_number()

