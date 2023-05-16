def main():
  # Display the intro screen
  intro()

  # Get the number of miles
  try:
    miles = (int(input('Enter the number of miles: ')))
  
  # Convert the miles to kilometers
    milestokm(miles)

  except:
    print("An exception occurred, try again entering only a number")
    print()
    main()

def intro():
  print('This program converts distance')
  print('in miles to kilometers. For your')
  print('reference the formula is:')
  print('1 mile = 1.60934 kilometers')
  print()


def milestokm(x):
  kilometers = x * 1.60934
  print('That converts to', kilometers, 'kilometers.')

main()