#Asks for the user's total bill without tip and what percent they want to add for tip
bill = float(input("Welcome to my tip calculator. What is your total bill without tip? $"))


tip_percent = int(input("What tip percentage do you want to give out (No need to type the percentage symbol. Just type the number in?"))


def tip_calculation(bill, tip_percentage):
    flat_tip = str(round(tip_percentage / 100 * bill, 2))
    print("The total amount that will be added to your bill as tip is: $" + flat_tip + ". Thank you for allowing us to serve you today! Have a good day!")
    

#if tip_percentage == 15:
    #flat_tip = bill_no_tip * .15
#elif tip_percentage == 18:
    #flat_tip = bill_no_tip * 0.18 
#elif tip_percentage == 20:
    #flat_tip = bill_no_tip * 0.20 

tip_calculation(bill, tip_percent)









#print("The total amount that will be added to your bill as tip is: $" + flat_tip + ". Thank you for allowing us to serve you today! Have a good day!")