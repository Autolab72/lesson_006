from random import randint

hidden_number = []
user_numbers = []
def get_hidden_number():
    print("Число загаданно, приступайте...")
    for i in range(4):
        hidden_number.append(randint(1, 9))


def get_number():
    global user_numbers
    user_numbers = []
    for i in range(len(hidden_number)):
        input_number = int(input(f"Введите {i}е число от 1 до 9: "))
        if input_number < 0 :
            print("Это число меньше 0, введите целое число от 1 до 9")
            continue
        elif input_number > 9 :
            print("Это число больше 9 введите целое число от 1 до 9")
            continue
        else:
            user_numbers.append(i)


def check_number():
    pass

