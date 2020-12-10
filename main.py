###############################################################
##                                                           ##
##   Magic Mania-An Epic Adventure mini-game [Text-Based]    ##
##   Group- D (Runtime Terror)                               ##
##   Anjitha Antony (C0796673)                               ##
##   Ankur Kishorbhai Rokad (C0793757)                       ##
##   Devadharsini Muralidharan (C0788103)                    ##
##   Gursanjam Kaur (C0788089)                               ##
##   Sahista Patel (C0796681)                                ##
##                                                           ##
###############################################################

try:
    #Imports for printing slow characters
    import sys
    import time
    #Imports for to get random choices from list, enemeis selections or random golds
    import random
    import pygame
    from pygame import mixer
    #Imports for clearing console
    import os
    #In jupyter notebook working these uncomment clear_output function call
    # #from IPython.display import clear_output
except:
    print('\nPlease install "Pygame" package first to enjoy this game...')
    quit()


#Global variables
name, division = '', ''
inventory, enemy_details, skills = [], [], []
current_location = 'Outside Cabin'

#Skills set division wise
# strength_skills [0] = Skill Name
# strength_skills [1] = Damage amount which skill can cause
# strength_skills [2] = Mana minimum amount needed to use the skill
strength_skills = [['Stomp', 100, 20], ['Mighty Hammer', 250, 35], ['Body Smash', 300, 40]]
agile_skills = [['Critical Strike', 120, 25], ['Swift Attack', 200, 30], ['1000 Cuts', 350, 45]]
magic_skills = [['Magic Blast', 60, 10], ['Thunder Storm', 250, 20], ['Fire & Ice', 400, 30]]
gold, hp, mp, attack, max_hp, max_mp, hp_regen, mp_regen, lc = 0, 0, 0, 0, 0, 0, 0, 0, 0



#Clearing consol function
def clear_output():
    """" For clearing console."""
    print('\n' * 2)
    # os.system('cls' if os.name == 'nt' else 'clear')
    # os.system('cls')
    # For jupyter notebook
    # lplambda: os.system('cls')

#Printing on console screen
def print_slow(x):
    """"Printing slow on console with the sleep of 0.05"""
    for letter in x:
        sys.stdout.write(letter)
        time.sleep(0.05)
    print('')

#Called when player chooses to enter the game
def player(Name, Division):
    """As per division choice player equipped with special skills and initial Health and Mana and its regeration rates"""
    global name, division, hp, mp, gold, inventory, attack, skills, strength_skills, magic_skills, agile_skills, max_hp, max_mp, hp_regen, mp_regen
    name = Name
    division = Division
    hp = 100
    mp = 100
    attack = 25
    gold = 1000
    if division == 'Strength':
        hp = 150
        skills = strength_skills
        hp_regen = 3
        mp_regen = 1
    elif division == 'Agile':
        attack = 50
        skills = agile_skills
        hp_regen = 2
        mp_regen = 2
    elif division == 'Magic':
        mp = 150
        skills = magic_skills
        hp_regen = 1
        mp_regen = 3
    inventory = [['Apple', 'hp', 20, 10, 't'], ['Book', 'mp', 20, 10, 't'], ['Knife', 'dmg', 5, 45, 'p']]
    max_hp = hp
    max_mp = mp
    # return ()

#Enemy Initialization
def enemy():
    """Assigning enemies powers and list here multiple entries for enemies as to increase probability of enemy encounter
        enemy_list[0] = Enemy Name
        enemy_list[1] = Max Health
        enemy_list[2] = Min Damage which enemy can delt
        enemy_list[3] = Max Damage which enemy can delt"""
    global enemy_details
    enemy_list = [['Goblin', 500, 5, 15], ['Goblin', 500, 5, 15], ['Goblin', 500, 5, 15], ['Goblin', 500, 5, 15],
                  ['Goblin', 500, 5, 15], ['Corrupt Soul', 750, 10, 20], ['Corrupt Soul', 750, 10, 20],
                  ['Corrupt Soul', 750, 10, 20], ['Rogue Soldier', 1000, 15, 25]]
    enemy_details = random.choice(enemy_list)
    # return ()

#When enemy encounter then choices to fight and run
def enemy_encounter():
    """While encountered enemy asking for choice and calling functions accordingly"""
    global hp, mp, enemy_details
    print('While searching you encounter ' + enemy_details[0])
    print('Your Current Health: ', str(hp))
    print('Your Current Mana: ', str(mp))
    print('What you do???')
    print('(a). Fight')
    print('(b). Run')
    fight_choice = input()
    clear_output()
    fight_choice = fight_choice.lower()

    if fight_choice in ['a', 'fight']:
        print_slow('You choose to fight')
        clear_output()
        fight()
    elif fight_choice in ['b', 'run']:
        print('You chose to run')
        clear_output()
        run()
    else:
        while fight_choice not in ['a', 'fight', 'b', 'run']:
            print('Enter valid choice')
            fight_choice = input()
            if fight_choice in ['a', 'fight']:
                print('you choose to fight')
                clear_output()
                fight()
            elif fight_choice in ['b', 'run']:
                print('You chose to run')
                clear_output()
                run()
    # return ()

#Figh Function definiton
def fight():
    """As per users health, Mana and other skills as per Mana balance it will show thw options and fight with enemy
        Enemy attacks right after user attack and it cause damage to user
        Enemy attacks as per its health and mana balance random in between its minimum damage and maximum damage
        If user health reaches to 0.. User die and game over.
            And if Enemy health reaches to 0 enemy die and user can continue to play as still survived ;)
        After each successful move Mana and Health regeneration as per division rate"""
    global hp, mp, attack, enemy_details, skills, hp_regen, mp_regen, name
    while hp > 0 and enemy_details[1] > 0:
        print("{:<15} {:<10} {:<10} {:<30}".format('Player', 'Health', 'Mana', 'Attack'))
        print("{:<15} {:<10} {:<10} {:<30}".format(name, str(hp), str(mp), 'Choice'))
        print("{:<15} {:<10} {:<10} {:<30}".format(enemy_details[0], str(enemy_details[1]), '-', 'Random in ('+str(enemy_details[2])+'-'+str(enemy_details[3])+')'))
        print('Select your move')
        print('a. Normal Attack (' + str(attack) + ' DMG)')
        print('b. Inventory')
        print('Skills (If empty then on cooldown)')
        for i in range(len(skills)):
            if skills[i][2] < mp:
                print(str(i + 1) + '. Use ' + skills[i][0] + ' Damage: ' + str(skills[i][1]) + ' Mana:' + str(skills[i][2]))
        fight_choice = input()
        clear_output()
        fight_choice = fight_choice.lower()
        if fight_choice in ['a', 'normal attack']:
            enemy_details[1] = enemy_details[1] - attack
        elif fight_choice in ['b', 'inventory']:
            clear_output()
            show_inventory()
        elif fight_choice == '1':
            if mp < skills[0][2]:
                print('Not enough Mana. Used normal attack.')
                enemy_details[1] = enemy_details[1] - attack
            else:
                enemy_details[1] = enemy_details[1] - skills[0][1]
                mp = mp - skills[0][2]
        elif fight_choice == '2':
            if mp < skills[1][2]:
                print('Not enough Mana. Used normal attack.')
                enemy_details[1] = enemy_details[1] - attack
            else:
                enemy_details[1] = enemy_details[1] - skills[1][1]
                mp = mp - skills[1][2]
        elif fight_choice == '3':
            if mp < skills[2][2]:
                print('Not enough Mana. Used normal attack.')
                enemy_details[1] = enemy_details[1] - attack
            else:
                enemy_details[1] = enemy_details[1] - skills[2][1]
                mp = mp - skills[2][2]
        else:
            while fight_choice not in ['a', 'normal attack', 'b', 'inventory', '1', '2', '3']:
                print('Invalid Choice')
                fight_choice = input()
                fight_choice = fight_choice.lower()
                clear_output()
                if fight_choice in ['a', 'normal attack']:
                    enemy_details[1] = enemy_details[1] - attack
                elif fight_choice in ['b', 'inventory']:
                    clear_output()
                    show_inventory()
                elif fight_choice == '1':
                    if mp < skills[0][2]:
                        print('Not enough Mana. Used normal attack.')
                        enemy_details[1] = enemy_details[1] - attack
                    else:
                        enemy_details[1] = enemy_details[1] - skills[0][1]
                        mp = mp - skills[0][2]
                elif fight_choice == '2':
                    if mp < skills[1][2]:
                        print('Not enough Mana. Used normal attack.')
                        enemy_details[1] = enemy_details[1] - attack
                    else:
                        enemy_details[1] = enemy_details[1] - skills[1][1]
                        mp = mp - skills[1][2]
                elif fight_choice == '3':
                    if mp < skills[2][2]:
                        print('Not enough Mana. Used normal attack.')
                        enemy_details[1] = enemy_details[1] - attack
                    else:
                        enemy_details[1] = enemy_details[1] - skills[2][1]
                        mp = mp - skills[2][2]
        mp = mp + (1 * mp_regen)
        hp = hp + (1 * hp_regen)
        if mp > max_mp:
            mp = max_mp
        if hp > max_hp:
            hp = max_hp
        #Enemy attacks random function
        AttackSound = mixer.Sound("Attack.mp3")
        AttackSound.play()
        dmg_delt = random.randint(enemy_details[2], enemy_details[3])
        clear_output()
        print('Enemy attacked and deal ' + str(dmg_delt) + ' damage to you!')
        hp_change(0, dmg_delt)
    if hp <= 0:
        print_slow('You Died.....')
        print_slow('Game will end. Please start again to play.')
        input("Press Enter to exit...")
        quit()
    elif enemy_details[1] <= 0:
        gold_drop = random.randint(enemy_details[2], enemy_details[3]) * 2
        print_slow('Bravo! You killed opponent........')
        gold_change(gold_drop, 0)
        print('Got ' + str(gold_drop) + ' gold!')
        enemy_details.clear()
        input("Press Enter to continue...")
        clear_output()
    # return ()

def run():
    """Run function will cause determine the health damage by running..
        Random number of damage in the range of attack value of enemy..
        If it health doesn't reach to 0 surviced otherwise died while running and game ends"""
    global hp, mp, enemy_details
    print('Your Health: ' + str(hp) + '\nYour Mana: ' + str(mp))
    print('Enemy Name: ' + enemy_details[0] + '\nEnemy Health: ' + str(enemy_details[1]))
    # Enemy attacks random function
    dmg_delt = random.randint(enemy_details[2], enemy_details[3])
    clear_output()
    print('Running from fight..' + str(dmg_delt) + ' damaged your health!')
    hp_change(0, dmg_delt)
    RunSound = mixer.Sound("running.mp3")
    RunSound.play()
    time.sleep(2)
    if hp <= 0:
        print_slow('You Died.....While running..')
        print_slow('Game will end. Please start again to play.')
        input("Press Enter to exit...")
        quit()
    else:
        print_slow('Bravo! You made enemy down..Ran far away from him........')
        gold_drop = random.randint(enemy_details[2], enemy_details[3]) * 2
        gold_change(gold_drop, 0)
        print('Got ' + str(gold_drop) + ' gold!')
        enemy_details.clear()
        input("Press Enter to continue...")
        clear_output()
    # return ()


# Changes in equipments, whenevr and amoun to change increase and decrease two parameters to avoid multiple line of code
def gold_change(inc, dec):
    """Gold amount increase or decrease as per call"""
    global gold
    gold = gold + inc
    gold = gold - dec
    GoldSound = mixer.Sound("gold_coin.mp3")
    GoldSound.play()
    # return ()


def hp_change(inc, dec):
    """Health amount increase or decrease as per call"""
    global hp, max_hp
    hp = hp + inc
    hp = hp - dec
    if hp > max_hp:
        hp = max_hp
    # return ()


def mp_change(inc, dec):
    """Mana amount increase or decrease as per call"""
    global mp, max_mp
    mp = mp + inc
    mp = mp - dec
    if mp > max_mp:
        mp = max_mp
    # return ()


def max_hp_change(inc):
    """Health [Capacity] max amount increase or decrease as per call"""
    global hp, max_hp
    max_hp = max_hp + inc
    hp = max_hp
    # return ()


def max_mp_change(inc):
    """Mana [Capacity] max amount increase or decrease as per call"""
    global mp, max_mp
    max_mp = max_mp + inc
    mp = max_mp
    # return ()


def dmg_change(inc):
    """Damage amount increase as per call"""
    global attack
    attack = attack + inc
    # return ()


def search():
    """Search function call to increse the probability of gold in random entry of gold wrote multiple"""
    random_search = ['gold', 'gold', 'gold', 'gold', 'gold', 'enemy', 'enemy']
    random_number = random.randint(5, 25)
    random_drop = random.choice(random_search)
    if random_drop == 'enemy':
        enemy()
        enemy_encounter()
    elif random_drop == 'gold':
        gold_change(random_number, 0)
        print('Found gold: ' + str(random_number))
    # return ()


def add_to_inventory(item, typE, weight, cost, effect):
    """This describes user's inventory... when user purchase something it will add to its inventory
    with re-selling price as half of its original price"""
    global inventory
    #Selling price is half of it's cost
    cost = cost / 2
    inventory.append([item, typE, weight, cost, effect])
    # return ()


def shop():
    """"Shop to purchase as per your need..
    listing iterm [0]: Name
    listing iterm [1]: Description
    listing iterm [2]: Cost
    listing iterm [3]: Health/Attack as per description
    listing iterm [2]: type (p=permanent t=temporary)"""
    global gold, name
    hp_item = [['Apple', 'Eat to recover 20 health', 20, 20, 't'],
               ['Health Potion', 'Drink to recover 50 health', 40, 50, 't'],
               ['Medicine', 'Take to recover 100 health', 70, 100, 't'],
               ['Lion Skin', 'Permanently increase Health by 100', 1200, 100, 'p'],
               ['Dragon Heart', 'Permanently increase Health by 300', 2000, 300, 'p']]
    mp_item = [['Magic Crystal', 'Recover 20 mana', 20, 20, 't'],
               ['Magic Potion', 'Drink to recover 50 mana', 40, 50, 't'],
               ['Woodoo Braclet', 'Recover 100 mana', 70, 100, 't'],
               ['Book of Witchcraft', 'Permanently increase Health by 100', 1200, 100, 'p'],
               ['Book of the Damned', 'Permanently increase Health by 300', 2000, 300, 'p']]
    att_item = [['Knife', '+5 Attack', 90, 5, 'p'], ['Sword', '+10 Attack', 170, 10, 'p'],
                ['Spear', '+20 Attack', 300, 20, 'p'], ['Cross Bow', '+40 Attack', 500, 40, 'p'],
                ['The First Blade', '+100 Attack', 750, 100, 'p']]

    print_slow(f'Welcome {name}.... What are you looking for?')
    print('(a). Health')
    print('(b). Mana')
    print('(c). Damage')
    print('(d). Return')
    shop_choice = input()
    shop_choice = shop_choice.lower()
    if shop_choice in ['a', 'health']:
        clear_output()
        while True:
            print('Health Item----------------------------------Your Gold Balance: ' + str(gold))
            print("{:<8} {:<20} {:<40} {:<16}".format('Choice', 'Item', 'Description', 'Price (In Gold)'))
            for i in range(len(hp_item)):
                print("{:<8} {:<20} {:<40} {:<16}".format(str(i), hp_item[i][0], hp_item[i][1], str(hp_item[i][2])))

            # print('5. Return')
            print("{:<8} {:<20}".format('5', 'Return'))
            print('Select any number to buy item')

            buy_hp_choice = int(input())
            if buy_hp_choice == 5:
                clear_output()
                break
            while buy_hp_choice not in [0, 1, 2, 3, 4]:
                print('Please enter valid choice')
                buy_hp_choice = int(input())
            for i in range(len(hp_item)):
                if buy_hp_choice == i:
                    if gold >= hp_item[i][2]:
                        gold_change(0, hp_item[i][2])
                        add_to_inventory(hp_item[i][0], 'hp', hp_item[i][3], hp_item[i][2], hp_item[i][4])
                        clear_output()
                        print('Bought')
                    else:
                        clear_output()
                        print('Not enough gold')
        shop()
    elif shop_choice in ['b', 'mana']:
        clear_output()
        while True:
            print('Mana Items----------------------------------Your Gold Balance: ' + str(gold))
            print("{:<8} {:<20} {:<40} {:<16}".format('Choice', 'Item', 'Description', 'Price (In Gold)'))
            for i in range(len(mp_item)):
                print("{:<8} {:<20} {:<40} {:<16}".format(str(i), mp_item[i][0], mp_item[i][1], str(mp_item[i][2])))
            # print('5. Return')
            print("{:<8} {:<20}".format('5', 'Return'))
            print('Select any number to buy item')

            buy_hp_choice = int(input())
            if buy_hp_choice == 5:
                clear_output()
                break
            while buy_hp_choice not in [0, 1, 2, 3, 4]:
                print('Please enter valid choice')
                buy_hp_choice = int(input())
            for i in range(len(mp_item)):
                if buy_hp_choice == i:
                    if gold >= mp_item[i][2]:
                        gold_change(0, mp_item[i][2])
                        add_to_inventory(mp_item[i][0], 'mp', mp_item[i][3], mp_item[i][2], mp_item[i][4])
                        clear_output()
                        print('Bought')
                    else:
                        clear_output()
                        print('Not enough gold')
        shop()
    elif shop_choice in ['c', 'damage']:
        clear_output()
        while True:
            print('Damage Items----------------------Your Gold Balance: ' + str(gold))
            print("{:<8} {:<20} {:<40} {:<16}".format('Choice', 'Item', 'Description', 'Price (In Gold)'))
            for i in range(len(att_item)):
                print("{:<8} {:<20} {:<40} {:<16}".format(str(i), att_item[i][0], att_item[i][1], str(att_item[i][2])))
            # print('5. Return')
            print("{:<8} {:<20}".format('5', 'Return'))
            print('Select any number to buy item')

            buy_hp_choice = int(input())
            if buy_hp_choice == 5:
                clear_output()
                break
            while buy_hp_choice not in [0, 1, 2, 3, 4]:
                print('Please enter valid choice')
                buy_hp_choice = int(input())
            for i in range(len(att_item)):
                if buy_hp_choice == i:
                    if gold >= att_item[i][2]:
                        gold_change(0, att_item[i][2])
                        add_to_inventory(att_item[i][0], 'dmg', att_item[i][3], att_item[i][2], att_item[i][4])
                        clear_output()
                        print('Bought')
                    else:
                        clear_output()
                        print('Not enough gold')
        shop()
    elif shop_choice in ['d', 'return']:
        clear_output()
        what_next()
    elif shop_choice not in ['a', 'health', 'b', 'mana', 'c', 'damage', 'd', 'return']:
        clear_output()
        print('Invalid choice')
        shop()

    # return ()


def show_inventory():
    """Inventory to purchase or sell.. If you sell you will get gold in return as per it cost
    If you purchase you will have to pay gold...
    Selling price is half of it's cost"""
    global inventory
    print('Inventory')
    print('')
    val = '-'
    print("{:<8} {:<8} {:<8} {:<8} {:<20}".format('Choice', 'Item', 'Type', 'Effect', 'Selling Price'))
    for i in range(len(inventory)):
        if inventory[i][1] == 'hp':
            val = 'Health'
        elif inventory[i][1] == 'mp':
            val = 'Mana'
        elif inventory[i][1] == 'dmg':
            val = 'Damage'
        else:
            val = inventory[i][1]
        print("{:<8} {:<8} {:<8} {:<8} {:<20}".format(str(i), inventory[i][0], val, '+'+str(inventory[i][2]), str(inventory[i][3])))
    print('Select number to use/sell item..')
    inventory_choice = int(input())
    while inventory_choice < 0:
        print('Please enter valid value')
        inventory_choice = int(input())
    while inventory_choice >= len(inventory):
        print('Please enter valid value')
        inventory_choice = int(input())
    for i in range(len(inventory)):
        if inventory_choice == i:
            print('Do you want to use or buy: ' + inventory[i][0])
            print('(a). Use')
            print('(b). Sell (' + str(inventory[i][3]) + ' Gold)')
            print('(c). Return')
            use_buy_choice = input()
            use_buy_choice = use_buy_choice.lower()
            while use_buy_choice not in ['a', 'use', 'b', 'sell', 'c', 'return']:
                print('Please enter valid choice')
                use_buy_choice = input()
            if use_buy_choice in ['a', 'use']:
                if inventory[i][4] == 't':
                    if inventory[i][1] == 'hp':
                        hp_change(inventory[i][2], 0)
                    elif inventory[i][1] == 'mp':
                        mp_change(inventory[i][2], 0)
                elif inventory[i][4] == 'p':
                    if inventory[i][1] == 'hp':
                        max_hp_change(inventory[i][2])
                    elif inventory[i][1] == 'mp':
                        max_mp_change(inventory[i][2])
                    elif inventory[i][1] == 'dmg':
                        dmg_change(inventory[i][2])
                del inventory[i]
                print('Item used please press enter to return')
                input()
                clear_output()
                break
            elif use_buy_choice in ['b', 'sell']:
                gold_change(inventory[i][3], 0)
                del inventory[i]
                print('Item used please press enter to return')
                input()
                clear_output()
                break
            elif use_buy_choice in ['c', 'return']:
                clear_output()
                break
    # return ()


def dark_forest():
    """Its one land which user have to pass after successfully completing all of its huddles/roadblocks"""
    global enemy_details
    print_slow('The First Land\nWelcome to the Dark Forest. The trees here hide many secrets')
    print_slow('You will encounter people, creature and unknown beings who require your help.')
    print_slow('You can choose to help them or continue your adventure. By helping them you might get rewarded.')
    input('Press Enter to continue')
    print_slow('You proceed into the jungle. This jungle seems weird to you.')
    print_slow('While passing through you notice one sad old man in the woods....')
    print('What you do? \n(a). Approch or \n(b). Skip')
    dark_forest_choice = input()
    dark_forest_choice = dark_forest_choice.lower()
    while dark_forest_choice not in ['a', 'approch', 'b', 'skip']:
        print('Enter valid choice')
        dark_forest_choice = input()
        dark_forest_choice = dark_forest_choice.lower()
    if dark_forest_choice in ['a', 'approch']:
        print_slow('You approach the old man. And ask him what happened.')
        print_slow('Old Man: I lost my sheep somewhere north in the jungle. And I am afraid to go in that part of the jungle.')
        print_slow('Old Man: Can you help me by finding my sheep?')
        print('Would you like to help him? \n(a). Yes or\n (b). No')
        old_man_choice = input()
        old_man_choice = old_man_choice.lower()
        while old_man_choice not in ['a', 'yes', 'b', 'no']:
            print('Enter valid choice')
            old_man_choice = input()
            old_man_choice = old_man_choice.lower()
        if old_man_choice in ['a', 'yes']:
            print_slow('You agreed to help him and went in the direction he pointed.')
            print_slow('You heard something... looks like the voice of animal trapped in a cage.')
            print_slow('You followed the voice and encountered a man-sized spider.')
            print_slow('Need to kill this spider to rescue the sheep.')
            input('press enter to continue.')
            clear_output()
            enemy_details = ['Big Spider', 500, 10, 20]
            fight()
            print_slow('Sheep was rescued. You return it to Old Man.')
            print_slow('Old Man: Thank you stranger. I have nothing to offer you.')
            print_slow('Old Man: But will give you one advice, there is a mighty Dragon in the north. It might be your destiny.')
        elif old_man_choice in ['b', 'no']:
            print_slow('Left the Old Man behind.')
    elif dark_forest_choice in ['b', 'skip']:
        print_slow('You didn\'t bother to look..')
    print_slow('You moved forward.')
    print_slow('As you move deep into the forest, the forest was so dense that even sunlight was not reaching the ground.')
    print_slow('There was constant mumbling of someone, but as far as your eyes can see, there were no living creatures.')
    print_slow('Suddenly a tree in front of you asked you for some water.')
    print_slow('You were shocked to hear tree speaking.')
    print_slow('Tree: In this jungle, trees can speak to each other and warn in case of any danger.')
    print_slow('Do you want to water the tree? \n(a). Yes or \n(b). No')

    dark_forest_choice1 = input()
    dark_forest_choice1 = dark_forest_choice1.lower()
    while dark_forest_choice1 not in ['a', 'yes', 'b', 'no']:
        print('Enter valid choice')
        dark_forest_choice1 = input()
        dark_forest_choice1 = dark_forest_choice1.lower()
    if dark_forest_choice1 in ['a', 'yes']:
        WaterSound = mixer.Sound("watering.mp3")
        WaterSound.play()
        time.sleep(3)
        print_slow('You watered the tree, it dropped an apple...')
        print('Apple added to inventory')
        input('Press enter to continue...')
        add_to_inventory('Apple', 'hp', 20, 20, 't')
    elif dark_forest_choice1 in ['b', 'no']:
        print('You left the tree..')
    print_slow('In this forest, it was difficult to tell whether its day or night')
    print_slow('While moving you encounter an enemy, there is no chance to run away.')
    enemy()
    fight()
    input('Press enter to continue...')
    clear_output()
    print_slow('After the fight you notice smoke coming from not too far place.')
    print_slow('You move in the direction of the smoke.')
    print_slow('There was a small hotel and looks like you were able to cross this forest.')
    print_slow('Do you want to rest? \n(a). Yes Cost 30 Gold and recover Health and Mana or \n(b). No')
    dark_forest_choice2 = input()
    dark_forest_choice2 = dark_forest_choice2.lower()
    while dark_forest_choice2 not in ['a', 'yes', 'b', 'no']:
        print('Enter valid choice')
        dark_forest_choice2 = input()
        dark_forest_choice2 = dark_forest_choice2.lower()
    if dark_forest_choice2 in ['a', 'yes']:
        print_slow('You decided to take rest')
        hp_change(100000, 0)
        mp_change(100000, 0)
        gold_change(0, 30)
        input('Press enter to continue')
    elif dark_forest_choice2 in ['b', 'no']:
        print('You do not want rest')
    print_slow('You can explore the nearby area.')
    # return ()

def print_win():
    """ Display if user wins the game.Motivation in such fonts.."""
    print('\n\n\n')
    print(' \ \ / / _ \| | | | \ \    / /_ _| \| | \n'
          '  \ V / (_) | |_| |  \ \/\/ / | || .` | \n'
          '   |_| \___/ \___/    \_/\_/ |___|_|\_| \n')


def road_of_sacrifices():
    """Its 2nd and last land which user have to pass after successfully completing all of its huddles/roadblocks
    If user able to complete all it user will win otherwise loose...
    Do or Die if you are an adventurer otherwise you can skip but, it will prove user's adventurer level less."""
    global enemy_details
    print_slow('Welcome to Last Land...\tThe Road of Sacrifices.....')
    print_slow('This place grants things you wished or you desired.')
    print_slow('But everything comes at a price.')
    print_slow('At this day no one has crossed this road without any sacrifices.')
    print_slow('Some have sacrificed their dearest thing.')
    print_slow('Some have sacrificed their loved ones.')
    print_slow('And....')
    print_slow('Someone paid the price with their life.')
    print_slow('You can hear many crying souls, those who are still trapped in this place.')
    print_slow('There is a child weeping. Do you want to check him? \n(a). Yes or \n(b). No')
    road_choice = input()
    road_choice = road_choice.lower()
    while road_choice not in ['a', 'yes', 'b', 'no']:
        print('Enter valid choice')
        road_choice = input()
        road_choice = road_choice.lower()
    if road_choice in ['a', 'yes']:
        print_slow('You walk to the child. And it turns out to be a soul. Dead a long time ago...')
        print_slow('It tried to attack and you now need to deal with it..')
        enemy_details = ['Dead Child', 150, 25, 30]
        fight()
        print('For killing that Dead Child you got 50 gold')
        gold_change(50, 0)
        input('Press enter to continue')
    elif road_choice in ['b', 'no']:
        print('No need to take the risk.')
    print_slow('You move forward. Further on the way, you notice one road sign.')
    print_slow('Out of curiosity, you read that sign.')
    print_slow('Pointing toward the path it was mention: DO NOT TAKE THIS ROUTE with skull drew with blood.')
    print_slow('You can continue your quest or do you want to find out where that path leads?')
    print_slow('Do you want to go on that dangerous path? \n(a). Yes or \n(b). No')
    road_choice = input()
    road_choice = road_choice.lower()
    while road_choice not in ['a', 'yes', 'b', 'no']:
        print('Enter valid choice')
        road_choice = input()
        road_choice = road_choice.lower()
    if road_choice in ['a', 'yes']:
        print_slow('A true hero never fears little challenge.')
        print_slow('You continue on that path. And after walking for a while, this seems to no way near danger.')
        print_slow('So after all, the sign was all lie... Wait there was another road sign ahead')
        print_slow('This road sign says:')
        print_slow('No one have return after crossing this point. GO BACK!!!')
        print_slow('Do you wnat to continue(WARNING: You might get killed) \n(a). Yes or \n(b). No')
        no_return_choice = input()
        no_return_choice = no_return_choice.lower()
        while no_return_choice not in ['a', 'yes', 'b', 'no']:
            print('Enter valid choice')
            no_return_choice = input()
            no_return_choice = no_return_choice.lower()
        if no_return_choice in ['a', 'yes']:
            print_slow('You crossed the point.')
            print_slow('Suddenly you were at a different place, in front of stand the Horse of Death')
            print_slow('Horse of Death: No mortal have ever dare to cross that point. And the one who have never returned.')
            print_slow('Horse of Death: Give me the answer of my riddle and earn you freedom.')
            print_slow('Horse of Death: Failed to answer will be rewarded with death. You have 3 chance.')
            print_slow('Horse of Death: Listen carefully')
            print_slow('\n\t"I never was, am always to be. No one ever saw me, nor ever will.')
            print_slow('\tAnd yet I am the confidence of all, To live and breathe on this terrestrial ball."')
            print('')
            print_slow('You only have 3 chance to guess...(Avoid mistyping)')
            riddle_chance = 3
            riddle_result = 'death'
            while riddle_chance > 0:
                answer = input('Your Answer: ')
                answer = answer.lower()
                riddle_chance -= 1
                if answer == 'tomorrow':
                    riddle_result = 'survived'
                    break
                else:
                    print(str(riddle_chance) + ' Chance left')

            if riddle_result == 'death':
                print_slow('You should have trusted road signs....')
                print_slow('Died')
                input('Press enter to exit')
                quit()
            print_slow('Well done you have answered the riddle correctly')
            print_slow('Horse of Death: You are the first to answer this. Here, take this')
            print('You recieved Potion of Rebirth use to to recover health to max')
            add_to_inventory('Potion of Rebirth', 'hp', 9999999, 600, 't')
            print('You did it..')
            print_win()
            quit()
        elif no_return_choice in ['b', 'no']:
            print_slow('You return back. Sometime its good to play by rules.\n But the game ends as it was last huddle..')
            # input('Press enter to exit')
            quit()
    elif road_choice in ['b', 'no']:
        print('No need to take the risk.\n But the game ends as it was last huddle..')
        quit()
    print_slow('move forward')
    # return ()


def forward():
    """Locations list commented can be define if we explore this implementation further
    Currently, only two locations function defined to complete this mini game"""
    global current_location, lc
    location_list = ['Dark Forest', 'Road of Sacrifices', 'The Swamp']
    # location_list = ['Road of Sacrifices', 'The Swamp',
    #                  'Land of First Mortals', 'Cemetery of Fallen Knights',
    #                  'Garden of Last Queen', 'Sea of Unknown Creature',
    #                  'Ghost Village', 'Blood River', 'Land of Living Dead',
    #                  'Frost Land', 'Winter Hell', 'Ruins of Dragon']
    current_location = location_list[lc]
    lc = lc + 1
    if lc >= 3:
        input("No further locations to explore...Thanks for playing..")
    if current_location == 'Dark Forest':
        dark_forest()
    elif current_location == 'Road of Sacrifices':
        road_of_sacrifices()
    input("Press Enter to continue...")
    clear_output()
    # return ()


def what_next():
    """It shows the user for next next steps after overcoming disaster or initial
        Steps....To show variery of questions list used as every time single statement makes user bored.."""
    global inventory, current_location
    random_what_next = ['What you want to do next?', 'Your next choice.', 'Where to go adventurer?',
                        'Waiting for you decision.', 'Point the direction explorer.', 'Select your move.']

    print_slow(random.choice(random_what_next))
    print('Current Location:', current_location)
    print('(a). Shop')
    print('(b). Search')
    print('(c). Forward')
    print('(d). Inventory')
    print('(e). Quit')

    next_choice = input()
    next_choice = next_choice.lower()
    clear_output()
    if next_choice in ['a', 'shop']:
        shop()
        what_next()
    elif next_choice in ['b', 'search']:
        search()
        what_next()
    elif next_choice in ['c', 'forward']:
        forward()
        what_next()
    elif next_choice in ['d', 'inventory']:
        show_inventory()
        what_next()
    elif next_choice in ['e', 'quit']:
        print('You choose to quit!')
        quit()
    else:
        while next_choice not in ['a', 'shop', 'b', 'search', 'c', 'forward','e','quit']:
            print('Enter valid choice')
            what_next()


def help_fuction():
    print('Three divisions of the game.\nEach has diffrent default criterias..')
    print('Strength Division')
    print("{:<5} {:<12} {:<10} {:<18}".format('', 'Health/Mana', 'Default', 'Regenration Rate'))
    print("{:<5} {:<12} {:<10} {:<18}".format('', 'Health', '150', '3'))
    print("{:<5} {:<12} {:<10} {:<18}".format('', 'Mana', '100', '1'))
    print("{:<5} {:<12} {:<10} {:<18}".format('', 'Attack', '25', '-'))
    print("{:<5} {:<12} {:<10} {:<18}".format('', 'Gold', '1000', 'Random'))
    print("{:<5} {:<15} {:<10} {:<18}".format('', 'Special-Skills', 'Power', 'Minimum Mana'))
    print("{:<5} {:<15} {:<10} {:<18}".format('', 'Stomp', '100', '20'))
    print("{:<5} {:<15} {:<10} {:<18}".format('', 'Mighty Hammer', '250', '35'))
    print("{:<5} {:<15} {:<10} {:<18}".format('', 'Body Smash', '300', '40'))

    print('\nAgile Division')
    print("{:<5} {:<12} {:<10} {:<18}".format('', 'Health/Mana', 'Default', 'Regenration Rate'))
    print("{:<5} {:<12} {:<10} {:<18}".format('', 'Health', '100', '2'))
    print("{:<5} {:<12} {:<10} {:<18}".format('', 'Mana', '100', '2'))
    print("{:<5} {:<12} {:<10} {:<18}".format('', 'Attack', '50', '-'))
    print("{:<5} {:<12} {:<10} {:<18}".format('', 'Gold', '1000', 'Random'))
    print("{:<5} {:<15} {:<10} {:<18}".format('', 'Special-Skills', 'Power', 'Minimum Mana'))
    print("{:<5} {:<15} {:<10} {:<18}".format('', 'Criticle Strike', '120', '25'))
    print("{:<5} {:<15} {:<10} {:<18}".format('', 'Swift Attack', '200', '30'))
    print("{:<5} {:<15} {:<10} {:<18}".format('', '100 Cuts', '350', '45'))

    print('\nMagic Division')
    print("{:<5} {:<12} {:<10} {:<18}".format('', 'Health/Mana', 'Default', 'Regenration Rate'))
    print("{:<5} {:<12} {:<10} {:<18}".format('', 'Health', '100', '1'))
    print("{:<5} {:<12} {:<10} {:<18}".format('', 'Mana', '150', '3'))
    print("{:<5} {:<12} {:<10} {:<18}".format('', 'Attack', '25', '-'))
    print("{:<5} {:<12} {:<10} {:<18}".format('', 'Gold', '1000', 'Random'))
    print("{:<5} {:<15} {:<10} {:<18}".format('', 'Special-Skills', 'Power', 'Minimum Mana'))
    print("{:<5} {:<15} {:<10} {:<18}".format('', 'Magic Blast', '60', '10'))
    print("{:<5} {:<15} {:<10} {:<18}".format('', 'Thunder Storm ', '250', '20'))
    print("{:<5} {:<15} {:<10} {:<18}".format('', 'Fire & Ice', '400', '30'))

    print('\nEnemies...')
    print("{:<5} {:<15} {:<10} {:<20} {:<20}".format('', 'Name', 'Health', 'Min Attack', 'Max Attack'))
    print("{:<5} {:<15} {:<10} {:<20} {:<20}".format('', 'Goblin', '500', '5', '15'))
    print("{:<5} {:<15} {:<10} {:<20} {:<20}".format('', 'Corrupt Soul', '750', '10', '20'))
    print("{:<5} {:<15} {:<10} {:<20} {:<20}".format('', 'Rogue Soldier', '1000', '15', '25'))

    print('\nYou have to select the options and play..Not everytime all options are available..')
    print('\nSearch will drop gold or enemy.. Fight or Run [Not the all time available option] '
          'Do the adventure by going forward, till end....by saving your health and wealth..'
          'Make wise choice..Good Luck')
    clear_output()
    welcome()


def welcome():
    """The initial function call which is the entry point of the game.."""

    print('************************************')
    print('*     Welcome to Epic Adventure    *')
    print('*     -Play                        *')
    print('*     -Help                        *')
    print('*     -Quit                        *')
    print('************************************')
    print_slow('Please select one option to proceed...')
    welcome_choice = input('Choice: ')
    welcome_choice = welcome_choice.lower()
    if welcome_choice == 'play':
        clear_output()
        player_config()
    elif welcome_choice == 'help':
        print('Need help')
        help_fuction()
    elif welcome_choice == 'quit':
        print('Want to quit')
        quit()
    else:
        while welcome_choice not in ['play', 'help', 'quit']:
            print('Please enter valid choice')
            welcome_choice = input()
            welcome_choice = welcome_choice.lower()
        if welcome_choice == 'play':
            clear_output()
            player_config()
        elif welcome_choice == 'help':
            print('Need help')
            help_fuction()
        elif welcome_choice == 'quit':
            print('Want to quit!')
            quit()


def player_config():
    """After welcoming user asking for his/her name simple validations used as max & empty length of name
        choices to division.. In which division user wants to play.."""
    print_slow('Hello adventurer welcome....')
    print_slow('What shall I call you?')
    player_name = input()
    if player_name == '':
        while player_name == '':
            print('Please enter valid name')
            player_name = input()
    elif len(player_name) > 15:
        while len(player_name) > 15:
            print('Please select name with 15 or less character')
            player_name = input()
    print_slow('There are three division from which you can choose one.')
    print('(a). Strength')
    print('(b). Agile')
    print('(c). Magic')
    class_choice = input()
    if class_choice in ['a', 'Strength']:
        class_choice = 'Strength'
    elif class_choice in ['b', 'Agile']:
        class_choice = 'Agile'
    elif class_choice in ['c', 'Magic']:
        class_choice = 'Magic'
    else:
        while class_choice not in ['a', 'Strength', 'b', 'Agile', 'c', 'Magic']:
            print('Enter valid choice')
            class_choice = input()
            if class_choice in ['a', 'Strength']:
                class_choice = 'Strength'
            elif class_choice in ['b', 'Agile']:
                class_choice = 'Agile'
            elif class_choice in ['c', 'Magic']:
                class_choice = 'Magic'

    player(player_name, class_choice)
    print_slow('Now you are ready for the quest.')
    print_slow('You are out of your cabin. In the jungle.....')
    print_slow('Beware of the creatures living in this world. You can randomly encounter them and need to fight.')
    print_slow('Make sure you have enough item in your inventory to survive this quest.')
    print_slow('Shop will only be available at certain checkpoints only.')
    print_slow('Good luck.....')
    input("Press Enter to continue...")
    clear_output()
    what_next()

#The one and only entry point call of the game...
#Audio Track For Background
pygame.mixer.init()
mixer.music.load('background.mp3')
mixer.music.play(-1)
welcome()