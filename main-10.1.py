def main():
  file_name = input("Please enter the new file name: ")

  file = open(file_name, "a")

  name = input("What is your name? ")
  address = input("What is your address? ")
  phone = input("What is your phone number? ")

  file.write(f"{name}, {address}, {phone}")
  file.close()

  file = open(file_name, "r")
  
  print("File contents: ",file.read())

main()