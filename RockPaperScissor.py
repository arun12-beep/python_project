import random
import time
computer_list=['rock','paper','scissor']
print("WELCOME TO ROCK PAPER SCISSOR GAME")
time.sleep(3)
print("THE FIRST ONE TO SCORE 3 TIMES WINS THE MATCH.")
time.sleep(3)
print("ARE YOU READY?")
time.sleep(3)
user_score=0
computer_score=0
while user_score<3 and computer_score<3:
    computer_choice=random.choice(computer_list)
    user=input('rock | paper| scissor:').lower()
    if computer_choice==user:
      print(f"computer choose: {computer_choice}")
      time.sleep(2)
      print(f"you choose: {user}")
      print("match tied......")
      time.sleep(2)
      print(f"user {user_score} computer :{computer_score}\n")
    else:
       match user:
          case 'rock':
            if computer_choice=='scissor':
                time.sleep(1)
                print(f"computer choice: {computer_choice}")
                time.sleep(2)
                print(f"you choose: {user}")
                user_score=+1
                time.sleep(2)
                print(f"user: {user_score} computer:{computer_score}\n")
                
            elif computer_choice=='paper':
                time.sleep(1)
                print(f"computer choice: {computer_choice}")
                time.sleep(2)
                print(f"you choose: {user}")
                time.sleep(1)
                print("computer won...")
                time.sleep(1)
                computer_score+=1
                time.sleep(2)
                print(f"user: {user_score} computer:{computer_score}\n")
                
          case 'paper':
            if computer_choice=='rock':
                time.sleep(1)
                print(f"computer choice: {computer_choice}")
                time.sleep(2)
                print(f"you choose: {user}")
                time.sleep(1)
                print("user won....")
                user_score+=1
                time.sleep(2)
                print(f"user: {user_score} computer:{computer_score}\n")
            elif computer_choice=='scissor':
                time.sleep(1)
                print(f"computer choice: {computer_choice}")
                time.sleep(2)
                print(f"you choose: {user}")
                time.sleep(1)
                print("computer won...")
                time.sleep(1)
                computer_score+=1
                print(f"user: {user_score} computer:{computer_score}\n")

          case 'scissor':
            if computer_choice=='paper':
                time.sleep(1)
                print(f"computer choice: {computer_choice}")
                time.sleep(2)
                print(f"you choose: {user}")
                time.sleep(1)
                print("you won....")
                user_score+=1
                time.sleep(2)
                print(f"user: {user_score} computer:{computer_score}\n")
            elif computer_choice=='rock':
                time.sleep(1)
                print(f"computer choice: {computer_choice}")
                time.sleep(2)
                print(f"you choose: {user}")
                time.sleep(1)
                print("computer won....")
                computer_score+=1
                time.sleep(2)
                print(f"user: {user_score} computer:{computer_score}\n")
          case other:
            print(f"i didn't recognize {other} keyword. please enter between rock|paper|scissor")
print(f"overall score:")
time.sleep(2)
print("loading .....")
time.sleep(2)
print(f"user: {user_score} and computer :{computer_score}")
time.sleep(1)
print("user won" if user_score==5 else "computer won...")


