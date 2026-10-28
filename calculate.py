def main():
    total = 0
    user_input = input("Calculate: ").strip().lower()
    #while input not quit
    i = 0
    while user_input != "quit":
        # if clear reset total 
        if user_input == "clear":
            total = 0
            print("calculator cleared!")
            user_input = input("Calculate: ").strip().lower()
        #figure out if the string is a complete calculation
        elif not user_input[len(user_input) - 1].isnumeric():
            print("Invalid calculation, please try again.")
            user_input = input("Calculate: ").strip().lower()
        elif (":" <= user_input[i] <= "~"):
            print("Invalid calculation, please try again.")
            user_input = input("Calculate: ").strip().lower()
        #division by 0
        #elif ValueError:
          #  print("undefined")
        # legit calculation, continue to calculate
        else:
            answer = calculate(user_input)
            print(answer)
            user_input = input()
        i += 1
    if user_input == "quit":
        print("Goodbye, thank you for using my calculator!")

def calculate(input):

    parse(input)
# perhaps use min/ max for operand ascii values to determine which comes first
def parse(input): #want to parse the string, separating or appending operands to their own list and numerics to another and return the different values appropriately so they can be used in calculation
    total = 0 #integer total
    stotal = "" #string total
    i = 0
    while i < len(input) and not ("!" <= input[i] <= "/"): #while loop counter less than length of string and is not in range
        num = input[i]                                     #numeric value before first operand
        stotal = stotal + num                              #string total 
        i += 1  
    if i < len(input):
        op1 = input[i]
        stotal1 = int(stotal)
    print(op1)
    total = total + stotal1
    print(total)

    stotal = ""
    j = i + 1
    while j < len(input) and not ("!" <= input[i] <= "/"):
        num = input[j]
        stotal = stotal + num
        j += 1
    if j < len(input):
        op2 = input[j]
        print(op2)
        stotal2 = int(stotal)
        print(stotal2)
    else:
        total = operate(total, stotal2, op1, op2)
        input = total
        return input

def operate(t, st):
    if 

main()