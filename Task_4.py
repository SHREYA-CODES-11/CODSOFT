import random
print("Welcome to the game of Rock, Paper, Scissors!")
rock = '''
    _______
   /\| | | |
  / /|_|_|_|
  \        |
   \_______/
'''
paper = '''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'
'''
scissors = '''
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
'''
game_images = [rock, paper, scissors]
user_choice = int(input("Type 0 for 'rock', 1 for 'paper' and 2 for 'scissors'.\n"))
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])
computer_choice = random.randint(0,2)
print("Computer chose:\n")
print(game_images[computer_choice])
if user_choice >= 3 or user_choice < 0:
    print("Invalid choice. Play again.")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("Match draw!")