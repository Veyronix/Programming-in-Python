from string import ascii_lowercase
from collections import OrderedDict


def calculate_sigma(onp):  # wylicza sigme
    correct_variables = list(ascii_lowercase) + list(map(str, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    arguments = OrderedDict()
    sigma = []
    for i in onp:
        if (i[0] not in correct_variables):
            pass
        else:

            arguments[i] = True
            arguments.move_to_end(i, last=False)

    max_number = pow(2, len(arguments))
    for i in range(max_number):
        tmp = i
        for j, value in list(arguments.items())[::-1]:
            #pierwsze dwa warunki sa po to ze uznajemy 1 za True, a 0 za False
            # if(j == "1"):
            #     arguments[j] = True
            # elif(j == "0"):
            #     arguments[j] = False
            if (tmp % 2):
                arguments[j] = True
            else:
                arguments[j] = False
            tmp = int(tmp / 2)
        if (calculate_for_chosen_variables(onp, arguments)):
            sigma.append(i)
    if (len(sigma) == 0):
        print("Always false.")
        exit(0)
    elif (len(sigma) == max_number):
        print("Always true.")
        exit(0)
    return [sigma, list(arguments.keys())]


def calculate_for_chosen_variables(expression, variables):
    stack = []
    for i in expression:
        if (i == "&"):
            top = stack.pop()
            lower = stack.pop()
            stack.append(top and lower)
        elif (i == "|"):
            top = stack.pop()
            lower = stack.pop()
            stack.append(top or lower)
        elif (i == "^"):
            top = stack.pop()
            lower = stack.pop()
            stack.append(bool(top) ^ bool(lower))
        elif (i == "~"):
            top = stack.pop()
            stack.append(not top)
        elif (i == ">"):
            top = stack.pop()
            lower = stack.pop()
            stack.append((not lower) or top)
        elif (i == "="):
            top = stack.pop()
            lower = stack.pop()
            stack.append(lower == top)
        else:
            stack.append(variables[i])

    return stack.pop()
