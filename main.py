myName = input("What is your name? ")
print("Hi " + myName + ", you have chosen to book a horse riding lesson, press enter to continue")
input("")
print("please answer the following 2 questions to ensure that you will be prepared on the day of your lesson.")
input("")

QuestionOne = None
while QuestionOne not in ("yes" , "no"):
    QuestionOne = str(input("have you got your own helmet? "))
    if QuestionOne == "yes":
        print("great!")
    elif QuestionOne == "no":
        input("To rent a riding hat, you will have to pay a fee of £4 every lesson. Are you size small, medium or large? ")
        print("thank you")
    else:
        print("please enter yes or no")
input("")

QuestionTwo = None
while QuestionTwo not in ("yes" , "no"):
    QuestionTwo = str(input("have you got your own riding shoes? "))
    if QuestionTwo == "yes":
        print("great!")
    elif QuestionTwo == "no":
        print("To rent riding shoes, you will have to pay a fee of £5 every lesson.")
    else:
        print("please enter yes or no")
input("")

print("SUMMARY: For riding hat you chose: " + QuestionOne + " for riding shoes you chose: " + QuestionTwo + ".")
Payment = input("To continue to payment, please type 'yes': ")
if Payment == "yes":
    print("Thank you!")
else:
    print("you have chosen not to go ahead with payment. see you again next time!")
