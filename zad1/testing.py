import string
from collections import OrderedDict
import numpy
import sys


def propriety_of_sentence(sentence):
    # & -> and, | -> or, ~ -> not, > -> implikacja, = -> rownowaznosc, ^ -> XOR
    correct_operators = ['&', '|', '~', '>', "=", "^"]
    correct_variables = list(string.ascii_lowercase) + list(map(str, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    brackets = 0
    was_char = 0
    was_space = 0
    # sprawdzenie czy mozna usunac spacje
    for i in sentence:
        if i in correct_variables:
            if (was_char == 1 and was_space == 1):
                print("Blad")
                return False
            was_char = 1
            was_space = 0
        elif i == " ":
            was_space = 1
        else:
            was_space = 0
            was_char = 0
    # ostateczne sprawdzenie poprawnosci
    sentence = sentence.replace(" ", "")
    last_char = -1  # 0 - variable, 1 - operator, 2 - left bracket, 3 -right bracket
    amount_of_equivalence = 0
    for i in sentence:
        if (i == "("):
            if (last_char == 0 or last_char == 3):
                print("zle nawiasy")
                return False
            brackets += 1
            last_char = 2

        elif (i == ")"):
            if (last_char == 1 or last_char == 2):
                print("zle nawiasy")
                return False
            brackets -= 1
            last_char = 3
        elif (i == "="):
            if (amount_of_equivalence == 1 or brackets != 0 or last_char == 1):
                print("zla rownosc")
                return False
            amount_of_equivalence = 1
            last_char = 1
        elif (i in correct_variables):
            if (last_char == 3):
                print("zmienna w zlym miejscu")
                return False
            last_char = 0
            pass
        elif (i == "~"):
            if (last_char == 0 or last_char == 1):
                print("zle zaprzeczenie")
                return False
            last_char = 1
        elif (i in correct_operators):
            if (last_char == 1):
                print("dwa operatory obok siebie")
                return False
            last_char = 1
        if (brackets < 0):
            print("zle nawiasy")
            return False

    if brackets != 0:
        print("zle nawiasy")
        return False
    if last_char == 1:
        print("na koncu jest operator")
        return False
    return True


def pow(a, b):
    result = 1
    for i in range(0, b):
        result *= a
    return result


def dec_to_bin(number):
    result = 0
    i = 0
    while number:
        result += pow(10, i) * (number % 2)
        number //= 2
        i += 1
    return result


def changing_to_onp(sentence):
    operators = {'&': 1, '|': 1, '>': 0, "=": 0, "^": 1, "(": 0, ")": 0, "~": 1}
    correct_variables = list(string.ascii_lowercase) + list(map(str, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    out = []
    stack = []

    variable = []
    for i in sentence:
        if (i in correct_variables):
            variable.append(i)
        elif (i == "("):
            stack.append(i)
        elif (i == ")"):
            if (variable != ""):
                out.append(("").join(variable))
                variable = []
            while (True):
                top = stack.pop()
                if (top == "("):
                    break
                out.append(top)
        elif (i in operators.keys()):
            if (variable != []):
                out.append(("").join(variable))
                variable = []
            if (len(stack) == 0):
                stack.append(i)
            else:
                top = stack.pop()
                if (i != ">"):
                    while (True):
                        if (top in operators and operators[i] <= operators[top]):
                            out.append(top)
                            if (len(stack)):
                                top = stack.pop()
                            else:
                                stack.append(i)
                                break

                        else:
                            stack.append(top)
                            stack.append(i)
                            break
                else:
                    while (True):
                        if (top in operators and operators[i] < operators[top]):
                            out.append(top)
                            if (len(stack)):
                                top = stack.pop()
                            else:
                                stack.append(i)
                                break

                        else:
                            stack.append(top)
                            stack.append(i)
                            break
    if (variable != []):
        out.append(("").join(variable))
    while (len(stack)):
        out.append(stack.pop())
    print("ONP is ", out)
    return out


# check onp for chosen variables if it is true or false
def calculate_onp_with_chosen_variables(sentence, variables):
    stack = []
    for i in sentence:
        if (i == "&"):
            Top = stack.pop()
            Lower = stack.pop()
            stack.append(Top and Lower)
        elif (i == "|"):
            Top = stack.pop()
            Lower = stack.pop()
            stack.append(Top or Lower)
        elif (i == "^"):
            Top = stack.pop()
            Lower = stack.pop()
            stack.append(bool(Top) ^ bool(Lower))
        elif (i == "~"):
            Top = stack.pop()
            stack.append(not Top)
        elif (i == ">"):
            Top = stack.pop()
            Lower = stack.pop()
            stack.append((not Lower) or Top)
        elif (i == "="):
            Top = stack.pop()
            Lower = stack.pop()
            stack.append(Lower == Top)
        else:
            stack.append(variables[i])

    return stack.pop()


# ostatni krok algorytmu w ktorym wybiera sie koncowy wynik przy pomocy tablicy
def sec_part_of_Qalgorithm(almost_done, arguments, sigma):
    # otrzymanie pojedynczych wartosci np 1x10
    tmp = set()
    for i in almost_done:
        if almost_done[i] in tmp:
            continue
        tmp.add(almost_done[i])
    list_of_almost_done = []
    for i in tmp:
        for j in almost_done:
            if (i == almost_done[j]):
                list_of_almost_done.append(j)
                break
    # tworzenie tablicy w celu uproszczenia wyrazenia
    table = numpy.zeros((len(list_of_almost_done), len(sigma)))
    for index_i, i in enumerate(list_of_almost_done):
        tmp = i.split(",")
        for j in sigma:
            for index_k, k in enumerate(tmp):
                if (str(j) == k):
                    table[index_i][sigma.index(j)] = 1
    # wybieranie koniecznych wyrazow przy pomocy tablicy np 0,4,1,5
    from_table = set()
    for i in range(len(sigma)):
        amount_of_ones = 0
        for j in range(len(list_of_almost_done)):
            if (table[j][i] == 1):
                amount_of_ones += 1
        if (amount_of_ones == 1):
            # sprawdzanie dla ktorego wyraznia np 1x01 jest w kolumnie jeden X
            for j in range(len(list_of_almost_done)):
                if (table[j][i] == 1):
                    from_table.add(list_of_almost_done[j])

    # znalezenie odpowiadajacej wartosci np 0,4,1,5 -> 0x0
    last_values = set()
    for i in from_table:
        last_values.add(almost_done[i])
    # budowanie ostatecznego wyniku, wynik jest w roznej kolejnosci bo set nie ma kolejnosci
    out = []
    for index, i in enumerate(last_values):
        for j in range(len(i)):
            if (i[j] == "1"):
                if (j < len(i) and out != [] and out[len(out) - 1] != "|"):
                    out.append("&")
                out.append(list(arguments.keys())[j])
            elif (i[j] == "0"):
                if (j < len(i) and out != [] and out[len(out) - 1] != "|"):
                    out.append("&")
                out.append("(~" + list(arguments.keys())[j] + ")")
        if (index < len(last_values) - 1):
            out.append("|")

    print("out ", ("").join(out))


def calculate_sigma(onp):  # wylicza sigme
    correct_variables = list(string.ascii_lowercase) + list(map(str, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
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
        if (calculate_onp_with_chosen_variables(onp, arguments)):
            sigma.append(i)
    if (len(sigma) == 0):
        print("Always false.")
        exit(0)
    elif (len(sigma) == max_number):
        print("Always true.")
        exit(0)
    return [sigma, arguments]


def dec_to_bin_string(number, size):
    out = []
    while number:
        out.append(str(number % 2))
        number = int(number / 2)

    while size - len(out):
        out.append("0")
    out = ("").join(out[::-1])
    return out


def number_of_ones(number):
    out = 0
    for i in number:
        if i == "1":
            out += 1
    return out


def if_diffrence_in_one_char(number1, number2):
    i = len(number1) - 1
    amount_of_differs = 0
    while (i > -1):
        if (number1[i] != number2[i]):
            if not (amount_of_differs):
                amount_of_differs = 1
            else:
                return False
        i -= 1
    if (amount_of_differs == 0):
        return False
    return True


# connect two variables e.g 11x0 and 10x0 => 1xx0
def connection(number1, number2):
    out = []
    i = len(number1) - 1
    while (i > -1):
        if (number1[i] != number2[i]):
            out.append("x")
        else:
            out.append(number1[i])
        i -= 1
    return ("").join(out[::-1])


# compare two variable e.g (0,1) (2,3)
def comparator(variable1, variable2):
    variable1 = variable1.split(",")
    variable2 = variable2.split(",")
    length = max(len(variable1), len(variable2))
    for i in range(0, length):
        if (int(variable1[i]) < int(variable2[i])):
            return -1
        elif (int(variable1[i]) > int(variable2[i])):
            return 1
    return 0


def qs(list):
    lesser = []
    greater = []
    equal = []
    if (len(list) > 1):
        pivot = list[0]
        for i in list:
            if (comparator(i, pivot) == -1):
                lesser.append(i)
            elif (comparator(i, pivot) == 1):
                greater.append(i)
            else:
                equal.append(i)
        return qs(lesser) + equal + qs(greater)
    else:
        return list


def sort_keys(out):
    keys = list(out.keys())
    sorted_keys = qs(keys)
    return sorted_keys


def q_algorithm(sigma, arguments):
    #print("sigma = ", sigma)
    tmp = OrderedDict()
    for i in sigma:
        tmp[str(i)] = dec_to_bin_string(i, len(arguments))
    new_list = tmp
    lastOut = OrderedDict()  # koncowy wynik
    while (True):
        keys = []
        used_keys = set()
        for i in new_list.keys():
            keys.append(i)
        out = OrderedDict()
        for index, i in enumerate(keys):
            for j in keys[index + 1:]:
                # print(i," ",new_list[i]," ",j," ",new_list[j])
                if (if_diffrence_in_one_char(new_list[i], new_list[j])):
                    used_keys.add(i)
                    used_keys.add(j)
                    connection1 = connection(new_list[i], new_list[j])
                    for m in out:
                        if (out[m] == connection1):
                            continue
                    out[i + "," + j] = connection(new_list[i], new_list[j])
        not_used_keys = set(new_list.keys()).difference(used_keys)
        for i in not_used_keys:
            lastOut[i] = new_list[i]
        sorted_keys = sort_keys(out)
        tmp = OrderedDict()
        for i in sorted_keys:
            tmp[i] = out[i]
        if not (bool(out)):
            for l in new_list.keys():
                lastOut[l] = new_list[l]
            return lastOut
        new_list = tmp


if __name__ == "__main__":
    # sentence = " ".join(sys.argv[1:])
    sentence = "b & c > d"
    print(sentence)
    if propriety_of_sentence(sentence):
        ONP = changing_to_onp(sentence)
        sigma_and_arguments = calculate_sigma(ONP)
        after_first_part_q_algorithm = q_algorithm(sigma_and_arguments[0], sigma_and_arguments[1])
        sec_part_of_Qalgorithm(after_first_part_q_algorithm, sigma_and_arguments[1], sigma_and_arguments[0])
