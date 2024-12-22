import random

v_computer_choice=random.choice(['rock','paper','scissors'])
v_user_choice = input('Do you want rock, paper, or scissors?\n')
print (f"The computer chose {v_computer_choice}")

if v_computer_choice == v_user_choice:
    print ("This was a draw")
elif v_user_choice == 'rock' and v_computer_choice == 'scissors':
    print ("You Win")
elif v_user_choice == 'paper' and v_computer_choice == 'rock':
    print ("You win")
elif v_user_choice == 'scissors' and v_computer_choice == 'paper':
    print ("You win")
else:
    print ("You lose")
   