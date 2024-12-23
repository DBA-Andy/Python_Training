import random
import argparse

def roll_dice(p_dice_sides, p_dice_count,p_modifier):
    v_dice_list=[]
    for i in range(p_dice_count):
        v_dice_roll = random.randint(1,p_dice_sides)
        v_dice_list.append(v_dice_roll)
        print (f"Dice {i+1} rolled a {v_dice_roll}")

    if p_dice_sides == 20:
        if v_dice_roll == 20:
            print ("CRITICAL SUCCESS!")
        elif v_dice_roll == 1:
            print ("CRITICAL FAIL!")

    return sum(v_dice_list)+p_modifier

def prompt_until_valid(p_prompt):
    # Define variables to be used
    # Dictionary of Prompts
    v_dice_prompts = {'Sides':"Please enter the type of dice to roll.  For example, for a d20, enter 20:\n",
                      'Count':"Please enter the number of dice to roll\n",
                      'Modifier':"Please enter the modifier for the skill or attack you're rolling for.  If none, enter 0:\n"}
    
    v_question_response=None
    
    # Keep prompting until the caller out until they enter a valid response.
    while not v_question_response:
        v_question_response=input(v_dice_prompts[p_prompt])
        if v_question_response and not v_question_response.isnumeric():
            print ("Only a number is valid here!")
            v_question_response=None
        elif p_prompt == 'Sides' and v_question_response and int(v_question_response) not in g_valid_sides:
            print (f"Only the values {sorted(g_valid_sides)} are allowed")
            v_question_response=None

    return int(v_question_response)

def main():
    v_parser=argparse.ArgumentParser()
    v_parser.add_argument('--d','--dice',type=int,help="Roll a dice with this number of sides.  For example, for a d20, enter 20.")
    v_parser.add_argument('--c','--count',type=int)
    v_parser.add_argument('--m','--mod',type=int)
    v_args = v_parser.parse_args()
    
    if v_args.d and int(v_args.d) in g_valid_sides:
        v_dice_sides = int(v_args.d)
    else:
        v_dice_sides = prompt_until_valid("Sides")
    
    if v_dice_sides == 20: # You can only roll 1 d20 in my experience, so we'll default to 1 if the sides are 20
        v_dice_count = 1
    elif v_args.c:
        v_dice_count = v_args.c
    else:
        v_dice_count = prompt_until_valid("Count")
    
    if v_args.m or v_args.m == 0:
        v_modifier = v_args.m
    else:
        v_modifier = prompt_until_valid("Modifier")
 
    v_result = roll_dice(v_dice_sides,v_dice_count,v_modifier)
    print (f"The result of this roll is a {v_result}")

# Define static global variable for use in multiple functions
g_valid_sides = {4,6,8,10,12,20} # Set ctonaining only valid values in pathfinder for sides of dice

main()
