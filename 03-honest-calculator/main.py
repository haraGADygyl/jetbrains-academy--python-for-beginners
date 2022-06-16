import sys

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"


def check(value1, value2, value3):
    message = ''
    if is_one_digit(value1) and is_one_digit(value2):
        message += msg_6
    if (value1 == 1 or value2 == 1) and value3 == '*':
        message += msg_7
    if (value1 == 0 or value2 == 0) and (value3 == '*' or value3 == '+' or value3 == '-'):
        message += msg_8
    if message != '':
        message = msg_9 + message

    print(message)


def is_one_digit(value):
    if -10 < int(value) < 10 and value.is_integer():
        return True
    return False


memory = 0
while True:
    print(msg_0)
    calc = input()
    x, operand, y = calc.split()

    if x == 'M':
        x = memory

    if y == 'M':
        y = memory

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue

    if operand not in ['+', '-', '*', '/']:
        print(msg_2)
        continue
    check(x, y, operand)

    if operand == '/' and int(y) == 0:
        print(msg_3)
        continue

    result = 0
    if operand == '+':
        result = x + y
    elif operand == '-':
        result = x - y
    elif operand == '*':
        result = x * y
    elif operand == '/' and y != 0:
        result = x / y

    print(result)

    while True:
        print(msg_4)
        answer = input()

        if answer == 'y':
            if is_one_digit(result):
                message_index = 10

                while True:
                    print(eval(f'msg_{message_index}'))
                    answer3 = input()

                    if answer3 == 'y':
                        if message_index < 12:
                            message_index += 1
                            continue
                        else:
                            memory = result
                            break
                    if answer3 == 'n':
                        break
                    else:
                        continue
            else:
                memory = result

        elif answer == 'n':
            pass
        else:
            continue

        while True:
            print(msg_5)
            answer2 = input()

            if answer2 == 'y':
                break
            else:
                if answer2 == 'n':
                    sys.exit()
        break
