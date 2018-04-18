from collections import OrderedDict
from numpy import zeros


def if_diffrence_in_one_char(number1, number2):
    i = len(number1) - 1
    amount_of_differs = 0
    while (i > -1):
        if (number1[i] != number2[i]):
            if not amount_of_differs:
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


def dec_to_bin_string(number, size):
    out = []
    while number:
        out.append(str(number % 2))
        number = int(number / 2)

    while size - len(out):
        out.append("0")
    out = ("").join(out[::-1])
    return out


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


#redukowanie wartosci do najmniejszej ilosci
def first_part_of_algorithm(sigma, len_of_arguments):
    tmp = OrderedDict()
    for i in sigma:
        tmp[str(i)] = dec_to_bin_string(i, len_of_arguments)
    sigma_with_bin_version = tmp
    lastOut = OrderedDict()  # koncowy wynik
    while (True):
        keys = []
        used_keys = set()
        for i in sigma_with_bin_version.keys():
            keys.append(i)
        out = OrderedDict()
        # porownywanie wartosci z kazda inna 'wieksza' wartoscia
        for index, i in enumerate(keys):
            for j in keys[index + 1:]:
                if (if_diffrence_in_one_char(sigma_with_bin_version[i], sigma_with_bin_version[j])):
                    used_keys.add(i)
                    used_keys.add(j)
                    new_connection= connection(sigma_with_bin_version[i], sigma_with_bin_version[j])
                    for m in out:
                        if (out[m] == new_connection):
                            continue
                    out[i + "," + j] = connection(sigma_with_bin_version[i], sigma_with_bin_version[j])
        not_used_keys = set(sigma_with_bin_version.keys()).difference(used_keys)
        # dodawanie nieuzytych wartosci do wynikowej mapy
        for i in not_used_keys:
            lastOut[i] = sigma_with_bin_version[i]
        sorted_keys = sort_keys(out)
        # sortowanie nowych wartosci i wartosci ktore uzylismy w laczeniu ostatnio
        tmp = OrderedDict()
        for i in sorted_keys:
            tmp[i] = out[i]
        if not (bool(out)): #jesli nie bylo zadnych zmian
            for l in sigma_with_bin_version.keys():
                lastOut[l] = sigma_with_bin_version[l]
            return lastOut
        sigma_with_bin_version = tmp

# ostatni krok algorytmu w ktorym wybiera sie koncowy wynik przy pomocy tablicy
def sec_part_of_algorithm(connected_values_of_sigma, arguments, sigma):
    # otrzymanie pojedynczych wartosci np 1x10
    singular_values = set()
    for i in connected_values_of_sigma:
        if connected_values_of_sigma[i] in singular_values:
            continue
        singular_values.add(connected_values_of_sigma[i])
    code_of_values = []
    # otrzymanie wartosci np xx0 -> 0,4,2,6
    for i in singular_values:
        for j in connected_values_of_sigma:
            if (i == connected_values_of_sigma[j]):
                code_of_values.append(j)
                break
    # tworzenie tablicy w celu uproszczenia wyrazenia
    table = zeros((len(code_of_values), len(sigma)))
    for index_i, i in enumerate(code_of_values):
        # connected_values np 1,3 -> ['1','3']
        singular_values = i.split(",")
        for j in sigma:
            for k in singular_values:
                if (str(j) == k):
                    table[index_i][sigma.index(j)] = 1
    # wybieranie koniecznych wyrazow przy pomocy tablicy np 0,4,1,5
    from_table = set()
    for i in range(len(sigma)):
        amount_of_ones = 0
        for j in range(len(code_of_values)):
            if (table[j][i] == 1):
                amount_of_ones += 1
        if (amount_of_ones == 1):
            # sprawdzanie dla ktorego wyraznia np 1x01 jest w kolumnie jeden X
            for j in range(len(code_of_values)):
                if (table[j][i] == 1):
                    from_table.add(code_of_values[j])

    # znalezenie odpowiadajacej wartosci np 0,4,1,5 -> 0x0
    last_values = set()
    for i in from_table:
        last_values.add(connected_values_of_sigma[i])
    # budowanie ostatecznego wyniku, wynik jest w roznej kolejnosci bo set nie ma kolejnosci
    out = []
    for index, i in enumerate(last_values):
        for j in range(len(i)):
            if (i[j] == "1"):
                if (j < len(i) and out != [] and out[len(out) - 1] != "|"):
                    out.append("&")
                out.append(arguments[j])
            elif (i[j] == "0"):
                if (j < len(i) and out != [] and out[len(out) - 1] != "|"):
                    out.append("&")
                out.append("(~" + arguments[j] + ")")
        if (index < len(last_values) - 1):
            out.append("|")

    return ("").join(out)


def quine_mcc_algorithm(sigma,arguments):
    return sec_part_of_algorithm(first_part_of_algorithm(sigma,len(arguments)),arguments,sigma)
