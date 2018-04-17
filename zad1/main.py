import string
from collections import OrderedDict
import operator

#chyba dziala :)
def proper_sentence(sentence):
    correct_operators = ['&', '|', '~', '>', "=", "/"]
    correct_variables = list(string.ascii_lowercase)
    brackets = 0
    last_char = 0 # 0 - variable, 1 - operator, 2 - left bracket, 3 -right bracket
    was_char = 0
    was_space = 0
    for i in sentence:
        if( i in correct_variables):
            if(was_char == 1 and was_space == 1):
                print("Blad")
                exit(1)
            was_char = 1
            was_space = 0
        elif(i == " "):
            was_space = 1
        else:
            was_space = 0
            was_char = 0

    sentence = sentence.replace(" ","")
    print(sentence)
    last_char = -1  # 0 - variable, 1 - operator, 2 - left bracket, 3 -right bracket
    amount_of_equivalence = 0
    for i in sentence:
        if(i == "("):
            if(last_char == 0 or last_char == 3):
                print("zle nawiasy")
                exit(1)
            brackets+=1
            last_char = 2

        elif(i == ")"):
            if(last_char == 1 or last_char == 2):
                print("zle nawiasy")
                exit(1)
            brackets-=1
            last_char = 3
        elif(i == "="):
            if(amount_of_equivalence == 1 or brackets != 0 or last_char == 1):
                print("zla rownosc")
                exit(1)
            amount_of_equivalence=1
            last_char = 1
        elif(i in correct_variables):
            if(last_char == 3):
                print("zmienna w zlym miejscu")
                exit(1)
            last_char = 0
            pass
        elif(i == "~"):
            if(last_char == 0 or last_char == 1):
                print("zle zaprzeczenie")
                exit(1)
            last_char = 1
        elif(i in correct_operators):
            if(last_char == 1):
                print("dwa operatory obok siebie")
                exit(1)
            last_char = 1
        if(brackets<0):
            print("zle nawiasy")
            exit(1)

    if(brackets!=0):
        print("zle nawiasy")
        exit(1)
    return True

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


def pow(a, b):
    result = 1
    for i in range(0,b):
        result *= a
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
    operators = {'&': 2, '|': 2, '>': 1, "=": 0, "^": 2, "(": -1, "~":2}
    correct_variables = list(string.ascii_lowercase)
    out = []
    stack = []

    variable = ""

    for i in sentence:
        '''
        print("out ",out)
        print("stack ",stack)
        print("variable ",variable)
        print("i = ", i, "\n\n")
        '''
        if(i in correct_variables):
            variable+=i
        elif(i == "~"):
            stack.append(i)
        elif(i == "("):
            stack.append(i)
        elif(i == ")"):
            if (variable != ""):
                out.append(variable)
                variable = ""
            while(True):
                top = stack.pop()
                if(top == "("):
                    break
                out.append(top)
        elif(i in operators.keys()):
            if(variable != ""):
                out.append(variable)
                variable = ""
            if(len(stack) == 0):
                stack.append(i)
            else:
                top = stack.pop()
                count = 0
                if(i != ">"):
                    while(True):
                        if(top in operators and operators[i]<=operators[top]):
                            out.append(top)
                            if(len(stack)):
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


    if(variable != ""):
        out.append(variable)
        variable = ""
    while(len(stack)):
        out.append(stack.pop())
    print("ONP is ",out)
    return out


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


def calculate_sigma(ond):
    correct_variables = list(string.ascii_lowercase)
    arguments = []
    sigma = []
    for i in ond:
        if(i[0] not in correct_variables):
            pass
        else:
            arguments.append(i)
    arguments = set(arguments)
    arguments = dict.fromkeys(arguments,True)
    actual_number = 0
    max_number = pow(2,len(arguments))
    for i in range(max_number):
        tmp = i
        for j,value in arguments.items():
            if(tmp%2):
                arguments[j]=True # moze wkladac True/False?
            else:
                arguments[j]=False
            tmp = int(tmp/2)
        #print("All arguments ", arguments)
        if(calculate_onp(ond,arguments)):
            sigma.append(i)
    Qalgorytm(sigma,arguments)

def dec_to_bin_string(number,size):
    out = ""
    while(number):
        out += str(number%2)
        number = int(number/2)

    while(size-len(out)):
        out += "0"
    out = out[::-1]
    return out
    #print(out)


def number_of_ones(number):
    out = 0
    for i in number:
        if i == "1":
            out +=1
    return out

def Qalgorytm(sigma,arguments):
    print(sigma)
    print(len(arguments))
    print(arguments)
    test = OrderedDict()
    for i in sigma:
        test[str(i)]=dec_to_bin_string(i,len(arguments))

    print(test)
    ###
    new_list = OrderedDict()
    for i in range(len(arguments)+1):
        for j in test:
            if(number_of_ones(test[j]) == i):
                new_list[j] = test[j]
                new_list.move_to_end(j, last=False)
    ## jako osobna funkcja?
   # print(new_list.keys())
    i = 1
    while(i):
        tmp = next_step(new_list)
        if(len(tmp.items()) == len(new_list.items())):
            print("hej")
            break
        new_list = tmp
        i-=1

    pass


def if_diffrence_in_one_char(number1,number2):
    i = len(number1)-1
    amount_of_differs = 0
    while(i>-1):
        if(number1[i] != number2[i]):
            if not (amount_of_differs):
                amount_of_differs = 1
            else:
                return False
        i-=1
    if(amount_of_differs == 0):
        return False
    return True


def connection(number1,number2):
    out = ""
    i = len(number1) - 1
    while(i>-1):
        if(number1[i] != number2[i]):
            out += "x"
        else:
            out += number1[i]
        i-=1
    return out[::-1]


def next_step(table):
    pass
    #wkladac odrazu dany wiersz i po przegladnieciu z innymi rekordami usunac(jesli z kims ise polaczyl lub zostawic w liscie
    out = OrderedDict()
    used_keys = []
    new_table = []
    for i in table.keys():
        new_table.append(i)
    new_table = new_table[::-1]
    print("table ",new_table)
    for index,i in enumerate(new_table):
        used_keys =[]
        out[i] = table[i]
        for j in new_table[index+1:]:

            if(if_diffrence_in_one_char(table[i],table[j])):
                used_keys = True
                used_keys.add(i)
                used_keys.add(j)
                #print(i,j,table[i],table[j])
                out[i +","+ j] = connection(table[i],table[j])
                #nie usuwa tego z ktorym sie laczy
        while ( used_keys):
            del out[i]

    print(out)

    new_list = OrderedDict()
    for i in range(len(out.items()) + 1):
        for j in out:
            if (number_of_ones(out[j]) == i):
                new_list[j] = out[j]
        new_list.move_to_end(j, last=False)
    print("po sortowaniu ",new_list,"\n")
    return new_list

def next_step2(table):
    out = OrderedDict()
    used_keys = set()
    new_table = []
    for i in table.keys():
        new_table.append(i)
    new_table = new_table[::-1]
    #print(new_table)
    for index,i in enumerate(new_table):
        for j in new_table[index+1:]:
            if(if_diffrence_in_one_char(table[i],table[j])):
                used_keys.add(i)
                used_keys.add(j)
                #print(i,j,table[i],table[j])
                out[str(i) +","+ str(j)] = connection(table[i],table[j])
    for i in (set(new_table) - (used_keys)):
        out[str(i)] = table[i]
    print(out)

    new_list = OrderedDict()
    for i in range(len(out.items()) + 1):
        for j in out:
            if (number_of_ones(out[j]) == i):
                new_list[j] = out[j]
                new_list.move_to_end(j, last=False)
    print("po sortowaniu ",new_list,"\n")
    return new_list




def calculate_onp(sentence,variables):
    stack = []
    i = 0
    for i in sentence:
        if( i == "&"):
            Top = stack.pop()
            Lower = stack.pop()
            stack.append(Top and Lower)
        elif(i == "|"):
            Top = stack.pop()
            Lower = stack.pop()
            stack.append(Top or Lower)
        elif(i == "^"):
            Top = stack.pop()
            Lower = stack.pop()
            stack.append(bool(Top) ^ bool(Lower))
        elif(i == "~"):
            Top = stack.pop()
            stack.append(not Top)
        elif(i == ">"):
            Top = stack.pop()
            Lower = stack.pop()
            stack.append((not Lower) or Top)
        elif(i == "="):
            Top = stack.pop()
            Lower = stack.pop()
            stack.append(Lower == Top)
        else:
            stack.append(variables[i])

    return stack.pop()


if __name__ == "__main__":
    print(if_diffrence_in_one_char("1010","1110"))
    proper_sentence("a&b| c = (d >e)")
    #dec_to_bin_string(10)
    onp = changing_to_onp("a&b| c = e|f")
    #onp = changing_to_onp("(a&ba)>(~c)|d=((~d&b)|a)")
    calculate_sigma(onp)
    #print(False and False or True)
    #print(dec_to_bin(15))
