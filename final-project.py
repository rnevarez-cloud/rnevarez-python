#Ricardo Nevarez 2023-05-14 Draft

import json, requests
base_url = "https://api.openweathermap.org/data/2.5/weather"
appid = "9d43f0575fba95fb329e4df161d64aa5"

def main():

  location = input('Please input city name or zipcode: ')

  ##Determining which query parameter to use depending on input. If a zipcode is detected, the zip query parameter will be used.
  if location.isdigit() :
    query = "zip"
  else :
    query = "q"
  
  url = f"{base_url}?{query}={location}&units=imperial&APPID={appid}"
  print(url)
  print ()

  ##Testing connection to openweathermap.org
  try:
    response = requests.get(url)
    
  except:
    print("An exception occurred. Please try again.")
    main()  

  unformatted_data = response.json()

  ##Displays any errors from the request and prompts the user to retry
  if unformatted_data["cod"] != 200:
    print("Data entered was not valid. Please enter a city name or zip code.")
    print("-----")
    print("Error code: ",unformatted_data["cod"])
    print("Error message:",unformatted_data["message"])
    print("-----")
    main()
    
  ##Prints response data from valid API request  
  else:
    print("Temperature data for",unformatted_data["name"],"(",unformatted_data["sys"]["country"],"):")
    print("-----")
    print("Current temperature:",unformatted_data["main"]["temp"], chr(176),"F")
    print("High:",unformatted_data["main"]["temp_max"],chr(176),"F")
    print("Low:",unformatted_data["main"]["temp_min"],chr(176),"F")
    print("-----")

    ##Asks the user if they would like to re-run the program for another location
    restart = ''

    while restart != "Yes" and restart != "No":
      restart = input("Would you like to run the program again? (Yes/No): ")
    if restart == "Yes" :
      main()
    elif restart == "No" :
      exit()

main()