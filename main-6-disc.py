def main():
  # Display the intro screen
  intro()

  try:
    selection = (int(input('Select your desired conversion: ')))

    # Convert the cups to ounces
    if selection == 1:
      # Get the number of cups
      cups = (int(input('Enter the number of cups: ')))
      
      # Convert the cups to ounces
      cups_to_ounces(cups)

    elif selection == 2:
      # Get the number of liters
      liters = (int(input('Enter the number of gallons: ')))
  
    # Convert the gallons to liters
      gallons_to_liters(liters)
  
  except:
    print("An exception occurred, try again entering only a number")
    print()
    main()

def intro():
  print('This program converts measurements.')
  print('Please select your desired conversion:')
  print('1. Cups -> Ounces')
  print('2. Gallons -> Liters')
  print()

def cups_to_ounces(x):
  ounces = x * 8
  print('That converts to', ounces, 'ounces.')

def gallons_to_liters(x):
  liters = x * 3.78541
  print('That converts to', liters, 'liters.')

main()