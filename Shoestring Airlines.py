# Shoestring Airlines Application
# Steve Dale

import os    # import = modules that can be used 
import sys
import random
import flights_ENG    # custom module of flights imported from another file
import HELP

# D = Design
D_dash_lng = ("-"*80)    # lng = long
D_dash_med = ("-"*45)    # med = medium
D_dash_sht = ("-"*4)     # sht = short    
D_star = ("*"*1)
D_equals = ("="*10)

# pricing
p_Adults = 30.00    # p = prices
p_Children = 18.00    # child seat 60% of £28.00
p_Infants = 10.00

Adult = p_Adults
Child = p_Children
Infant = p_Infants
x = 30
print(D_dash_lng)    # prints D_dash to add some style to the program
print("                                        **Welcome to Shoestring Airlines!**")
print("""                                        This is an online program for you
                                        to book flights and treat yourself to
                                        a lovely holiday.""")    # """ Triple quotation for multi-line strings

print(D_dash_lng)
print("By using this program you also gain\n " + (D_star) + "5% OFF" + (D_star) + 
" all tickets!")

print("""To use, we have a handful of options to improve your experience
and usability. Thank you.\n  """)    # \n assigns a newline
print(D_dash_lng)

print('Please enter [1] "No square bracket"  to Read more...')

def adultCalc(x, y):
    return (x * y)

def dis_options():    # dis = display    # def is used to define a new function so that you're not limited to vanilla py functions
    # displays menu for user
    print("****Please use this menu to navigate through options.****")
    print(D_dash_med)
    print(" [C] - Opens list regarding CURRENT flights")
    print(D_dash_med)
    print(" [F] - Opens list regarding FUTURE flights")
    print(D_dash_med)
    print(" [B] - Book a flight")
    print(D_dash_med)
    print(" [H] - Brings up help menu")
    print(D_dash_med)
    print(" [R] - Re-prints menu (Useful for when a lot of data is shown on the screen)") 
    print(D_dash_med)
    print(" [Q] - Quits the program")

while input() != "1":    # while loop to run dis_options when the input is == TO "1"
    choice = print("Please enter [1]. No other characters are allowed... ")
    print(D_dash_med)
    input('Please enter [1] "No square bracket"  to Read more... Press Enter and input the correct value')
dis_options()

print("                       *Note*: Is case sensitive!")
choice = input("\n          Option: ")
while choice != "Q":
    # this loops until the user quits the program
    if choice == "C":    
        # opens list for CURRENT flights
        flights_ENG.flights_C_ENG()    # module imported from the top used here to print list of flights

    elif choice == "F":
        flights_ENG.flights_F_ENG()    # module imported from the top used here to print list of flights

    elif choice == "H":
        HELP.h_HELP()                         # module imported from the top used here to print list of flights

    elif choice == "B":
        print("To book a flight we need to know what ticket-types you need and how many you need.")
        print("Please enter one of the valid ticket-types. \n")
        print(D_equals)
        print("Adult: £", format(Adult, ",.2f"))
        print("Child: £", format(Child, ",.2f"))
        print("Infant: £", format(Infant, ",.2f"))
        print(D_equals)
        print("Please specify the amount of tickets for each ticket-type")
        num2 = input("Adult: ")
        print(num2 + " Adult ticket(s) cost £", adultCalc(num2, 30))
        y = input("Child: ")
        z = input("Infant: ")
        
    elif choice == "R":
        # re-prints the menu
        dis_options()
    else:
        print("The following value you entered cannot be used, please try again.")

    choice = input("\n New option: ")
    
print("Thank you, goodbye")

        

    

    
    
        






        
