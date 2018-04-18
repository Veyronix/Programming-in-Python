from property import propriety_of_expression
from onp import changing_to_onp
from sigma import calculate_sigma
from quine_mccluskey import quine_mcc_algorithm
from sys import argv


def simplify_boolean_expression(expression):
    if not(propriety_of_expression(expression)):
        print("Not proper expression")
        return
    onp = changing_to_onp(expression)
    [sigma,arguments] = calculate_sigma(onp)
    return quine_mcc_algorithm(sigma, arguments)


if __name__ == "__main__":
    # simplify_boolean_expression(" ".join(argv[1:]))
    print(simplify_boolean_expression("a & b > 0"))
