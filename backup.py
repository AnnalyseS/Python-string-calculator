def main():
    total = 0
    user_input = input("Calculate: ")
    user_input = user_input.strip().replace(" ", "").lower()
    #while input not quit
    i = 0
    while user_input != "quit":
        # if clear reset total 
        if user_input == "clear":
            total = 0
            print("calculator cleared!")
            user_input = input("Calculate: ").strip().replace(" ", "").lower()
        #figure out if the string is a complete calculation
        elif not user_input[len(user_input) - 1].isnumeric():
            print("Invalid calculation, please try again.")
        # need to add another elif here for when they use two operators back to back in the middle of the string
            user_input = input("Calculate: ").strip().replace(" ", "").lower()
        elif (":" <= user_input[i] <= "~"):
            print("Invalid calculation, please try again.")
            user_input = input("Calculate: ").strip().replace(" ", "").lower()
        #division by 0
        #elif ValueError:
          #  print("undefined")
        # legit calculation, continue to calculate
        else:
            answer = calculate(user_input)
            #print(answer)
            user_input = input().strip().replace(" ", "").lower()
        i += 1
    if user_input == "quit":
        print("Goodbye, thank you for using my calculator!")

def calculate(input):

    parse(input)


def parse(input): #want to parse the string, separating or appending operands to their own list and numerics to another and return the different values appropriately so they can be used in calculation
    # need to make a list for nums, take the last values in the lists and calculate them
    tempnums = []
    ops = []
    stotal = ""
    for char in input:
        if char.isnumeric():
                stotal += char
                tempnums.append(stotal)
        else:
            stotal = ""
            ops.append(char)
            tempnums.append(" ")
    tempnums.append(" ")

    print(tempnums) 
    print(ops)

    nums = []
    i = 0
    while i < len(tempnums):
        if tempnums[i] == " ":
            num = tempnums[i - 1]
            nums.append(num)
        else:
            pass
        i += 1
    print(nums)
#def operate():

main()