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
        elif ("!" <= user_input[i] <= "~"):
            print("Invalid calculation, please try again.")
            user_input = input("Calculate: ").strip().lower()
        #division by 0
        #elif ValueError:
          #  print("undefined")
        # legit calculation, continue to calculate
        else:
            answer = calculate(user_input)
            total = total + answer
            user_input = input()
        i += 1
    if user_input == "quit":
        print("Goodbye, thank you for using my calculator!")

def calculate(input):
    total = 0
    i = 0
    while i < len(input) and not ("!" <= input[i] <= "/"):
        i += 1
    if i < len(input):
        a = input[i] # operator
        print(a)

main()