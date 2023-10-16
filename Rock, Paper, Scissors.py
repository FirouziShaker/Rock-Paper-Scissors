import random

user_wins=0
computer_wins=0

options= ["rock","paper","scissors"]


while True:
    user_input= input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    
    
    #If the input was q , go out 
    if user_input== "q":
        break  
          
    #If the input was not in the list of options start again 
    if user_input not in options:
        continue
    
    #choice a random number between 0,1,2
          # rock=0 , paper=1 , scissors=2
    random_number=random.randint(0,2)
      
      #conforming the random number, choice a item of options
    computer_pick = options[random_number]
    print("Computer picked" , computer_pick + ".")
    
    if user_input=="rock" and  computer_pick=="scissors":
        print("You won!")
        user_wins +=1
          
    elif user_input=="paper" and  computer_pick=="rock":
        print("You won!")
        user_wins +=1
          
    elif user_input=="scissors" and  computer_pick=="paper":
        print("You won!")
        user_wins +=1
        
    else:
        print("You lost!")
        computer_wins +=1
          
      
print("You won" , user_wins , "times.")
print("The Computer won" , computer_wins , "times.")     
 
print("Goodbye!")
    