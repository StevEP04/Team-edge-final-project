# #Start of the game
# #NAME: S-class Hunter
# #Classes:
user_playing = True
player_items = []
import random


# START OF THE FIGURES AND SOME ANIMATION
def welcome_user(wlcm):
    if wlcm == True:
        print("\n\n")
        print("       |\                     / |||||||||||| ||           ||||||||||||| |||||||||||| ||         || ||||||||||||    ||")
        print("        |\                   /  |/           ||           |             |          | || \      / | |/              ||")
        print("         |\                 /   |            ||           |             |          | ||  \    /  | |               ||")
        print("          |\               /    |\           ||           |             |          | ||   \  /   | |\              ||")
        print("           |\             /     |||||||||||| ||           |             |          | ||    \/    | ||||||||||||    ||")
        print("            |\     /\    /      |/           ||           |             |          | ||          | |/              ||")
        print("             |\   /  \  /       |            ||           |             |          | ||          | |               ||")
        print("              |\ /    \/        |\           ||           |             |          | ||          | |\              ||")
        print("               |\/    \/        |||||||||||| |||||||||||| ||||||||||||| |||||||||||| ||          | ||||||||||||    ◉\n")
        print("||||||||||||||||||| |||||||||||||                ")
        print("        |||         |           |               ")
        print("        |||         |           |               ")
        print("        |||         |           |               ")
        print("        |||         |           |               ")
        print("        |||         |           |               ")
        print("        |||         |           |               ")
        print("        |||         |           |               ")
        print("        |||         |||||||||||||               ")
        print("               ")
        print("               ")
        print("        |           ||        | |||||||||||||   ||        |  ||||||||   ||||||||  ||         || ||||||||||||| ||          |   ///////////               ")
        print("       | |          | |       | |           |   | |       |    ||    | |     ||   || \      / | |           | ||          |  |/               ")
        print("      |   |         |  |      | |           |   |  |      |       |   |   |       ||  \    /  | |           | ||          |  ||               ")
        print("     |     |        |   |     | |           |   |   |     |         |   |         ||   \  /   | |           | ||          |  |\               ")
        print("    |       |       |    |    | |           |   |    |    |         |   |         ||    \/    | |           | ||          |   \////////\                ")
        print("   |||||||||||      |     |   | |           |   |     |   |         |   |         ||          | |           | ||          |            \|               ")
        print("  |           |     |      |  | |           |   |      |  |         |   |         ||          | |           | ||          |            ||               ")
        print(" |             |    |       | | |           |   |       | |         |   |         ||          | |           | ||          |            /|               ")
        print("|               |   |        || |||||||||||||   |        ||         |||||         ||          | ||||||||||||| |||||||||||||  ///////////                \n")

        print("|||||||||||||||||||  ||          |   /////////// ||||||||||||||||||| ||| ||||||||||||| ||||||||||||               ")
        print("       |||          ||          |  |/                   |||         ||| |             |/               ")
        print("       |||          ||          |  ||                   |||         ||| |             |               ")
        print("       |||          ||          |  |\                   |||         ||| |             |\               ")
        print("       |||          ||          |   \////////\          |||         ||| |             ||||||||||||               ")
        print("       |||          ||          |            \|         |||         ||| |             |/               ")
        print("|||    |||          ||          |            ||         |||         ||| |             |               ")
        print(" ||||  |||          ||          |            /|         |||         ||| |             |\               ")
        print("   \||||/           |||||||||||||  ///////////          |||         ||| ||||||||||||| ||||||||||||               ")
def dragon_smoke(smoke):
    if smoke == True:
        print("Somthing here")

def god_mode(activation):
    if activation == True:
        print("\n|----------- |----------| |    \             ")
        print("|            |          | |      \          ")
        print("|----------| |          | |        |       ")
        print("|          | |          | |       /        ")
        print("|__________| |----------| |     /           \n")
        print("| \       /| |----------| |    \     |--------")
        print("|   \   /  | |          | |      \   |        ")
        print("|     |    | |          | |        | |-----  ")
        print("|          | |          | |       /  |       ")
        print("|          | |----------| |     /    |--------\n")


def sword(active):
    if active == True:
        print("\n            /\         ")
        print("           / 和\         ")
        print("           | 的|        ")
        print("           | 和|        ")
        print("           | 平|        ")
        print("           | 破|        ")
        print("           | 冰|        ")
        print("           | 爱|        ")
        print("           | 船|        ")
        print("      \--\ |和和| /--/        ")
        print("           \.../        ")
        print("            |☯|        ")
        print("            |☯|        ")
        print("             ☯          \n")


#------------------------------------------------------------------------------------


#THIS IS WHERE I CAN CREATE CAVES AND WHAT IS INSIDE OF IT
class Rooms:
    def __init__(self, name, intro, monster, items):
        self.name = name
        self.intro = intro
        self.monster = monster
        self.items = items
        self.paths = []
        self.is_lock = False
        self.unlock = ""

    def __repr__(self):
        return f"You can go to {self.name}"

        
    def enter(self, player_items):
        if self.is_lock == False or self.unlock in player_items:
            print(self.intro)
        else:
            print(f"You need the {self.unlock}")

    def user_items(self):
        print(self.items)


#------------------------------------------------------------------------------------

list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))


#THIS IS THE FINAL BATTLE WITH THE DRAGON "DARKSMOKE"
class Final_battle:
    global player_items

    # list1 = [0, 1, 2, 3, 4, 5]
    # edge = random.choice(list1)
    def __init__(self, name, health, powers, items):
        self.name = name
        self.health = health
        self.powers = powers
        self.items = items

    def __repr__(self):
        return f"{self.name}"


#------------------------------------------------------------------------------------

#INTRODUCTION AND HOW TO MOVE FROM CAVE TO CAVE
intro_1 = "\nThis is room 1. Time to give that company what they deserve. how much is 2+2?"
intro_2 = "\nUh Oh! you entered the wrong room, this room, has given the police able to track your location, there for you got arrested. better luck next time."
intro_3 = "\nnice one, getting to the right area. keep going, your help is needed."
intro_4 = "\nNo No No! this was not what was supposed to happen. this room is a trap! now you're going to get arrested."
intro_5 = "\ngood one, but you know what they say. take your time and hurry up."
intro_6 = "\nThis is room 6"
intro_7 = "\nThis is room 7"
intro_8 = "\nThis is room 8"
intro_9 = "\nwait, what? this isn't right. this was a trap the whole time! well it's time to get some nice prison food. ;-;"
intro_10 = "\nNO! this can't be right! we were so close."
intro_11 = "\nThis is room 11"
intro_12 = "\nThis is room 12"

room1 = Rooms("room1", intro_1, False, [])
room2 = Rooms("room2", intro_2, False, [])
room3 = Rooms("room3", intro_3, False, ["letter"])
room4 = Rooms("room4", intro_4, False, ["sword"])
room5 = Rooms("room5", intro_5, False, ["key"])
room6 = Rooms("room6", intro_6, False, [])
room7 = Rooms("room7", intro_7, True, [])
# room7.is_lock = True
# room7.unlock = "key"
room8 = Rooms("room8", intro_8, False, ["health_potion", "unknown_potion"])
room9 = Rooms("room09", intro_9, True, [])
room10 = Rooms("room10", intro_10, True, [])
room11 = Rooms("room11", intro_11, True, [])
room12 = Rooms("room12", intro_12, True, [])

room1.paths = [room2, room3]
room2.paths = [room1]
room3.paths = [room1, room5, room4, room6]
room4.paths = [room3]
room5.paths = [room7, room8, room3]
room6.paths = [room9, room3]
room7.paths = [room5, room10, room11]
room8.paths = [room5, room12]
room9.paths = [room6]
room10.paths = [room7]
room11.paths = [room7, room12]
room12.paths = [room11, room8]

current_cave = room1

#------------------------------------------------------------------------------------

#THIS IS WHERE THE USER STARTS TO PLAY THE GAME
user_start = input("If your ready to start the game type 'start': \n").lower()
if user_start == "start":
    welcome_user(True)
    print("\n\t\tWelcome Anon_9312 \n\tA big company by the name of chicken network \n\ttook ideas from a very small company by the name of yoyo.")
    print("\tHack them and delete the information stolen from \n\tyoyo to get justice over chicken network")
    print("\tBest of luck Anon_9312!\n")
    print("\nType 'Help' to learn how to play")
    room1.enter(player_items)


def player_question():
    reply = input("What do you want to do ?\n").lower()
    return reply


def nav(input):
    global current_input
    global current_cave
    global player_items
    print("\nchecking question :  " + input)
    current_input = input

    splitting = current_input.split(" ")


    if current_input == "help":
        print(
            "\n\tType 'look' to look everything in that room\n \tType 'move ____' and the room you want to move"
        )
        print(
            "\tType 'use' to use a item you have\n\tType 'take' to add an item\n\tType 'room' to know where can you go"
        )
        print("\tType 'attack' hack the company in a room\n")
    
    # elif splitting[0] == "move":
    #     move = False
    #     for rmm in current_cave.paths:
    #         if splitting[1] == rmm.name:
    #             current_cave = rmm
    #             move = True
    #             rmm.enter(player_items)
    #     if move == False:
    #         print("You cannot move to that room")

    # elif splitting[0] == "look":
    #     for item in current_cave.items:
    #         print("There is: " + item)

    # elif splitting[0] == "take":
    #     taking_item = str(splitting[1])
    #     c_room = current_cave
    #     print(taking_item)

    #     if taking_item in current_cave.items:
    #         player_items.append(taking_item)
    #         print("Your current items is/are: " + str(player_items))
    #     else:
    #         print("You can't take anything")

    # elif splitting[0] == "use":
    #     item_use = splitting[1]
    #     if item_use in player_items:
    #         print("You can use that item!")

    # elif splitting[0] == "room":
    #     print(str(current_cave.paths))

    # elif splitting[0] == "attack" and current_cave.monster == True:
    #     print("\n\n\n")
    #     monster_vs(True)

    #     print(
    #         "Yoohin Han : I'll have to kill you since you killed my little brother, I don't have any choice\n "
    #     )
    # elif splitting[0] == "attack" and current_cave.monster == False:
    #     print("There is nothing to hack in this room")
    # elif splitting[0] == "die":
    #     print("You have die!")
    # else:
    #     print("You can't do that")


#------------------------------------------------------------------------------------
answer = input("This is cave1 there is a high chance that the police is traking you \nDo you want to escape or stay at your place\nType 'escape' to escape or 'stay' to stay at yor home>>>\n")

if answer == "escape":
    print("\nYou have made a good choice\n the police was traking your steps, be more careful!")
elif answer == "stay":
    print("\nThe police arrested you, You have lost!")
    exit()

print("You have sucesfully passed level 1 you have to hack the company now!\n if you do not then they are going to win billions stealing from people!")
answer2 = input("you have 3 options: not hack, hack them in a way \nType 'hack' to hack them 'not hack' to not hack them")
 if answer == "not hack":
     print("vhjfyfy")
while user_playing:
    nav(player_question())




#second part




# ||||||||||||||||||| |||||||||||||
#         |||         |           |
#         |||         |           |
#         |||         |           |
#         |||         |           |
#         |||         |           |
#         |||         |           |
#         |||         |           |
#         |||         |||||||||||||


#            |           ||        | |||||||||||||   ||        |  ||||||||   ||||||||  ||         || ||          |   ///////////
#           | |          | |       | |           |   | |       |    ||    | |     ||   || \      / | ||          |  |/
#          |   |         |  |      | |           |   |  |      |       |   |   |       ||  \    /  | ||          |  ||
#         |     |        |   |     | |           |   |   |     |         |   |         ||   \  /   | ||          |  |\
#        |       |       |    |    | |           |   |    |    |         |   |         ||    \/    | ||          |   \////////\ 
#       |||||||||||      |     |   | |           |   |     |   |         |   |         ||          | ||          |            \|
#      |           |     |      |  | |           |   |      |  |         |   |         ||          | ||          |            ||
#     |             |    |       | | |           |   |       | |         |   |         ||          | ||          |            /|
#    |               |   |        || |||||||||||||   |        ||         |||||         ||          | |||||||||||||  /////////// 

#    |||||||||||||||||||  ||          |   /////////// ||||||||||||||||||| ||| ||||||||||||| ||||||||||||
#            |||          ||          |  |/                   |||         ||| |             |/
#            |||          ||          |  ||                   |||         ||| |             |
#            |||          ||          |  |\                   |||         ||| |             |\
#            |||          ||          |   \////////\          |||         ||| |             ||||||||||||
#            |||          ||          |            \|         |||         ||| |             |/
#     |||    |||          ||          |            ||         |||         ||| |             |
#      ||||  |||          ||          |            /|         |||         ||| |             |\
#        \||||/           |||||||||||||  ///////////          |||         ||| ||||||||||||| ||||||||||||


#             =====
#           ||     ||
#          ||       ||
#  ________||___
# |            |
# |     O      |
# |    /_\     |
# |____________|

#      /====\
#    ||     ||
#   ||       ||
#  ||________ ||
# |             |
# |      O      |
# |     /_\     |
# |_____________|

#   ./ \     / \      / \.
#  |    \__/     \__/    |
#  |         |||         |
#  |         |||         |
#  |         |||         |
#  |         |||         |
#  |         |||         |
#   \        ___         /
#    \       |||        /
#     \                /
#      \______________/


#         ||
#        |  |
#       |    |
#      |  ||  |
#     |   ||   |
#    |    ||    |
#   |     __     |
#  |      ||      |
# |________________|






        #       |
        #       |
        #       |
        #       |   
        #       /\ 
        #     /
        #   /
#       /     / \      ____ ____      / \
#     /     -  |  \    \       /    /  |
#   /     -    |   \    \     /    /   |
#  |    -      |     \ / \   / \ /     |
# |   /        |       |  \ /  |       |
# |  /         |       /   |   \       |
# | /             \    /   |   \    /
# |/                 \ /   |   \ /
#                     /    |    \
#   |\ __           /      |      \           __ /|
#    \    \ _     /        |        \     _ /    /
#     \ _     \ /      /   |   \      \ /     _ /
#         \         /      |      \         /
#            \   /         |         \   /



                                                                                
#          ......                                                       ....      
#       ...........                                                    .......    
#      .............                                                  ........,   
#     ,..................                                         .............   
#    .,..,,,,,,**,,,,,,.....                          ...     .....,,,,,,*,,...*  
#    ,,,,,**//(##########/*,,..........        ............,,,*/((((////////,,,,  
#    ,,,*///((&@@@&&%&%*,,,*(((/*,,...............,,,,,,*//,,.%@@@@&&@@#,/(((,,,  
#   ,,,,*((@@@@@%%@@@&%%%%%%%%.,/##/*,,....   ...,,,*(*,&#@@&&&%%&&%&&&&@@@/(*,,. 
#   *,*,*(*,....       .,@@@@@&@@@#,/#/*,,,.....,,*/#%@@@@@&@&,.         ..,@,,,, 
#   *,,,**,.....        ...,*%@@@@@@@*,**,,,....,#&@@@@@@&*,....         ...,,,,/ 
#   /,,(*,........      .....,*///@#*,,,,......../@@@@*/*,,.......      ....,,,,/ 
#   /*,.*,,...................,,*///*,,.........,,*//**,,,,.................,,.,/ 
#   *,,..*,,,,,,*#%%#(*/#####(*******,,.       ..,****,,,,,*(((((/*,,,,,.,,.,..,* 
#   /*,....(*(#(/,,,@@@@@@@@@@@@/(*,....       ...,**#(,,,*(%&@@(.,.*#(,,,,,...,* 
#   /,*(,./***/(*. *@@@@@@@@@@/..**  ...         ..,(#.@@@@@@@@@@@@@. .((//(/*/.* 
#   (*(*....      ,,*#%%&&%%#***                     ,//#(,.......,(/,,     ../., 
#   #*,.....                         .                                       ..,* 
#    *,,,.....                                                            .....** 
#    /*,,,,.....                                                         ....,,** 
#    #****,,,,.....    ......                                         .....,,,*** 
#     /*/****,,,,,.............,.                    .....................,,,*,*. 
#     #(,*/(///***********////*..   . ..              .,/***,,,,,,,,,,,,,**/,,**  
#      ((*///(##%%%###(/*..   ...   ...          ... ..    .*((((((((///(/*,,**/  
#       ((//((*@@&%#,,....     ,***,,..............,,,.      ...,,,%&&&//,,,***   
#       (((///(,#@@%%......     ..,.@@#***,,*****@/.,.       ....(%&@///,,,****   
#        (((////,.@@&#.....         %%@&@@@@@@@&%%             ##&&@//*,.,****    
#         ((((/**/.@@@@&&&&&@&*  /%%@@@@@@@@@@@&&&&#      .%@#%&@@.//*..*****     
#          ((/(/**/*.*@@@@@@@@@@@@&@@@@@&***/@@@@%&&%@&&&%&&&&@@.,/**..*****      
#            ((((**///,.  ...,*//((#%%#######(#@@&&%%##(**,,.  .//*,.,/***/       
#             ,((((*,/*//,,.       .... ,/(((/, .          .,*//**.,****/         
#               ((((/,******((/*,,.....................*//****/*,.,****           
#                 ((#(*,/*,,,,,,****/@@&&&&%%&%##(//**,,,,*//,,.,****.            
#                   (##(****,,,,,,,,,,*@@@@@@@@*,,,,,,,,,,*,,.,*****              
#                     ###/,**,,,,......@@@@@@&&........,,/..,*****                
#                       (#(*,*,,.......&@@@@@%%      ..,,.,****.                  
#                         .(*,,,,,.....@@@@@@&&      .,.,****                     
#                            (*,,,,,....@@@@@@@.   ...,*/**                       
#                              (***,,,,,@@@@@@,....,,,***                         
#                                ,//****,@@@@&********                            
#                                   .%###@@@@##(((.      