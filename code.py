from difflib import get_close_matches as match
import random
slang = {
    "FOMO": 'Fear of missing out',
    'YOLO': "You only live once",
    "IKR": 'I know right?',
    'TLDR': 'Too long didn\'t read',
    'NOOB': 'newbie',
    'OP': 'Original post or sometimes also may refer to OverPower',
    'AFK': 'Away from keyboard',
    'BRB': "Be right back",
    'IMO': 'In my opinion',
    "IDK": 'i dont know',
    'IMHO': 'In my honest opinion',
    "EOD": "End of discussion",
    "OOTD": "Outlook of the day",
    "EOT": "End of thread",
    "BAE": 'Before anyone else',
    "FYI": "For your infromation",
    'ICYMI': "In case you missed it"
}
print("This is a acronym dictionary with some popular used acronym .")
while True:
  query = input(
        "\nPlease enter your query or \nPress Enter for a random acronym: ")
  query = query.upper()
  if query == "":
    random_word = random.choice(list(slang.keys()))
    print(random_word + ": " + slang[random_word])
  elif query in slang:
    print(query + ": " + slang[query])
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
