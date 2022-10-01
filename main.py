# Password Manager
## MAIN PROGRAM ##
from lockmodule import *
fstpage()
go = True
while go:
  try:
    option = int(input("Enter 1 New Registration\nEnter 2 To Login\nEnter 3 To Exit\n: "))

    if option == 1:
      sndpage()
      adduser()
      print("""\n"Now You are member of LOCKWORD..."\n""")

    elif option == 2:
      trdpage()
      username = input("Please enter your Username: ")
      password = input("Please enter your Password: ")  
      login(username, password)
      go=False
      
    elif option == 3:
      go = False
      
    elif option >=3:
      print("Error... please try again.\n")
      
  except:
    print("Error... please try again.\n")
## END MAIN PROGRAM ##

