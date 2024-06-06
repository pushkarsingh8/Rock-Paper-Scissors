#Rock-Paper-Scissors
from prettytable import PrettyTable
import random
import time
print("Enter Your Name")
name = input("> ").capitalize()
user_score = 0
computer_score = 0
tie = 0


while True:
    print(f"""\nWelcome {name}to the Rock-Paper-Scissors Game:-
1.Enter (1) for Rock.
2.Enter (2) for Paper.
3.Enter (3) for Scissor.
      """)

    print(f"{name} Enter Your Choice: ")
    user_choice = int(input(">"))
    
    if user_choice == 1:
        user = "rock"
            

    elif user_choice == 2:
        user = "paper"
            
    elif user_choice == 3:
        user = "scissor"
            
    else:
        print("Invalid entered")
        continue
                
    print(f"{name} choose is {user}\n")
    print("Computer Chance")

    computer_choice = random.randint(1,3)

    if computer_score == 1:
        computer = "rock"
            

    elif computer_score == 2:
        computer = "paper"
            
    else:
        computer = "scissor"
        
    print("Please wait...")
    time.sleep(2)
    print(f"\n@ Computer choose a {computer} ")


    #decision make for win

    if (user == 'scissor' and computer == 'paper') or (user == "rock" and computer == 'scissor') or\
    (user == 'paper' and computer == 'rock'):
        
        print(f"{name} wins this round")
        user_score +=1
        
    elif user == computer:
        print("It's a tie!")
        tie+=1
        
    else:
        print("Computer wins this round!")
        computer_score+=1
        
        
    print(f"\n{name} You want to play next Round\nEnter(yes/no)")
    next_round = input("> ")
    
    if next_round == "no":
        break
    elif next_round != "yes":
        print("Invalid response, exiting game.")
        break

win = "N/A"
        
    
if user_choice>computer_choice:
    win = f"{name} WINs"

elif computer_choice>user_choice:
    win = "Computer WINs"
        
else:
    win = "It's a TIE"      
    
mytable = PrettyTable(["Playes_Name","Score"])
mytable.add_row([name,user_score])
mytable.add_row(["Computer",computer_score])
mytable.add_row(["Tie",tie])
print(mytable)

    
    
    
    
    
    
    
    
    
    
    