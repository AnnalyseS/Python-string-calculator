
print("\n Welcome to my calculator!\n Please note that '/' will give you a decimal value.\n If you wish to do clean division, use '//'\n if you want to clear calculator and start a new calculation, type: 'clear'")
def main():
    operators = "*/%^+=-"
        
    while True:
        user_input = input("\nWhat would you like to calculate? ")
        #get rid of extra spaces so iteration is simpler
        command = user_input.strip().replace(" ", "").lower()
        #make a loop to reprompt user for input if they make a typo and only input half a calculation
        if command == "clear":
            print("Calculator cleared.")
            continue

        incomplete = False

        for char in operators:
            if command.endswith(char):
                incomplete = True

            if incomplete:
                print("Incomplete caclulation. Please enter a valid calculation.")
                continue

            if ValueError:
                print("undefined")
                continue
                
        result = calculate(command)
        print(result)

def calculate(command):
# start the loop to iterate over command to figure out if x is numeric or not, concatenate the correct values and convert to integers.
    string = ""
    i = 0
    while i < len(command):
        for char in command:
            if char.isnumeric():
                string = string + char
                number = int(string)
            else:
                print("First number: ", number)
                string = ""
                operator = char
            print("Second number: ", number)
        i += 1  

            if y == "-":
                total = total - z #command[i] = y here since we are inside the elif
            elif y == "+":
                total = total + z
            elif y == "*":
                total = total * z
            elif y == "//":
                if z == 0:
                    total = "undefined"
                else:
                    total = total // z
            elif y == "/":
                if z == 0:
                    total = "undefined"
                else:
                    total = total / z
            elif y == "%":
                total = total % z
            elif y == "**" or y == "^":
                total = total ** z
                    #now we must make it so that the calculator can take multiple operators at once
                    #also make a special case for division by zero and output "undefined"
                    #also make a special case for ** beause the i + 1 solution is not recognized here as an operator, we get an out of range error
        result = total
        i += 1
    print(total)
    command = total
    return str(command)

#below is a loop to continue calculating
def calc(result):
    total = result
    user_input = input()
    i = 0
    while i < len(user_input):    
        total = calculate(user_input)
        result = total
        return result
    print(result)
main()