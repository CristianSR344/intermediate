from random import randint
def my_function():
    for i in range(1,20 ):
        if i == 20:
            print("You got it")
            
def dice():
    dice_images = ["1", "2", "3", "4", "5", "6"]
    dice_num = randint(0,5)
    print(dice_images[dice_num]) 
    


def years():
    year = int(input("What's your year of birth? "))

    if year > 1980 and year <1994:
        print("You are a milenial")
    elif year >= 1994:
        print("You are a Gen Z")
        
        
        
def age():
    try:
        age = int(input("How old are you? "))
    except ValueError:
        print("You have typed in an invalid number. Please try again with a numerical number")
        age = int(input("How old are you"))
        
    if age > 18:
        print(f"You can drive at {age}.")
        


def pages():
    word_per_page = 0
    pages = int(input("Number of pages: "))
    word_per_page = int(input("Number of words per page: "))
    total_words = pages * word_per_page
    print(total_words)
    
import random
import maths

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1,3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)
    
mutate([1, 2, 3, 5, 8, 13])