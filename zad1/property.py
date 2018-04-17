from string import ascii_lowercase


def propriety_of_expression(expression):
    # & -> and, | -> or, ~ -> not, > -> implikacja, = -> rownowaznosc, ^ -> XOR
    correct_operators = ['&', '|', '~', '>', "=", "^"]
    correct_variables = list(ascii_lowercase) + list(map(str, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    if expression is [] or expression[0] in correct_operators:
        return False
    brackets = 0
    was_char = 0
    was_space = 0
    # sprawdzenie czy mozna usunac spacje
    for i in expression:
        if i in correct_variables:
            if (was_char == 1 and was_space == 1):
                print("Blad")
                return False
            was_char = 1
            was_space = 0
        elif i == " ":
            was_space = 1
        elif i in correct_operators:
            was_space = 0
            was_char = 0
        elif i == "(" or i == ")":
            pass
        else:
            return False
    # ostateczne sprawdzenie poprawnosci
    expression = expression.replace(" ", "")
    last_char = -1  # 0 - variable, 1 - operator, 2 - left bracket, 3 -right bracket
    amount_of_equivalence = 0
    for i in expression:
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
