from string import ascii_lowercase


def changing_to_onp(expression):
    operators = {'&': 1, '|': 1, '>': 0, "=": -1, "^": 1, "(": 0, ")": 0, "~": 1}
    correct_variables = list(ascii_lowercase) + list(map(str, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    out = []
    stack = []
    variable = []
    for i in expression:
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
                # zaleznosc czy jest prawolacznny czy lewostronnie laczny
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
