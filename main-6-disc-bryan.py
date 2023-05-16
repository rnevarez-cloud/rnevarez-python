# Defining main.
def main():

    # Displays the introduction.
    intro()

    # Inputing the amount of gallons that need to be converted.
    try:
      gallons_needed = float(input("Enter the number of gallons you would like to convert: "))

      gallons_to_liters(gallons_needed)

    # Stopping for anything that is not a number and restarting.
    except:
      print("An error was made.  Please try again entering only a number.")
      print()
      main()

# Tells the user what this program is going to do.
def intro():
    print("This program is going to convert measurements")
    print("in gallons to liters.  For your")
    print("reference the formula is:")
    print("1 gallon = 3.78541 liters.")
    print()


# Converts gallons into liters and then outputs it.
def gallons_to_liters(gallons):
      
      liters = gallons * 3.78541
      print("That converts to", liters, "liters.")

# Calling main.
main()