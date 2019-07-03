

print ("Welcome To My Hangman Game")
print ("--------------------------")
line1 =" ----"
line2 =" |   |"
line3 =" |   O"
line4 =" |  -|-"
line5 ="_|_ / \ "

def print_board(tries):
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    return


user_input = "yes"
while user_input == "yes":
    user_input = input("Do you want to go again? yes or no: ")
    print_board()

