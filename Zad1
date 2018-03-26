import string


def property_of_sentence(sentence):
    correct_operators = ['&','|','~','>',"=","/"] # wlasne zasady dla ~ ,  = , chyba dla >     / - xor
    correct_variables = list(string.ascii_lowercase)

    recent_position = 1
    what_recent_was = 3   # 0 - variable, 1 - bracket left, 2 - bracket right, 3 - operator
    czy_cos_jest_w_nawiasach = True
    brackets = 0
    space_after_variable = False

    for i in sentence:
        if(i == "~"):
            if(what_recent_was == 1):
                recent_position+=1
                what_recent_was = 3
            elif(recent_position == 1):
                what_recent_was = 3
                recent_position+=1
            else:
                print("zle ~")
                return False
        elif(i == "="):
            if(what_recent_was != 3 and brackets == 0):
                recent_position+=1
                what_recent_was = 3
            else:
                print("zle =")
                return False
        elif(i == "(" and what_recent_was != 0): #1
            czy_cos_jest_w_nawiasach = False
            recent_position+=1
            what_recent_was = 1
            brackets+=1
        elif(i == ")" and what_recent_was != 3 and czy_cos_jest_w_nawiasach is True): #2
            recent_position+=1
            what_recent_was = 2
            brackets-=1
        elif(i in correct_variables): #3
            czy_cos_jest_w_nawiasach = True
            if(what_recent_was == 0):
                if( space_after_variable is False):
                    recent_position+=1
                else:
                    print("zle 3")
                    return False
            elif(what_recent_was != 2):
                recent_position += 1
                what_recent_was = 0
            else:
                print("zle 3.5 ")
                return False
        elif(i in correct_operators and i != "~"): #4
            if(what_recent_was == 1 or what_recent_was == 3):
                print("zle 4")
                return False
            else:
                what_recent_was = 3
                recent_position+=1
        elif(i == " "):
            if(what_recent_was == 0):
                space_after_variable = True
            recent_position+=1
        else: #5
            print("zle 5")
            return False
        if(brackets<0):
            print("zle")
            return False
    if (brackets != 0):
        print("zle 6")
        return False
    for i in range(-1,-len(sentence),-1):
        if(sentence[i] in correct_variables):
            break
        elif(sentence[i] in correct_operators):
            print("Zly koniec")
            return False
    print("DOBRZE")
    return True


def pow(a,b):
    result = 1
    for i in range(0,b):
        result*=a
    return result


def dec_to_bin(number):
    result = 0
    i = 0
    while(number):
        result += pow(10,i)*(number%2)
        number //= 2
        i+=1
    return result


def changing_to_onp(sentence):
    operators = {'&': 1, '|': 1, '~': 0, '>': 0, "=": 3, "/": 1} # ~ traktowac jakosc inaczej ? moze jako czesc zmiennej?
    correct_variables = list(string.ascii_lowercase)
    out = []
    stack = []

    space_after_variable = False
    variable = ""

    for i in sentence:
        print("out ",out)
        print("stack ",stack)
        print("i = ",i,"\n\n")
        print
        if(i in correct_variables):
            variable+=i
        elif(i in operators.keys()):
            if(variable != ""):
                out.append(variable)
                variable = ""
            if(len(stack) == 0):
                stack.append(i)
            else:
                top = stack.pop()
                if(top in operators.keys() and operators[top] < operators[i] and top == ">"):
                    out.append(top)
                    stack.append(i)
                elif(top in operators.keys() and operators[top] <= operators[i] and top != ">"):
                    out.append(top)
                    stack.append(i)
                else:
                    stack.append(top)
                    stack.append(i)

        elif(i == "("):
            stack.append(i)
        elif(i == ")"):
            while(True):
                top = stack.pop()
                if(top == "("):
                    break
                out.append(top)

    if(variable != ""):
        out.append(variable)
        variable = ""
    while(len(stack)):
        out.append(stack.pop())
    print(out)
    #for i in sentence:


def program(sentence):
    all_variables = []
    variable = ""
    correct_variables = list(string.ascii_lowercase)
    for i in sentence:
        if(i in correct_variables):
            variable+=i
        elif(variable != ""):
            all_variables.append(variable)
            variable = ""
    if(variable != ""):
        all_variables.append(variable)
    print(all_variables)
    all_variables = (set(all_variables))
    all_variables = dict.fromkeys(all_variables, 0)
    for i in all_variables.keys():
        all_variables[i] = 0
    print(all_variables)


def shorting_sentence(sentence):
    correct_operators = ['&', '|', '^', '~', '>', "="]  # wlasne zasady dla ~ ,  = , chyba dla >
    correct_variables = list(string.ascii_lowercase)
    all_variables = []



if __name__ == "__main__":
    changing_to_onp("c>a>b&c&d")
    #print(False and False or True)
    #print(dec_to_bin(15))

    """
    if_proper = property_of_sentence("a&(bc|c)&b")
    if(if_proper is False):
        print("Sentense isn't proper.")
        exit(1)
    """
