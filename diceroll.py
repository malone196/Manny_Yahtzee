from random import randint
dice_roll_1 = randint(1,6)
dice_roll_2 = randint(1,6)
dice_roll_3 = randint(1,6)
dice_roll_4 = randint(1,6)
dice_roll_5 = randint(1,6)
rolls = [dice_roll_1, dice_roll_2, dice_roll_3, dice_roll_4, dice_roll_5]
print ("You rolled a :")
print rolls
keepers = input("select your keepers based on dice position!")
keepers_list = []
if keepers == 1:
    print("You kept your first dice:"); print dice_roll_1; rolls.remove(dice_roll_1); keepers_list.insert(0,dice_roll_1);

if keepers == 2:
    print("You kept your second dice:"); print dice_roll_2; rolls.remove(dice_roll_2); keepers_list.insert(0,dice_roll_2);

if keepers == 3:
    print ("You kept your third dice:"); print dice_roll_3; rolls.remove(dice_roll_3); keepers_list.insert(0,dice_roll_3);

if keepers == 4:
	print ("You kept your fourth dice:"); print dice_roll_4; rolls.remove(dice_roll_4); keepers_list.insert(0,dice_roll_4);

if keepers == 5:
	print("You kept your fifth dice:"); print dice_roll_5; rolls.remove(dice_roll_5); keepers_list.insert(0,dice_roll_5);

print ("These are the dice you have left:")
print rolls

print ("These are your keepers:")
print keepers_list