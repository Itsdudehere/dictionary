import random
from data import slang
from difflib import get_close_matches as match

print("This is an Acronym Dictionary with some popular used acronym.")

while True:
  query = input('''Please enter your query or
  \rPress Enter for a random acronym: ''')
  query = query.upper()
  
  # When user doesn't enter anyting
  if query == "":
    random_word = random.choice(list(slang.keys()))
    print(random_word + ": " + slang[random_word])
  
  # When queried string is present in dictionary keys
  elif query in slang:
    print(query + ": " + slang[query])
  
  # When queried string matches some chars of slang keys
  elif len(match(query, slang.keys())) > 0:
    alternate = match(query, slang.keys())[0]
    print("Do you mean " + alternate + " ?")
    decide = input("If yes enter Y or N for No: ")
    
    if decide.lower() == "y":
      print(alternate + ": " + slang[alternate])
    else:
      print("Sorry , we couldn't solve your query")
  
  else:
    print("your query isnt in our database")
  decide = input("\nWould you like to do more searches? Y or N: ")
  
  if decide.lower()=="y":
    continue
  else:
    break 
	
    
print("Thank you for using our program.")
