# HELP MODULE TO IMPORT

A = ("A flight I would like isn't listed here//My flight isn't listed here.")
B = ("\n \n \n How do I book a flight?")


def h_HELP1():
    print(A)
    print("-"*70)
    print("If your flight isn't listed here, it can be due to multiple reasons... \n")
    print("     A.    Your connection to the internet might be limited, our servers work over the internet therefore flight information isn't being updated \n")
    print("     B.    It could just be that there isn't an available flight for you at the moment, please wait for at least another day. \n")
    print("     C.    Sometimes our systems doesn't display all flights \n")
    print("     D.    When tickets are sold the system rarely displays the available flights. Soon to be fixed \n")    # this doesn't actually happen to the program but I need some data to use for the help section

    
def h_HELP2():
    print(B)
    print("-"*70)
    print("We've made booking flights easy for people with no technical experience. \n Just follow the options shown followed by a [B] for 'Book a Flight'")
    print("You'll be asked for information such as your name, email address and phone number. This is just for security reasons and so you can create an account.")


