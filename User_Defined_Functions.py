#Activity: Simple_function
def listen ():
    sound = input ("What sound did I hear? ")
    print (f"That was a loud {sound}")
listen()


#Activity: function_with_condition
def identify ():
    target = input("What lies before us?")
    if target == "a large boulder":
        print("It's time to run!")
    else: print("We will be fine.")
identify()


def identify ():
    target = input("What lies before us?")
    if target == "a large boulder":
        print("It's time to run!")
    else: print("We will be fine.")
identify()


#Activity: function_with_parameter
def escape (plan):
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "going deeper": 
        print("That might just work! Let's go deeper!")
    else: print("We cannot escape that way! The boulder is in the way!")

escape("jumping over")
escape("running around")
escape("going deeper")


#Activity: return_values
def sum_weights(weight1,weight2):
    return weight1+weight2
def calc_avg_weight(weight1,weight2):
    return (weight1+weight2)/2
def run ():
    bop_weight= int(input("What is the weight of Bop? "))
    beep_weight= int(input("What is the weight of Beep?"))
    calculation = input("What would you like to calculate (sum or average)? ")
    if calculation == "sum":
        print(f"The sum of Beep's and Bop's weight is {sum_weights(bop_weight,beep_weight)}")
    elif calculation == "average":
        print(f"The average of Beep's and Bop's weight is {calc_avg_weight(bop_weight,beep_weight)}")
    else: print("Error, Just say sum or average")
run()                                       
