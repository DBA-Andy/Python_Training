import random

def roll_dice(p_dice_sides, p_dice_count,p_modifier):
    v_dice_list=[]
    for i in range(p_dice_count):
        v_dice_roll = random.randint(1,p_dice_sides)
        v_dice_list.append(v_dice_roll)
        print (f"Dice {i+1} rolled is a {v_dice_roll}")

    return sum(v_dice_list)+p_modifier

def prompt_until_valid(p_prompt):
    # Define variables to be used
    v_dice_prompts = {'Sides':"Please enter the type of dice to roll.  For example, for a d20, enter 20:\n",
                      'Count':"Please enter the number of dice to roll\n",
                      'Modifier':"Please enter the modifier for the skill you're rolling for.  If none, enter 0:\n"}
    v_valid_sides = {4,6,8,10,12,20} # Only valid values in pathfinder
    v_question_response=None
    
    # Don't let the caller out until they enter a valid response.
    while not v_question_response:
        v_question_response=input(v_dice_prompts[p_prompt])
        if v_question_response and not v_question_response.isnumeric():
            print ("Only a number is valid here!")
            v_question_response=None
        elif p_prompt == 'Sides' and v_question_response and int(v_question_response) not in v_valid_sides:
            print (f"Only the values {v_valid_sides} are allowed")
            v_question_response=None

    return int(v_question_response)

def main():
    v_valid_dice=[4,6,8,10,12,20]
    v_dice_sides = prompt_until_valid("Sides")
    if v_dice_sides == 20: # You can only roll 1 d20 in my experience, so we'll default to 1 if the sides are 20
        v_dice_count = 1
    else:
        v_dice_count = prompt_until_valid("Count")
    v_modifier = prompt_until_valid("Modifier")
    

    v_result = roll_dice(v_dice_sides,v_dice_count,v_modifier)
    print (f"The result of this roll is a {v_result}")

main()