import art
import game_data
import random

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

def game():
    score = 0
    flag = False
    personA = random.choice(game_data.data) 
    
    # 'name': 'Cristiano Ronaldo',
    # 'follower_count': 215,
    # 'description': 'Footballer',
    # 'country': 'Portugal'
    print(art.logo) 
    
    while flag == False: #while for game
        if score > 0:
            print(f"You're right! Current score: {score}")
            
        personB = random.choice(game_data.data)
        
        if personA == personB:
            while personA == personB: 
                personB = random.choice(game_data.data)
                #endW
        
        print(f"Compare A: {personA['name']}, a {personA['description']}, from {personA['country']}, followers {personA['follower_count']}")
        print(art.vs)
        print(f"Against B: {personB['name']}, a {personB['description']}, from {personB['country']}, followers {personB['follower_count']}")
        
        choice = input(r"Who has more followers? Type 'A' or 'B' : ")
        
        print("\n*20")
        print(art.logo)
        
        if choice == 'A':
            if personA['follower_count'] > personB['follower_count']:
                score += 1
            else:
                flag = True
        else: 
            if personB['follower_count'] > personA['follower_count']:
                score += 1
                personA = personB
            else:
                flag = True
        
        


game()