"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

# repeat forever:
def calculator_two():
#     read input
    string = input("Please enter a operation and numbers:")
    #     tokenize input
   ##print (string)
    token = string.split(' ')
    ###print (token)
    #         ##if the first token is "q":
    #print (token[0])
    #print (int(token[1]) + int(token[2]))
    if token[0] == "q":
    #             quit
        quit()
    #         else:
    else:
        if token[0] == "+":
            return add(int(token[1]), int(token[2]))
    #             (decide which math function to call based on first token)
    #             if the first token is 'pow':
    #                   call the power function with the other two tokens
print (calculator_two())
# Replace this with your code
